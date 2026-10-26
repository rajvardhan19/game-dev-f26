# Open questions and ambiguities

Recorded instead of guessed, as the Week 3 plan requires. Each entry gives
what the source does, what a reader might expect, and what the
reconstruction does. "Kept" means the source's behaviour is reproduced.

| # | Question | Source | Reconstruction | Status |
|---|---|---|---|---|
| Q1 | QB64 on x86 computes integer `/` in 80-bit long double; on arm64 (where every comparison was run) long double is a double. Could a rounding boundary differ between the two builds? | generated C++ `a/((long double)b)` | Uses double, matching the arm64 build all 48 recorded games came from. | `assumed` identical in practice; untested on x86 |
| Q2 | When a Union army loses a defence and two or more friendly cities qualify, the original asks the human where to retreat | SUB retreat lines 3617-3637 | Answers ESC, which falls through to the automatic choice (most valuable friendly neighbour) | `design`; a human could pick differently |
| Q3 | After an unopposed capture of a fortified city the original asks the human "Raze ?" | lines 2564-2574 | Always No | `design` |
| Q4 | `randsel` reads `armysize(0)`, a scratch slot `combine` leaves holding the last merged size. The screen never shows it. | lines 2152, 1063, 1078 | The opponent uses the true value (it is the engine). The Union baseline, playing from the screen, reads 0. | `design` (boundary) |
| Q5 | A surrender or a crushed army gives 25 VP to the **defender's** side, even when the defender is the one destroyed | line 2541 (`victory(3 - s)` with `s` the attacker's side) | Kept | `code`; probably unintended upstream |
| Q6 | Every battle subtracts 1 supply from Union armies 1 and 2, not the combatants | line 947 (`FOR i = 1 TO 2: IF supply(i) > 0`) | Kept | `code`; probably unintended |
| Q7 | `cash < 222` in smarts reads an undeclared scalar, always 0, so it is always true | line 2251 | Kept (it only matters for the computer's Union, i.e. our baseline) | `code` |
| Q8 | The "crossing moves" guard compares a friend's destination with the mover's army **size** | line 2327 (`armymove(y) = x`, `x = armysize(i)` from line 2307) | Kept | `code` |
| Q9 | `evaluate` adds 50 when `cityp(m) = capcity(side)`, comparing an owner (0-2) with a city number | line 3031 | Kept; it can only fire if a capital is city 1 or 2 | `code` |
| Q10 | (Closed 2026-10-25.) Navies were out of scope until 2026-10-25, which left the computer richer than in v2.11 | lines 2256-2297 | Navies are now in scope and verified against QB64 | closed |
| Q11 | Random events default to "Favor Rebels" for a Union player (line 160) but are a Utility option | lines 160, 587-619 | OFF | `design`; removes a source of luck that would favour the opponent |
| Q12 | `RANDOMIZE TIMER` makes every original game different; which "seed" is faithful? | line 219 | `RANDOMIZE seed` with the episode seed (any value TIMER can take) | `design` |
| Q13 | The two opening `50 * RND` cash rolls happen before `RANDOMIZE TIMER`, so in v2.11 they are always the same (+35, +27). Intended? | lines 167, 219 | Kept: every game opens with Union 525, Rebel 318 | `code`, `observed` |
| Q14 | Several `SELECT CASE` branches are unreachable (`< .2` after `< .5`; `> 800` after `> 300`; `> 800`, `> 1000` after `> 400`) | lines 891-900, 970-975, 981-986, 2416-2425 | Kept | `code` |
| Q15 | `CWS.CFG` ships with January campaigns allowed (`jancam = 1`), so the no-January-campaign rule never applies here | CWS.CFG field 10; line 814 | Implemented but inactive | `code` |
| Q16 | The human's "Supply" list shows armies at supply 1 or less; the computer resupplies only at 0 | lines 407, 2221 | Kept | `code` |
| Q17 | (Closed 2026-10-25.) Railroads were out of scope until 2026-10-25 | lines 1969-2072, 2301 | Railroads are now in scope and verified against QB64. The original AI's standard-map record over 20 seeds was 2 wins, 17 held out, 1 loss before fleets and trains (`results/20261023-baselines`) and 7, 8, 5 after (`results/20261025-baselines`); the baseline was also corrected in between (line 2251), so this is not a controlled comparison | closed |
| Q18 | Victory point share is shown on screen, but a side conquered early can end with a higher share than one that held out (VP decay, and the deadline's x .7) | lines 2641-2648, 4498 | The evaluation ranks by outcome tier, then turns, and reports VP share for information only | `design`; see EVALUATION.md |
| Q19 | Casualty bookkeeping tests `attack > 2`, not `attack > 20`, so a Rebel attacker's losses can be booked to the wrong side | line 1028 | Kept; it feeds only the Battles report, not any rule | `code` |
| Q20 | When a defender is destroyed, the winner "absorbs" its supply after it has been set to 0, so it gains nothing | line 2545 | Kept | `code` |
| Q21 | In evaluate, `IF fort(a) = 3` is nested inside `IF fort(a) = 1` and cannot hold, so a level-2 fort counts like no fort (x1 = 1) | line 2989 | Kept | `code` |
| Q22 | The Rebel bonus for more than 34 cities sets `victory(2) = victory(1) + 100`, using the Union's points | line 2647 | Kept | `code` |
| Q23 | `playb` adds a difficulty bonus to a new army's size, which `newarmy` then overwrites (line 1898); at Balanced it adds nothing anyway | lines 2174-2177, 1898 | Kept | `code` |
| Q24 | SUB cancel finds the army by name: the last army in that city whose name contains the menu text (`INSTR`). Two "Banks" (CWSLEAD.DAT slots 7 and 18), or "Union I" beside "Union II", can cancel a different army than the one chosen. | lines 2703, 2716 | `cancel <id>` cancels exactly that army. The harness runs the original SUB cancel; no recorded game reached the ambiguous case. | `design`; differs only for duplicate or prefix names |
| Q25 | A one-army "join" (lines 1098-1116) changes nothing visible but resets `occupied(target)` and caps supply at 10 | lines 1094-1116 | `join` is listed only when two or more armies would merge | `design`; it is not a merge |
| Q26 | Every SUB navy call writes `cityp(0) = who`, the owner of a city that does not exist; the computer later reads `cityp(navyloc)` with no fleet, so this side effect decides whether it saves money or builds a fleet | lines 1483, 2259, 2271 | Kept; the engine models city 0 and the harness compares it. In the original, opening Ships and pressing ESC also sets `cityp(0) = 1`, which can stop a fleetless Rebel from saving (2259) or rebuilding (2271); the interface has no such action, so here only a navy order sets it | `code`; the ESC case is a `design` gap |
| Q27 | The computer's ironclads cost $100; only the human's branch doubles the price | line 1537 | Kept | `code` |
| Q28 | The computer's 50% "sail instead of bombard" jumps back with `choose` still 2, so it bombards anyway | line 1582 | Kept | `code` |
| Q29 | A destroyed fleet gives 10 VP to its own side | lines 1796, 1815 | Kept | `code` |
| Q30 | `nest` returns menu row 30 (half the time) when the Rebel fleet is at Philadelphia: a row, not a city. No list in scope reaches row 30, so `array(30)` is 0 and line 1659 leaves the fleet in port | lines 1865, 1659 | Kept; every write to `array()` is modelled and compared with QB64; all 16 recorded cases read 0 | `code`, `observed` |
| Q31 | A rail destination needs friendly links at both ends, but the track between is never checked: a train can cross enemy country | lines 2010-2017 | Kept | `code` |
| Q32 | Train capacity's base (11 or 23 cities) depends on the human's side, for both sides | line 4056 | Kept | `code` |
| Q33 | The human's naval-battle "Attack / Retreat" menu, shown only in a battle the human's fleet starts | lines 1766-1772, 1823-1830 | Always Attack, as the computer does: you cannot break off a battle you start, where the original's Retreat sails the fleet to an own shipyard | `design` |
| Q34 | A computer Union with no free army slot that tries an invasion loops forever (line 1723 jumps back with `choose` still 5). The Rebels can invade only with Realism off (line 1505) | lines 1723, 1505 | Unreachable here: the Union is never the computer, and Realism is on. The engine raises an error if line 1723's loop is reached. | `code`; not reachable |
| Q35 | The Union baseline cannot see `cityp(0)` or the computer's `grudge` | lines 1483, 1478 | It assumes the Rebels last ran SUB navy, and sets its grudge after a visible Rebel raid | `design` (boundary) |
| Q36 | The human's Invasion with no free commander still runs in the original: `empty` is 0, so newarmy and capture act on army slot 0 (not a real army). The port is captured and a ship lost | lines 1721-1729 | `fleet invade` is not listed when no commander is free | `design`; differs only when every commander slot is in use |
