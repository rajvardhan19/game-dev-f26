"""Print the held-out comparison tables in EVALUATION.md from the result files. Run from the project folder: python3 tools/eval_tables.py"""
import json
import statistics
from collections import Counter

base = {}
for line in open("results/20261025-baselines/results.jsonl"):
    r = json.loads(line)
    if r["seed"] in (1, 2):
        base[(r["player"], r["scenario"], r["seed"])] = r
passive = {(s, sd): base[("passive", s, sd)]["turns"] for s in ("standard", "alternate", "reckless") for sd in (1, 2)}
live = [json.loads(l) for run in ("20261103-live", "20261103-live-flash37")
        for l in open(f"results/{run}/results.jsonl")]
MODEL = {"gemini-3.5-flash-lite": "3.5 Flash-Lite", "gemini-3.7-flash": "3.7 Flash"}


def label(r):
    if r["player"] == "model-lessons":
        book = "gemini-f" if r["model_version"] == "gemini-3.5-flash-lite" else "gemini-h"
        return f"model-lessons, `{book}` ({MODEL[r['model_version']]})"
    if r["player"].startswith("model-"):
        return f"{r['player']} ({MODEL[r['model_version']]})"
    return r["player"]


ORDER = ["original-ai", "model-lessons, `gemini-h` (3.7 Flash)", "model-history (3.7 Flash)",
         "model-lessons, `gemini-f` (3.5 Flash-Lite)", "model-obs-only (3.5 Flash-Lite)",
         "model-history (3.5 Flash-Lite)", "random", "passive"]
rows = {k: [] for k in ORDER}
for r in live:
    rows[label(r)].append(r)
for (p, s, sd), r in base.items():
    rows[p].append(r)

print("| Player | Won | Held out | Lost | Turns beyond passive (mean) | Model calls (failed) | Fallbacks | Est. cost USD |")
print("|---|---|---|---|---|---|---|---|")
for k in ORDER:
    rs = rows[k]
    t = Counter(r["tier"] for r in rs)
    gain = statistics.mean(r["turns"] - passive[(r["scenario"], r["seed"])] for r in rs)
    calls = sum(r["model_calls"] for r in rs)
    cost = sum(r.get("cost_usd") or 0 for r in rs)
    print(f"| {k} | {t['win']} | {t['held out']} | {t['decisive loss']} | "
          f"{'-' if k == 'passive' else f'{gain:+.2f}'} | "
          f"{f'{calls} ({sum(r['failed_calls'] for r in rs)})' if calls else '-'} | "
          f"{sum(r['fallback_actions'] for r in rs)} | {f'{cost:.2f}' if calls else '-'} |")

print()
print("| player | scenario | trials | win | held out | decisive loss | incomplete | mean turns | mean Union cities "
      "| invalid actions | fallbacks | model calls (failed) | mean latency s | tokens in / out | est. cost USD |")
print("|" + "---|" * 15)
for k in ORDER:
    for sc in ("standard", "alternate", "reckless"):
        rs = sorted((r for r in rows[k] if r["scenario"] == sc), key=lambda r: r["seed"])
        t = Counter(r["tier"] for r in rs)
        calls = sum(r["model_calls"] for r in rs)
        lat = sum(r["model_latency_total"] for r in rs) / calls if calls else None
        cost = sum(r.get("cost_usd") or 0 for r in rs)
        print(f"| {k} | {sc} | {len(rs)} | {t['win']} | {t['held out']} | {t['decisive loss']} | {t['incomplete']} | "
              f"{statistics.mean(r['turns'] for r in rs):.1f} | {statistics.mean(r['cities_union'] for r in rs):.1f} | "
              f"{sum(r['invalid_actions'] for r in rs)} | {sum(r['fallback_actions'] for r in rs)} | "
              f"{f'{calls} ({sum(r['failed_calls'] for r in rs)})' if calls else '-'} | "
              f"{f'{lat:.2f}' if lat else '-'} | "
              f"{f'{sum(r['input_tokens'] for r in rs)} / {sum(r['output_tokens'] for r in rs)}' if calls else '-'} | "
              f"{f'{cost:.4f}' if calls else '-'} |")
print()
print("model_version:", sorted({r["model_version"] for r in live}), "run_date:", sorted({r["run_date"] for r in live}))
print("total live cost", round(sum(r["cost_usd"] or 0 for r in live), 2), "calls", sum(r["model_calls"] for r in live),
      "failed", sum(r["failed_calls"] for r in live))
