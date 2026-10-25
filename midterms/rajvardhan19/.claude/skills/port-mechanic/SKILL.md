---
name: port-mechanic
description: "Use when porting, changing or fixing one rule of VGA Civil War Strategy from CWSTRAT.BAS: supply, recruiting, movement, fortification, battle, the opponent's smarts, or victory. Reads only that SUB, writes a hand-traced test with scripted dice first, ports with QB64 numeric semantics, checks the result against the original under QB64, and ends with a summary for the independent reviewer."
---

# Port one mechanic from CWSTRAT.BAS

A rule is correct only if it matches what CWSTRAT.BAS computes from the same
state and dice. This skill is the student's Week 3 method made repeatable.

## Steps

1. **Name the mechanic and its SUB.** Find it with
   `grep -n "SUB name" source/CWSTRAT.BAS` (some SUBs are
   indented). Read only that SUB and the SUBs it calls, plus
   `source/VariablesGuide.md`. Do not read other mechanics "for
   context".
2. **Find its row in `docs/rule-source-map.md`.** Quote the row and its label.
   If it is missing, add it first with the strongest honest label: `code`
   (a CWSTRAT.BAS line or data file), `observed` (seen in a QB64 run),
   `assumed` (unverified) or `design` (our choice, with the reason).
3. **Trace one case by hand.** Pick a small state and a list of RND values.
   Walk the SUB line by line on paper: every `RND` in order (QBasic `AND` does
   not short-circuit, so a condition can roll even when its first half is
   false), every rounding (`DEFINT A-Z`: an assignment rounds half to even),
   every unreachable `CASE`. Write the expected numbers and the number of
   rolls consumed.
4. **Write the test before the port.** Use `cws.qb.ScriptedDice(values)` so a
   port that rolls once too often or too rarely fails. Run it; confirm it fails
   for the expected reason.
5. **Port.** One method per SUB in `cws/engine.py` or `cws/smarts.py`, with
   `line N` citations. Numeric rules (`cws/qb.py`): decimal literals are
   doubles; arithmetic runs in double; an INTEGER assignment is
   `cint(f32(expr))`; a SINGLE assignment is `f32(expr)`; a comparison is
   `f32(lhs) op f32(rhs)` (use `S(literal)`); `\` is `idiv`; `INT` is `qint`.
6. **Check the information boundary.** In `cws/interface.py`: `observe` shows
   only what the original shows a human Union player; `legal_actions` names
   nothing the observation has not shown and rolls no dice; a refused action
   changes nothing and is counted. Run the two-seed test
   (`tests/test_interface.py`): observations must be identical before any roll.
7. **Check against the original.** If QB64-PE is installed, run
   `python3 tools/qb64-harness/compare.py --qb64 PATH --bas PATH --seeds 1 2 3`.
   Any `DIFF` names the first command whose state differs; build the
   `--debug` harness and `debug_compare.py` to align the computer's decisions.
   If you changed engine behaviour on purpose, re-record with `--out` and say
   why in the summary.
8. **Record ambiguities** in `QUESTIONS.md`: what the source does, what a
   reader might expect, what we chose.
9. **Run** `python -m unittest discover -s tests -v`. All pass, or stop and
   report the failure.
10. **Write the summary for the reviewer**, in this order: the rule as it now
    reads with its label and line; the test and that it failed first; the
    QB64 comparison result; any boundary effect, or "none"; anything assumed.

## Do not

- write a rule from memory of the game or from what "should" happen;
- correct a quirk of the original (record it instead);
- give the playing agent file access, the Game, the map or the opponent's code;
- mark your own work reviewed.
