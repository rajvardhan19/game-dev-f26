# Declared evaluation suite

Declared **2026-10-23**, before any prompt tuning and before any live model
call. The same definition is in code (`cws/evaluate.py`, `SUITE`), so the
runs and this file cannot drift apart. Changes after this date are listed at
the bottom with their reason.

## Starting situations

| Situation | What it is | Why it is in the suite |
|---|---|---|
| `standard` | `CWS.INI`, March 1861: the original map, leaders and order of battle; deadline March 1865 (24 turns); opponent aggression NORMAL (3) | The game as shipped. The original AI wins, holds out or loses here (7, 8 and 5 of 20 seeds), so a player can show up as stronger or weaker. |
| `alternate` | `ALTMAP.INI`, April 1861: the alternate map, leaders and setup the original ships with `ALTMAP.BAT`; 60% income wins; deadline October 1865 | Different geography and conditions. The original AI usually wins quickly (17 of 20 seeds), so it measures competence and speed. |
| `reckless` | `CWS.INI` with the Utility menu's opponent aggression at RECKLESS (5) | **Held out.** A stronger, different opponent never seen during prompt work. |

## Seeds and splits

- **Development seeds (for prompt work only):** 101, 102 on `standard` and
  `alternate`. Prompt tuning may use these and nothing else.
- **Evaluation seeds:** 1 and 2 on every situation, so two live trials per
  situation per model variant. Every player runs on exactly these seeds.
- **Held out from tuning:** all evaluation seeds, and the whole `reckless`
  situation.
- **Extra free trials:** the cheap players (original AI, random, passive)
  also run seeds 3-20. These are reported separately from the paired
  comparison on seeds 1-2.

## Players

| Player | What it is |
|---|---|
| `model-history` | Gemini on Vertex AI (`COURSE_MODEL`, suggested `gemini-3.5-flash-lite`) with its own last 3 turns as memory |
| `model-obs-only` | the same model and prompt, without the memory: the memory ablation |
| `original-ai` | the original game's `smarts`/`evaluate` playing the Union on the Union's observation: the strong baseline |
| `random` | uniform over legal actions, ending the turn with probability 1/5: the floor |
| `passive` | ends every turn: the do-nothing floor |

## Outcome measures (decided before running)

1. **Outcome tier**, from the game's own end screens: *win* (any Union
   victory condition); *held out* ("Confederates will win a technical
   victory": the deadline passed); *decisive loss* (any other Rebel
   victory condition); *incomplete* (a runner limit ended the episode).
2. **Turns:** fewer to a win, or more before a decisive loss.
3. **Reported as well:** Union cities at the end, VP share, invalid
   actions, fallback actions, model calls (failed), latency, tokens and
   estimated cost.

## Limits (same for every player)

600 steps; 150 model calls; 30 s and one attempt per call; 30 minutes per
episode; 40 actions per turn; 3 failures per turn before the runner ends the
turn (labelled `fallback`).

## Commands

From `midterms/rajvardhan19/`:

```sh
python -m cws.evaluate --players original-ai random passive --extra-baseline-seeds --run 20261025-baselines
python -m cws.evaluate --players model-history model-obs-only --split eval --live --run <date>-live
python -m cws.evaluate --players model-history --split dev --live --run dev-<n>   # tuning only
```

## Changes after declaration

- **2026-10-25: navies and railroads added to the game, at the student's
  request.**
  - This was before any live model run or prompt tuning, so no player had
    been tuned on the old rules.
  - Situations, seeds, players, measures and limits are unchanged. Every
    player meets the same expanded game.
  - The baselines were re-run (`20261025-baselines`); the 2026-10-23 run is
    superseded and kept in `results/20261023-baselines/`.

- **2026-10-25, after the second independent review (navies and railroads).**
  No change to situations, seeds, players, measures or limits.
  - The Union baseline dropped line 2251's `navysize(1) < 1` test, so it
    stopped fortifying half the time where the original goes on. Fixed, and
    `20261025-baselines` re-run in place. Original AI over 20 seeds: standard
    7 wins, 8 held out, 5 losses (was 5, 7, 8); alternate 17, 0, 3 (was 19,
    0, 1); reckless unchanged at 2, 12, 6. Random and passive are unchanged.
  - The "why" column above was written from the 2026-10-23 run ("usually
    holds out", "always wins") and is restated from the current run.

- **2026-10-25, prompt change (dev seeds only).** The prompt grouped
  `move` and `rail` actions by army (`move 4 <city>, <city> one of: ...`).
  In the first dev episode (`results/dev-20261025/`, standard seed 101) the
  model answered "move 4 Paducah, Lexington". The prompt now lists every
  legal action whole, one per line.
  - Re-tested with `model-history` on dev seeds 101 and 102, standard and
    alternate (`results/dev-20261025-fulllist/`).
  - No format errors. The 5 rejected actions were all made illegal by an
    earlier action in the same batch: drilling an army just ordered to
    move (3), and a second fleet order in one turn (2).
  - All 4 games were decisive losses in 4-8 turns. The model never
    recruited.
  - 27 calls, none failed, about $0.04. No evaluation seed was played.

- **2026-10-23, after the independent review.** No change to situations,
  seeds or measures. The tooling now refuses a model run without an
  explicit `--split`, and watching a model defaults to dev seed 101, so
  that evaluation seeds cannot be played by accident during prompt work.
