"""Build harness.bas: the original game code, verbatim, driven by a command script.

Usage: python3 make_harness.py PATH/TO/CWSTRAT.BAS [--debug] > harness.bas

What is verbatim, and what is not. Each piece is marked in the output.

- Lines 1-104 (declarations) and every SUB from line 771 on, verbatim, with
  exactly these changes:
  - `SUB TICK` waits on the clock: emptied.
  - `SUB menu` reads the keyboard. It answers the menus the midterm answers
    by design (Retreat: ESC; Raze: No by ESC; End Game: Yes; Options: Quit)
    and otherwise returns the next scripted menu row.
  - `SUB railroad`: emptied, because railroads are out of scope.
  - `SUB maxx`, the hall of fame, does file and keyboard I/O and is not a
    rule: reduced to its last statement, `pcode = 1`.
  - `DO WHILE INKEY$ = "": LOOP` key waits: the condition becomes 0.
  - In SUB victor, one added line after `finis:` copies the condition number
    `j` to a shared variable so the dump can print it.
- Main-module rules, copied by line number from CWSTRAT.BAS:
  - newgame (128-136), `filer(1)` (138-139), fonts (148-149), the opening
    options and cash (151-167), unionplus (204, 749-752), cities (206-217);
  - END TURN (352) and newmonth with SUB victor (252-278, without 277's
    two-player branch);
  - the Supply menu (402-425) and the Drill menu (460-467), with
    `GOTO menu0` / `GOTO optmen` turned into `RETURN`;
  - the font DATA (763-769).
- Harness glue, marked `' harness:`:
  - argument parsing, and the midterm scope's two settings (Random Events
    OFF, no fleets);
  - `RANDOMIZE seed` for line 219's `RANDOMIZE TIMER`;
  - the command loop, which calls the original SUBs (armies, cancel,
    recruit, fortify, combine) or the copied blocks;
  - the state dump.
"""

import re
import sys
from pathlib import Path

REPLACE = {
    "TICK": "SUB TICK (sec!)\n' harness: no clock wait\nEND SUB\n",
    "menu": (
        "SUB menu (switch%)\n"
        "' harness: the midterm's design answers, then scripted menu rows (ESC when none are left)\n"
        "IF mtx$(0) = \"Retreat\" OR mtx$(0) = \"Raze ?\" THEN choose = -1: EXIT SUB\n"
        "IF mtx$(0) = \"End Game\" OR mtx$(0) = \"Options\" THEN choose = 1: EXIT SUB\n"
        "choose = -1: IF hqp < hqn THEN choose = hq(hqp): hqp = hqp + 1\n"
        "END SUB\n"
    ),
    "railroad": "SUB railroad (who)\n' harness: railroads are out of the midterm scope\nEND SUB\n",
    "maxx": "SUB maxx\n' harness: hall of fame (file and keyboard I/O) skipped; its last statement:\npcode = 1\nEND SUB\n",
}

GLUE_TOP = r'''
' harness: ============ main module: verbatim extracts (marked with their lines) and harness glue ============
DIM SHARED hq(20), hqn, hqp, harnessj
SCREEN 12
' harness: arguments are DATADIR SEED SCRIPT; DATADIR holds the four files filer(1) and line 207 read
args$ = COMMAND$: DIM argv$(3): n = 0
FOR k = 1 TO LEN(args$)
    ch$ = MID$(args$, k, 1)
    IF ch$ = " " THEN n = n + 1 ELSE argv$(n) = argv$(n) + ch$
NEXT k
cwsdatapath$ = argv$(0): seed# = VAL(argv$(1))
'''

GLUE_SCOPE = r'''
' harness: midterm scope. Random Events OFF (Utility option, line 600); navies out of scope (no fleets)
randbal = 0
FOR k = 1 TO 2: fleet$(k) = "": navysize(k) = 0: navyloc(k) = 0: NEXT k
'''

GLUE_LOOP = r'''
' harness: line 219 is RANDOMIZE TIMER; the episode seed stands in for TIMER
RANDOMIZE seed#
CALL topbar ' harness: menu0 (line 287) draws the topbar before the first turn
GOSUB dump

' harness: command loop. Each line is "OP ids | menu rows"; only the menu rows are used here.
OPEN "I", 2, argv$(2)
DO WHILE NOT EOF(2)
    LINE INPUT #2, c$
    op$ = LEFT$(c$, 1)
    hqn = 0: hqp = 0
    rows$ = MID$(c$, INSTR(c$ + "|", "|") + 1) + " "
    DO
        rows$ = LTRIM$(rows$): sp = INSTR(rows$, " ")
        IF sp <= 1 THEN EXIT DO
        hq(hqn) = VAL(LEFT$(rows$, sp - 1)): hqn = hqn + 1: rows$ = MID$(rows$, sp + 1)
    LOOP
    SELECT CASE op$
        CASE "M": CALL armies
        CASE "X": CALL cancel(side)
        CASE "T", "R": CALL recruit((side))
        CASE "F": CALL fortify(target)
        CASE "J": x = side: CALL combine(x)
        CASE "S": GOSUB hsupply
        CASE "D": GOSUB hdrill
        CASE "E"
            GOSUB hendturn
            IF thrill = 0 THEN CALL topbar ' harness: back at menu0 unless the game ended
    END SELECT
    GOSUB dump
LOOP
CLOSE #2
SYSTEM

dump: ' harness: the state compared with the Python engine
_DEST _CONSOLE
PRINT "STATE"; month; year; cash(1); cash(2); income(1); income(2); control(1); control(2); victory(1); victory(2); capcity(1); capcity(2); rflag; CVL(MKS$(aggress!)); armysize(0); thrill; harnessj
FOR i = 1 TO 40
    PRINT "A"; i; armysize(i); armyloc(i); armymove(i); armylead(i); armyexper(i); supply(i)
NEXT i
FOR i = 1 TO 40
    PRINT "C"; i; cityp(i); fort(i); occupied(i)
NEXT i
PRINT "END"
_DEST 0
RETURN
'''

DEBUG_PROBES = [
    # (anchor text in the SUB, statement printed just after it)
    ("\t\tc = occupied(a)\n", '_DEST _CONSOLE: PRINT "EC"; index; j; a; c; armysize(c): _DEST 0\n'),
    ("\t\tarray(j) = y\n", '_DEST _CONSOLE: PRINT "EV"; index; j; y: _DEST 0\n'),
    ("\t\tarmymove(i) = matrix(target, choose)\n", '_DEST _CONSOLE: PRINT "MV"; i; armymove(i): _DEST 0\n'),
    ("\twin = defend: lose = attack: IF hit = 1 THEN win = attack: lose = defend\n",
     '_DEST _CONSOLE: PRINT "BT"; attack; defend; x; x1; win: _DEST 0\n'),
    ("\tactive = INT(brray(j) / 100): active = brray(j) - 100 * active: s = 1: IF active > 20 THEN s = 2\n",
     '_DEST _CONSOLE: PRINT "GO"; active; armymove(active): _DEST 0\n'),
]


def instrument(subs: str) -> str:
    """--debug only: print the computer's intermediate decisions for diagnosis."""
    for anchor, probe in DEBUG_PROBES:
        assert anchor in subs, anchor
        subs = subs.replace(anchor, anchor + probe, 1)
    return subs


def extract(lines: list[str], a: int, b: int, returns: bool = False) -> str:
    """Lines a-b of CWSTRAT.BAS, verbatim; menu jumps become RETURN if asked."""
    body = "\n".join(lines[a - 1:b])
    if returns:
        # `IF c GOTO menu0` (no THEN) must become `IF c THEN RETURN`; any other jump is just RETURN.
        body = re.sub(r"(\bIF\b(?:(?!\bTHEN\b)[^\n:])*?)\s+GOTO (?:menu0|optmen)\b", r"\1 THEN RETURN", body)
        body = re.sub(r"\bGOTO (?:menu0|optmen)\b", "RETURN", body)
    return f"' ---- CWSTRAT.BAS lines {a}-{b}{', GOTO menu0/optmen as RETURN' if returns else ''}\n{body}\n"


def main(path: str, debug: bool = False) -> None:
    lines = Path(path).read_text(encoding="latin-1").splitlines()
    head = [l for l in lines[:104] if not l.startswith(("$EXEICON", "_ICON", "_TITLE"))]
    subs = "\n".join(lines[770:])
    declared = set(re.findall(r"^\s*SUB (\w+)", subs, re.M))
    for name, body in REPLACE.items():
        pattern = re.compile(rf"^[ \t]*SUB {name}\b.*?^[ \t]*END SUB[ \t]*$", re.S | re.M)
        subs, n = pattern.subn(body.replace("\\", "\\\\"), subs, count=1)
        assert n == 1, name
    assert set(re.findall(r"^\s*SUB (\w+)", subs, re.M)) == declared, "a replacement swallowed another SUB"
    subs, waits = re.subn(r'DO WHILE INKEY\$ = "": LOOP', "DO WHILE 0: LOOP", subs)
    subs, n = re.subn(r"^(\tfinis:)$", r"\1\n\t\tharnessj = j ' harness: report the condition number", subs, count=1, flags=re.M)
    assert n == 1, "finis label"
    if debug:
        subs = instrument(subs)

    main_module = (
        GLUE_TOP
        + extract(lines, 128, 136) + extract(lines, 138, 139) + extract(lines, 148, 149)
        + extract(lines, 151, 167) + GLUE_SCOPE
        + extract(lines, 204, 204) + extract(lines, 206, 217)
        + GLUE_LOOP
        + extract(lines, 749, 752)
        + "hendturn: ' harness: END TURN, then newmonth through SUB victor\n"
        + extract(lines, 352, 352) + extract(lines, 252, 276) + extract(lines, 278, 278) + "RETURN\n"
        + "hsupply: ' harness: Commands > Supply\n" + extract(lines, 402, 425, returns=True) + "RETURN\n"
        + "hdrill: ' harness: Commands > Army Drill\n" + extract(lines, 460, 467, returns=True) + "RETURN\n"
        + extract(lines, 763, 769)
    )
    print("$CONSOLE")
    print("$SCREENHIDE")
    print(f"' Generated by make_harness.py from CWSTRAT.BAS; see its docstring. {waits} key waits disabled.")
    print("\n".join(head))
    print(main_module)
    print(subs)


if __name__ == "__main__":
    main(sys.argv[1], "--debug" in sys.argv)
