# Evaluation

Game version: this folder at the submitted commit. The engine reproduces
VGA Civil War Strategy v2.11 (`source/CWSTRAT.BAS`, upstream `dac8db1`)
within the scope in the [README](README.md#scope-statement).

## Declared suite

[SUITE.md](SUITE.md), declared 2026-10-23, before any prompt tuning or live
call. In brief:

- **Situations:** three, `standard`, `alternate` and `reckless`.
  `reckless` (opponent aggression 5) is held out entirely.
- **Evaluation seeds:** 1 and 2 for every situation, so two live trials per
  situation per model variant.
- **Development seeds:** 101 and 102 on `standard` and `alternate`, for
  prompt work only.
- **Same cases for everyone:** every player runs the same seeds, under the
  same observations, action rules and limits.

**Outcome tiers** come from the game's own end screens:

- **win:** any Union victory condition;
- **held out:** "Confederates will win a technical victory", meaning the
  deadline passed;
- **decisive loss:** any other Rebel victory condition;
- **incomplete:** a runner limit ended the game.

Ties are broken by turns resolved.

**VP share is not the score.** A player conquered in 1862 can end with a
higher VP share than one that held out to 1865, because of VP decay and the
deadline's ×0.7. `tests/test_episodes.py` has a case of this, standard
seed 3.

## Comparison table

### Paired suite: evaluation seeds 1 and 2

Run `20261023-baselines` (offline). Model rows will be filled from the live
run; nothing below is estimated.

| player | scenario | trials | win | held out | decisive loss | incomplete | mean turns | mean Union cities | invalid actions | fallbacks | model calls (failed) | mean latency s | tokens in / out | est. cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| model-history | standard | **not yet run** | | | | | | | | | | | | |
| model-history | alternate | **not yet run** | | | | | | | | | | | | |
| model-history | reckless (held out) | **not yet run** | | | | | | | | | | | | |
| model-obs-only | standard | **not yet run** | | | | | | | | | | | | |
| model-obs-only | alternate | **not yet run** | | | | | | | | | | | | |
| model-obs-only | reckless (held out) | **not yet run** | | | | | | | | | | | | |
| original-ai | standard | 2 | 0 | 2 | 0 | 0 | 24.0 | 20.0 | 0 | 0 | - | - | - | - |
| original-ai | alternate | 2 | 2 | 0 | 0 | 0 | 5.5 | 21.0 | 0 | 0 | - | - | - | - |
| original-ai | reckless | 2 | 0 | 2 | 0 | 0 | 24.0 | 14.5 | 0 | 0 | - | - | - | - |
| random | standard | 2 | 0 | 0 | 2 | 0 | 3.5 | 9.0 | 0 | 0 | - | - | - | - |
| random | alternate | 2 | 0 | 0 | 2 | 0 | 5.5 | 8.5 | 0 | 0 | - | - | - | - |
| random | reckless | 2 | 0 | 0 | 2 | 0 | 3.5 | 8.0 | 0 | 0 | - | - | - | - |
| passive | standard | 2 | 0 | 0 | 2 | 0 | 7.0 | 4.0 | 0 | 0 | - | - | - | - |
| passive | alternate | 2 | 0 | 0 | 2 | 0 | 6.5 | 6.5 | 0 | 0 | - | - | - | - |
| passive | reckless | 2 | 0 | 0 | 2 | 0 | 6.5 | 5.0 | 0 | 0 | - | - | - | - |

Live command, from `midterms/rajvardhan19/`:

```sh
uv run --extra live python -m cws.evaluate --players model-history model-obs-only --split eval --live --run <date>-live
```

When it finishes, `results/<run>/table.md` holds the model rows in the same
format. Record the `COURSE_MODEL` value, the `model_version` the API
returned (in `results.jsonl`) and the run date here.

### The cheap players over more seeds (1-20)

Free, deterministic per seed, and not part of the paired comparison:
[results/20261023-baselines/table.md](results/20261023-baselines/table.md).

| player | scenario | trials | win | held out | decisive loss | mean turns | mean Union cities |
|---|---|---|---|---|---|---|---|
| original-ai | standard | 20 | 2 | 17 | 1 | 22.0 | 16.3 |
| original-ai | alternate | 20 | 20 | 0 | 0 | 8.5 | 19.8 |
| original-ai | reckless | 20 | 1 | 10 | 9 | 20.4 | 12.5 |
| random | standard | 20 | 0 | 0 | 20 | 4.2 | 7.7 |
| random | alternate | 20 | 0 | 0 | 20 | 5.8 | 8.6 |
| random | reckless | 20 | 0 | 0 | 20 | 4.8 | 7.7 |
| passive | standard | 20 | 0 | 0 | 20 | 7.5 | 5.2 |
| passive | alternate | 20 | 0 | 0 | 20 | 7.2 | 7.0 |
| passive | reckless | 20 | 0 | 0 | 20 | 6.9 | 5.2 |

What these show:

- **The baseline is a real competitor.** The original AI never loses on the
  alternate map, holds out in most standard games, and is clearly stressed
  by the reckless opponent (9 decisive losses in 20).
- **Random and passive lose every game decisively.** Random falls in 2-12
  turns, passive in 5-11.
- **The suite has room in both directions.** A model can be shown to beat the
  original AI (wins on `standard`, or fewer decisive losses on `reckless`),
  to match it, or to fall to the floor. With two live trials per situation,
  only large differences are visible; this is not a statistical test.

### Cost

Price used: $0.30 per million input tokens and $2.50 per million output
tokens (thinking tokens counted as output) for `gemini-3.5-flash-lite` on
Vertex AI. Source: third-party listings quoting Vertex AI
([Maxim](https://www.getmaxim.ai/bifrost/llm-cost-calculator/provider/vertex_ai/model/gemini-3.5-flash-lite),
"verified Aug 6, 2026"; [Requesty](https://www.requesty.ai/models-new/vertex/gemini-3.5-flash-lite)),
retrieved 2026-10-23. Google's pricing page did not load. **TODO: confirm
against Google's page on the day of the live run and update
`cws/evaluate.py` `PRICES`.** The estimate is tokens × price; it is not a
bill.

## Memory experiment

The game is partially observed. Enemy leaders, experience, supply and
orders are hidden, as are the dice. So the suite compares:

- `model-history`: the observation, plus the agent's own last 3 turns
  (actions it took, its one-line notes, and each turn's visible report);
- `model-obs-only`: the observation alone. It includes the most recent
  turn's report, because a human just watched it.

Both variants get the same feedback after a rejected action. If memory does
not help, that is a result.

## Traces

- Baselines, paired seeds: [traces/20261023-baselines/](traces/20261023-baselines/).
  One JSONL per episode. The first line is a header with the result and
  configuration; then each turn's board summary and every action with
  `source` (`scripted`, `model` or `fallback`), `accepted` and the game's
  reply.
- Live model traces: `traces/<date>-live/` (TODO after the live run). Each
  model call is a line with `ok`, `error`, `latency`, tokens, the `proposed`
  actions and the model's `note`, followed by the actions actually submitted.

## Fidelity to the original

The original game code was compiled with QB64-PE 4.7.0 and run against
this engine on the same seeds and commands. The run went through every SUB,
including SUB victor, and the main-module rule paths copied by line number.

- **36 games and 3,392 commands produced identical full game states after
  every command.** The original AI, a random player and a passive player
  played the Union in all three situations.
- **Covered:** all nine command types, and eight end conditions.
- **Not reached:** annihilation and a Union strength-ratio win. These two
  are hand-traced in `tests/test_mechanics.py`.
- **Where:** the recordings are in `tools/qb64-harness/recorded/`, re-checked
  in CI by `tests/test_qb64_recorded.py`.

What the harness changes, and the three bugs it found, are in
[docs/rule-source-map.md](docs/rule-source-map.md).

## CI

Workflow: `.github/workflows/midterm-rajvardhan19.yml`. It runs on pull
requests touching this folder, on Python 3.11 and 3.12, using only the
standard library and no secrets.

| Check kind (brief) | Where |
|---|---|
| Rule invariants | `tests/test_interface.py` `Invariants` (every step of 12 whole games, including the two-month calendar); `tests/test_mechanics.py` (hand traces, every victory condition); `tests/test_qb64_recorded.py` (3,428 states against the original) |
| Legal and illegal actions | `tests/test_interface.py` `LegalAndIllegal`, `InformationBoundary` (two-seed leak test) |
| A successful path and terminal outcomes | `tests/test_episodes.py` (Union wins on income, takes Richmond, deadline reached); `tests/test_interface.py` (terminal refuses everything) |
| An observed regression | `tests/test_regressions.py` (three engine bugs found on 2026-10-23); `tests/test_runner.py` `test_batch_stops_when_the_turn_resolves_whatever_the_spelling` (the review's blocking finding) |
| Episode limits | `tests/test_runner.py`: step, model-call, wall-clock (mid-game) and per-turn limits; the decision watchdog; failed calls counted; fallback labels; batches stop when the turn resolves |
| Model application (no network) | `tests/test_model_player.py`: scripted client and a stand-in Vertex SDK |

CI run for the submitted commit: **TODO: link the green Actions run.**

## Limitations

**TODO (student, in your own voice).** Points the evidence supports, to use
or discard:

- the small sample (two live trials per situation);
- the exclusions (navies, railroads, events) and that the opponent is
  slightly richer without navies (QUESTIONS Q10);
- the opponent sees the full state, as in the original, while the players
  see only the screen;
- the fixed design answers to the retreat and raze prompts;
- x86 QB64 untested (Q1);
- the price source;
- what the peer playtest found;
- if partner notes have not arrived by 2026-11-06, say so here.
