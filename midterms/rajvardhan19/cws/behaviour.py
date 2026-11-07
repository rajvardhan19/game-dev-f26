"""What a player actually did in one game, measured from its trace.

Used to follow how a learning player's play changes from game to game, next
to what its notebook says. It reads only the trace (orders, the visible turn
reports and the opening board of each turn), never the engine.
"""

import json
import re
from collections import Counter
from pathlib import Path

BATTLE = re.compile(r"(?P<a>.+?) attacks (?P<d>.+?) in (?P<c>.+?): (?P<w>.+?) wins "
                    r"\(attack \d+ vs defend \d+, odds (?P<o>\d+)%\)")
VERBS = ("troops", "recruit", "move", "drill", "fortify", "join", "supply", "build", "fleet", "rail", "cancel")


def tier(reason: str) -> str:
    if reason.startswith("Union victory"):
        return "win"
    if reason == "Rebel victory: time expired":
        return "held out"
    if reason.startswith("Rebel victory"):
        return "decisive loss"
    return "incomplete"


def profile(rows: list[dict]) -> dict:
    """Counts and trajectories for one game. `rows` are the trace's lines, header first."""
    h = rows[0]["header"]
    boards, leaders, reports = [], [], []
    orders, refused = Counter(), 0
    for r in rows[1:]:
        if "turn_start" in r or "game_end" in r:
            boards.append(r["board"])
            leaders.append(set(r.get("leaders", [])))
            reports.append(r.get("report", []))
        elif "action" in r:
            verb = r["action"].split()[0] if r["action"].strip() else ""
            if r["accepted"]:
                if verb in VERBS:
                    orders[verb] += 1
            else:
                refused += 1
    # The report shown at board k describes the turn that ended there; its own attackers are
    # the leaders of board k-1, plus any army raised during that turn (named at board k).
    attacks, wins, odds, rebel_attacks = 0, 0, [], 0
    for k in range(1, len(boards)):
        ours = leaders[k - 1] | leaders[k]
        for e in reports[k]:
            m = BATTLE.match(e["text"]) if e.get("kind") == "battle" else None
            if not m:
                continue
            if m["a"] in ours:
                attacks += 1
                wins += m["w"] == m["a"]
                odds.append(int(m["o"]))
            else:
                rebel_attacks += 1
    cities = [b["owners"].count("U") for b in boards]
    men = [sum(a[2] for a in b["union"]) for b in boards]
    enemy = [sum(a[2] for a in b["rebel"]) for b in boards]
    opening = boards[:-1] if len(boards) > 1 else boards     # the last board is the final position
    cash = [b["cash"] for b in opening]
    gained = lost = 0
    for k in range(1, len(boards)):
        before, after = boards[k - 1]["owners"], boards[k]["owners"]
        gained += sum(1 for x, y in zip(before, after) if x != "U" and y == "U")
        lost += sum(1 for x, y in zip(before, after) if x == "U" and y != "U")
    turns = max(h.get("turns", 0), 1)
    return {
        "reason": h["reason"], "tier": tier(h["reason"]), "turns": h["turns"], "date": h["date"],
        "orders": {v: orders.get(v, 0) for v in VERBS}, "refused": refused,
        "recruits_per_turn": round(orders["recruit"] / turns, 2), "drills_per_turn": round(orders["drill"] / turns, 2),
        "attacks": attacks, "attack_wins": wins, "mean_attack_odds": round(sum(odds) / len(odds)) if odds else None,
        "long_shot_attacks": sum(1 for o in odds if o < 35), "rebel_attacks": rebel_attacks,
        "cities_start": cities[0] if cities else 0, "cities_peak": max(cities) if cities else 0,
        "cities_end": cities[-1] if cities else 0, "cities_gained": gained, "cities_lost": lost,
        "mean_cash": round(sum(cash) / len(cash)) if cash else 0, "peak_cash": max(cash) if cash else 0,
        "last_turn_cash": cash[-1] if cash else 0,
        "men_start": men[0] if men else 0, "men_peak": max(men) if men else 0, "men_end": men[-1] if men else 0,
        "enemy_men_end": enemy[-1] if enemy else 0,
    }


def profile_file(path: Path) -> dict:
    return profile([json.loads(line) for line in Path(path).read_text().splitlines() if line])
