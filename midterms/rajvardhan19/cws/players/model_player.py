"""The model-driven Union player.

It receives the observation, the legal actions and, in "history" mode, a
bounded summary of its own last turns. It has no tools: the request carries
no function declarations and automatic function calling is disabled. It
cannot read files, the Game, the rule map or the opponent's code; the only
thing it can do is name actions, which the runner submits through the
interface one at a time.

Providers: "vertex" (Gemini on Vertex AI, the course default) and "fake",
a scripted stand-in for offline tests. A fake is never used in a live
evaluation; results record the provider and the model's own version string.
"""

import json
import os
import time

from ..runner import Decision

SCHEMA = {
    "type": "object",
    "properties": {
        "actions": {"type": "array", "items": {"type": "string"}, "maxItems": 8},
        "note": {"type": "string"},
    },
    "required": ["actions", "note"],
}

SYSTEM = """You are the Union commander in VGA Civil War Strategy (W. R. Hutsell, 1998), \
a turn-based strategy game. You play against the game's built-in Confederate computer player. \
You see what a human Union player sees on screen. Nothing else is available to you.

How a turn works. Each turn is two months. You give orders, then "end turn". The Rebels then \
plan, and every ordered move resolves in an order that is partly random: leaders rated higher \
tend to go earlier, armies over 40,000 men go later, armies out of supply go last.

Orders. An idle army may move to one adjacent city. A newly raised army, an army that joined, \
drilled or fortified this turn, rests and cannot move (reinforcing an existing army does not make \
it rest). Moving into an empty enemy or neutral city captures it. \
Moving into a city held by enemy troops starts a battle. Strength comes from size (about 1 point \
per 100 men, capped), the leader rating and experience, outnumbering the enemy, and supply. \
Forts multiply a defender's strength (x2 at level 1, x3 at level 2) when the defender is not \
moving that turn. An army out of supply fights at half strength. A beaten attacker falls back. \
A beaten defender retreats to a friendly neighbouring city, or surrenders if it has none.

Money and supply. Each turn you earn the value of every city you hold, plus 100 while you hold \
your capital. Each turn an army gains 1 supply if your treasury can pay a fifth of its size in \
hundreds and it is not cut off (it needs a friendly neighbouring city). In January, March, May \
and November, armies outside seaports lose 1 supply. An army at 0 supply may lose a tenth of \
its men. Moving costs 1 supply.

Commands (each listed only when it is possible now):
- troops: see which of your cities offer recruits this turn (free). The list is kept for the turn; \
if no city is offered you may try troops again.
- recruit <city>: $100. Raises a new army there, or reinforces the army already there. Big cities \
give more men; a city with no friendly neighbour gives a third.
- fortify <city>: $200. Fort level +1 (maximum 2). The army there rests.
- join <city>: merge the idle armies in that city under the best leader (limit 125,000 men).
- supply <army>: buy supply for an army at 1 or less (up to 5).
- drill <army>: +1 experience, up to the leader's rating (maximum 6). The army rests.
- move <army> <city>, cancel <army>, end turn.

Reply with JSON only: {"actions": [...], "note": "..."}. "actions" is an ordered list of up to 8 \
strings, each copied exactly from LEGAL ACTIONS. They are carried out one at a time, and the \
list stops at the first one that is no longer legal. Put "end turn" last when you are done for \
the turn. "note" is one or two sentences on your plan, which you will see again next turn if \
memory is on."""


def render(obs: dict, legal: list[str], memory: dict, history: list[dict] | None) -> str:
    t = obs["treasury"]
    vp = obs["victory_points"]
    lines = [
        f"DATE {obs['date']} (turn {obs['turn']}, {obs['turns_left']} turns until the deadline)",
        f"UNION cash {t['Union']['cash']} income {t['Union']['income']} cities {t['Union']['cities']} | "
        f"REBEL cash {t['Rebel']['cash']} income {t['Rebel']['income']} cities {t['Rebel']['cities']}",
        f"VICTORY POINTS Union {vp['Union']} Rebel {vp['Rebel']} (Union share {vp['union_share_percent']}%)",
        "VICTORY CONDITIONS: " + "; ".join(obs["victory_conditions"]),
        "",
        "CITIES: id name | owner | value | fort | port | capital | neighbours (id)",
    ]
    for c in obs["cities"]:
        cap = c["capital_of"] or "-"
        lines.append(f"{c['id']} {c['name']} | {c['owner']} | {c['value']} | {c['fort']} | "
                     f"{'port' if c['port'] else '-'} | {cap} | {','.join(map(str, c['neighbors']))}")
    lines += ["", "YOUR ARMIES: id leader | men | city | leader rating | experience | supply | order"]
    for a in obs["your_armies"]:
        lines.append(f"{a['id']} {a['name']} | {a['men']} | {a['city_name']} ({a['city']}) | "
                     f"{a['leader']} | {a['experience']} | {a['supply']} | {a['order']}")
    lines += ["", "ENEMY ARMIES: id leader | men | city | out of supply"]
    for a in obs["enemy_armies"]:
        lines.append(f"{a['id']} {a['name']} | {a['men']} | {a['city_name']} ({a['city']}) | "
                     f"{'yes' if a['out_of_supply'] else 'no'}")
    if obs["recruiting"]["rolled"]:
        lines.append("RECRUITS OFFERED THIS TURN IN: " + ", ".join(obs["recruiting"]["offered"]))
    if obs["last_turn_report"]:
        lines += ["", "WHAT HAPPENED LAST TURN:"] + [f"- {e['text']}" for e in obs["last_turn_report"]]
    if history:
        lines += ["", "YOUR MEMORY OF EARLIER TURNS (most recent last):"]
        for h in history:
            done = [a["action"] for a in h["actions"] if a["accepted"]]
            lines.append(f"* {h['date']}: you did {', '.join(done) or 'nothing'}. Your note: {h.get('note') or '-'}")
            for e in h["report"][:12]:
                lines.append(f"    - {e['text']}")
    if obs["this_turn_messages"]:
        lines += ["", "THIS TURN SO FAR:"] + [f"- {m}" for m in obs["this_turn_messages"]]
    if memory.get("feedback"):
        lines += ["", "FEEDBACK: " + " ".join(memory["feedback"])]
    lines += ["", "LEGAL ACTIONS:"] + legal
    return "\n".join(lines)


class ModelPlayer:
    uses_model = True

    def __init__(self, client, memory: str = "history", history_turns: int = 3) -> None:
        if memory not in ("history", "obs-only"):
            raise ValueError("memory must be 'history' or 'obs-only'")
        self.client = client
        self.memory = memory
        self.history_turns = history_turns
        self.name = f"model-{memory}"
        self._notes: dict[int, str] = {}
        self.config = {"provider": client.provider, "model": client.model, "memory": memory,
                       "history_turns": history_turns if memory == "history" else 0,
                       "max_output_tokens": client.max_output_tokens, "timeout_seconds": client.timeout}

    def decide(self, obs: dict, legal: list[str], memory: dict) -> Decision:
        history = None
        if self.memory == "history":
            history = [dict(h, note=self._notes.get(h["turn"], "")) for h in memory["turns"][-self.history_turns:]]
        prompt = render(obs, legal, memory, history)
        started = time.monotonic()
        try:
            reply = self.client.generate(SYSTEM, prompt, SCHEMA)
        except Exception as error:                       # timeouts, quota, network: a failed call
            return Decision([], "model", True, False, f"{type(error).__name__}: {str(error)[:200]}",
                            time.monotonic() - started)
        latency = time.monotonic() - started
        d = Decision([], "model", True, True, "", latency, reply["input_tokens"], reply["output_tokens"], raw=reply["text"][:2000])
        if not reply["complete"]:
            d.ok, d.error = False, f"incomplete response ({reply['finish']})"
            return d
        try:
            data = json.loads(reply["text"])
            actions = data["actions"]
            if not isinstance(actions, list) or not all(isinstance(a, str) for a in actions):
                raise ValueError("actions must be a list of strings")
        except (ValueError, KeyError, TypeError) as error:
            d.ok, d.error = False, f"unusable JSON: {error}"
            return d
        d.actions = actions[:8]
        d.note = str(data.get("note", ""))[:400]
        self._notes[obs["turn"]] = d.note
        return d


class VertexClient:
    """Gemini on Vertex AI with the starter's request controls (one attempt, bounded output)."""

    provider = "vertex"

    def __init__(self, model: str | None = None, timeout: float = 30.0, max_output_tokens: int = 2048) -> None:
        self.model = model or os.environ.get("COURSE_MODEL", "").strip()
        missing = [n for n in ("GOOGLE_CLOUD_PROJECT", "GOOGLE_CLOUD_LOCATION") if not os.environ.get(n)]
        if not self.model:
            missing.append("COURSE_MODEL")
        if missing:
            raise RuntimeError("Configure " + ", ".join(missing) + " (see README, Live model).")
        self.timeout, self.max_output_tokens = timeout, max_output_tokens
        from google import genai
        from google.genai import types
        self._types = types
        self._client = genai.Client(
            vertexai=True, project=os.environ["GOOGLE_CLOUD_PROJECT"],
            location=os.environ["GOOGLE_CLOUD_LOCATION"],
            http_options=types.HttpOptions(timeout=int(timeout * 1000),
                                           retry_options=types.HttpRetryOptions(attempts=1)),
        )

    def generate(self, system: str, prompt: str, schema: dict) -> dict:
        types = self._types
        response = self._client.models.generate_content(
            model=self.model, contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system, response_mime_type="application/json",
                response_json_schema=schema, max_output_tokens=self.max_output_tokens,
                automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
            ),
        )
        usage = response.usage_metadata
        cand = response.candidates[0] if response.candidates else None
        finish = cand.finish_reason if cand else None
        output = (getattr(usage, "candidates_token_count", 0) or 0) + (getattr(usage, "thoughts_token_count", 0) or 0)
        self.model_version = response.model_version or self.model
        return {"text": response.text or "", "complete": finish == types.FinishReason.STOP,
                "finish": str(finish), "input_tokens": getattr(usage, "prompt_token_count", 0) or 0,
                "output_tokens": output}


class FakeClient:
    """Scripted replies for offline tests. Its results are never reported as a model's."""

    provider = "fake"
    model = "scripted-fixture"
    timeout = 0
    max_output_tokens = 0

    def __init__(self, replies) -> None:
        self.replies = list(replies)
        self.prompts: list[str] = []

    def generate(self, system: str, prompt: str, schema: dict) -> dict:
        self.prompts.append(prompt)
        if not self.replies:
            raise TimeoutError("fake client has no more replies")
        reply = self.replies.pop(0)
        if isinstance(reply, Exception):
            raise reply
        if callable(reply):
            reply = reply(prompt)
        text = reply if isinstance(reply, str) else json.dumps(reply)
        return {"text": text, "complete": True, "finish": "STOP", "input_tokens": len(prompt) // 4,
                "output_tokens": len(text) // 4}
