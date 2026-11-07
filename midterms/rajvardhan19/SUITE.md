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

- **Development seeds (for prompt work only):** 101-104 on `standard` and
  `alternate`. Prompt tuning may use these and nothing else.
- **Evaluation seeds:** 1 and 2 on every situation, so two live trials per
  situation per model variant. Every player runs on exactly these seeds.
- **Held out from tuning:** all evaluation seeds, and the whole `reckless`
  situation.
- **Training seeds (the learning player's notebooks only):** 201-208
  (notebook `gemini-a`) and 301-350 (notebook `gemini-b`), on `standard`
  and `alternate`, played in a fixed order (seed 201 standard, 201
  alternate, 202 standard, ...). No other player uses them, and they
  share no seed with the development or evaluation sets.
- **Extra free trials:** the cheap players (original AI, random, passive)
  also run seeds 3-20. These are reported separately from the paired
  comparison on seeds 1-2.

## Players

| Player | What it is |
|---|---|
| `model-history` | Gemini on Vertex AI (`COURSE_MODEL`, suggested `gemini-3.5-flash-lite`) with its own last 3 turns as memory |
| `model-obs-only` | the same model and prompt, without the memory: the memory ablation |
| `model-lessons` | `model-history` plus its own lessons notebook (at most 12 lessons), written by the model in a review after each training game (`cws/players/learner.py`). It learns only on the training seeds and is frozen before any development check or evaluation game: memory across games |
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
python -m cws.learn train --book lessons/<name>.json --run learn-<date> --live      # training seeds only
python -m cws.learn freeze --book lessons/<name>.json                              # before any check
python -m cws.evaluate --players model-lessons --lessons lessons/<name>.json --split dev --live --run dev-<n>
```

## Changes after declaration

- **2026-11-03: the held-out evaluation, declared before any evaluation
  game.** No model has played seeds 1-2 or the `reckless` situation.
  - **Players.**
    - The declared pair: `model-history` and `model-obs-only`, on
      `gemini-3.5-flash-lite`, with the declared limits (30 s, 2,048
      output tokens).
    - Two learned notebooks, chosen from training and practice results
      only:
      - `gemini-f` (Flash-Lite, the same limits), the best notebook its
        model wrote;
      - `gemini-h`, on `gemini-3.7-flash` (90 s, 8,192 tokens), with
        `model-history` on 3.7 Flash as its no-notes control.
  - **Runs.** `20261103-live` (the three Flash-Lite players) and
    `20261103-live-flash37` (the two 3.7 Flash players). Each player plays
    seeds 1 and 2 on `standard`, `alternate` and `reckless`: 6 episodes,
    30 in all.
  - **Compared with** the original AI, random and passive on the same
    seeds (`20261025-baselines`).
  - **Reported as observed:** tiers, turns, Union cities, invalid
    actions, fallbacks, failed calls, latency, tokens and estimated cost.
    No player or prompt changes after this point.
  - **If a network failure stops a run** (the guard stops an episode with
    half or more failed calls, without recording it), only the
    unrecorded episodes are played again, with `--seeds`. Recorded
    episodes are never replayed.
  - **Done the same day.** 30 episodes; 1 of 504 model calls failed
    (0.2%); no episode stopped or replayed. About $2.66. Tables in
    EVALUATION.md (`tools/eval_tables.py`). Six wars per player, as won /
    held out / lost:
    - original AI 3 / 3 / 0;
    - `gemini-h` (3.7 Flash) 2 / 2 / 2: both alternate wars won, both
      reckless wars held out, both standard wars lost;
    - `model-history` on 3.7 Flash 1 / 0 / 5;
    - every Flash-Lite player 0 / 0 / 6, with turns beyond passive:
      `gemini-f` +2.17, `model-obs-only` +0.67, `model-history` -0.17;
    - random and passive 0 / 0 / 6.

- **2026-10-27: `gemini-h`, a frontier model with the plain method.**
  Declared before any of it runs.
  - **Model.** `gemini-3.7-flash`, the newest Gemini this project can
    call. Gemini 3.5 Pro is not released; `gemini-3.1-pro-preview` is
    callable but an older generation. Introductory price $0.75 / $3.75 per
    million tokens to 2026-12-31 (third-party listings; Google's page not
    retrieved), now in `cws/evaluate.py` with 3.5 Flash's $1.50 / $9.00.
    Priced afterwards, the four 3.5 Flash runs cost about $30.55.
  - **Method.** `gemini-b`'s plain method: after each game the same model
    reviews only what the player saw and rewrites its own notebook. There
    is no mirror, track record, contrast, teacher or reference. Same 100
    games (seeds 301-350, same order). Limits `--timeout 90`,
    `--max-output-tokens 8192`; the review gets 8,192 tokens and 90 s.
    Stops at an estimated $75.
  - **Order.**
    1. A no-notebook control: `model-history` on the 8 practice games
       (`dev-20261027-history-flash37`). This also checks the model works;
       the chain stops if 10% or more of its calls fail.
    2. Training (`learn-20261027-h`), then freeze and journal.
    3. The frozen notebook's check on the 8 practice games
       (`dev-learn-20261027-h`).
  - **Valid** only if fewer than 10% of calls fail, in training and in each
    run of 8.
  - **Predictions:**
    1. A gain over the passive player above `gemini-b`'s -0.25, on a
       paired test over the same 100 games.
    2. It improves with experience: games 51-100 gain more than games
       1-50 (permutation test).
    3. The frozen notebook's check has at least 2 more games not lost
       than the control.
  - Also compared with `gemini-f` (+2.54) and with `gemini-f` played by
    3.5 Flash (6 of 8 not lost).
  - **Control done. Valid:** 4 of 76 calls failed (5.3%). 1 of 8 not
    lost: a Union victory on standard 101 in 4 turns.
  - **Network drop at game 50 (22:50).** Every call failed on name
    resolution. The guard stopped training without recording game 50.
    The Mac did not sleep (`pmset` log), and the connection was back by
    22:57. Game 49's review also failed on the network, so game 50 uses
    notebook v47, as after any failed review.
    - Training resumed from game 50 with the same command.
    - Before the drop: 49 games, 21 wins, 5 hold-outs, 29 failed calls of
      1,063 (2.7%). Reviews failed after games 45 (a 504) and 49 (the
      network).
  - **Stopped at 50 games, at the student's request,** after the drop.
    The notebook is frozen after game 50, and the check runs as declared.
    - Prediction 1 is tested on the same 50 games as `gemini-b`'s first
      50.
    - Prediction 2 becomes games 26-50 against 1-25. This change was made
      after seeing the first 49 games' wins by block (no clear rise), so
      it is weaker evidence than a declared split.
  - **Training done** (`learn-20261027-h`, 50 games, about $11.29).
    **Valid:** 29 of 1,077 calls failed (2.7%), with 4 fallback moves.
    Frozen at v48 (sha `bdae8c3e0ff35eeb`).
    - **22 wins and 5 hold-outs in 50 games** (17 wins on alternate; 5
      wins and 5 hold-outs on standard). Every Flash-Lite learner had 0 or
      1 over the same 50 games.
    - Gain over the passive player +4.92 turns (+6.04 standard / +3.80
      alternate). Wins average 11 turns, so turns understate it.
    - **Prediction 1 met:** against `gemini-b`'s -0.40 on the same 50
      games, +5.32 paired (p < 0.0001, sign-flip test, 100,000 draws).
    - It is also ahead of every engineered method on the same 50 games:
      `gemini-c` +3.86 (p < 0.0001), `gemini-f` +2.14 (p = 0.04),
      `gemini-g` +2.16 (p = 0.02).
    - **Prediction 2 not met:** games 26-50 gained 2.08 turns more than
      games 1-25, but p = 0.27. Games not lost were 13 and 14. The gain is
      there from the first games; on this evidence it comes from the
      model, not from its notes.
    - It attacks 0.95 times a turn, 3-6 times as often as the Flash-Lite
      learners, and recruits 1.54 times a turn. Washington fell in 11
      games, against 2-6 for the others over the same games. A first count
      said 15; it wrongly included 4 Union wins by taking Richmond.
    - Against the original AI playing the Union on the same 50 games
      (`learn-20261026-b-reference`):
      - By tier, `gemini-h` is better in 9 games, worse in 18 and the same
        in 23 (sign test p = 0.12). By turns over the passive player it is
        -2.66 (p = 0.06).
      - Standard: 5 wins, 5 hold-outs and 15 losses, against the original
        AI's 1, 14 and 10.
      - Alternate: 17 wins and 8 losses, against 21 and 4. Where both won,
        the original AI was faster (7.6 turns against 9.8).
  - **Check stopped by a second network drop** (about 00:04). Six games
    were recorded: standard 101-104 and alternate 101-102. On alternate
    103, all 12 calls failed, and the guard stopped without recording it.
    The Mac did not sleep.
    - The six recorded games are kept, not replayed: replaying them after
      seeing them would re-roll a result.
    - Only alternate 103 and 104 are played, with the new `--seeds` filter
      in `cws/evaluate.py`. It only narrows the split's own seeds. They
      play as `dev-learn-20261027-h-rest` and are merged into
      `dev-learn-20261027-h`.
    - The failed partial trace is kept as
      `invalid-network-model-lessons-alternate-103.jsonl`.
  - **Check done** (`dev-learn-20261027-h`, 8 games, about $2.83).
    **Valid:** 13 of 298 calls failed (4.4%).
    - Twelve of the 13 failures, and all 4 fallback moves, fell in
      alternate 102, played just before the drop. That game was lost on
      income in May 1864.
    - **6 of 8 not lost:** 3 wins (alternate 101 and 103 by share of
      income; standard 102 on cities controlled, September 1864) and 3
      hold-outs (standard 101, 103, 104, to March 1865). Washington fell
      once (alternate 104).
    - Gain over the passive player +10.75 turns (+16.25 standard / +5.25
      alternate).
    - **Prediction 3 met:** 6 games not lost against the control's 1.
  - **Reading.**
    - On the practice games, 3.7 Flash with a notebook it wrote by the
      plain method does as well as 3.5 Flash with `gemini-f`'s engineered
      notebook (6 of 8 not lost, +10.0), and better than the original AI
      (5 of 8).
    - Without a notebook it lost 7 of 8, so the notes matter.
    - Training showed no rise between its halves (prediction 2). If the
      notes help, they help within the first few games.
    - That last point is a reading after the fact, not a test: the
      no-notebook control is on the practice seeds, not on the training
      seeds.


- **2026-10-27: the stronger model with a learned notebook.** Declared
  before it runs.
  - `gemini-3.5-flash` plays with `gemini-f`'s frozen notebook (v100, sha
    `b268f897393d855e`), which Flash-Lite wrote in training. Only the
    playing model changes. Limits as in `dev-20261026-oracle-flash2`:
    `--max-output-tokens 8192`, `--timeout 90`, no aids. Practice seeds
    101-104, both maps (`dev-20261027-gemini-f-flash`).
  - Valid only if fewer than 10% of calls fail. Price not in
    `cws/evaluate.py`; tokens are reported.
  - Compared with `gemini-f` under Flash-Lite on the same games (14.75 /
    6.25 turns, no win or hold-out) and the ceiling-test notebook under
    Flash (2 wins, 3 hold-outs).
  - Bar: if it wins or holds out at least one game, `gemini-f` played by
    Flash becomes a candidate evaluation player, since its notebook is
    the agent's own. If not, the learned notebook is the limit. A short
    Flash training run would then come next, declared separately.
  - **Done the same day. Valid:** 3 of 261 calls failed (1.15%: two 504s
    and one 429), with no fallback moves. **Meets the bar.**
    - **3 Union victories** on alternate (seeds 101, 103 and 104, by
      share of income, May to November 1863). **3 hold-outs** on standard
      (101-103, to March 1865).
    - Two losses: alternate 102 on cities controlled in March 1862, and
      standard 104 when Washington fell in January 1862.
    - Gain over the passive player: +10.00 turns (+12.25 standard / +7.75
      alternate). A win ends the game early, so turns understate it.
    - Played by Flash-Lite, the same notebook had no win or hold-out on
      these games. The original AI had 4 wins and 1 hold-out. The
      ceiling-test notebook under Flash had 2 wins and 3 hold-outs.
    - Tokens 1,350,188 in / 1,005,455 out, about 1.6 hours of play.
    - Open question: how much of this is the notebook and how much is
      Flash alone. Flash without a notebook has not been run on these
      games.
  - **Control, declared before it runs:** `model-history` (memory of its
    last 3 turns, no notebook) played by `gemini-3.5-flash`, same limits,
    same 8 games (`dev-20261027-history-flash`). Valid only if fewer than
    10% of calls fail. Flash-Lite as `model-history` lost all 8 of these
    games (`dev-20261026`).
    - Reading, by games not lost (the notebook run had 6 of 8):
      - 5 or more: the result is mostly Flash itself.
      - 3 or fewer: the learned notebook adds a clear part.
      - 4: unresolved on 8 games.
    - **Done the same day. Valid:** 3 of 114 calls failed (2.6%: two 429s
      and one 504), with no fallback moves.
      - **1 game not lost of 8, so the learned notebook adds a clear
        part.** The one game was a Union victory on alternate 101 by share
        of income, December 1861.
      - The other 7 were lost, Washington falling in 5 of them, by
        January 1863 at the latest on standard. Standard 104 lasted to
        November 1864.
      - Gain over the passive player +3.50 turns (+5.50 standard / +1.50
        alternate), against +10.00 with the notebook.
      - Tokens 492,129 in / 417,671 out, about 0.7 hours of play.
    - The four runs on these 8 games, by games not lost and gain over the
      passive player:
      - Flash-Lite without a notebook: 0, -0.13.
      - Flash-Lite with `gemini-f`: 0, +4.50.
      - Flash without a notebook: 1, +3.50.
      - Flash with `gemini-f`: 6, +10.00.
    - Neither the notebook nor the stronger model is enough alone; the
      gain comes from both together. Eight games, so only the large
      difference counts.

- **2026-10-26: `gemini-g`, and a fair re-run of the stronger model.**
  Declared before either runs.
  - `gemini-g`: `gemini-f`'s method (mirror, track record, actionable,
    contrast) with the player planning each turn before ordering
    (`--plan`), on the same 100 games (seeds 301-350, same order). The
    frozen notebook keeps the plan step when checked or evaluated.
    Predictions: a gain over the passive player above `gemini-f`'s +2.54
    on a paired test over the same games; at least one win or hold-out in
    training; fewer games with Washington lost than `gemini-f`.
  - Then the stronger-model diagnostic again, with limits that suit a
    model that reasons before answering: `gemini-3.5-flash`,
    `--max-output-tokens 8192`, `--timeout 90` (runner watchdog 105 s), the
    ceiling-test notebook, no aids, practice seeds 101-104
    (`dev-20261026-oracle-flash2`). Valid only if fewer than 10% of calls
    fail. Its price is not in `cws/evaluate.py`; tokens are reported.
  - **First attempt invalid: a network outage.** From game 17, every
    call failed on name resolution ("nodename nor servname provided"),
    and the runner played the remaining games as end-turn fallbacks. The
    notebook froze at v16; the check and the stronger-model run failed
    entirely (no tokens used). Games 1-16 were valid: +5.7 turns over the
    passive player in games 1-10, with hold-outs in games 9 and 12, at
    about $1.23. Everything is kept under `invalid-network-*` names.
  - Training and evaluation now stop when half or more of a game's model
    calls fail, without recording that game, so an outage can no longer
    turn into fallback games (`tests/test_learner.py`). Both runs restart
    from scratch under the declared names.
  - **`gemini-g` done** (`learn-20261026-g`, about $5.58), with 0 of
    2,358 calls failed. Frozen at v100 (sha `b7de0f45a16f8f99`), 9
    lessons.
    - It gained +2.83 turns over the passive player, against `gemini-f`'s
      +2.54: +0.29 paired, p = 0.61, so prediction 1 is not met.
    - Two hold-outs in training (games 17 and 69, standard): prediction 2
      is met.
    - Washington was lost in 8 games, the same as `gemini-f`: prediction 3
      is not met.
    - Games 1-50 averaged +2.76 and games 51-100 +2.90.
  - Check (`dev-learn-20261026-g`): standard 9.25 turns against the
    passive player's 7.0, alternate 6.5 against 5.0, with no win or
    hold-out.
  - **Stronger-model diagnostic done** (`dev-20261026-oracle-flash2`,
    2026-10-27). **Valid:** 27 of 271 calls failed (9.96%), all on the
    service side: 13 disconnects, 9 rate limits (429), 3 deadlines (504)
    and 2 read timeouts. None reached the output cap. There were 3
    fallback moves, none in a game it won.
    - **2 Union victories** on alternate (seeds 102 and 103, by share of
      income, September 1863 and January 1863). **3 hold-outs** on
      standard (101, 102 and 104, to March 1865). Washington fell on
      standard 103 in turn 20, and the other two alternate games were lost
      by turn 7.
    - Gain over the passive player: +10.50 turns (+16.00 standard / +5.00
      alternate). With the same notebook, `gemini-3.5-flash-lite` gained
      +6.50 and had no win or hold-out. A win ends the game early, so
      turns understate the alternate result.
    - The original AI on the same games had 4 wins and 1 hold-out (all
      alternate wins, by turn 9; one standard hold-out). The stronger model
      matches its 5 of 8 non-losses; it does worse on alternate and better
      on standard.
    - Tokens 1,277,430 in / 1,125,511 out, mean latency about 25 s a
      call, about 1.9 hours of play. Price not in `cws/evaluate.py`.
    - Reading: with the right knowledge, the model is the larger lever.
      The cheaper model knew the same rules and could not carry them out.
      This is one notebook we wrote, on 8 practice games, so it is not an
      evaluation result.

- **2026-10-26: execution diagnostics, declared before they run.** The
  student wants to keep improving the agent. The ceiling test showed
  knowledge lifts survival (+6.5 turns) but not winning (0 of 8), so these
  test execution. Knowledge is held fixed: every run plays
  `lessons/oracle-diagnostic.json` on practice seeds 101-104, both maps.
  None of these is an evaluation player.
  1. `--aids fronts` (`dev-20261026-oracle-fronts`): the prompt adds a
     front summary, the map organised by army (neighbouring cities, owner,
     enemy men seen there) and the threatened Union cities. It uses only
     what the observation shows.
  2. `--aids plan` (`dev-20261026-oracle-plan`): one extra call at the
     start of each turn writes a short plan; the order calls then show it.
  3. `--aids fronts,plan` (`dev-20261026-oracle-both`).
  4. `COURSE_MODEL=gemini-3.5-flash` with no aids
     (`dev-20261026-oracle-flash`), to see whether the model itself is the
     limit. Its price is not in `cws/evaluate.py`, so its cost is reported
     as tokens.

  An aid helps if it wins or holds out a game, or clearly beats the
  ceiling test's +6.5 turns over the passive player (8 games: large
  differences only). Helpful aids are then combined with `gemini-f`'s
  learning method in a new 100-game run, declared separately.
  - **Done the same day.** Gain over the passive player on the same
    games (standard / alternate); ceiling test without aids: +6.50 (+4.25
    / +8.75), no win or hold-out.
    - *fronts*: +6.25 (-2.75 / +15.25). 2 hold-outs (alternate 101 and
      104, to November 1865), but Washington was lost in 5 of 8 games; on
      standard three times by turn 3, when McDowell left the capital for an
      empty neighbour. Meets the bar.
    - *plan*: +5.25 (-0.50 / +11.00). **Union victory on standard 104**
      (Richmond captured, November 1861: Gemini's first win) and a hold-out
      on alternate 103. Washington was lost once. Meets the bar.
    - *fronts,plan*: +2.88 (-1.50 / +7.25), no win or hold-out. Does not
      meet the bar.
    - *gemini-3.5-flash*: **not valid.** 127 of 141 calls failed: 106
      reached the 2,048-token output cap (that model spends output tokens
      on reasoning) and 20 hit the 30 s timeout, so the runner ended most
      turns.
    - About $2.59 for the three valid runs. Each is 8 games, so only the
      wins and hold-outs are clear signals.

- **2026-10-26: `gemini-f`, learning from a measured contrast.** Declared
  before its first game, after `gemini-e` showed that a raw replay of the
  teacher is not enough.
  - `gemini-c`'s method on the same 100 games (seeds 301-350, same
    order). After each game the review also sees, measured:
    1. its rates against the original AI's on the same game: recruits,
       battles started and won, drills and moves a turn, peak cities, cash
       going into the last turn, and the result;
    2. across all its games so far, its mean turns beyond the passive
       player grouped by its recruiting, attacking and drilling rates.

    Gemini still writes every lesson. No replay log is shown.
  - Predictions: a gain over the passive player above `gemini-c`'s +1.07
    on a paired test over the same games; recruits and attacks a turn both
    above `gemini-c`'s (1.17 and 0.25); at least one win or hold-out.
  - Run by `tools/learn_pipeline.sh gemini-f learn-20261026-f 301-350
    --mirror --track-record --actionable --contrast --reference
    learn-20261026-b-reference`; status every 10 games.
  - **Done the same day** (`learn-20261026-f`, about $3.52; check about
    $0.26). Frozen at v100 (sha `b268f897393d855e`), 7 lessons.
    - It gained +2.54 turns over the passive player on the same 100 games,
      against `gemini-c`'s +1.07: +1.47 paired, p = 0.0025, so prediction 1
      is met. It outlasted the passive player in 68 of 100 games
      (`gemini-c`: 53).
    - Prediction 2 is half met: 1.58 recruits a turn (above 1.17), but
      0.24 attacks a turn (not above 0.25).
    - Prediction 3 failed: no win or hold-out.
    - No trend inside the run: +2.78 in games 1-50, +2.30 in games 51-100;
      the slope is -1.2 turns per 100 games, p = 0.31.
  - Check: standard 14.75 turns against the passive player's 7.0, the best
    practice-check result of any notebook. Alternate 6.25 against 5.0.

- **2026-10-26: next experiment, declared before it runs.** The question is
  whether the learner's ceiling is knowledge or execution.
  - *Step 1, ceiling test (diagnostic, never a player).*
    `lessons/oracle-diagnostic.json` is written by the implementation
    agent from the original AI's measured play on the training seeds: about
    2 recruits and 1.5 attacks a turn, little drilling, rail and fleet
    every game. It plays practice seeds 101-104 on both maps
    (`dev-20261026-oracle`). It counts as reaching its ceiling if any
    game is won or held out, or it gains 2 or more turns over the passive
    player on average; otherwise the limit is execution.
  - *Step 2, if the limit is knowledge: `gemini-e`, learning with a
    teacher.* It uses `gemini-c`'s method on the same 100 games; after each
    game the review also sees the original AI's game on the same seed
    (result, orders per turn, cities taken), and writes its own lessons.
    Predictions: recruiting above 1.5 and attacks above 0.8 per turn; a
    gain over the passive player larger than `gemini-c`'s +1.07, on a
    paired test over the same games; at least one win or hold-out on
    alternate. Reported as its own condition (learning from
    demonstration), beside the self-taught notebooks.
  - **Step 1 done** (`dev-20261026-oracle`, about $0.59). It gained +6.5
    turns over the passive player on the same games (standard +4.25,
    alternate +8.75; longest game 22 turns), with no win or hold-out. The
    declared bar is met: the limit is knowledge, so Step 2 (`gemini-e`)
    ran.
  - **Step 2 done** (`learn-20261026-e`, about $1.74; check about $0.12).
    Every prediction failed:
    - It gained -0.14 turns over the passive player, against `gemini-c`'s
      +1.07: -1.21 on the same games, paired p = 0.006. That is
      significantly worse.
    - 0.40 recruits and 0.35 attacks a turn (predicted above 1.5 and 0.8).
    - No win or hold-out.

    Its notebook copied the teacher's visible habits (fleet, fortify,
    supply, moving on neutral cities) and set a $300 threshold for
    recruiting, but never the tempo that made the teacher win. Check:
    standard 8.75 turns, alternate 4.0. Frozen at v100 (sha
    `ea436d9d292b000d`).

- **2026-10-26: a fourth notebook, `gemini-d`, at the student's request.**
  Declared before its first game. Same 100 games as `gemini-b` and
  `gemini-c` (seeds 301-350, same order), same player and review model,
  and `gemini-c`'s three switches. It adds three changes to how it learns,
  never what:
  1. *champion and challenger*: the notebook plays rounds of 5 games. A
     new version replaces the current one unless its round score (mean
     turns against the passive player, same games) is more than 0.5 turns
     below the current one's. Otherwise the review improves the current
     one again. The notebook kept at the end is the last champion. This
     also means the review runs after every round of 5 games, seeing all
     5, instead of after every game;
  2. *opening plan per map*: the review writes turn-1 orders for each map,
     shown to the player on turn 1 only;
  3. *priority order*: lessons are asked for most important first; the
     player is told the earlier lesson wins a conflict.
  - Run by `tools/learn_pipeline.sh ... --select 5 --priority --openings`
    (train, freeze, journal, check on 101-104), with status every 10
    games in `results/learn-20261026-d/status.md`.
  - These changes come together, so a difference from `gemini-c` cannot
    be split between them.
  - **Done the same day.** `learn-20261026-d`: 100 games, all decisive
    losses, about $1.84.
    - 7 of 19 challengers were kept. The kept notebook is champion v14,
      from round 15, which scored +3.0; no later challenger came within 0.5
      of that one lucky round. Frozen as v20 (sha `66a976c6197fdf1f`), 6
      lessons. Only the standard map got an opening plan.
    - On the same 100 games, against the passive player: +0.75 turns (it
      outlasted it in 54 of 100). That is +1.00 against `gemini-b`
      (p < 0.001) and -0.32 against `gemini-c` (p = 0.40, no difference).
    - Its play turned defensive: 19.8 drills, 1.6 recruits and 0.45
      attacks a game (`gemini-c`: 13.9, 9.1 and 1.7).
  - Check (`dev-learn-20261026-d`, about $0.14): standard 8.0 turns,
    alternate 6.0, every game lost on city count and none by losing
    Washington.

- **2026-10-26: a third notebook, `gemini-c`, at the student's request.**
  Declared before its first game.
  - The same 100 games as `gemini-b` (seeds 301-350, same order), so
    the two learning curves compare game by game.
  - The same player, review model, limits and notebook size. Only how the
    review learns changes; every lesson is still written by the model
    itself. Three switches:
    1. *mirror*: the review also sees what the player actually did that
       game (order counts, battles, cash each turn, army size), measured
       from its own orders;
    2. *track record*: each lesson shows the games it was in the notebook
       for, and the mean turns lasted against the passive player on the
       same seed (`learn-20261026-b-reference`), this game included;
    3. *actionable*: lessons are asked for as "When <what you see>, <the
       orders>" rules.
  - Run unattended by `tools/learn_pipeline.sh` (train, freeze, journal,
    check on 101-104), with a progress report every 10 games in
    `results/learn-20261026-c/status.md`.
  - All three switches change at once, so a difference from `gemini-b`
    cannot be split between them without further runs.
  - **Done the same day.** `learn-20261026-c`: 100 games, 100 reviews,
    all decisive losses, about $2.81. The notebook was frozen at version
    100 (sha `077d5b63649dbcc6`).
    - On the same 100 games it lasted 1.32 turns longer than `gemini-b`
      (paired sign-flip p = 0.002): standard 8.3 against 7.3, alternate
      6.6 against 5.0. It outlasted the passive player in 53 of 100 games
      (`gemini-b`: 34).
    - It recruited in 82 games (`gemini-b`: 37) and won 63 of 172 attacks
      (`gemini-b`: 21 of 149).
    - No trend inside the run: against the passive player it averaged
      +1.06 turns in the first 50 games and +1.08 in the last 50.
  - Check (`dev-learn-20261026-c`, about $0.12): standard 3.5 turns,
    alternate 6.0. In 3 of 4 standard games its first orders emptied
    Washington and Jackson took it on turn 2, against its own lessons 6
    and 8.

- **2026-10-26: a second notebook, `gemini-b`, trained on 100 games, at
  the student's request.** Declared before its first game.
  - Seeds 301-350 on both maps, normal aggression: 100 different games.
    The held-out `reckless` opponent and any setting not checked against
    QB64 stay out of training.
  - Same player, review prompt and limits as `gemini-a`, starting from an
    empty notebook. One change for long runs: the review's scoreboard
    summarises games older than the last 20 per map instead of listing
    them all. It is identical to `gemini-a`'s for the first 20 games.
  - Played in blocks of 10 games (`--games 10, 20, ...`); the run resumes
    where it stopped.
  - When the 100 games are done the notebook is frozen and checked on
    seeds 101-104, as `gemini-a` was. Which frozen notebook or notebooks
    enter the evaluation is decided from training and development results
    only, before any evaluation game.
  - **Done the same day.** `learn-20261026-b`: 100 games, 100 reviews,
    all decisive losses. About $1.88. The notebook `lessons/gemini-b.json`
    was frozen at version 100 (sha `2aca9bd2a15690a9`).
    - Against the passive player on the same seeds, the first 50 games
      averaged -0.40 turns and the last 50 -0.10. The slope is +0.14 turns
      per 100 games, with permutation p = 0.85: no detectable trend.
  - Check (`dev-20261026-lessons-b`, about $0.20), mean turns on seeds
    101-104, all decisive losses:

    | Map | gemini-b | gemini-a | No notebook | Passive |
    |---|---|---|---|---|
    | standard | 6.8 | 8.8 | 7.2 | 7.0 |
    | alternate | 9.0 | 4.0 | 4.5 | 5.0 |

    On alternate, `gemini-b` lasted 17 turns on seed 103. It recruited 33
    times and grew to 256,500 men, but attacked only 4 times.

- **2026-10-26: a learning player, at the student's request.** Declared
  before any training game, and before any model has played an
  evaluation seed.
  - New player `model-lessons` and training seeds 201-208 (above).
  - Protocol: train on all 16 scheduled games, then freeze the final
    notebook version. There is no choosing among versions by results.
    Check it on the development seeds 101-104 against the `model-history`
    games of 2026-10-26 (same seeds), then run it once with the others on
    the evaluation seeds.
  - The review after each game sees only what the player saw (its orders,
    refusals, notes, the visible reports and the end screen), never the
    seed, the dice or the opponent's code (`tests/test_learner.py`).
  - Each training game's result, notebook version and measured behaviour
    is in `results/<run>/curve.jsonl`; every notebook version, with what
    changed and why, is kept in `lessons/<name>.json`.
  - **Done the same day.** `learn-20261026`: 16 games, 16 reviews, all
    decisive losses. The notebook `lessons/gemini-a.json` was frozen at
    version 16 (sha `e7862f80e966d088`). About $0.27.
  - Check (`dev-20261026-lessons`, about $0.14), mean turns survived on
    seeds 101-104, all decisive losses:

    | Map | Frozen notebook | No notebook (2026-10-26) | Passive |
    |---|---|---|---|
    | standard | 8.8 | 7.2 | 7.0 |
    | alternate | 4.0 | 4.5 | 5.0 |

    The notebook player recruited 27 times in these 8 games, where
    `model-history` recruited 0 times.

- **2026-10-26: development seeds 103 and 104 added, at the student's request,**
  for exploratory live runs of both memory variants. Evaluation seeds (1, 2) and
  the held-out `reckless` situation are unchanged and still unplayed by any model.

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
