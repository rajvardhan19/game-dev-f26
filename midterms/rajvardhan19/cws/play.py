"""Play the midterm scope in a terminal, or watch an agent play it.

    python -m cws.play                                  # you command the Union
    python -m cws.play --scenario alternate --seed 7
    python -m cws.play --watch original-ai --seed 2     # the baseline plays; you watch
    python -m cws.play --watch model-history --live     # Gemini plays (paid calls; dev seed 101)

Type an action's number or its text. Also: map, cities, armies, report, help, quit.
"""

import argparse
import os
import sys
import time

from .interface import CivilWarEpisode, PLAYER_ID

USE_COLOR = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None
COLOR = {"Union": "\033[94m", "Rebel": "\033[37m", "NEUTRAL": "\033[91m"}
RESET, BOLD, DIM = "\033[0m", "\033[1m", "\033[2m"


def paint(text: str, owner: str) -> str:
    return f"{COLOR[owner]}{text}{RESET}" if USE_COLOR else text


def ascii_map(obs: dict, width: int = 72, height: int = 24) -> str:
    """The original's screen positions (CITIES.GRD x, y) on a character grid."""
    grid = [[" "] * width for _ in range(height)]
    owners = {}
    armies = {}
    for a in obs["your_armies"]:
        armies[a["city"]] = "U"
    for a in obs["enemy_armies"]:
        armies[a["city"]] = "R" if a["city"] not in armies else "*"
    xs = [c["x"] for c in obs["cities"]]
    ys = [c["y"] for c in obs["cities"]]
    for c in sorted(obs["cities"], key=lambda c: (c["y"], c["x"])):
        col = int((c["x"] - min(xs)) / (max(xs) - min(xs)) * (width - 5))
        row = int((c["y"] - min(ys)) / (max(ys) - min(ys)) * (height - 1))
        label = f"{c['id']}{armies.get(c['id'], '')}"
        while any(grid[row][k] != " " for k in range(max(col - 1, 0), min(col + len(label) + 1, width))):
            col += 1                                     # slide right past a neighbour's label
            if col + len(label) >= width:
                col, row = 0, min(row + 1, height - 1)
        for k, ch in enumerate(label):
            grid[row][col + k] = ch
        owners[(row, col)] = (len(label), c["owner"])
    lines = []
    for r, row in enumerate(grid):
        out, col = "", 0
        while col < width:
            if (r, col) in owners:
                n, owner = owners[(r, col)]
                out += paint("".join(row[col:col + n]), owner)
                col += n
            else:
                out += row[col]
                col += 1
        lines.append(out.rstrip())
    legend = (f"{paint('Union', 'Union')}  {paint('Rebel', 'Rebel')}  {paint('neutral', 'NEUTRAL')}   "
              "number = city id; U/R = army there (* both)")
    return "\n".join(lines + [legend])


def header(obs: dict) -> str:
    t, vp = obs["treasury"], obs["victory_points"]
    return (f"{BOLD if USE_COLOR else ''}{obs['date']}{RESET if USE_COLOR else ''}  turn {obs['turn']}, "
            f"{obs['turns_left']} to the deadline | Union cash {t['Union']['cash']} income {t['Union']['income']} "
            f"cities {t['Union']['cities']} | Rebel cities {t['Rebel']['cities']} | VP {vp['Union']}-{vp['Rebel']}")


def armies(obs: dict) -> str:
    rows = ["Your armies:  id leader            men      city        ldr exp sup  order"]
    for a in obs["your_armies"]:
        rows.append(f"              {a['id']:<2} {a['name'][:16]:<16} {a['men']:>7}  {a['city_name']:<11} "
                    f"{a['leader']:>3} {a['experience']:>3} {a['supply']:>3}  {a['order']}")
    rows.append("Enemy armies: id leader            men      city        (out of supply)")
    for a in obs["enemy_armies"]:
        rows.append(f"              {a['id']:<2} {a['name'][:16]:<16} {a['men']:>7}  {a['city_name']:<11} "
                    f"{'yes' if a['out_of_supply'] else ''}")
    return "\n".join(rows)


def cities(obs: dict) -> str:
    rows = []
    for c in obs["cities"]:
        cap = f" capital of {c['capital_of']}" if c["capital_of"] else ""
        rows.append(paint(f"{c['id']:>2} {c['name']:<11} {c['owner']:<8} value {c['value']:>2} fort {c['fort']}"
                          f"{' port' if c['port'] else ''}{cap}  -> {', '.join(map(str, c['neighbors']))}", c["owner"]))
    return "\n".join(rows)


def report(obs: dict) -> str:
    if not obs["last_turn_report"]:
        return "(nothing happened yet)"
    return "\n".join("  " + e["text"] for e in obs["last_turn_report"])


def human(args) -> None:
    ep = CivilWarEpisode(args.scenario)
    obs = ep.reset(args.seed)
    print(__doc__)
    print("Victory conditions: " + "; ".join(obs["victory_conditions"]))
    print(ascii_map(obs))
    while ep.outcome()["status"] == "ongoing":
        print("\n" + header(obs))
        print(armies(obs))
        legal = ep.legal_actions(PLAYER_ID)
        for k, a in enumerate(legal, 1):
            print(f"  {k:>2}. {a}", end="\n" if k % 3 == 0 else "")
        print()
        try:
            text = input("> ").strip()
        except EOFError:
            return
        if text in ("quit", "q"):
            return
        if text == "help":
            print(__doc__)
            continue
        if text == "map":
            print(ascii_map(obs))
            continue
        if text == "cities":
            print(cities(obs))
            continue
        if text == "armies":
            print(armies(obs))
            continue
        if text == "report":
            print(report(obs))
            continue
        if text.isdigit() and 1 <= int(text) <= len(legal):
            text = legal[int(text) - 1]
        res = ep.step(PLAYER_ID, text)
        print(("" if res["accepted"] else "Refused: ") + res["text"])
        obs = res["observation"]
        if text == "end turn" and res["accepted"]:
            print("\nWhat happened:\n" + report(obs))
            print(ascii_map(obs))
    out = ep.outcome()
    print(f"\nGAME OVER: {out['reason']} ({out['date']}). Victory points Union {out['victory_points']['Union']}, "
          f"Rebel {out['victory_points']['Rebel']}.")


def watch(args) -> None:
    from .evaluate import make_player
    from .runner import Limits, run_episode
    player = make_player(args.watch, args.seed, args)

    def on_turn(obs):
        print("\n" + "=" * 78)
        print(header(obs))
        if obs["last_turn_report"]:
            print("What happened:\n" + report(obs))
        print(ascii_map(obs))
        print(armies(obs))

    def on_step(e):
        if "call" in e:
            ok = "ok" if e["ok"] else f"FAILED ({e['error']})"
            print(f"  [model call {e['call']}: {ok}, {e['latency']}s, {e['input_tokens']}+{e['output_tokens']} tokens]"
                  + (f" note: {e['note']}" if e.get("note") else ""))
        elif "action" in e:
            mark = "+" if e["accepted"] else "x"
            who = e["source"] + (f": {e['why']}" if e.get("why") else "")
            print(f"  {mark} [{who}] {e['action']}  -> {e['text'][:90]}")
            time.sleep(args.delay)

    r = run_episode(player, args.scenario, args.seed, Limits(engine_timeout=args.timeout + 30),
                    on_step=on_step, on_turn=on_turn)
    print(f"\nEPISODE OVER: {r.reason} ({r.date}). Steps {r.steps}, invalid {r.invalid_actions}, "
          f"fallbacks {r.fallback_actions}, model calls {r.model_calls} ({r.failed_calls} failed).")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scenario", default="standard", choices=["standard", "alternate", "reckless"])
    ap.add_argument("--seed", type=float, help="default 1; 101 (a dev seed) when watching a model")
    ap.add_argument("--watch", help="original-ai, random, passive, model-history or model-obs-only")
    ap.add_argument("--live", action="store_true", help="confirm paid model calls")
    ap.add_argument("--timeout", type=float, default=30.0)
    ap.add_argument("--delay", type=float, default=0.15, help="seconds between shown actions")
    args = ap.parse_args()
    if args.seed is None:
        # Evaluation seeds are held out from prompt work (SUITE.md): a casual model watch uses a dev seed.
        args.seed = 101 if (args.watch or "").startswith("model-") else 1
    watch(args) if args.watch else human(args)


if __name__ == "__main__":
    main()
