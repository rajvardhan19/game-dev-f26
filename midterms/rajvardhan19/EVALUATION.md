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
- **Development seeds:** 101-104 on `standard` and `alternate`, for
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
seed 13.

## Comparison table

### Held-out evaluation: seeds 1 and 2, three situations

Run on 2026-11-03 and declared in [SUITE.md](SUITE.md) the same day, before any
evaluation game. No model had played these seeds or the `reckless` opponent.

- **Runs.**
  - `20261103-live`: `COURSE_MODEL=gemini-3.5-flash-lite`; the API returned
    `model_version` `gemini-3.5-flash-lite`. 30 s and 2,048 output tokens per call.
  - `20261103-live-flash37`: `gemini-3.7-flash`, returned as `gemini-3.7-flash`.
    90 s and 8,192 tokens per call, because that model reasons before answering.
- **Baselines:** `20261025-baselines` (offline).
- **Frozen notebooks:** `gemini-f` v100 (sha `b268f897393d855e`) and `gemini-h` v48
  (sha `bdae8c3e0ff35eeb`).
- **Calls:** 504 model calls, 1 failed (0.2%). No episode was stopped or replayed.

Nothing below is estimated except cost; `python3 tools/eval_tables.py` regenerates both tables from the result files.

**At a glance: six wars per player** (seeds 1 and 2 on `standard`, `alternate` and `reckless`):

| Player | Won | Held out | Lost | Turns beyond passive (mean) | Model calls (failed) | Fallbacks | Est. cost USD |
|---|---|---|---|---|---|---|---|
| original-ai | 3 | 3 | 0 | +10.83 | - | 0 | - |
| model-lessons, `gemini-h` (3.7 Flash) | 2 | 2 | 2 | +8.83 | 184 (0) | 0 | 1.88 |
| model-history (3.7 Flash) | 1 | 0 | 5 | -1.33 | 42 (0) | 0 | 0.39 |
| model-lessons, `gemini-f` (3.5 Flash-Lite) | 0 | 0 | 6 | +2.17 | 133 (0) | 5 | 0.21 |
| model-obs-only (3.5 Flash-Lite) | 0 | 0 | 6 | +0.67 | 76 (1) | 0 | 0.09 |
| model-history (3.5 Flash-Lite) | 0 | 0 | 6 | -0.17 | 69 (0) | 0 | 0.10 |
| random | 0 | 0 | 6 | -2.50 | - | 0 | - |
| passive | 0 | 0 | 6 | - | - | 0 | - |

**By situation:**

| player | scenario | trials | win | held out | decisive loss | incomplete | mean turns | mean Union cities | invalid actions | fallbacks | model calls (failed) | mean latency s | tokens in / out | est. cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| original-ai | standard | 2 | 1 | 1 | 0 | 0 | 22.5 | 26.0 | 0 | 0 | - | - | - | - |
| original-ai | alternate | 2 | 2 | 0 | 0 | 0 | 6.5 | 19.0 | 0 | 0 | - | - | - | - |
| original-ai | reckless | 2 | 0 | 2 | 0 | 0 | 24.0 | 25.0 | 0 | 0 | - | - | - | - |
| model-lessons, `gemini-h` (3.7 Flash) | standard | 2 | 0 | 0 | 2 | 0 | 9.0 | 5.5 | 2 | 0 | 33 (0) | 14.36 | 149785 / 54771 | 0.3177 |
| model-lessons, `gemini-h` (3.7 Flash) | alternate | 2 | 2 | 0 | 0 | 0 | 14.0 | 22.5 | 1 | 0 | 53 (0) | 12.40 | 306837 / 85513 | 0.5508 |
| model-lessons, `gemini-h` (3.7 Flash) | reckless | 2 | 0 | 2 | 0 | 0 | 24.0 | 26.0 | 9 | 0 | 98 (0) | 12.37 | 533533 / 161984 | 1.0076 |
| model-history (3.7 Flash) | standard | 2 | 0 | 0 | 2 | 0 | 4.0 | 15.0 | 0 | 0 | 12 (0) | 14.29 | 47976 / 20642 | 0.1134 |
| model-history (3.7 Flash) | alternate | 2 | 1 | 0 | 1 | 0 | 7.5 | 16.0 | 0 | 0 | 16 (0) | 15.00 | 74108 / 26844 | 0.1562 |
| model-history (3.7 Flash) | reckless | 2 | 0 | 0 | 2 | 0 | 5.0 | 16.0 | 0 | 0 | 14 (0) | 11.81 | 60198 / 20678 | 0.1227 |
| model-lessons, `gemini-f` (3.5 Flash-Lite) | standard | 2 | 0 | 0 | 2 | 0 | 11.5 | 7.5 | 26 | 0 | 65 (0) | 1.12 | 297366 / 4674 | 0.1009 |
| model-lessons, `gemini-f` (3.5 Flash-Lite) | alternate | 2 | 0 | 0 | 2 | 0 | 5.0 | 9.0 | 0 | 0 | 13 (0) | 1.26 | 56885 / 904 | 0.0193 |
| model-lessons, `gemini-f` (3.5 Flash-Lite) | reckless | 2 | 0 | 0 | 2 | 0 | 10.5 | 5.5 | 30 | 5 | 55 (0) | 1.95 | 250096 / 3943 | 0.0849 |
| model-obs-only (3.5 Flash-Lite) | standard | 2 | 0 | 0 | 2 | 0 | 10.5 | 6.5 | 15 | 0 | 38 (0) | 1.61 | 134147 / 2702 | 0.0470 |
| model-obs-only (3.5 Flash-Lite) | alternate | 2 | 0 | 0 | 2 | 0 | 4.0 | 8.5 | 3 | 0 | 11 (0) | 1.88 | 40724 / 829 | 0.0143 |
| model-obs-only (3.5 Flash-Lite) | reckless | 2 | 0 | 0 | 2 | 0 | 8.0 | 5.5 | 10 | 0 | 27 (1) | 1.74 | 87062 / 1786 | 0.0306 |
| model-history (3.5 Flash-Lite) | standard | 2 | 0 | 0 | 2 | 0 | 8.5 | 8.5 | 10 | 0 | 28 (0) | 1.15 | 113532 / 1949 | 0.0389 |
| model-history (3.5 Flash-Lite) | alternate | 2 | 0 | 0 | 2 | 0 | 5.0 | 8.5 | 6 | 0 | 16 (0) | 1.35 | 65785 / 1238 | 0.0228 |
| model-history (3.5 Flash-Lite) | reckless | 2 | 0 | 0 | 2 | 0 | 6.5 | 7.0 | 11 | 0 | 25 (0) | 1.45 | 96327 / 1842 | 0.0335 |
| random | standard | 2 | 0 | 0 | 2 | 0 | 4.5 | 7.0 | 0 | 0 | - | - | - | - |
| random | alternate | 2 | 0 | 0 | 2 | 0 | 4.0 | 7.5 | 0 | 0 | - | - | - | - |
| random | reckless | 2 | 0 | 0 | 2 | 0 | 4.5 | 7.5 | 0 | 0 | - | - | - | - |
| passive | standard | 2 | 0 | 0 | 2 | 0 | 8.0 | 4.5 | 0 | 0 | - | - | - | - |
| passive | alternate | 2 | 0 | 0 | 2 | 0 | 5.5 | 7.5 | 0 | 0 | - | - | - | - |
| passive | reckless | 2 | 0 | 0 | 2 | 0 | 7.0 | 4.5 | 0 | 0 | - | - | - | - |

What this shows, as far as six wars per player can:

- **The 1998 AI is the strongest Union player on the held-out wars:** 3 wins, 3 hold-outs
  and no loss.
- **`gemini-h` is the only model player with a war not lost.**
  - It won both alternate wars and held out twice against the reckless opponent, which
    no player was tuned on.
  - It lost both standard wars, where the 1998 AI won one and held out the other.
- **Notes matter for the stronger model.** The same 3.7 Flash with no notes lost 5 of 6.
  That repeats the practice-war pattern: 1 of 8 not lost without notes, 6 of 8 with.
- **Flash-Lite lost every held-out war, with or without notes.** Its notebook
  (`gemini-f`) lasted longest of the three (+2.17 turns beyond passive) but refused
  orders most: 56, and 5 fallback turns, all "repeated failures" on `reckless`.
- **Memory of recent turns made no visible difference** (below).
- Two trials per situation is not a statistical test; only large differences mean
  anything.

Live commands, from `midterms/rajvardhan19/`, after loading the Vertex settings:

```sh
COURSE_MODEL=gemini-3.5-flash-lite uv run --extra live python -m cws.evaluate \
    --players model-history model-obs-only model-lessons --lessons lessons/gemini-f.json \
    --split eval --live --run 20261103-live
COURSE_MODEL=gemini-3.7-flash uv run --extra live python -m cws.evaluate \
    --players model-history model-lessons --lessons lessons/gemini-h.json \
    --split eval --live --timeout 90 --max-output-tokens 8192 --run 20261103-live-flash37
```

### The cheap players over more seeds (1-20)

Free, deterministic per seed, and not part of the paired comparison:
[results/20261025-baselines/table.md](results/20261025-baselines/table.md).

| player | scenario | trials | win | held out | decisive loss | mean turns | mean Union cities |
|---|---|---|---|---|---|---|---|
| original-ai | standard | 20 | 7 | 8 | 5 | 17.5 | 18.9 |
| original-ai | alternate | 20 | 17 | 0 | 3 | 6.7 | 19.3 |
| original-ai | reckless | 20 | 2 | 12 | 6 | 19.0 | 17.7 |
| random | standard | 20 | 0 | 0 | 20 | 4.8 | 7.0 |
| random | alternate | 20 | 0 | 0 | 20 | 4.3 | 7.2 |
| random | reckless | 20 | 0 | 0 | 20 | 5.0 | 7.0 |
| passive | standard | 20 | 0 | 0 | 20 | 7.5 | 5.2 |
| passive | alternate | 20 | 0 | 0 | 20 | 5.0 | 7.7 |
| passive | reckless | 20 | 0 | 0 | 20 | 7.7 | 4.7 |

What these show:

- **The baseline is a real competitor.** The original AI, now using its own
  fleet and trains, wins 17 of 20 on the alternate map. On the standard map
  it wins 7, holds out in 8 and loses 5. Against the reckless opponent it
  mostly holds out (12 of 20).
- **Random and passive lose every game decisively.** Random falls in 2-11
  turns, passive in 3-10.
- **The war swings more with fleets and trains.** In the 2026-10-23 run,
  before they were added, the original AI's standard-map record was 2 wins,
  17 held out and 1 loss
  ([results/20261023-baselines/](results/20261023-baselines/table.md),
  superseded). This is not a controlled comparison: the baseline was also
  corrected in between (line 2251, second review in `review.md`).
- **The suite has room in both directions.** A model can be shown to beat
  the original AI (more wins, or fewer decisive losses on `standard`), to
  match it, or to fall to the floor. With two live trials per situation,
  only large differences are visible; this is not a statistical test.

### Cost

Estimates are tokens × the dated price in `cws/evaluate.py` `PRICES`, with thinking
tokens counted as output. They are not a bill.

| Model | Input / output, USD per million tokens | As of | Source |
|---|---|---|---|
| `gemini-3.5-flash-lite` | 0.30 / 2.50 | 2026-10-23 | third-party listings quoting Vertex AI ([Maxim](https://www.getmaxim.ai/bifrost/llm-cost-calculator/provider/vertex_ai/model/gemini-3.5-flash-lite), [Requesty](https://www.requesty.ai/models-new/vertex/gemini-3.5-flash-lite)) |
| `gemini-3.5-flash` | 1.50 / 9.00 | 2026-10-27 | third-party listings ([Maxim](https://www.getmaxim.ai/bifrost/llm-cost-calculator/provider/vertex_ai/model/gemini-3.5-flash), [pricepertoken](https://pricepertoken.com/pricing-page/model/google-gemini-3.5-flash)) |
| `gemini-3.7-flash` | 0.75 / 3.75, introductory to 2026-12-31 | 2026-10-27 | [DataCamp](https://www.datacamp.com/blog/gemini-3-7-flash), [TechJack](https://techjacksolutions.com/ai-tools/google-gemini/gemini-3-7-flash/) |

Google's own pricing page did not load on any of those days, so none of these prices
is confirmed against it.

- The held-out evaluation cost about $2.66: $0.40 for the three Flash-Lite players and
  $2.27 for the two 3.7 Flash players.
- Every live run of the project together, training included, cost about $71.

## Memory experiment

The game is partially observed. Enemy leaders, experience, supply and
orders are hidden, as are the dice. So the suite compares:

- `model-history`: the observation, plus the agent's own last 3 turns
  (actions it took, its one-line notes, and each turn's visible report);
- `model-obs-only`: the observation alone. It includes the most recent
  turn's report, because a human just watched it.

- `model-lessons` (added 2026-10-26, before any evaluation game):
  `model-history` plus memory across games. That is a notebook of at most 12
  lessons that the model rewrites in a review after each training war, on
  training seeds only. It is then frozen. The review sees what the player saw
  and nothing else.

All variants get the same feedback after a rejected action. If memory does
not help, that is a result. How the learning player's notebook and play
changed during training is in `results/learn-<date>/journal.md` and
`curve.jsonl`.

**Result on the held-out wars.**
- **Within one game, memory made no visible difference.** On Flash-Lite, both
  `model-history` and `model-obs-only` lost all six. The screen-only player lasted
  slightly longer (+0.67 against -0.17 turns beyond passive), a difference six wars
  cannot separate from chance.
- **Memory across games helped, but only the stronger model could use it.**
  - Flash-Lite with its notebook (`gemini-f`): 0 of 6 not lost, +2.17 turns.
  - 3.7 Flash with its notebook (`gemini-h`): 4 of 6 not lost.
  - 3.7 Flash without one: 1 of 6.

### Learning experiments (beyond the declared suite)

Seven ways of learning from experience were trained on the same training wars (seeds
301-350, both maps, in the same order). Each was declared with its predictions before
it ran (SUITE.md). The results:

| Learner | Model | Training wars | Won / held out in training | Turns beyond passive (95% CI) |
|---|---|---|---|---|
| `gemini-b`: plain reflection | Flash-Lite | 100 | 0 / 0 | -0.25 (-0.66 to 0.17) |
| `gemini-c`: plus measured behaviour, track record and rules | Flash-Lite | 100 | 0 / 0 | +1.07 (0.33 to 1.83) |
| `gemini-d`: plus keeping the best notebook | Flash-Lite | 100 | 0 / 0 | +0.75 (0.29 to 1.21) |
| `gemini-e`: plus the 1998 AI's replay | Flash-Lite | 100 | 0 / 0 | -0.14 (-0.64 to 0.38) |
| `gemini-f`: plus a measured contrast with the 1998 AI | Flash-Lite | 100 | 0 / 0 | +2.54 (1.85 to 3.23) |
| `gemini-g`: f plus a plan each turn | Flash-Lite | 100 | 0 / 2 | +2.83 (1.99 to 3.74) |
| `gemini-h`: plain reflection | 3.7 Flash | 50 | 22 / 5 | +4.92 (3.12 to 6.74) |

- No learner kept improving after its first ten wars: each one's second half was no
  better than its first.
- On the same 50 training wars, the 1998 AI playing the Union also won 22 and lost 14
  (`gemini-h` lost 23).
- The full analysis, with figures, is in `SUITE.md` and the research report.

## Traces

- Baselines, paired seeds: [traces/20261025-baselines/](traces/20261025-baselines/).
  One JSONL per episode. The first line is a header with the result and
  configuration; then each turn's board summary and every action with
  `source` (`scripted`, `model` or `fallback`), `accepted` and the game's
  reply.
- Held-out evaluation: [traces/20261103-live/](traces/20261103-live/) and
  [traces/20261103-live-flash37/](traces/20261103-live-flash37/). Each model call is
  a line with `ok`, `error`, `latency`, tokens, the `proposed` actions and the model's
  `note`, followed by the actions actually submitted.
- Practice checks and diagnostics: `traces/dev-*`.
- Training: `traces/learn-*`, one compressed `.jsonl.gz` per war in the submitted
  copy. `gunzip -k traces/learn-*/*.jsonl.gz` restores the paths that each run's
  `curve.jsonl` names.
- Any trace can be replayed in [viewer/index.html](viewer/index.html).

## Fidelity to the original

The original game code was compiled with QB64-PE 4.7.0 and run against
this engine on the same seeds and commands. The run went through every SUB,
including SUB victor, and the main-module rule paths copied by line number.

- **48 games and 3,637 commands produced identical full game states after
  every command.** The compared state includes both fleets, the trains and
  the menus' shared `array()`. The original AI, a random player, a passive
  player and a naval test driver played the Union in all three situations.
- **Covered:** all eleven command types, including 416 navy and 212
  railroad commands, plus the computer's own fleet and trains every turn;
  nine of the ten end conditions.
- **Not reached:** annihilation, which is hand-traced in
  `tests/test_mechanics.py`.
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
| Rule invariants | `tests/test_interface.py` `Invariants` (every step of 12 whole games, including the two-month calendar); `tests/test_mechanics.py` (hand traces, every victory condition); `tests/test_navy_rail.py` (hand traces of fleets and trains); `tests/test_qb64_recorded.py` (3,685 states against the original) |
| Legal and illegal actions | `tests/test_interface.py` `LegalAndIllegal`, `InformationBoundary` (two-seed leak test) |
| A successful path and terminal outcomes | `tests/test_episodes.py` (Union wins on income, takes Richmond, deadline reached); `tests/test_interface.py` (terminal refuses everything) |
| An observed regression | `tests/test_regressions.py` (three engine bugs found on 2026-10-23); `tests/test_runner.py` `test_batch_stops_when_the_turn_resolves_whatever_the_spelling` (the review's blocking finding) |
| Episode limits | `tests/test_runner.py`: step, model-call, wall-clock (mid-game) and per-turn limits; the decision watchdog; failed calls counted; fallback labels; batches stop when the turn resolves |
| Model application (no network) | `tests/test_model_player.py`: scripted client and a stand-in Vertex SDK |

CI run for the submitted commit: the pull request's checks (`midterm-rajvardhan19`), which also run the browser UI's 15 bridge tests. Last green run, on commit `949207f`: [Actions run 42340700237](https://github.com/rajvardhan19/game-dev-f26/actions/runs/42340700237); the pull request's checks run them again on the final commit.

## Limitations

The samples are small: six held-out wars per player, so only large differences mean
anything, and I make no statistical claim. I changed things after seeing data: `gemini-h`
was stopped at 50 of its 100 training wars, and its trend test was changed after seeing the
results. The scope is narrow: one game, one model family, some rules excluded, and prices
from third-party listings. Within those limits, the best model came close to the 1998 AI
but didn't beat it.

My partner's playtest notes arrived on 2026-11-06. They found no bugs and confirmed that the agent
saw only a player's view. Their one request, a spend preview, is now in the browser UI
([PEER-NOTES.md](PEER-NOTES.md)).
