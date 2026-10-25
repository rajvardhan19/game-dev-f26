"""Differential check: the Python engine against the original SUBs compiled by QB64.

    python3 tools/qb64-harness/compare.py --qb64 PATH/TO/qb64pe --bas PATH/TO/CWSTRAT.BAS \
        --scenario standard --seeds 1 2 3 --player original-ai --out tools/qb64-harness/recorded

For each seed: play an episode through cws.interface with a scripted
player, translating every accepted action into the command the harness
replays (a menu row where the original asks through a menu). Run the
harness, replay the same script on a fresh cws.engine.Game, and compare
the full state after every command. Recorded QB64 output is saved so CI can
re-check the Python engine without QB64 (tests/test_qb64_recorded.py).
"""

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from cws.data import DATA_DIR                                    # noqa: E402
from cws.engine import Game, UNION, starfin                      # noqa: E402
from cws.interface import CivilWarEpisode, PLAYER_ID             # noqa: E402
from cws.players.baselines import OriginalAI, PassivePlayer, RandomPlayer  # noqa: E402
from cws.scenarios import SCENARIOS                              # noqa: E402

PLAYERS = {"original-ai": OriginalAI, "random": RandomPlayer, "passive": PassivePlayer}


def menu_row(entries: list[tuple[str, int]], value: int) -> int:
    """Row of `value` in a menu built like the original: SUB bubble's stable sort by text."""
    ordered = sorted(entries, key=lambda e: e[0])
    return 1 + [v for _, v in ordered].index(value)


def movefrom_rows(g: Game, army: int) -> list[int]:
    """SUB movefrom, lines 1443-1469: the "From" city row, then "Which" if several idle armies."""
    idle = [i for i in starfin(UNION) if g.armyloc[i] > 0 and g.armymove[i] == 0]
    rows = [menu_row([(g.city[g.armyloc[i]], g.armyloc[i]) for i in idle], g.armyloc[army])]
    here = [i for i in idle if g.armyloc[i] == g.armyloc[army]]
    if len(here) > 1:
        rows.append(menu_row([(f"Army {i}", i) for i in here], army))   # "Army" + STR$(i)
    return rows


def cancel_name(name: str) -> str:
    """SUB cancel line 2703: a name over 10 characters keeps what follows its first blank."""
    return name[name.find(" ") + 1:] if len(name) > 10 else name


def to_command(g: Game, action: str) -> str:
    """'OP ids | menu rows': Python replays the ids, the harness feeds the rows to SUB menu."""
    verb, _, rest = action.partition(" ")
    city = {g.city[c].lower(): c for c in range(1, 41)}
    if action == "end turn":
        return "E |"
    if verb == "troops":
        return "T |"
    if verb == "recruit":
        c = city[rest.lower()]
        return f"R {c} | {menu_row([(g.city[x], x) for x in g.rcity], c)}"
    if verb == "move":
        army, _, dest = rest.partition(" ")
        army, d = int(army), city[dest.lower()]
        rows = movefrom_rows(g, army)
        rows.append(menu_row([(g.city[m], m) for m in g.neighbours(g.armyloc[army])], d))
        return f"M {army} {d} | {' '.join(map(str, rows))}"
    if verb == "cancel":
        army = int(rest)
        entries = [(cancel_name(g.armyname[j]), j) for j in starfin(UNION) if g.armyloc[j] > 0 and g.armymove[j] > 0]
        return f"X {army} | {menu_row(entries, army)}"
    if verb == "fortify":
        c = city[rest.lower()]
        entries = [(g.city[g.armyloc[i]], g.armyloc[i]) for i in starfin(UNION)
                   if g.armyloc[i] > 0 and g.fort[g.armyloc[i]] < 2]
        return f"F {c} | {menu_row(entries, c)}"
    if verb == "join":
        c = city[rest.lower()]
        return f"J {c} | {1 + g.combine_cities(UNION).index(c)}"
    if verb == "supply":
        army = int(rest)
        listed = [i for i in starfin(UNION) if g.armyloc[i] > 0 and g.supply[i] <= 1
                  and not (g.realism > 0 and g.cutoff(UNION, g.armyloc[i]) < 1)]
        return f"S {army} | {1 + listed.index(army)}"                      # this menu is not sorted
    if verb == "drill":
        army = int(rest)
        return f"D {army} | {' '.join(map(str, movefrom_rows(g, army)))}"
    raise ValueError(action)


def script_for(scenario: str, seed: float, player_name: str, max_turns: int) -> list[str]:
    ep = CivilWarEpisode(scenario)
    obs = ep.reset(seed)
    player = PLAYERS[player_name](seed)
    commands = []
    while ep.outcome()["status"] == "ongoing" and ep._game.turn <= max_turns:
        action = player.act(obs, ep.legal_actions(PLAYER_ID))
        command = to_command(ep._game, action)
        res = ep.step(PLAYER_ID, action)
        assert res["accepted"], action
        commands.append(command)
        obs = res["observation"]
    return commands


def dump(g: Game) -> list[str]:
    from struct import pack, unpack
    bits = unpack("<i", pack("<f", g.aggress))[0]
    thrill = g.result["checked_for"] if g.result else 0     # SUB victor: thrill = i
    condition = g.result["condition"] if g.result else 0    # SUB victor: j
    out = [" ".join(str(v) for v in ("STATE", g.month, g.year, g.cash[1], g.cash[2], g.income[1], g.income[2],
                                     g.control[1], g.control[2], g.victory[1], g.victory[2],
                                     g.capcity[1], g.capcity[2], g.rflag, bits, g.armysize[0], thrill, condition))]
    for i in range(1, 41):
        out.append(" ".join(str(v) for v in ("A", i, g.armysize[i], g.armyloc[i], g.armymove[i],
                                             g.armylead[i], g.armyexper[i], g.supply[i])))
    for i in range(1, 41):
        out.append(" ".join(str(v) for v in ("C", i, g.cityp[i], g.fort[i], g.occupied[i])))
    return out


def python_dumps(scenario: str, seed: float, commands: list[str]) -> list[list[str]]:
    """Replay the ids (the part before '|') through the engine, dumping after each command."""
    s = SCENARIOS[scenario]
    g = Game(s.map_files, s.settings)
    g.randomize(seed)
    dumps = [dump(g)]
    for c in commands:
        op, *args = c.split("|")[0].split()
        v = [int(a) for a in args]
        if op == "E":
            g.end_turn()                                  # newmonth, SUB victor, then topbar
        elif op == "T":
            g.recruit_open(UNION)
        elif op == "R":
            g.levy(UNION, v[0])
        elif op == "M":
            g.order_move(v[0], v[1])
        elif op == "X":
            g.cancel(v[0])
        elif op == "F":
            g.fortify(UNION, v[0])
        elif op == "J":
            g.combine(UNION, v[0])
        elif op == "S":
            g.resupply(v[0])
        elif op == "D":
            g.drill(v[0])
        dumps.append(dump(g))
    return dumps


def state_hash(state: list[str]) -> str:
    return hashlib.sha256("\n".join(state).encode()).hexdigest()[:16]


def parse_qb(text: str) -> list[list[str]]:
    dumps, cur = [], []
    for line in text.splitlines():
        line = " ".join(line.split())
        if not line:
            continue
        if line == "END":
            dumps.append(cur)
            cur = []
        else:
            cur.append(line)
    return dumps


def run_qb(exe: Path, scenario: str, seed: float, commands: list[str]) -> str:
    """Lay the data out as SUB filer expects (ALTMAP.BAT's renaming for the alternate map), then run."""
    s = SCENARIOS[scenario]
    with tempfile.TemporaryDirectory() as tmp:
        data = Path(tmp) / "cws"
        data.mkdir()
        for src, name in ((s.map_files.leaders, "cwslead.dat"), (s.map_files.ini, "cws.ini"),
                          (s.map_files.cities, "cities.grd")):
            (data / name).write_bytes((DATA_DIR / src).read_bytes())
        # cws.cfg: the shipped CWS.CFG with display and sound off and the scenario's aggression.
        cfg = (DATA_DIR / "CWS.CFG").read_text().strip().split(",")
        cfg[1], cfg[2], cfg[16] = "0", "0", str(s.settings.bold)
        (data / "cws.cfg").write_text(",".join(cfg) + "\n")
        script = Path(tmp) / "script.txt"
        script.write_text("\n".join(commands) + "\n")
        proc = subprocess.run([str(exe), f"{data} {float(seed)!r} {script}"], capture_output=True,
                              text=True, timeout=600, cwd=tmp)
    return proc.stdout


def first_difference(a: list[list[str]], b: list[list[str]], commands: list[str]) -> str | None:
    for k, (x, y) in enumerate(zip(a, b)):
        if x != y:
            for lx, ly in zip(x, y):
                if lx != ly:
                    where = "initial state" if k == 0 else f"after command {k} ({commands[k - 1]})"
                    return f"{where}: QB64 `{lx}` vs Python `{ly}`"
    if len(a) != len(b):
        return f"QB64 produced {len(a)} states, Python {len(b)}"
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--qb64", type=Path, required=True)
    ap.add_argument("--bas", type=Path, default=ROOT / "source" / "CWSTRAT.BAS")
    ap.add_argument("--scenario", default="standard")
    ap.add_argument("--player", default="original-ai", choices=sorted(PLAYERS))
    ap.add_argument("--seeds", type=float, nargs="+", default=[1, 2, 3])
    ap.add_argument("--turns", type=int, default=40)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    here = Path(__file__).resolve().parent
    bas = here / "harness.bas"
    with bas.open("w") as f:
        subprocess.run([sys.executable, str(here / "make_harness.py"), str(args.bas)], stdout=f, check=True)
    exe = here / "harness"
    subprocess.run([str(args.qb64), "-x", str(bas), "-o", str(exe)], check=True, capture_output=True)

    failures = 0
    for seed in args.seeds:
        commands = script_for(args.scenario, seed, args.player, args.turns)
        qb_text = run_qb(exe, args.scenario, seed, commands)
        qb, py = parse_qb(qb_text), [[" ".join(l.split()) for l in d] for d in python_dumps(args.scenario, seed, commands)]
        diff = first_difference(qb, py, commands)
        turns = sum(c.startswith("E") for c in commands)
        status = "MATCH" if diff is None else f"DIFF {diff}"
        print(f"{args.scenario} seed={seed:g} player={args.player} commands={len(commands)} turns={turns}: {status}")
        failures += diff is not None
        if args.out:
            args.out.mkdir(parents=True, exist_ok=True)
            name = f"{args.scenario}-{args.player}-seed{seed:g}.json"
            (args.out / name).write_text(json.dumps({
                "scenario": args.scenario, "seed": seed, "player": args.player,
                "qb64": "QB64-PE v4.7.0-GLFW, macOS arm64", "source": "CWSTRAT.BAS at dac8db1",
                "commands": commands, "match": diff is None, "difference": diff,
                "qb64_state_sha256_16": [state_hash(st) for st in qb],
                "qb64_final_state": qb[-1] if qb else [],
            }, indent=0))
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
