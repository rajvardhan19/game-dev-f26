# Open questions and ambiguities

Recorded instead of guessed, as the Week 3 plan requires. Each entry gives
what the source does, what a reader might expect, and what the
reconstruction does. "Kept" means the source's behaviour is reproduced.

| # | Question | Source | Reconstruction | Status |
|---|---|---|---|---|
| Q1 | QB64 on x86 computes integer `/` in 80-bit long double; on arm64 (where every comparison was run) long double is a double. Could a rounding boundary differ between the two builds? | generated C++ `a/((long double)b)` | Uses double, matching the arm64 build all 36 recorded games came from. | `assumed` identical in practice; untested on x86 |
| Q2 | When a Union army loses a defence and two or more friendly cities qualify, the original asks the human where to retreat | SUB retreat lines 3617-3637 | Answers ESC, which falls through to the automatic choice (most valuable friendly neighbour) | `design`; a human could pick differently |
| Q3 | After an unopposed capture of a fortified city the original asks the human "Raze ?" | lines 2564-2574 | Always No | `design` |
| Q4 | `randsel` reads `armysize(0)`, a scratch slot `combine` leaves holding the last merged size. The screen never shows it. | lines 2152, 1063, 1078 | The opponent uses the true value (it is the engine). The Union baseline, playing from the screen, reads 0. | `design` (boundary) |
| Q5 | A surrender or a crushed army gives 25 VP to the **defender's** side, even when the defender is the one destroyed | line 2541 (`victory(3 - s)` with `s` the attacker's side) | Kept | `code`; probably unintended upstream |
| Q6 | Every battle subtracts 1 supply from Union armies 1 and 2, not the combatants | line 947 (`FOR i = 1 TO 2: IF supply(i) > 0`) | Kept | `code`; probably unintended |
| Q7 | `cash < 222` in smarts reads an undeclared scalar, always 0, so it is always true | line 2251 | Kept (it only matters for the computer's Union, i.e. our baseline) | `code` |
| Q8 | The "crossing moves" guard compares a friend's destination with the mover's army **size** | line 2327 (`armymove(y) = x`, `x = armysize(i)` from line 2307) | Kept | `code` |
| Q9 | `evaluate` adds 50 when `cityp(m) = capcity(side)`, comparing an owner (0-2) with a city number | line 3031 | Kept; it can only fire if a capital is city 1 or 2 | `code` |
| Q10 | With navies out of scope, the computer never spends on ships, and the Union AI never builds the ship line 2256 would buy | lines 2256-2297 | Fleets start at zero; navy branches cannot fire | `design`; the opponent may be slightly richer than in v2.11 |
| Q11 | Random events default to "Favor Rebels" for a Union player (line 160) but are a Utility option | lines 160, 587-619 | OFF | `design`; removes a source of luck that would favour the opponent |
| Q12 | `RANDOMIZE TIMER` makes every original game different; which "seed" is faithful? | line 219 | `RANDOMIZE seed` with the episode seed (any value TIMER can take) | `design` |
| Q13 | The two opening `50 * RND` cash rolls happen before `RANDOMIZE TIMER`, so in v2.11 they are always the same (+35, +27). Intended? | lines 167, 219 | Kept: every game opens with Union 525, Rebel 318 | `code`, `observed` |
| Q14 | Several `SELECT CASE` branches are unreachable (`< .2` after `< .5`; `> 800` after `> 300`; `> 800`, `> 1000` after `> 400`) | lines 891-900, 970-975, 981-986, 2416-2425 | Kept | `code` |
| Q15 | `CWS.CFG` ships with January campaigns allowed (`jancam = 1`), so the no-January-campaign rule never applies here | CWS.CFG field 10; line 814 | Implemented but inactive | `code` |
| Q16 | The human's "Supply" list shows armies at supply 1 or less; the computer resupplies only at 0 | lines 407, 2221 | Kept | `code` |
| Q17 | Does the original's rail move change the computer's strength enough that excluding it misrepresents the opponent? | lines 1969-2072, 2301 | Excluded for both sides | `assumed` minor; not measured |
| Q18 | Victory point share is shown on screen, but a side conquered early can end with a higher share than one that held out (VP decay, and the deadline's x .7) | lines 2641-2648, 4498 | The evaluation ranks by outcome tier, then turns, and reports VP share for information only | `design`; see EVALUATION.md |
| Q19 | Casualty bookkeeping tests `attack > 2`, not `attack > 20`, so a Rebel attacker's losses can be booked to the wrong side | line 1028 | Kept; it feeds only the Battles report, not any rule | `code` |
| Q20 | When a defender is destroyed, the winner "absorbs" its supply after it has been set to 0, so it gains nothing | line 2545 | Kept | `code` |
| Q21 | In evaluate, `IF fort(a) = 3` is nested inside `IF fort(a) = 1` and cannot hold, so a level-2 fort counts like no fort (x1 = 1) | line 2989 | Kept | `code` |
| Q22 | The Rebel bonus for more than 34 cities sets `victory(2) = victory(1) + 100`, using the Union's points | line 2647 | Kept | `code` |
| Q23 | `playb` adds a difficulty bonus to a new army's size, which `newarmy` then overwrites (line 1898); at Balanced it adds nothing anyway | lines 2174-2177, 1898 | Kept | `code` |
| Q24 | SUB cancel finds the army by name: the last army in that city whose name contains the menu text (`INSTR`). Two "Banks" (CWSLEAD.DAT slots 7 and 18), or "Union I" beside "Union II", can cancel a different army than the one chosen. | lines 2703, 2716 | `cancel <id>` cancels exactly that army. The harness runs the original SUB cancel; no recorded game reached the ambiguous case. | `design`; differs only for duplicate or prefix names |
| Q25 | A one-army "join" (lines 1098-1116) changes nothing visible but resets `occupied(target)` and caps supply at 10 | lines 1094-1116 | `join` is listed only when two or more armies would merge | `design`; it is not a merge |
