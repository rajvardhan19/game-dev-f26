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

# Training blocks: 201-208 for gemini-a, 301-350 for gemini-b (both declared 2026-10-26).
TRAIN_SEEDS = list(range(201, 209)) + list(range(301, 351))

# Declared 2026-10-23, before any prompt tuning or live call (SUITE.md).
SUITE = {
    "standard": {"dev": [101, 102, 103, 104], "eval": [1, 2],     # dev 103-104 added 2026-10-26
                 "train": TRAIN_SEEDS},                           # the learning player's notebooks only
    "alternate": {"dev": [101, 102, 103, 104], "eval": [1, 2], "train": TRAIN_SEEDS},
    "reckless": {"dev": [], "eval": [1, 2], "train": []},          # held out: never used while tuning
}
BASELINE_EXTRA_SEEDS = list(range(3, 21))            # free extra trials for the cheap players

# Dated price used for the cost estimate; confirm against Google's page before relying on it.
PRICES = {"gemini-3.5-flash-lite": {"input_per_m": 0.30, "output_per_m": 2.50,
                                    "as_of": "2026-10-23",
                                    "source": "third-party listings (Maxim, Requesty) quoting Vertex AI; "
                                              "Google's pricing page not retrieved"},
          "gemini-3.5-flash": {"input_per_m": 1.50, "output_per_m": 9.00,
                               "as_of": "2026-10-27",
                               "source": "third-party listings (Maxim, pricepertoken) quoting Vertex AI; "
                                         "Google's pricing page not retrieved"},
          "gemini-3.7-flash": {"input_per_m": 0.75, "output_per_m": 3.75,
                               "as_of": "2026-10-27",
                               "source": "introductory rate to 2026-12-31 (DataCamp, TechJack); "
                                         "Google's pricing page not retrieved"}}


def price_for(model: str) -> dict | None:
    """The longest PRICES key the model name starts with, so flash-lite is never priced as flash."""
    keys = [k for k in PRICES if model.startswith(k)]
    return PRICES[max(keys, key=len)] if keys else None

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


def make_player(name: str, seed: float, args, scenario: str | None = None):
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
        client = VertexClient(timeout=args.timeout, max_output_tokens=getattr(args, "max_output_tokens", 2048))
        if name == "model-lessons":
            from .players.learner import LessonBook
            if not getattr(args, "lessons", None):
                sys.exit("model-lessons needs --lessons PATH, a frozen notebook (python -m cws.learn freeze)")
            book = LessonBook(Path(args.lessons))
            if not book.frozen:
                sys.exit(f"{args.lessons} is not frozen: freeze it before validation or evaluation")
            method = book.data.get("method", {})
            opening = book.data.get("openings", {}).get(scenario) if method.get("openings") else None
            chosen = aids(args)                          # a notebook keeps the aids it learned with
            chosen = {k: chosen[k] or bool(method.get(k)) for k in chosen}
            player = ModelPlayer(client, "history", 3, lessons=book.lessons, name="model-lessons",
                                 priority=bool(method.get("priority")), opening=opening, **chosen)
            player.config.update(lessons_book=book.data["name"], lessons_version=book.version,
                                 lessons_sha=book.sha())
            return player
        return ModelPlayer(client, memory=name[len("model-"):], history_turns=3, **aids(args))
    raise SystemExit(f"unknown player {name!r}")


def aids(args) -> dict:
    """Execution aids for model players: --aids fronts,plan."""
    chosen = set(filter(None, (getattr(args, "aids", "") or "").split(",")))
    if chosen - {"fronts", "plan"}:
        raise SystemExit(f"unknown aids {sorted(chosen - {'fronts', 'plan'})}")
    return {"fronts": "fronts" in chosen, "plan": "plan" in chosen}


def cost(result) -> float | None:
    price = price_for(result.config.get("player", {}).get("model", ""))
    if price is None:
        return None
    return round(result.input_tokens / 1e6 * price["input_per_m"]
                 + result.output_tokens / 1e6 * price["output_per_m"], 5)


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
    ap.add_argument("--split", choices=["eval", "dev", "train"],
                    help="dev seeds for prompt work, eval for the declared comparison, train for the learning "
                         "player's training seeds (reference runs); required for model players")
    ap.add_argument("--scenarios", nargs="+", default=list(SUITE))
    ap.add_argument("--seeds", type=int, nargs="+",
                    help="only these of the split's seeds (to finish a run an outage stopped); never adds a seed")
    ap.add_argument("--extra-baseline-seeds", action="store_true",
                    help="also run the free players on seeds 3-20")
    ap.add_argument("--live", action="store_true", help="confirm paid model calls")
    ap.add_argument("--timeout", type=float, default=30.0, help="per model call, seconds")
    ap.add_argument("--run", default=datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--lessons", help="the frozen notebook for model-lessons (lessons/<name>.json)")
    ap.add_argument("--max-output-tokens", type=int, default=2048, help="per model call (thinking models need more)")
    ap.add_argument("--aids", default="", help="execution aids for model players: fronts, plan (comma-separated)")
    args = ap.parse_args()

    models = [p for p in args.players if p.startswith("model-")]
    if models and args.split is None:
        sys.exit("Model players need an explicit --split: dev (seeds 101-104, for prompt work) "
                 "or eval (the held-out comparison seeds; see SUITE.md).")
    if models and not args.live:
        sys.exit("Model players make paid calls: pass --live to confirm.")
    args.split = args.split or "eval"
    if args.split in ("dev", "train") and "reckless" in args.scenarios:
        args.scenarios = [s for s in args.scenarios if s != "reckless"]
    traces = ROOT / "traces" / args.run
    results = ROOT / "results" / args.run
    results.mkdir(parents=True, exist_ok=True)
    (results / "results.jsonl").write_text("")
    rows = []
    for player_name in args.players:
        for scenario in args.scenarios:
            seeds = [s for s in SUITE[scenario][args.split] if not args.seeds or s in args.seeds]
            if args.extra_baseline_seeds and not player_name.startswith("model-"):
                seeds += BASELINE_EXTRA_SEEDS
            for seed in seeds:
                extra = seed not in SUITE[scenario][args.split]
                player = make_player(player_name, seed, args, scenario)
                limits = Limits(engine_timeout=args.timeout + 30, decision_timeout=max(45.0, args.timeout + 15))
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
                if r.model_calls and r.failed_calls * 2 >= r.model_calls:
                    sys.exit(f"stopping: {r.failed_calls} of {r.model_calls} model calls failed in {player_name} "
                             f"{scenario} seed {seed} (check the connection and quota); that episode is not recorded.")
                print(f"   -> {r.reason} | turns {r.turns} | Union cities {r.cities_union} | "
                      f"invalid {r.invalid_actions} | calls {r.model_calls} | {r.wall_seconds}s", flush=True)
                with (results / "results.jsonl").open("a") as f:
                    f.write(json.dumps(row) + "\n")
    (results / "table.md").write_text(table(rows) + "\n")
    print(table(rows))


if __name__ == "__main__":
    main()
