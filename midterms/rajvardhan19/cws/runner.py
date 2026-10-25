"""The episode runner: holds the engine process, enforces every limit, writes the trace.

A player is any object with `decide(obs, legal, memory) -> Decision` or the
simpler `act(obs, legal) -> str`. The runner, never the player, decides when
an episode ends, and every action in the trace says who chose it:
"model", "scripted" (a baseline) or "fallback" (the runner, with the reason).
"""

import json
import threading
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .client import EngineError, EngineProcess, EngineTimeout


@dataclass
class Limits:
    max_steps: int = 600               # engine-enforced: actions, valid or not
    max_model_calls: int = 150         # failed calls count
    max_wall_seconds: float = 1800.0   # whole episode
    max_actions_per_turn: int = 40     # then the runner ends the turn (fallback)
    max_failures_per_turn: int = 3     # failed calls or fully rejected replies, then fallback
    max_batch: int = 8                 # actions taken from one model reply
    engine_timeout: float = 30.0
    decision_timeout: float = 45.0     # runner watchdog on one decision (the SDK's own limit is 30 s)


@dataclass
class Decision:
    actions: list[str]
    source: str = "scripted"           # "model" or "scripted"
    model_call: bool = False
    ok: bool = True
    error: str = ""
    latency: float = 0.0
    input_tokens: int = 0
    output_tokens: int = 0
    note: str = ""
    raw: str = ""


@dataclass
class EpisodeResult:
    player: str
    scenario: str
    seed: float
    status: str = ""
    reason: str = ""
    winner: str | None = None
    score: int = 0
    turns: int = 0
    date: str = ""
    cities_union: int = 0
    steps: int = 0
    invalid_actions: int = 0
    model_calls: int = 0
    failed_calls: int = 0
    fallback_actions: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    model_latency_total: float = 0.0
    wall_seconds: float = 0.0
    config: dict = field(default_factory=dict)


def board_summary(obs: dict) -> dict:
    """What the trace keeps of each turn's opening observation (for replay and review)."""
    return {
        "date": obs["date"], "cash": obs["treasury"]["Union"]["cash"],
        "vp": [obs["victory_points"]["Union"], obs["victory_points"]["Rebel"]],
        "owners": "".join(c["owner"][0] for c in obs["cities"]),
        "forts": "".join(str(c["fort"]) for c in obs["cities"]),
        "union": [[a["id"], a["city"], a["men"]] for a in obs["your_armies"]],
        "rebel": [[a["id"], a["city"], a["men"]] for a in obs["enemy_armies"]],
    }


def _as_decision(player, obs, legal, memory) -> Decision:
    if hasattr(player, "decide"):
        return player.decide(obs, legal, memory)
    return Decision([player.act(obs, legal)])


def _decide_with_watchdog(player, obs, legal, memory, timeout: float) -> Decision:
    """Run one decision in a thread; a hang or an exception becomes a failed decision."""
    box: dict = {}

    def work():
        try:
            box["decision"] = _as_decision(player, obs, legal, memory)
        except Exception as error:                     # a player bug must not end the suite silently
            box["error"] = f"{type(error).__name__}: {str(error)[:200]}"

    started = time.monotonic()
    worker = threading.Thread(target=work, daemon=True)
    worker.start()
    worker.join(timeout)
    model = getattr(player, "uses_model", False)
    if worker.is_alive():
        return Decision([], "model" if model else "scripted", model, False,
                        f"runner watchdog: no decision within {timeout:g}s", time.monotonic() - started)
    if "error" in box:
        return Decision([], "model" if model else "scripted", model, False, box["error"],
                        time.monotonic() - started)
    return box["decision"]


def _same_action(a: str, b: str) -> bool:
    """Compare actions as step() does: case and spacing do not matter."""
    return " ".join(str(a).lower().split()) == b


def run_episode(player, scenario: str, seed: float, limits: Limits | None = None,
                trace_path: Path | None = None, on_step=None, on_turn=None) -> EpisodeResult:
    limits = limits or Limits()
    result = EpisodeResult(getattr(player, "name", type(player).__name__), scenario, seed,
                           config={"limits": asdict(limits), "player": getattr(player, "config", {})})
    trace: list[dict] = []
    memory = {"turns": [], "this_turn": [], "feedback": []}
    started = time.monotonic()

    def record(entry: dict) -> None:
        entry["t"] = round(time.monotonic() - started, 3)
        trace.append(entry)
        if on_step:
            on_step(entry)

    with EngineProcess(limits.engine_timeout) as engine:
        try:
            engine.reset(scenario, seed, limits.max_steps)
            port = engine.port()
            turn, per_turn, failures = None, 0, 0
            while True:
                out = engine.outcome()
                if out["status"] == "terminal":
                    result.reason = out["reason"]
                    break
                if time.monotonic() - started > limits.max_wall_seconds:
                    result.reason = "timeout: episode wall clock"
                    break
                obs, legal = port.observe(), port.legal_actions()
                if obs["turn"] != turn:
                    if turn is not None:
                        memory["turns"].append({"turn": turn, "date": prev_date, "actions": memory["this_turn"],
                                                "report": obs["last_turn_report"]})
                    turn, prev_date, per_turn, failures = obs["turn"], obs["date"], 0, 0
                    memory["this_turn"], memory["feedback"] = [], []
                    record({"turn_start": turn, "board": board_summary(obs)})
                    if on_turn:
                        on_turn(obs)
                if per_turn >= limits.max_actions_per_turn or failures >= limits.max_failures_per_turn:
                    why = "turn action limit" if per_turn >= limits.max_actions_per_turn else "repeated failures"
                    res = port.step("end turn")
                    result.fallback_actions += 1
                    per_turn += 1
                    record({"turn": turn, "action": "end turn", "source": "fallback", "why": why,
                            "accepted": res["accepted"], "text": res["text"]})
                    continue
                uses_model = getattr(player, "uses_model", False)
                if uses_model and result.model_calls >= limits.max_model_calls:
                    result.reason = "model-call limit"
                    break
                decision = _decide_with_watchdog(player, obs, legal, memory, limits.decision_timeout)
                if not decision.model_call and not decision.ok:
                    result.reason = f"player error: {decision.error}"
                    break
                if decision.model_call:
                    result.model_calls += 1
                    result.model_latency_total += decision.latency
                    result.input_tokens += decision.input_tokens
                    result.output_tokens += decision.output_tokens
                    record({"turn": turn, "call": result.model_calls, "ok": decision.ok,
                            "error": decision.error, "latency": round(decision.latency, 3),
                            "input_tokens": decision.input_tokens, "output_tokens": decision.output_tokens,
                            "proposed": decision.actions, "note": decision.note})
                    if not decision.ok:
                        result.failed_calls += 1
                        failures += 1
                        memory["feedback"] = [f"Your last reply could not be used: {decision.error}"]
                        continue
                any_accepted = False
                for action in decision.actions[:limits.max_batch]:
                    res = port.step(action)
                    per_turn += 1
                    record({"turn": turn, "action": action, "source": decision.source,
                            "accepted": res["accepted"], "text": res["text"]})
                    memory["this_turn"].append({"action": action, "accepted": res["accepted"], "text": res["text"]})
                    if not res["accepted"]:
                        memory["feedback"] = [f"'{action}' was rejected: not in the legal list at that moment."]
                        break
                    any_accepted = True
                    memory["feedback"] = []
                    # Stop at new information: the turn resolved, the recruiting list appeared,
                    # or the game ended. The turn check also catches any spelling step() accepts.
                    if (res["observation"]["turn"] != turn or _same_action(action, "end turn")
                            or _same_action(action, "troops") or engine.outcome()["status"] == "terminal"):
                        break
                if not any_accepted:
                    failures += 1
        except EngineTimeout as error:
            result.reason = f"timeout: {error}"
        except EngineError as error:
            result.reason = f"engine error: {error}"
        out = engine.outcome() if not result.reason.startswith(("timeout: engine", "engine error")) else {}
        result.status = "terminal"
        result.winner = out.get("winner")
        result.score = out.get("score", 0)
        result.turns = max(out.get("turn", 1) - 1, 0)          # turns resolved
        result.date = out.get("date", "")
        result.cities_union = out.get("cities", {}).get("Union", 0)
        result.steps = out.get("steps", 0)
        result.invalid_actions = out.get("invalid_actions", 0)
    result.wall_seconds = round(time.monotonic() - started, 2)
    if trace_path:
        trace_path.parent.mkdir(parents=True, exist_ok=True)
        with trace_path.open("w") as f:
            f.write(json.dumps({"header": asdict(result)}) + "\n")
            for entry in trace:
                f.write(json.dumps(entry) + "\n")
    return result
