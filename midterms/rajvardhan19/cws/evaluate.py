"""Run the declared suite (SUITE.md) and write results, traces and a table.

    python -m cws.evaluate --players original-ai random passive          # offline, free
    python -m cws.evaluate --players model-history model-obs-only --live # Gemini on Vertex AI

Each episode's trace goes to traces/<run>/; the summary goes to
results/<run>/results.jsonl and results/<run>/table.md.
"""

import argparse
import datetime
import json
import statistics
import sys
from dataclasses import asdict
from pathlib import Path

from .players.baselines import OriginalAI, PassivePlayer, RandomPlayer
from .runner import Limits, run_episode

ROOT = Path(__file__).resolve().parent.parent

# Declared 2026-10-23, before any prompt tuning or live call (SUITE.md).
SUITE = {
    "standard": {"dev": [101, 102], "eval": [1, 2]},
    "alternate": {"dev": [101, 102], "eval": [1, 2]},
    "reckless": {"dev": [], "eval": [1, 2]},          # held out: never used while tuning
}
BASELINE_EXTRA_SEEDS = list(range(3, 21))            # free extra trials for the cheap players

# Dated price used for the cost estimate; confirm against Google's page before relying on it.
PRICES = {"gemini-3.5-flash-lite": {"input_per_m": 0.30, "output_per_m": 2.50,
                                    "as_of": "2026-10-23",
                                    "source": "third-party listings (Maxim, Requesty) quoting Vertex AI; "
                                              "Google's pricing page not retrieved"}}

TIER = {"win": 2, "held out": 1, "decisive loss": 0, "incomplete": -1}


def tier(outcome: dict) -> str:
    reason = outcome.get("reason", "")
    if reason.startswith("Union victory"):
        return "win"
    if reason == "Rebel victory: time expired":
        return "held out"
    if reason.startswith("Rebel victory"):
        return "decisive loss"
    return "incomplete"                               # step, call or time limit, or an engine error


def rank(outcome: dict) -> tuple:
    """Outcome tier first; then a faster win or a longer resistance."""
    t = tier(outcome)
    turns = outcome["turns"] if "turns" in outcome else outcome.get("turn", 1) - 1   # turns resolved
    return (TIER[t], -turns if t == "win" else turns)


def make_player(name: str, seed: float, args):
    if name == "original-ai":
        return OriginalAI(seed)
    if name == "random":
        return RandomPlayer(seed)
    if name == "passive":
        return PassivePlayer(seed)
    if name.startswith("model-"):
        from .players.model_player import ModelPlayer, VertexClient
        if not args.live:
            sys.exit("Model players make paid calls: pass --live to confirm.")
        client = VertexClient(timeout=args.timeout)
        return ModelPlayer(client, memory=name[len("model-"):], history_turns=3)
    raise SystemExit(f"unknown player {name!r}")


def cost(result) -> float | None:
    model = result.config.get("player", {}).get("model", "")
    for key, price in PRICES.items():
        if model.startswith(key):
            return round(result.input_tokens / 1e6 * price["input_per_m"]
                         + result.output_tokens / 1e6 * price["output_per_m"], 5)
    return None


def table(rows: list[dict]) -> str:
    out = ["| player | scenario | trials | win | held out | decisive loss | incomplete | mean turns | "
           "mean Union cities | invalid actions | fallbacks | model calls (failed) | mean latency s | "
           "tokens in / out | est. cost USD |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    groups: dict = {}
    for r in rows:
        groups.setdefault((r["player"], r["scenario"]), []).append(r)
    for (player, scenario), rs in sorted(groups.items()):
        tiers = [r["tier"] for r in rs]
        calls = sum(r["model_calls"] for r in rs)
        latency = (sum(r["model_latency_total"] for r in rs) / calls) if calls else 0
        costs = [r["cost_usd"] for r in rs if r["cost_usd"] is not None]
        out.append("| " + " | ".join(str(v) for v in (
            player, scenario, len(rs), tiers.count("win"), tiers.count("held out"),
            tiers.count("decisive loss"), tiers.count("incomplete"),
            f"{statistics.mean(r['turns'] for r in rs):.1f}",
            f"{statistics.mean(r['cities_union'] for r in rs):.1f}",
            sum(r["invalid_actions"] for r in rs), sum(r["fallback_actions"] for r in rs),
            f"{calls} ({sum(r['failed_calls'] for r in rs)})" if calls else "-",
            f"{latency:.2f}" if calls else "-",
            f"{sum(r['input_tokens'] for r in rs)} / {sum(r['output_tokens'] for r in rs)}" if calls else "-",
            f"{sum(costs):.4f}" if costs else "-",
        )) + " |")
    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--players", nargs="+", default=["original-ai", "random", "passive"])
    ap.add_argument("--split", choices=["eval", "dev"],
                    help="dev seeds for prompt work, eval for the declared comparison; required for model players")
    ap.add_argument("--scenarios", nargs="+", default=list(SUITE))
    ap.add_argument("--extra-baseline-seeds", action="store_true",
                    help="also run the free players on seeds 3-20")
    ap.add_argument("--live", action="store_true", help="confirm paid model calls")
    ap.add_argument("--timeout", type=float, default=30.0, help="per model call, seconds")
    ap.add_argument("--run", default=datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    models = [p for p in args.players if p.startswith("model-")]
    if models and args.split is None:
        sys.exit("Model players need an explicit --split: dev (seeds 101-102, for prompt work) "
                 "or eval (the held-out comparison seeds; see SUITE.md).")
    if models and not args.live:
        sys.exit("Model players make paid calls: pass --live to confirm.")
    args.split = args.split or "eval"
    if args.split == "dev" and "reckless" in args.scenarios:
        args.scenarios = [s for s in args.scenarios if s != "reckless"]
    traces = ROOT / "traces" / args.run
    results = ROOT / "results" / args.run
    results.mkdir(parents=True, exist_ok=True)
    (results / "results.jsonl").write_text("")
    rows = []
    for player_name in args.players:
        for scenario in args.scenarios:
            seeds = list(SUITE[scenario][args.split])
            if args.extra_baseline_seeds and not player_name.startswith("model-"):
                seeds += BASELINE_EXTRA_SEEDS
            for seed in seeds:
                extra = seed not in SUITE[scenario][args.split]
                player = make_player(player_name, seed, args)
                limits = Limits(engine_timeout=args.timeout + 30)
                printer = None if args.quiet else (lambda e: print("   ", json.dumps(e)[:200], flush=True))
                print(f"== {player_name} {scenario} seed {seed}", flush=True)
                r = run_episode(player, scenario, seed, limits,
                                trace_path=None if extra else traces / f"{player_name}-{scenario}-{seed}.jsonl",
                                on_step=printer if player_name.startswith("model-") else None)
                row = asdict(r)
                row.update(tier=tier({"reason": r.reason}), cost_usd=cost(r), run=args.run, split=args.split,
                           run_date=datetime.date.today().isoformat(),
                           model_version=getattr(getattr(player, "client", None), "model_version", None))
                rows.append(row)
                print(f"   -> {r.reason} | turns {r.turns} | Union cities {r.cities_union} | "
                      f"invalid {r.invalid_actions} | calls {r.model_calls} | {r.wall_seconds}s", flush=True)
                with (results / "results.jsonl").open("a") as f:
                    f.write(json.dumps(row) + "\n")
    (results / "table.md").write_text(table(rows) + "\n")
    print(table(rows))


if __name__ == "__main__":
    main()
