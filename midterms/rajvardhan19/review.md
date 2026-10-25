# Independent review

- **Reviewer:** a fresh Claude Code subagent (`claude-opus-5-5`), 2026-10-23,
  given only `.claude/agents/rules-reviewer.md`'s instructions and the
  project path.
- **Context:** it had none of the implementation session's context, and no
  instruction to approve.
- **Tools:** read-only (Read, Grep, Glob; Bash for inspection only). It wrote
  no files.

The report below is verbatim. The implementation agent's response to each
finding is in "Response" at the end. The student's decisions are in
AGENT-TEAM.md.

---

## Rules review: VGA Civil War Strategy v2.11 midterm (read-only)

Most serious first.

[blocking] cws/runner.py:161: a batch only stops at an exact lowercase `"end turn"` or `"troops"`, but `step` accepts any case or spacing (cws/interface.py:166-169). So a model reply like `"End turn"` resolves the turn and the rest of the batch runs blind in the next turn. Evidence: offline run with `FakeClient([{"actions": ["End turn", "move 1 Manassas", "end turn"]}])` on standard seed 101. One model call resolved two turns. `move 1 Manassas` was accepted in turn 2 without a new observation, and the trace and `memory["this_turn"]` (runner.py:153-155) logged it under turn 1. This contradicts docs/rule-source-map.md:203 ("stops ... after troops ... or at end turn"). The same happens with `"Troops"`: recruits get guessed before the list is seen. Fix: break when `res["observation"]["turn"]` changes, or compare the normalised string.

[should fix] README.md:98 and cws/play.py:180: the documented way to watch the live model (`cws.play --watch model-history --live`) defaults to standard seed 1, which is a held-out evaluation seed. SUITE.md:22-23 says every evaluation seed is held out from tuning. Relatedly, cws/evaluate.py:113 defaults to `--split eval`, so any model run that forgets `--split dev` plays held-out cases. Make dev the default for model players, or refuse eval without an explicit flag.

[should fix] tools/qb64-harness/make_harness.py:148-167 and compare.py:106-108: the differential "E" command runs tupdate and the newmonth bookkeeping but never calls SUB victor, and the Python replay uses `newmonth()` + `topbar()`, not `end_turn()`. So none of the six victory conditions, the +300/+100 VP or the ×.7 deadline penalty was ever compared with QB64. Recorded games also stop wherever the Python `victor` says (e.g. alternate-original-ai-seed1 stops at turn 4 on income). Yet docs/rule-source-map.md:30-31 and :63, README.md:29 and :39-42, and EVALUATION.md:137-140 present "all six victory conditions" and "identical full game states" as verified. Only city control and the deadline have hand-traced tests (tests/test_mechanics.py:150-164). Income share, capital, strength ratio and annihilation rest on reading plus Python-only snapshots (tests/test_episodes.py:19-27).

[should fix] EVALUATION.md:93: "Random and passive lose every game, by turn 4 to 8" is not what the results contain. In results/20261023-baselines/results.jsonl, random ends in 2-12 turns and passive in 5-11. In the paired seeds, random lost by turn 3 on standard and reckless seed 2.

[should fix] docs/rule-source-map.md:208-209: says every listed quirk "is in QUESTIONS.md". Five are not: line 1028 (map :214), line 2545 (:216), line 2989 (:219), line 2647 (:221), and `playb` lines 2174-2177 (:222). QUESTIONS.md has only Q5, Q6, Q7, Q8, Q9 and Q14 for quirks.

[should fix] cws/qb.py:4-5 and :43: the docstring says "decimal literals and RND are SINGLE" and "Decimal literals in the source are SINGLE constants". That contradicts the operative rule (docs/rule-source-map.md:45; AGENTS.md: "decimal literals are doubles"). The code is right only because `S()` appears in comparisons and single assignments. A porter following this docstring would bring back regression 3 (697 vs 696).

[should fix] tools/qb64-harness/make_harness.py:105-167 vs docs/rule-source-map.md:23-27: the map says the harness changes only TICK, menu, railroad and the key waits. But the main module is a hand transcription, not CWSTRAT.BAS lines 105-770. "M" sets `armymove(v) = w` (skipping SUB armies and movefrom), "X" sets `armymove(v) = 0` (skipping SUB cancel's name lookup at line 2716), and "D", "S" and the newmonth bookkeeping are retyped. For those rules the differential run checks one port against another.

[should fix] tests/test_interface.py:182: `g.month in (1,3,5,7,9,11) or g.month in (2,4,6,8,10,12)` is true for every month 1-12, so this invariant cannot fail. It would pass even if the calendar advanced one month per turn.

[should fix] cws/players/model_player.py:38-39 and :53: the prompt misstates rules to the playing agent. It says "An army that recruited ... rests", but reinforcing an existing army (label add2, lines 2125-2145) sets no rest; only `newarmy` does (line 1903). It says the troops list "is fixed for the turn", but an empty roll is not kept and can be re-rolled (line 2098, engine.py:269-270).

[note] cws/engine.py:357-361 (map :120 labels cancel `code`): SUB cancel (line 2716) picks the last army in the city whose name contains the chosen menu text (`INSTR`). With two Union "Banks" (CWSLEAD.DAT slots 7 and 18), or generic "Union I" next to "Union II", the original cancels a different army than `cancel <id>`. The harness bypasses SUB cancel, so this was never compared.

[note] cws/interface.py:147-149: `join` is hidden when only one army would merge. But the original's one-army join (lines 1098-1116) still sets `occupied(target) = best` and caps supply at 10, so it can change the game. That contradicts the "listed only when it would change the game" rule (map :198).

[note] cws/interface.py:28: the `plan` event reaches the model's report, but the map's boundary table (docs/rule-source-map.md:185-192) does not list it. Its text is printed only when `turbo! > 1` (line 2330), and CWS.CFG sets `turbo!` to 1. What the original actually shows is the map arrows from `icon(..., 1)` and `icon(..., 9)` (lines 2334-2335). cws/play.py:97 filters the same event out of the human view, so the human and the model see different reports.

[note] docs/rule-source-map.md:191: the battle citation "1011-1018" is `scribe(a$, 0)`, which writes only to the history file (SUB scribe 3737-3747; CWS.CFG history = 0). On screen, strengths and odds are lines 875, 921 and 930, and losses are 1003-1009. The panel also prints the enemy's Ldr/Exp lines (859, 886). The "Hidden" row (:192) should say that leader and experience can be partly inferred from battle reports, in the original and here (engine.py:829-830).

[note] docs/rule-source-map.md:200: "`commander()` is probed without creating a leader" does not describe the code; `legal_actions` never calls `commander` (interface.py:125-131). The cited two-seed test (tests/test_interface.py:120-131) cannot detect a die rolled without showing its value. It also never checks that its script was accepted: `drill 2` is refused after `fortify Cincinnati`.

[note] docs/rule-source-map.md:169-179: the smarts table has no evidence-label column. Design rows :94, :192, :200 and :204 give no alternative they beat (:204 gives no reason either).

[note] cws/runner.py:109: the wall clock is checked only between decisions. The 30 s per call is enforced only by the SDK's `HttpOptions` (model_player.py:176-177), with no runner watchdog. tests/test_runner.py:78-80 passes before any decision, because engine start-up alone exceeds 0.02 s. Exceptions other than engine errors, from a player or `render`, escape `run_episode` (runner.py:165-168) and stop the suite with no terminal reason.

[note] cws/players/baselines.py:17-23 and cws/evaluate.py:58-60: the baselines get the episode seed and the model does not. It is only used for the baseline's own dice. The docstring's list of differences from the original Union AI also omits three things. The original gives a computer Union `usadv` (252) extra income every turn when the human plays the Rebels (line 263), and the baseline gets none. The baseline plans before the Rebels instead of after. And `View.occupied` is rebuilt as the lowest-numbered army (view.py:61-64), not the engine's stored pointer.

[note] results/20261023-184551/results.jsonl: an empty run with a default timestamp name (default eval split) and no explanation in EVALUATION.md or SUITE.md. Say what it was.

[note] cws/evaluate.py:145-146: `row.update(date=...)` overwrites the episode's in-game end date (`EpisodeResult.date`) with the run date. Every row in results.jsonl says "2026-10-23".

[note] README.md:104: "12 episodes of up to 24 turns" is wrong for alternate. April 1861 to October 1865 is 27 two-month turns.

[note] cws/client.py:94: the docstring says the port "cannot reset ... or inspect the episode", but `port._call("reset" | "trace" | "outcome")` reaches the full server (server.py:21-35). Harmless today only because the player never receives the port.

[note] tests/test_model_player.py:97-101: `unittest.main()` comes before `class VertexAdapterWithFakeSDK`, so those tests run under `discover` but not when the file is run directly.

[note] cws/engine.py:829-830: the battle text names the winner and loser but not the attacker, while the losses are given as attacker/defender. The original marks the attacker with "*" (lines 1013-1015).

[note] tools/sync_to_course_repo.sh:15: `rsync --delete` will remove anything that exists only in the course-repo copy (for example a review.md written there), and it copies the empty results/20261023-184551 run.

### What was checked with nothing found

- **Fidelity.** I compared these line by line and found no discrepancy:
  - SUB battle 845-1036: strength steps, line 947, star-then-fin dice order, losses and caps, the line 1028 quirk, winner VP.
  - Initiative 2411-2432: one RND per slot in the condition.
  - Move, attack, withdraw (11*RND), retreat, crushed (`victory(3 - s)`), holdon, capture, raze, horde 2434-2590.
  - iterate 1406-1440.
  - recruit, randsel (XOR, RND per city) and levy 2074-2177; newarmy; commander.
  - smarts 2212-2364: RNDs at 2234, 2251 and 2252 always drawn; `3*side` at 2258; top priority; crossing check 2327; drill.
  - evaluate 2961-3047, every `side` / `3 - side` mapping, including the 3019 fix.
  - void 4514; VP 2641-2648; newmonth 255-274; topbar 3970; victor 4385-4512.
  - The `cint`, `f32`, `idiv` and `qint` uses match the stated numeric rules.
  - Replaying all 30 recordings in Python gave 2,787 states with 0 hash mismatches. Command counts (2,757 commands, nine types) match the docs.
- **Information boundary.** Enemy army keys are id, name, men, city and out-of-supply only. The prompt's enemy lines carry only those. No dice, seed, rating, lname, rcity or enemy orders appear in the observation, `legal_actions`, the action strings or the prompt. Every report text except `plan` and `turn` matches a message the original prints. `legal_actions` reads only Union or public fields and rolls no dice. The player gets only obs, legal and memory, never the port. View is built from the observation alone. The viewer is post-hoc only.
- **Limits and labels** (apart from the blocking item). Step limit is enforced by the engine. Model-call limit gives terminal reason "model-call limit". Failed and truncated calls count. Fallbacks are always labelled `fallback`.
- **Fairness and claims.** Every player runs SUITE seeds 1-2 under the same Limits. The EVALUATION tables match results.jsonl (recomputed), and model rows are honestly "not yet run".

### How I checked

Bash was used only for inspection. With bytecode writing disabled and no output files, I ran four deterministic test modules (29 tests, OK), an in-process replay of the recordings, and one offline `run_episode` with the fake client and no trace file.

### Files read

docs/rule-source-map.md; QUESTIONS.md; cws/engine.py, smarts.py, interface.py, qb.py, data.py, scenarios.py, runner.py, client.py, server.py, evaluate.py, play.py; cws/players/view.py, baselines.py, model_player.py; tests/test_mechanics.py, test_regressions.py, test_qb64_recorded.py, test_qb_numeric.py, test_interface.py, test_runner.py, test_episodes.py, test_model_player.py; SUITE.md; EVALUATION.md; README.md; AGENTS.md; CLAUDE.md; AGENT-TEAM.md; PEER-NOTES.md; agent-config.json; .claude/agents/rules-reviewer.md; tools/qb64-harness/compare.py, make_harness.py, recorded/*.json (summarised); results/20261023-baselines/table.md, table-paired-seeds-1-2.md, results.jsonl; results/20261023-184551/results.jsonl; data/original/CWS.CFG, CWS.INI, ALTMAP.INI, CWSLEAD.DAT; ci/midterm-rajvardhan19.yml; pyproject.toml; .gitignore; viewer/index.html; tools/sync_to_course_repo.sh.

source/CWSTRAT.BAS, sections: 1-220, 220-480, 740-770, 771-1128, 1129-1195, 1295-1470, 1889-1968, 2074-2180, 2212-2365, 2392-2730, 2827-2907, 2961-3060, 3404-3505, 3602-3640, 3737-3830, 3960-3999, 4385-4543.

---

## Response (implementation agent, same day)

Each line answers one finding in order. **Done** means changed and tested;
**documented** means the behaviour stays and the documents now say so.
The student accepts or rejects each response in AGENT-TEAM.md.

1. **[blocking] Batch past "End turn": done.** The runner compares actions
   as `step` normalises them, and stops a batch whenever the returned
   observation is in a new turn, whatever the spelling (`cws/runner.py`). The
   reviewer's case is now a test:
   `tests/test_runner.py::test_batch_stops_when_the_turn_resolves_whatever_the_spelling`
   (`"End turn"` and `"  TROOPS "`).
2. **Held-out seeds by default: done.** `cws.evaluate` refuses a model
   player without an explicit `--split`. `cws.play --watch model-*`
   defaults to dev seed 101. README and SUITE commands updated; SUITE.md
   records the tooling change (no change to the suite).
3. **victor never compared with QB64: done.**
   - The harness now runs END TURN through the original SUB victor, with
     the design answers to its prompts. Python replays with `end_turn()`.
   - The dump includes the end-game result (`thrill`, and `j` via one added
     line after `finis:`).
   - Re-recorded, with six games added to reach more end conditions: 36
     games, 3,392 commands, all identical, eight end conditions observed.
   - Annihilation and a Union strength-ratio win, which no game reached,
     have new hand-traced tests, as does the order of checks
     (`tests/test_mechanics.py`).
   - The docs now say exactly which conditions are `observed`.
4. **"by turn 4 to 8": done.** EVALUATION.md now gives the true ranges
   (random 2-12, passive 5-11).
5. **Quirks missing from QUESTIONS.md: done.** Added Q19-Q23 (lines 1028,
   2545, 2989, 2647, 2174-2177); the map points to them.
6. **qb.py docstring: done.** It now states the rules as read from QB64's
   C++ and warns against `S(.8) * v`.
7. **Harness main was hand-typed: done.**
   - The main module now copies the rule paths from CWSTRAT.BAS by line
     number: start-up 128-217, including `SUB filer` on the real files;
     newmonth and victor 252-278; Supply 402-425; Drill 460-467.
   - Only menu jumps become `RETURN`.
   - Moves go through SUB armies and movefrom, and cancels through SUB
     cancel, each with scripted menu rows.
   - Each extract is labelled in the generated file, and the map lists every
     change.
8. **Tautological month invariant: done.** The invariant test now checks
   that each turn advances exactly two months, wrapping December to January
   and the next year.
9. **Prompt misstatements: done.** Reinforcing does not make an army rest,
   and an empty recruiting roll can be retried (`cws/players/model_player.py`).

Notes:

- **cancel by name: documented** as QUESTIONS Q24 (`design`). The harness
  now runs the original SUB cancel, and no recorded game hit the ambiguous
  case.
- **one-army join: documented** as Q25 (`design`).
- **plan events: done.** Listed in the boundary table as the map's arrows
  (lines 2334-2335), and now shown to human players too.
- **battle citations and inference: done.** The citations now point to the
  panel lines (875, 921, 930, 967, 1003-1009). The hidden row now says
  leader and experience can be partly inferred from battle strengths, in
  the original and here.
- **commander text and the two-seed test: done.** The map text is
  corrected. The test now asserts every scripted action is accepted. A new
  test watches the dice counter, so a roll that is not shown would fail it.
- **smarts labels and design alternatives: done.**
- **runner watchdog and player exceptions: done.** Each decision runs under a
  45 s watchdog; a hang or an exception is a failed call, or "player error"
  for a baseline. The wall-clock test now stops a game partway.
- **baseline differences: documented** in the `OriginalAI` docstring
  (`usadv`, planning order, rebuilt occupant pointer).
- **empty run directory: removed.** `cws.evaluate` now refuses before
  writing anything.
- **date overwritten: done.** Rows keep the in-game `date`; the run date
  is `run_date`, and the split is recorded.
- **"up to 24 turns": done.** 24 standard or reckless, 27 alternate.
- **PlayerPort reaching the full server: done.** The port's channel refuses
  anything but `observe`, `legal_actions` and `step` (tested).
- **unittest.main placement: done.**
- **battle text attacker: done.** "A attacks D in C: W wins ... Attacker
  lost ..., defender lost ...".
- **sync --delete: documented.** `midterm/` is the source of truth; the
  script's header says so.
