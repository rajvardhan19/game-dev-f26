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

---

## Second review: navies and railroads (change of 2026-10-25, read-only)

Run by the `rules-reviewer` agent in a fresh session. Its report follows unedited.

Rules review: navies and railroads (change of 2026-10-25)

I found no blocking issue. Every navy and railroad rule I compared against CWSTRAT.BAS is ported faithfully. The findings are about weak tests, untested paths, doc claims the code or results do not support, and one prompt defect that a live trace shows causing rejected actions.

**Findings, most serious first**

[should fix] tests/test_navy_rail.py:104-117: the blockade test cannot tell the enemy's fleet from the army's own. Line 1424 tests `navyloc(3 - s)`. The test puts the Union fleet at Mobile, but CWS.INI already has the Rebel fleet at Mobile (line 21 of the test asserts it). So a port that wrongly used `navyloc(s)` still takes supply from 5 to 4 and passes.

[should fix] docs/rule-source-map.md:208: the raid row is labelled `observed` and says "otherwise a ship is lost and the roll repeats". That repeat (lines 2617-2624, `raider = 0`, barnacle, `GOTO allthru`) was never observed and never hand-traced. I replayed all 48 recordings in memory: 16 resolutions with commerce raiding, every one a success on the first roll, no "raiders have lost a ship" event. test_commerce_raiding_amount (test_navy_rail.py:97) scripts only the success path.

[should fix] cws/players/model_player.py:158: `compact()` prints `move 4 <city>, <city> one of: ...`. The literal "<city>, <city>" invites a comma list, and the model did exactly that. In traces/dev-20261025/model-history-standard-101.jsonl line 9, turn 2, the model played "move 4 Paducah, Lexington", which was rejected as an invalid action. tests/test_model_player.py:22-33 only checks that each action can be recovered from the grouped line, not that the format is unambiguous.

[should fix] docs/rule-source-map.md:219: "between a quarter and twice train(who)" is wrong. SUB traincapacity (lines 4058-4060) sets `x = 2 * train(who)` and floors at `x \ 4`, which is half of train(who) (300 for the Union, 150 for the Rebels). The code (railroad.py:21-23) is right; the floor is not tested (test_train_capacity checks the cap and 545 only).

[should fix] docs/rule-source-map.md:213 and QUESTIONS.md:38 (Q30): "it sails to whatever stale city is in array(30)" never happens in scope. The sail list has at most 9 rows (nine 99-ports in CITIES.GRD), and nothing else in scope writes a nonzero array(30). Recruit's loop at line 2086 only zeroes it. In all 48 recordings the highest nonzero array() index is 11. All 16 recorded returns of 30 from line 1865 read array(30) = 0, so line 1659 `IF array(choose) < 1 THEN EXIT SUB` applies. The real effect is that the Rebel fleet at Philadelphia stays put half the time.

[should fix] tests/test_navy_rail.py:84-95: test_ship_against_ship says it covers "an ironclad: 20 hits, and +.1 per shot", but it cannot fail on either. All ten rolls are .1, which is below .4, .5 and .6, so the Union lands every shot and never takes a hit. A port with the ±.1 reversed, or with 10 hits for an ironclad, passes. It also never reaches the attacker-eliminated branch (hitme1, lines 1805-1821) or checks grudge.

[should fix] SUITE.md:12-13: the reasons given for two situations are now contradicted by results/20261025-baselines/table.md.
- `standard` says "The original AI usually holds out"; it held out in 7 of 20 (5 wins, 8 losses).
- `alternate` says "always wins"; it won 19 of 20.

[note] README.md:52, EVALUATION.md:151, docs/rule-source-map.md:58: "360 navy and 197 railroad commands" is stale. The 48 recordings contain 416 N and 212 L commands. 360/197 is the count without standard-original-ai-seed10, standard-original-ai-seed56 and reckless-original-ai-seed144, which were added at 17:31, while the "48 games / 3,637 commands" figure next to it includes them.

[note] docs/rule-source-map.md:212: "raid from sea" does not match the code.
- At sea the computer calls `navy(who, 3)` (Sail via nest) at line 2268 (90%) or line 2283 (50%).
- Its own raid mode (chx = 4, line 1477) is always overridden by `grudge > 0` (line 1478), because line 2615 sets grudge whenever a Union raid makes raider > 0.
- No recording has a "Rebel ... sailing to RAID" event. The one Rebel raid came after it won a battle at sea.
- "Revenge after being raided" also leaves out that grudge is set by lines 1798 and 1817 after naval battles.

[note] Line 289 (`IF cash(side) < 100 AND navyloc(side) = 0 THEN nflag = 1`, at menu0) is in neither the Python engine nor the harness, which copies 322/325-340 but not menu0. So the nflag comparison cannot catch it. I found no rule effect: cash only falls during the human's turn, so no build is possible anyway. But `fleet_acted_this_turn` (interface.py:123) reads false where the original greys out Ships, and rule-source-map.md:211 cites 297/322 but not 289.

[note] cws/interface.py:272-274: `fleet invade` is withheld when no commander slot is free. The original's human branch (lines 1721-1729; the `chx > 0` guard at 1723 does not apply) goes on with `empty = 0`. It runs newarmy and capture on army slot 0, captures the neutral port and loses a ship. This deviation is not recorded in QUESTIONS.md; Q34 covers only the computer, and also leaves out the Rebels' realism = 0 case at line 1505.

[note] cws/players/baselines.py:115 drops line 2251's `navysize(1) < 1`. The Union now starts with 4 ships, so the original never jumps to signup there, but the baseline breaks 50% of the time. At bold 3 this changes only the baseline's own dice stream. The comment at cws/smarts.py:272 ("navysize(1) < 1 ... hold") is now false.

[note] The vocabulary has no "open Ships, then ESC". In the original that still sets `cityp(0) = 1` (line 1483), which stops a fleetless Rebel from saving (2259) or rebuilding (2271). It is state-changing, so it falls under the rule-map's "listed when it would change the game". Kept quirk; worth a line in Q26.

[note] Paths covered by neither hand traces nor recordings:
- the Type menu's Wooden answer `[1, 1]`;
- a new wooden fleet `[1, row]` or `[1, 1, row]`.

The recorded row patterns are [1]×48, [1,2]×4, [1,2,row]×2, [2]×191, [3,row]×136, [4]×12, [5]×23. Computer rail choice, `_naval_orders`, nest and invasion have no hand trace; they are covered only by recordings: about 200 Rebel hauls, 207 computer navy calls, 16 line-1865 returns, 23 invasions.

[note] tests/test_navy_rail.py:56, 77: two hand traces cannot catch plausible slips.
- The bombardment uses 4 ships, so `.5*4 + 1 = 3` is exact and half-even CINT is never exercised (3 or 5 ships would).
- The shore-battery rolls (.95, .1) give the same result if `navysize - fort` were reversed.

[note] EVALUATION.md:96-98 and QUESTIONS.md:25 (Q17) quote the 2026-10-23 baseline (2 wins, 17 held out, 1 loss). That results directory (results/20261023-baselines, read in review.md:27) is no longer in the repo, so no file backs the "before" numbers.

[note] QUESTIONS.md:9 (Q1) says "all 36 recorded games"; there are 48.

[note] README.md "design choices" list omits the naval battle's Attack answer. Q33 (QUESTIONS.md:41) does not say what it changes: the human cannot break off a battle it started. The original's Retreat (lines 1823-1830) sends the fleet to an own shipyard.

[note] docs/rule-source-map.md:270: the evidence for "at sea" cites the Army Report, but line 3474 prints nothing for navyloc 99. What shows it is SUB ships line 3805 (sea position) and usa's COMMERCE box (line 4360).

[note] cws/players/baselines.py:247-248: the baseline cannot sail to sea for revenge. `dest == AT_SEA` returns, while the original's grudge path (line 1639) sails to 99 and fights. This approximation is not in the class docstring.

[note] cws/smarts.py:5 cites cws/players/original_ai.py, which does not exist (the class is in baselines.py).

**1. Fidelity: what I compared line by line, no mismatch found**
- Top-of-navy chx changes (1473-1480).
- ahoy menu choices and invasion test (1482-1510), including `void(navyloc(1))` for both sides.
- Build: 1523 roll for every builder, Type menu, computer ironclad at $100, add2ship, Port menu with random choice (1551-1571).
- Attack (1579-1628): 1582's roll for the human and its `GOTO anchor` re-roll; casualties `cint(f32(size*pct!))`; supply `cint(.5n+1)`; shore-battery loop; blast; capital check.
- Sail and admiral (1629-1690): grudge `array(1)`, nest (1846-1866) with the RND only when the target is the enemy fleet, and line 1865.
- Raid (1691-1720) and invasion (1721-1731).
- pirate (1739-1821): hit init, `.5 ± .1` cast to single, VP and grudge on both branches, sail3.
- barnacle (836), ships (3799).
- Commerce raiding (2603-2633): loop, the 30% cap compared as single, x/0.
- Income deduction (272), blockade (1424).
- smarts signup with slush and cityp(0) (2255-2264), dock and movenavy (2265-2293, the OR at 2288 rolls every time), ships, combine, railroad order (2297-2301).
- railroad CASE 0 for the computer (1971-2003, including `target` carried into 1997), human path (2004-2019), haul, arrive (2034-2052), route, traincapacity.

`side` is the human everywhere it should be: void, the 1992-1993 cityy preference, 4056, nflag and the Type menu. `who` and `3 - who` match in navy and pirate.

**2. array()**

I checked every array() write in the routines the harness runs: 415, 808+810, 1046+1052, 1305+1309, 1447/1460+bubble, 1553, 1635, 1639, 2078/2086/2092+2100, 2704+2706, 2969/3035 and 3627+3632. newcity, menu, battle, victor, iterate and tupdate write none. I found no missing write, and the sort and no-sort choices match the source.

**3. Information boundary**

No leak found.
- Navies for both sides: lines 3468-3474, plus SUB ships and usa.
- Raid "by" and "last_loss": messages at 2611 and 2620.
- Train capacity: line 336. Own train: line 3475.
- Every navy and rail event text is printed unconditionally in the original.
- `legal_actions` rolls no dice: port_list, sail_list, route, can_board and destinations are pure, and test_no_die_is_rolled_before_a_roll passes.

For each listed navy and rail action I traced the rows through SUB navy, movefrom and newcity. None reaches a `GOTO ahoy`/`aboard` loop, a different CASE, or an exhausted menu.

**4. Tests**

I ran tests.test_navy_rail and tests.test_interface (33 tests, OK). I did not run the full 96.

**Files read**
- source/CWSTRAT.BAS: lines 1-104, 125-480, 797-845, 1038-1190, 1295-1330, 1406-2180, 2212-2460, 2494-2730, 2827-2908, 2943-2990, 3030-3048, 3342-3350, 3404-3480, 3602-3640, 3799-3831, 3992-4064, 4340-4385, 4514-4544, 4668-4850
- cws/navy.py, cws/railroad.py, cws/engine.py, cws/smarts.py, cws/interface.py, cws/qb.py, cws/data.py, cws/scenarios.py
- cws/players/baselines.py, cws/players/view.py, cws/players/model_player.py
- tests/test_navy_rail.py, tests/test_qb64_recorded.py, tests/test_interface.py, tests/test_model_player.py
- tools/qb64-harness/make_harness.py, tools/qb64-harness/compare.py, tools/qb64-harness/recorded/*.json (replayed in memory)
- docs/rule-source-map.md, QUESTIONS.md, README.md, SUITE.md, EVALUATION.md, AGENTS.md, CLAUDE.md, AGENT-TEAM.md, .claude/agents/rules-reviewer.md, review.md (searched)
- data/original/CWS.INI, ALTMAP.INI, CWS.CFG, CITIES.GRD
- results/20261025-baselines/table.md, table-paired-seeds-1-2.md, results.jsonl
- results/dev-20261025/results.jsonl, traces/dev-20261025/model-history-standard-101.jsonl

## Response to the second review (implementation agent, same day)

**Done** means changed and tested; **documented** means the behaviour stays
and the documents now say so. The student accepts or rejects each response
in AGENT-TEAM.md. Every new or rewritten test was mutation-checked: the
slip the reviewer describes was applied to a scratch copy and the test failed.

Should fix:

1. **Blockade test: done.** The Rebel fleet is moved to New Orleans, and a
   second case puts the Rebel fleet at Mobile with the Union fleet away:
   supply stays 5. A port using `navyloc(s)` now fails.
2. **Raid failure path: done.** Two hand traces: a failed roll loses a ship
   and rolls again (3 rolls, raider 90), and losing the last ship ends the
   raid. The map row is split: success `observed`, failure `code` plus
   hand trace, "no recorded game reached it".
3. **Grouped legal actions in the prompt: done.** The prompt now lists
   every legal action whole, one per line. The test checks the list under
   the heading equals `legal_actions` exactly and holds no `<` or `,`. Re-run
   live on dev seeds only (SUITE.md).
4. **Train capacity floor: done.** The map says "between half and twice";
   a test with `train = 101` checks the floor `(2*101) \ 4 = 50`.
5. **array(30): done.** Q30, the map row and the quirk list now say what
   happens: no list in scope reaches row 30, so the fleet stays in port half
   the time. Two hand traces of nest cover it (New Orleans with .55, .4;
   stays with .55, .6), and dropping line 1865 fails them.
6. **Ship against ship: done.** Replaced by two traces. An ironclad
   absorbs 15 hits and wins on rolls of .55 (fails with 10 hits or with the
   ±.1 reversed). A wooden attacker against an ironclad is eliminated
   (hitme1), gaining 10 VP and clearing grudge. Both check grudge and the
   roll count.
7. **SUITE.md reasons: done.** Restated from the current run, and the
   change log says the old text came from the 2026-10-23 run.

Notes:

- **Command counts: done.** 416 Ships and 212 Railroad commands, recounted
  from the 48 recordings, in README, EVALUATION and the map.
- **"Raid from sea": done.** The map row now follows lines 2265-2293: at
  sea it sails on 90%, it reaches the sea only through `grudge`, and
  `grudge` (2615, 1798, 1817) overrides the raid order.
- **Line 289: documented.** A map row says it is not ported and why; no
  navy action is possible then, and `fleet_acted_this_turn` reports only
  the order flag.
- **Invasion without a free commander: documented** as Q36 (`design`).
  Q34 now also covers the Rebels' Realism-off invasion (line 1505).
- **Baseline line 2251: done, and it changed results.** The baseline now
  rolls and jumps only when `navysize(1) < 1`, as the source does; the
  smarts comment is corrected. `20261025-baselines` was re-run in place:
  standard 7, 8, 5 (was 5, 7, 8), alternate 17, 0, 3 (was 19, 0, 1),
  reckless unchanged; random and passive identical. Three episode tests
  pinned to old baseline games were re-pinned to seeds showing the same
  paths (capital capture: seed 7; deadline: seed 3; VP counterexample:
  seed 13). SUITE.md and EVALUATION.md record this.
- **ESC from Ships: documented** in Q26 as a `design` gap.
- **Untested build paths: done.** Hand traces of the Type menu's Wooden
  answer `[1, 1]` and of a new fleet in a chosen shipyard `[1, 1]` with the
  enemy fleet excluding a port.
- **Weak bombardment and shore-battery traces: done.** A 3-ship
  bombardment checks CINT(2.5) = 2. The shore-battery rolls are now .95,
  .7, which sink another ship if `navysize - fort` is reversed.
- **2026-10-23 results missing: done.** Restored from the earlier course-
  repo copy as `results/20261023-baselines/` and
  `traces/20261023-baselines/`. EVALUATION and Q17 cite it and say it is not
  a controlled comparison.
- **Q1 count: done** (48).
- **Naval Attack answer: done.** In the README's design list. Q33 says
  what it changes.
- **"At sea" evidence: done.** It now cites SUB ships line 3805 and the
  COMMERCE box (lines 4357-4362), and says the Army Report prints no port.
- **Baseline cannot sail to sea for revenge: documented** in the OriginalAI
  docstring, with the battle and shore-battery grudge writes it ignores.
- **smarts.py citation: done.**

Not done: computer rail choice, `_naval_orders` and invasion still have no
hand trace. They remain covered by the 48 QB64 recordings only.
