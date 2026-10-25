# VGA Civil War Strategy v2.11: rule and source map

Every rule this reconstruction enforces, with its evidence. Line numbers
refer to `source/CWSTRAT.BAS` (an unmodified copy, upstream commit `dac8db1`);
data files are in `data/original/`; Python locations are in `cws/`.

## Evidence labels

| Label | Meaning here | Locator |
|---|---|---|
| `code` | What CWSTRAT.BAS (or the QB64 runtime it compiles against) computes | `line N`, a data file, or a QB64-PE source file and line |
| `observed` | Seen in a run of the original code compiled by QB64-PE 4.7.0 (macOS arm64) | a probe in `tools/qb64-harness/` or a recorded comparison |
| `assumed` | An inference about the original that no evidence has confirmed | a `QUESTIONS.md` entry |
| `design` | A choice made for this midterm, with the alternative it beat | the reason in this file |
| `manual` | Not used. No rule here comes from a manual; the official documentation at hutsellgames.com was not consulted, so where the code and the manual might differ, the code wins. | - |

## How the code labels were verified

1. **Hand traces.** Each mechanic was ported one at a time from its SUB and
   tested against a result traced by hand with scripted dice
   (`tests/test_mechanics.py`).
2. **Differential runs against the original.**
   `tools/qb64-harness/make_harness.py` compiles the original game code with
   QB64-PE 4.7.0.
   - **Kept verbatim:** every SUB from line 771 on, and the main-module rule
     paths copied by line number:
     - start-up 128-217 (including `SUB filer` reading the real data files);
     - END TURN and newmonth through SUB victor (252-278);
     - the Supply menu (402-425) and the Drill menu (460-467).
   - **Changed:**
     - `TICK` (clock wait), emptied;
     - `menu`, which gives the midterm's design answers (Retreat: ESC;
       Raze: ESC, i.e. No; End Game: Yes; Options: Quit) and otherwise the
       scripted menu rows;
     - `railroad`, out of scope;
     - `maxx`, the hall of fame, which does file and keyboard I/O;
     - the `INKEY$` key waits;
     - one added line in SUB victor that copies the condition number for the
       dump.
   - **How commands run:** moves go through the original SUB armies and
     movefrom menus, cancels through SUB cancel's name lookup, and recruits,
     forts and joins through their SUBs.
   - **The comparison:** the harness and the Python engine replay the same
     commands under the same seed. The full state (every army, city,
     treasury, VP, the opponent's `aggress!`, and the end-game result) is
     compared after every command.
   - **Results:** 36 games and 3,392 commands, every state identical. The
     original AI, a random player and a passive player played the Union in
     all three scenarios.
   - **Coverage:** all nine command types, and eight end conditions through
     the original SUB victor:
     - the deadline;
     - Union city control, income share and capital capture;
     - Rebel city control, income share, capital capture and strength ratio.
   - **Not reached by any recorded game:** annihilation, and a Union
     strength-ratio win. These have hand-traced tests instead.
   - `tests/test_qb64_recorded.py` re-checks the recorded hashes in CI.
3. **The differential run found three porting errors.** Each was fixed and
   has a regression test (see "Regressions found").

## Numeric semantics

| Rule | Label | Evidence |
|---|---|---|
| `DEFINT A-Z`: every unsuffixed variable is a 16-bit INTEGER | `code` | line 1 |
| `RND` is a 24-bit LCG: seed 327680, `seed = (seed * 16598013 + 12820163) AND &HFFFFFF`, value `seed / 2^24` | `code`, `observed` | QB64-PE `internal/c/libqb.cpp` lines 12861-12914 (main, 2026-10-22); probe printed .7055475 .533424 .5795186 |
| `RANDOMIZE s`: high word of the double `s`, folded (`m XOR m>>16`), becomes bits 8-23; the low byte of the old seed stays | `code`, `observed` | libqb.cpp lines 12878-12886; probe after `RANDOMIZE 12345.678#` printed .7454798 .5435709 |
| Decimal literals are double constants; arithmetic with them is double | `observed` | generated C++ for `v(1) = .8 * v(1) + .3 * s`: `qbr_float_to_long((0.8E+0*v)+(0.3E+0*s))` |
| Assigning to INTEGER converts once to SINGLE, then rounds half to even | `code`, `observed` | `qbr_float_to_long(float)` in `internal/c/libqb/include/rounding.h` (`nearbyintf`); probe: `.8*742+.3*343` (696.5) gives 696, `.7*45` gives 32 |
| Integer `/` integer is long double | `observed` | generated C++ `a/((long double)b)` |
| `IF` comparisons cast both sides to SINGLE | `observed` | generated C++ `((float)(a/(long double)b))>((float)(0.2E+0))` |
| `SELECT CASE` compares the same way | `assumed` | not read from generated C++; consistent with every recorded game (evaluate line 3004, battle line 891) |
| `SQR` returns a double | `code` | `internal/c/libqb/include/qbmath.h` line 51 |
| `AND`/`OR` do not short-circuit: an `RND` in a condition is consumed even when the first operand is false | `observed` | probe: after `IF q = 1 AND RND > .5` with `q = 0`, the next `RND` was the sequence's second value |
| SUB locals start at 0 on each call | `observed` | `enufarmies`' `y` (line 2357) accumulates from 0; every recorded game matches |
| Python implementation | - | `cws/qb.py` (`cint`, `f32`, `S`, `idiv`, `qint`, `QBRandom`) |

## Scope

**Included.** These play exactly as in v2.11:

- the 40-city map and its links (`CITIES.GRD`, or `ALTMAP.GRD`);
- the opening order of battle, treasury, capitals and victory conditions (`CWS.INI` / `ALTMAP.INI`);
- the leaders (`CWSLEAD.DAT` / `ALTLEAD.DAT`);
- the shipped options (`CWS.CFG`): Balanced difficulty, Realism on, January campaigns allowed, opponent aggression NORMAL;
- every Union command except those excluded below;
- the whole monthly resolution: the computer's turn, initiative, movement, battle, retreat, surrender, capture, supply, attrition, the calendar, victory points and all six victory conditions.

An episode is one war, from the start date to a victory condition. The
original's own deadline (March 1865 standard, October 1865 alternate) is a
victory condition, so every episode ends.

**Excluded.** Each exclusion and what it changes:

| Excluded | Source | Why | Effect on play |
|---|---|---|---|
| Navies: ships, blockades, raiding, invasions | SUB navy lines 1471-1887; iterate line 1424; tupdate lines 2603-2633; smarts lines 2256-2297 | A second game of its own (400+ lines) with its own menus. The scope keeps the land war. Fleets are set to zero at start (design). | No blockade supply loss and no commerce raiding. Neither side spends cash on ships, so the computer has more to recruit with (QUESTIONS Q10). |
| Railroads | SUB railroad lines 1969-2072; tupdate line 2408 | Long-range movement with its own capacity rules. Dropping it keeps one move per army per turn. | Both sides move only to adjacent cities. The computer's rail repositioning (line 2301) is absent. |
| Random events | SUB events lines 3049-3188 | Turned off with the original's own Utility option (Random Events OFF, line 600). The alternative, the default "Favor Rebels" for a Union player (line 160), adds variance no player controls. | No foreign aid, riots, emancipation or furlough events. |
| Relieve a commander | Commands menu line 470; SUB relieve lines 3350-3402 | Pool leaders are listed by name only, so the agent could not judge a swap, and listing every army-leader pair would bloat the action list. | The Union cannot replace a poor leader. |
| Move the capital | lines 428-442 | Costs $500 and gives the enemy 50 VP; it is rarely useful in this scope. | Capitals stay where `CWS.INI` puts them. |
| Detach | lines 443-458 | Rebel-only ("Option not available to Union", line 444), and the computer never uses it. | None for the Union. |
| Two-player mode, save/load, utility menus, history file, high scores, graphics, sound | lines 479-737, SUB filer, SUB maxx, drawing SUBs | Not part of the rules. | None. |

## Starting state

| Rule | Label | Evidence |
|---|---|---|
| Leaders: `lname$(i)`, `rating(i)` for slots 1-40 | `code` | SUB filer lines 1133-1137; `CWSLEAD.DAT` |
| Start month and year; victory flags; `vicflag(3) = .4 * vicflag(3)` (80 becomes 32 cities) | `code` | lines 1147-1153; `CWS.INI` |
| Union armies in slots 1-20, Rebel in 21-40, with leader = the slot's rating | `code` | lines 1156-1166 |
| Opening cash 300 / 50, ATKFAC 11, DEFAC 9, TCR 20 (alternate: 50 / 50, 13, 11, 25) | `code` | lines 1167-1170; `CWS.INI`, `ALTMAP.INI` |
| Capitals Washington and Richmond | `code` | line 1177 |
| `income(i) = cash(i)`, then `cash(i) += 50 * RND`, drawn **before** `RANDOMIZE TIMER`, so always from the default seed: Union +35, Rebel +27 | `code`, `observed` | line 167 (RANDOMIZE is line 219); harness opening state equals Python's |
| `usadv = 120 * difficult`, times .7 with realism (252) | `code` | lines 749-752 |
| Each owned city adds its value to the owner's cash and VP, and one to control | `code` | lines 209-216 |
| `RANDOMIZE TIMER` | `code` | line 219 |
| ...replaced by `RANDOMIZE seed`, the episode seed | `design` | Makes episodes reproducible and players comparable on the same dice. TIMER is seconds since midnight, so any seed in 0-86400 is a value the original could have drawn. Alternative rejected: keeping TIMER, under which no two trials face the same war. |
| The main menu clamps negative VP to 0 before every Union turn | `code` | SUB topbar line 3970, called at menu0 line 287 |

## Turn sequence

| Rule | Label | Evidence |
|---|---|---|
| The human gives orders from the main menu, then END TURN | `code` | lines 286-354 |
| END TURN: recruiting list cleared (`rflag = 0`) | `code` | line 352 |
| tupdate: the computer plans (`smarts`) after the human, then all moves resolve | `code` | line 2395 |
| After resolution: control and income recomputed from cities; cash clamped to 0-19,999 before income; +100 income while holding the capital; every order cleared | `code` | lines 256-274 |
| SUB victor checks the Union first, then the Rebels | `code` | lines 4396-4402 |
| The calendar advances two months per turn | `code` | iterate lines 1410-1411 |
| End-game prompt ("End Game / No-Override", then "Quit / Press Onward") answered End Game | `design` | A clear terminal state. Override would make episodes unbounded. |

## Union commands

All commands below are `code` for their effect. "Listed when" is `design`:
`legal_actions` lists a command only when it would change the game now,
and rolls no dice (see "Choices for the playing agent").

| Command | Listed when | Effect | Evidence |
|---|---|---|---|
| `troops` | cash >= 100 and no list kept this turn | Rolls the cities offering recruits. `max = 4` (3 if `RND > .8`). For each city in order, pct = .6*max/control (.4 if a friendly army is there; .3 in the fallbacks at lines 2084-2085). One RND per city until `max` are chosen. Realism skips cities originally the enemy's. The list is kept for the turn; an empty roll is not kept, so `troops` can be tried again. | SUB recruit lines 2074-2100; lines 2078, 2098-2099 |
| `recruit <city>` | the city is on this turn's list, cash >= 100, and the city has an army or a slot is free | $100. A new army has supply CINT(3+5*RND)+2, experience 1, men (3*value+33)*100, a third if no friendly neighbour, and rests this turn. An existing army gains (2*value+20)*100, a third if isolated. | levy lines 2102-2145; SUB newarmy lines 1889-1904; SUB commander lines 2887-2906 |
| `move <army> <city>` | army idle (order 0), city adjacent, not January into a non-friendly city when January campaigns are off | Sets the order | SUB armies lines 797-822; line 814 |
| `cancel <army>` | the army has an order | Order back to 0. The army is chosen by number; the original's menu chooses by name, which is ambiguous for duplicate names (QUESTIONS Q24, `design`). | SUB cancel lines 2697-2728 |
| `fortify <city>` | cash >= 200, a Union army there, fort < 2 | Fort +1, $200; the city's first army rests | SUB fortify lines 1295-1329 |
| `join <city>` | two or more idle armies there would merge, within the 1,250 cap (`design`: a one-army "join" only resets an internal pointer; QUESTIONS Q25) | Merges under the highest-rated leader. Experience is a size-weighted mean. Supply is summed, capped at 10. The merged army rests. | SUB combine lines 1038-1119 |
| `supply <army>` | supply <= 1, not cut off, can buy >= 1 | x = CINT(cash/size*10), capped so supply <= 5; costs .1*x*size | Supply menu lines 401-427; SUB resupply lines 3602-3615 |
| `drill <army>` | idle, experience <= 5 and < leader | Experience +1; the army rests | lines 459-469 |
| `end turn` | always | Resolves the turn | lines 341-354 |

## Resolution of a turn

| Rule | Label | Evidence |
|---|---|---|
| Resting orders (-1) become 0 before initiative | `code` | line 2413 |
| Initiative: `INT(4+4*RND)*100 + i` for armies with orders; `900+i` if out of supply; +100 if over 40,000 men (the 80,000 and 100,000 cases are unreachable); if `leader > 10*RND`, minus `100*(leader\2)`, floor `100+i`. One RND per slot even without orders. Ascending sort. | `code` | lines 2411-2432 |
| A mover loses 1 supply (floor 0). The city it leaves re-reads its occupant. | `code` | line 2442; SUB animate lines 772-778 |
| Into an empty or friendly city: arrive. Into a city held by the enemy: battle with its first army. | `code` | lines 2449-2465 |
| Battle strength, attacker: `.01*size` (cap TCR); +.3 leader +.3 experience if ratio > .2; +1 if experience > 8; halved under 1,500 men; -2 if ratio <= .5; +2 if > 3; TCR if > 10; 1 if <= .2; halved without supply | `code` | lines 855-874 |
| Battle strength, defender: realism `.02*size + 2` (cap 20); the same leader and experience terms; R! > 10 gives TCR, > 1.5 gives +2, < .5 gives x.8 (the `< .2` case is unreachable); halved without supply; times (1 + fort) only if its order is 0 | `code` | lines 878-920 |
| Winner: draw `CINT(scale*RND)` for each side until exactly one is within its strength | `code` | lines 950-959 |
| Line 947 subtracts 1 supply from **armies 1 and 2**, not the combatants | `code` (as written) | line 947; QUESTIONS Q6 |
| Losses: normal draws (12 RND each); blended .8/.2; caps 9x and 5x; never the whole army | `code` | lines 969-997; SUB normal lines 1948-1954 |
| The winner gains 1 VP and 1 experience (max 10) | `code` | lines 1032-1034, 2466 |
| Under 200 men left: crushed. The **defender's side** gains 25 VP whichever army it was. | `code` (as written) | lines 2468-2473, 2541; QUESTIONS Q5 |
| Beaten attacker returns to its origin; if `11*RND > defender's leader`, the defender's own order is cancelled | `code` | lines 2477-2494 |
| Beaten defender retreats to the most valuable friendly neighbour (preferring empty ones after the first), or surrenders if none | `code` | lines 2496-2535 |
| The human's retreat menu (shown when two or more cities qualify) is answered with ESC, which falls through to the automatic rule above | `design` | A mid-resolution prompt would need a second action type. ESC is the original's own default path (line 3635). Alternative: expose a retreat choice (rejected: rare, and it complicates the interface). |
| Further defenders in the city fight in turn | `code` | lines 2550-2553 |
| Capture: owner changes, the city's value is added to VP; a capital adds +100 and costs its owner 100; a fort drops one level if there was a battle | `code` | SUB capture lines 2827-2845 |
| The computer razes forts it takes unopposed in southern cities (`cityy > 150`) | `code` | lines 2575-2586 |
| The human's "Raze?" prompt is answered No | `design` | A one-off prompt. No keeps the captured fort, the conservative default. |
| On arrival, supply +1 (repeat with 20%), max 10 | `code` | line 2590 |
| Supply upkeep: +1 if cash >= .2*size and not cut off, paid; then -1 in Jan/Mar/May/Nov outside seaports (`matrix(c,7) = 99`); at 0, a 20% chance (one RND) to lose 10% of men over 5,000 | `code` | iterate lines 1413-1435 |
| `aggress!` = computer strength / Union strength (tenths summed in slot order, integer each step) | `code` | lines 1437-1440 |
| VP: `.8*VP + .3*(income + control)`; +50 over 29 cities, +100 more over 34 (the Rebel line adds to the Union's total, as written); `aggress! += .7` when the computer holds under 11 cities | `code` | lines 2641-2648 |

## Victory conditions

SUB victor checks the Union first, then the Rebels. The deadline is checked
before the Union's other conditions, so a Union that also holds 32 cities
on the deadline still gets the Confederate technical victory.
`observed` means at least one recorded game ended this way under the
original SUB victor with identical states.

| Condition | Label | Evidence |
|---|---|---|
| Enemy has no army: +300 VP, +100 more, wins | `code` | lines 4397, 4493; hand-traced in `tests/test_mechanics.py` (no recorded game reached it) |
| Date reached (`year >= vicflag(2)` and `month >= vicflag(1)`): **Confederate technical victory**; both VP x .7 | `code`, `observed` | lines 4399, 4459, 4498; 8 recorded games |
| Controls `vicflag(3)` cities (32 standard, 28 alternate) | `code`, `observed` | line 4400; Union 1 game, Rebel 16 |
| Earns `vicflag(4)`% of total income (80 standard, 60 alternate) | `code`, `observed` | line 4401; Union 5 games, Rebel 1 |
| Holds own capital while the enemy's is taken | `code`, `observed` | line 4402; Union 1 game, Rebel 3 |
| Total strength more than `vicflag(6)` : 1 (3 standard, 4 alternate) | `code`, `observed` (Rebel) | lines 4404-4412; Rebel 1 game; the Union case is hand-traced |

## The computer opponent (SUB smarts, lines 2212-2365)

Ported in `cws/smarts.py` with the full game state, as the original has it.

Every `code` row below is also `observed`: each recorded game runs the
original smarts under QB64 against this port.

| Step | Label | Lines | Note |
|---|---|---|---|
| Events | `design` (OFF) | 2213, 3049-3057 | Random Events OFF: returns at once |
| Resupply armies at 0 | `code` | 2221-2222 | |
| Fortify the occupied capital (fort < 2); then, while `1+RND >= bold+aggress!`, a city under threat (`void > size`) | `code` | 2225-2252 | At NORMAL (bold 3) the second branch never runs, since 1+RND < 3. The extra RNDs at 2251-2252 are always drawn (no short-circuit). |
| Recruit until cash < 100 unless it already has more than 5+3*RND armies (`enufarmies`, `randsel`) | `code` | 2255-2260, 2354-2364, 2146-2173 | `randsel`'s `x = 0 XOR armysize(x) < 155` is ported as written |
| Navy branches | `design` (excluded) | 2256-2297 | Out of scope; with no fleets none can fire |
| Combine in one random eligible city | `code` | 2300, 1054 | |
| Railroad | `design` (excluded) | 2301 | Out of scope |
| Each army: hold the capital if threatened; otherwise `evaluate` scores each neighbour and the army marches to the best | `code` | 2304-2339, 2961-3047 | Crossing-move check compares a destination with army size, as written (line 2327) |
| Drill every idle army that can | `code` | 2340-2351 | |

## Information boundary (what the Union player may know)

| Shown to the player | Label | Evidence in the original |
|---|---|---|
| Every city's owner, value and fort level; capitals; map links and positions | `code` | City Report lines 3480-3500; showcity lines 2186-2210; `CITIES.GRD` coordinates drawn on screen |
| Both sides' cash, income and cities | `code` | City Report lines 3495-3497 |
| Both sides' VP and the Union share | `code` | topbar lines 3973-3981; Army Report line 3437 |
| Own armies: size, city, leader, experience, supply, order | `code` | Army Report lines 3457-3461 |
| Enemy armies: number, leader name, size, city | `code` | Army Report line 3459 (`IF who <> side THEN PRINT : GOTO deadeye` stops before leader, experience and supply) |
| Enemy army out of supply (yes/no) | `code` | placearmy lines 1961-1966 draw an "S" for any army at 0 supply |
| Last turn's moves, battles, captures, retreats, new armies, fortifications | `code` | Messages the original prints: move line 2440; new armies 1894; reinforcements 2141; forts 2248. Battle panel: final strengths 875 and 921, odds 930, result line 967, losses 1003-1009. |
| The computer's planned moves before resolution (`plan` events) | `code` | The dashed arrows smarts draws for each order (icon kinds 1 and 9, lines 2334-2335). The original prints them as text only above Fast display speed (line 2330); here they are given as text. |
| **Hidden:** enemy leader rating, experience and supply level; enemy orders (they do not exist yet when the Union decides); the dice and seed; the opponent's routines; the unassigned leader pool | `design` (boundary) | Matches the Army Report. The original's battle panel also prints each side's intermediate "Ldr/Exp" strength (lines 859, 886), so a careful player can partly infer an enemy leader. Here only final strengths are shown, so the same inference is possible, a little less precisely. Alternative rejected: the opponent's full view (it is not what a human sees). Tests: `tests/test_interface.py` InformationBoundary; `cws/players/view.py` raises on hidden fields. |

## Choices for the playing agent

| Choice | Label | Reason, and the alternative it beat |
|---|---|---|
| One action string per menu choice the original offers; the list holds only actions that change the game now | `design` | Copying the starter's convention keeps illegal moves rare and countable. The alternative, the full verb list with the game's refusals, was rejected because it inflates invalid-action counts with menu noise and does not test strategy. |
| `troops` is its own action and rolls the recruiting list then, as opening the Troops menu does | `design` | Listing recruit cities at the start of a turn would roll dice before any action and leak the seed (Week 3 discernment test). |
| `legal_actions` never rolls dice. It checks for a free army slot directly instead of calling SUB commander, which can roll a generic leader's rating (line 2901). | `design` | Alternative rejected: a "recruit" list that runs the original's menu code, rolling as it lists. Tests: `tests/test_interface.py` two-seed test, and `test_no_die_is_rolled_before_a_roll`, which watches the dice counter. |
| Retreat menu answered ESC; Raze answered No; End Game answered Yes | `design` | Above |
| The engine runs in a separate process; the player holds a `PlayerPort` with only `observe`, `legal_actions` and `step` | `design` | Week 3 enforcement plan. In-process objects are reachable from Python, so a prompt is not a boundary. `tests/test_runner.py` ProcessBoundary. |
| The model may propose up to 8 actions per call; the runner submits them one at a time and stops at the first rejected one, after `troops` (new information) or at `end turn` | `design` | Over 24 turns, one call per action would be about 300 calls per episode. Batching brings that to about 3 per turn. Each action is still validated by `step` and appears in the trace. |
| The limits (all enforced by the runner; `tests/test_runner.py`):<br>- steps: 600<br>- model calls: 150<br>- per call: 30 s and one attempt, with a 45 s runner watchdog<br>- per episode: 30 min<br>- per turn: 40 actions, or 3 failures<br>after which the runner submits `end turn` labelled `fallback`. A crashing baseline ends with "player error". | `design` | A model game is about 24 turns of about 3 calls, so 150 calls is twice the need, and 600 steps is about four times the original AI's longest game. The per-turn caps stop a model cycling `move`/`cancel` or repeating a rejected action forever. Alternative rejected: no limits beyond the game's own deadline, under which a looping model never ends an episode. |

## Quirks kept as written

These look like bugs, but the reconstruction keeps them because the rule is
"what CWSTRAT.BAS computes". Each is in `QUESTIONS.md` (Q5-Q9, Q14, Q19-Q23).

- Line 898: `CASE IS < .2` can never run (after `< .5`).
- Lines 973, 984, 2419-2422: `CASE IS > 800` and `> 1000` can never run (after `> 300` or `> 400`).
- Line 947: battle subtracts supply from armies 1 and 2.
- Line 1028: casualty bookkeeping tests `attack > 2`, not `> 20` (statistics only).
- Line 2541: a surrender gives 25 VP to the surrendering side.
- Line 2545: the winner absorbs the loser's supply after it is zeroed (adds 0).
- Line 2251: `cash < 222` reads an undeclared scalar (always 0).
- Line 2327: the crossing-move check compares a destination with army size.
- Line 2989: `IF fort(a) = 3` is nested inside `= 1` and cannot hold.
- Line 3031: compares a city owner with a city number.
- Line 2647: the Rebel's 35-city bonus is computed from the Union's VP.
- `playb` (lines 2174-2177) adds a difficulty bonus that `newarmy` then overwrites.

## Regressions found

Each was found by evidence and has a test in `tests/test_regressions.py`.
All three were found on 2026-10-23.

1. **Leading blank in quoted fields.** `CITIES.GRD` writes `, "Phildelpha"`.
   Our tokenizer kept the blank, so `recruit  Pittsburg` never matched its own
   legal action, and the baseline lost every recruit. Fix: skip blanks before a
   quote, as `INPUT #` does.
2. **Line 3019's side.** `IF cityp(a) = 3 - side ...` penalises marching onto
   the computer's own resting army. It was ported as the enemy's side. Found by
   the differential run (seed 1, command 38) with the `--debug` harness.
3. **Rounding once.** QB64 computes `.8*v + .3*(income+control)` in double
   and rounds once. Rounding each product to SINGLE first gave 697 where the
   original gives 696 (seed 2, command 200). Fix: the numeric rules above,
   read from QB64's generated C++.
