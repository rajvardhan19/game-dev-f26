"""Diagnosis aid: align the --debug harness's decision probes with the same probes in Python.

    python3 make_harness.py ../../source/CWSTRAT.BAS --debug > harness_debug.bas
    PATH/qb64pe -x harness_debug.bas -o harness_debug
    python3 debug_compare.py SCENARIO SEED PLAYER [COMMANDS]

Prints the first probe line where the original's computer and the port
disagree (EV/EC: evaluate scores and defenders; MV: march orders; BT:
battle strengths; GO: initiative order), with context.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
sys.path.insert(0, str(HERE))
import compare                                           # noqa: E402
from cws import smarts                                   # noqa: E402


def main() -> None:
    scenario, seed, player = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    commands = compare.script_for(scenario, seed, player, 40)
    if len(sys.argv) > 4:
        commands = commands[:int(sys.argv[4])]
    probes: list[str] = []
    smarts.PROBE = probes
    try:
        compare.python_dumps(scenario, seed, commands)
    finally:
        smarts.PROBE = None
    out = compare.run_qb(HERE / "harness_debug", scenario, seed, commands)
    qb = [" ".join(l.split()) for l in out.splitlines() if l.strip()[:2] in ("EV", "EC", "MV", "BT", "GO")]
    for k, (a, b) in enumerate(zip(qb, probes)):
        if a != b:
            print(f"first probe difference at #{k}:")
            for j in range(max(0, k - 8), min(len(qb), k + 4)):
                print(f"  QB {qb[j]:30s} | PY {probes[j] if j < len(probes) else ''}")
            return
    print("probes agree for", min(len(qb), len(probes)), "lines")


if __name__ == "__main__":
    main()
