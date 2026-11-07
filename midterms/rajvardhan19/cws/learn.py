"""Train the learning player on the training seeds, freeze its notebook, write its journal.

    python -m cws.learn train --book lessons/gemini-a.json --run learn-<date> --live   # paid calls
    python -m cws.learn train --book lessons/gemini-b.json --run learn-<date>-b --seeds 301-350 --games 10 --live
    python -m cws.learn freeze --book lessons/gemini-a.json
    python -m cws.learn journal --book lessons/gemini-a.json --run learn-<date>

Training plays the declared schedule (SUITE.md): the training seeds, alternating
the standard and alternate maps. After each game the player reviews it and
rewrites its notebook. Per game, results/<run>/curve.jsonl records the result,
the notebook version used, the review, and what the player actually did
(cws/behaviour.py). An interrupted run resumes at the next game.
"""

import argparse
import datetime
import json
import sys
from pathlib import Path

from .behaviour import profile_file
from .evaluate import SUITE, cost, price_for
from .players.learner import (LearningPlayer, LessonBook, review, review_schema, review_system, review_text,
                               turn_lines)
from .runner import Limits, run_episode

ROOT = Path(__file__).resolve().parent.parent


DEFAULT_SEEDS = list(range(201, 209))                  # gemini-a's block
SCOREBOARD_RECENT = 20


def schedule(seeds: list[int] | None = None) -> list[tuple[str, int]]:
    """Training games in order: seed by seed, standard then alternate. Seeds must be training seeds."""
    seeds = list(seeds or DEFAULT_SEEDS)
    allowed = set(SUITE["standard"]["train"]) & set(SUITE["alternate"]["train"])
    if not set(seeds) <= allowed:
        raise SystemExit(f"not training seeds (SUITE.md): {sorted(set(seeds) - allowed)}")
    return [(scenario, seed) for seed in seeds for scenario in ("standard", "alternate")]


def parse_seeds(text: str) -> list[int]:
    """'301-350' or '301,305,310'."""
    out: list[int] = []
    for part in text.split(","):
        a, _, b = part.partition("-")
        out += list(range(int(a), int(b) + 1)) if b else [int(a)]
    return out


def _price(tokens_in: int, tokens_out: int, model: str) -> float:
    p = price_for(model)
    return tokens_in / 1e6 * p["input_per_m"] + tokens_out / 1e6 * p["output_per_m"] if p else 0.0


def scoreline(row: dict) -> str:
    p = row["behaviour"]
    return (f"game {row['game']} ({row['scenario']}, notebook v{row['book_version_used']}): {row['tier']} "
            f"after {row['turns']} turns, {p['cities_end']} cities at the end (peak {p['cities_peak']}); "
            f"you recruited {p['orders']['recruit']} times, drilled {p['orders']['drill']} times, "
            f"attacked {p['attacks']} times and won {p['attack_wins']}"
            + (f"; a player giving no orders lasted {row['passive_turns']} turns in the same game"
               if "passive_turns" in row else ""))


def mirror_text(p: dict, player: LearningPlayer) -> str:
    """What the player actually did this game, from its own orders and what it saw (the 'mirror')."""
    o = p["orders"]
    cash = [s["cash"] for _, s in sorted(player.seen.items())]
    odds = f" at {p['mean_attack_odds']}% odds on average" if p["mean_attack_odds"] is not None else ""
    return (f"Over {p['turns']} turns you ordered: troops {o['troops']}, recruit {o['recruit']}, drill {o['drill']}, "
            f"move {o['move']}, fortify {o['fortify']}, join {o['join']}, supply {o['supply']}, build {o['build']}, "
            f"fleet {o['fleet']}, rail {o['rail']}; {p['refused']} orders were refused. You started {p['attacks']} "
            f"battles{odds} and won {p['attack_wins']}. Cash at the start of each turn: "
            f"{', '.join(f'${c}' for c in cash)}. Your men: {p['men_start']:,} at the start, {p['men_peak']:,} at most, "
            f"{p['men_end']:,} at the end; the Rebels ended with {p['enemy_men_end']:,}.")


def teacher_text(trace: Path, max_turns: int = 25) -> str:
    """The original AI's game on the same seed, turn by turn: its numbers, orders, battles and captures."""
    rows = [json.loads(x) for x in Path(trace).read_text().splitlines() if x]
    h, out, cur = rows[0]["header"], [], None
    frames = []
    for r in rows[1:]:
        if "turn_start" in r or "game_end" in r:
            cur = {"board": r["board"], "report": r.get("report", []), "leaders": set(r.get("leaders", [])), "orders": {}}
            frames.append(cur)
        elif "action" in r and r["accepted"] and cur is not None:
            verb = r["action"].split()[0]
            if verb != "end":
                cur["orders"][verb] = cur["orders"].get(verb, 0) + 1
    out.append(f"Result: {h['reason']}, after {h['turns']} turns.")
    for k in range(len(frames) - 1)[:max_turns]:
        f, nxt = frames[k], frames[k + 1]
        b = f["board"]
        ours = f["leaders"] | nxt["leaders"]
        took = [e["text"].split(" has captured ")[-1] for e in nxt["report"]
                if e.get("kind") == "capture" and e["text"].split(" has captured ")[0] in ours]
        fights = [e["text"] for e in nxt["report"] if e.get("kind") == "battle" and e["text"].split(" attacks ")[0] in ours]
        won = sum(1 for t in fights if t.split(" attacks ")[0] == t.split(": ")[1].split(" wins")[0])
        orders = ", ".join(f"{v} {n}" for v, n in sorted(f["orders"].items(), key=lambda x: -x[1])) or "nothing"
        out.append(f"{b['date']}: ${b['cash']}, {b['owners'].count('U')} cities, {sum(a[2] for a in b['union']):,} men. "
                   f"Ordered {orders}. Started {len(fights)} battles, won {won}"
                   + (f"; took {', '.join(took)}." if took else "."))
    return "\n".join(out)


RATE_GROUPS = {"recruits": (lambda p: p["orders"]["recruit"], [(0, .01, "none"), (.01, 1, "under 1"), (1, 99, "1 or more")]),
               "attacks": (lambda p: p["attacks"], [(0, .01, "none"), (.01, .3, "up to 0.3"), (.3, 99, "over 0.3")]),
               "drills": (lambda p: p["orders"]["drill"], [(0, 1, "under 1"), (1, 2, "1 to 2"), (2, 99, "2 or more")])}


def contrast_text(mine: dict, teacher: dict, history: list[tuple[dict, int]]) -> str:
    """This game's rates beside the original AI's on the same game, and which of its own rates went with lasting
    longer. `history` is (behaviour, turns beyond the no-orders player) for every game so far, this one included."""
    def rate(p, n):
        return n / max(1, p["turns"])

    def won(p):
        return f"{100 * p['attack_wins'] / p['attacks']:.0f}%" if p["attacks"] else "-"

    lines = ["This game, per turn (you | the computer's Union on the same game):",
             f"recruits {rate(mine, mine['orders']['recruit']):.2f} | {rate(teacher, teacher['orders']['recruit']):.2f}; "
             f"battles started {rate(mine, mine['attacks']):.2f} | {rate(teacher, teacher['attacks']):.2f} "
             f"(won {won(mine)} | {won(teacher)}); drills {rate(mine, mine['orders']['drill']):.2f} | "
             f"{rate(teacher, teacher['orders']['drill']):.2f}; moves {rate(mine, mine['orders']['move']):.2f} | "
             f"{rate(teacher, teacher['orders']['move']):.2f}; peak cities {mine['cities_peak']} | {teacher['cities_peak']}; "
             f"cash going into the last turn ${mine['last_turn_cash']} | ${teacher['last_turn_cash']}; "
             f"result: {mine['tier']} after {mine['turns']} turns | {teacher['tier']} after {teacher['turns']} turns.",
             f"Across your {len(history)} games so far, turns lasted beyond the no-orders player, by your rate a turn:"]
    for name, (count, groups) in RATE_GROUPS.items():
        parts = []
        for lo, hi, label in groups:
            g = [s for p, s in history if lo <= count(p) / max(1, p["turns"]) < hi]
            if g:
                parts.append(f"{label}: {sum(g) / len(g):+.1f} ({len(g)} games)")
        lines.append(f"{name}: " + "; ".join(parts))
    return "\n".join(lines)


def lesson_records(rows: list[dict], book: LessonBook) -> dict:
    """lesson text -> (games it was in the notebook, mean turns against the no-orders player in those games)."""
    versions = {v["version"]: v["lessons"] for v in book.data["versions"]}
    scores: dict[str, list[int]] = {}
    for r in rows:
        if "passive_turns" in r:
            for lesson in versions.get(r["book_version_used"], []):
                scores.setdefault(lesson, []).append(r["turns"] - r["passive_turns"])
    return {k: (len(v), sum(v) / len(v)) for k, v in scores.items()}


def load_reference(root: Path, run: str) -> dict:
    """(scenario, seed) -> turns the passive player lasted, from a reference run on the training seeds."""
    rows = [json.loads(x) for x in (root / "results" / run / "results.jsonl").read_text().splitlines() if x]
    return {(r["scenario"], r["seed"]): r["turns"] for r in rows if r["player"] == "passive"}


def status_text(rows: list[dict], book: LessonBook, block: int = 10) -> str:
    """A progress report for the last block of games, written to results/<run>/status.md."""
    last = rows[-block:]
    out = [f"## After game {rows[-1]['game']}: notebook v{book.version}, {len(book.lessons)} lessons, "
           f"estimated cost so far ${sum(r['cost_usd'] for r in rows):.2f}", ""]
    for label, rs in ((f"games {last[0]['game']}-{last[-1]['game']}", last), ("all games", rows)):
        for sc in ("standard", "alternate"):
            g = [r for r in rs if r["scenario"] == sc]
            if not g:
                continue
            tiers = {t: sum(r["tier"] == t for r in g) for t in ("win", "held out", "decisive loss")}
            line = (f"- {label}, {sc}: {len(g)} games, {tiers['win']} won, {tiers['held out']} held out, "
                    f"{tiers['decisive loss']} lost; {sum(r['turns'] for r in g) / len(g):.1f} turns")
            if all("passive_turns" in r for r in g):
                line += (f" (no-orders player {sum(r['passive_turns'] for r in g) / len(g):.1f}; outlasted it in "
                         f"{sum(1 for r in g if r['turns'] > r['passive_turns'] or r['tier'] != 'decisive loss')})")
            out.append(line)
    b = [r["behaviour"] for r in last]
    n = len(b)
    out.append(f"- per game in this block: recruits {sum(x['orders']['recruit'] for x in b) / n:.1f} "
               f"(in {sum(1 for x in b if x['orders']['recruit'])} games), drills {sum(x['orders']['drill'] for x in b) / n:.1f}, "
               f"attacks {sum(x['attacks'] for x in b) / n:.1f} (won {sum(x['attack_wins'] for x in b)} of "
               f"{sum(x['attacks'] for x in b)}), last-turn cash ${sum(x['last_turn_cash'] for x in b) / n:.0f}, "
               f"peak men {sum(x['men_peak'] for x in b) / n:,.0f}")
    out.append(f"- reviews ok {sum(r['review_ok'] for r in last)}/{n}, failed calls {sum(r['failed_calls'] for r in last)}, "
               f"fallbacks {sum(r['fallback_actions'] for r in last)}")
    changes = [(v["version"], c) for v in book.data["versions"][1:] if v["after_game"]["game"] > rows[-1]["game"] - block
               for c in v["changes"]]
    out += ["", "Notebook changes in this block:"] + [f"- v{ver} {c['kind']}: {c['lesson']}" for ver, c in changes]
    if book.data.get("champion"):
        ch = book.data["champion"]
        out += ["", f"Champion: v{ch['version']} (round score {ch['score']:+.2f} turns against no orders); "
                    f"rounds accepted {sum(r['accepted'] for r in book.data.get('rounds', [])[1:])} of "
                    f"{max(0, len(book.data.get('rounds', [])) - 1)}"]
    if book.data["versions"][-1].get("strategy"):
        out += ["", f"Latest strategy: {book.data['versions'][-1]['strategy']}"]
    out += ["", "Notebook now:"] + [f"{i}. {x}" for i, x in enumerate(book.lessons, 1)] + ["", ""]
    return "\n".join(out)


def scoreboard(rows: list[dict]) -> list[str]:
    """The review's scoreboard: a summary of older games per map, then the most recent ones in full."""
    old, recent = rows[:-SCOREBOARD_RECENT], rows[-SCOREBOARD_RECENT:]
    lines = []
    for scenario in ("standard", "alternate"):
        rs = [r for r in old if r["scenario"] == scenario]
        if rs:
            n = len(rs)
            tiers = {t: sum(r["tier"] == t for r in rs) for t in ("win", "held out", "decisive loss")}
            lines.append(f"games 1-{len(old)} on {scenario} ({n} games): {tiers['win']} won, {tiers['held out']} held out, "
                         f"{tiers['decisive loss']} decisive losses; {sum(r['turns'] for r in rs) / n:.1f} turns on average; "
                         f"{sum(r['behaviour']['orders']['recruit'] for r in rs) / n:.1f} recruits, "
                         f"{sum(r['behaviour']['orders']['drill'] for r in rs) / n:.1f} drills and "
                         f"{sum(r['behaviour']['attacks'] for r in rs) / n:.1f} attacks a game")
    return lines + [scoreline(r) for r in recent]


def _calls_broken(r) -> bool:
    """Half or more of a game's model calls failed: a connection or quota problem, not the player."""
    return r.model_calls > 0 and r.failed_calls * 2 >= r.model_calls


def _stop_broken(r, game: int) -> None:
    raise SystemExit(f"stopping at game {game}: {r.failed_calls} of {r.model_calls} model calls failed (check the "
                     f"connection and quota). The game was not recorded; run the same command again to resume.")


def train(book_path: Path, run: str, client, review_client, root: Path = ROOT, games: int | None = None,
          limits: Limits | None = None, max_cost: float = 3.0, log=print, seeds: list[int] | None = None,
          method: dict | None = None, reference: str | None = None, status_every: int = 10) -> list[dict]:
    """`method` switches on mirror / track_record / actionable (how the review learns); `reference` names the
    passive player's run on the training seeds, needed by track_record. A notebook keeps one method for life."""
    book = LessonBook(book_path, model=client.model)
    if book.frozen:
        raise SystemExit(f"{book_path} is frozen: train a new notebook instead")
    seeds = list(seeds or book.data.get("seeds") or DEFAULT_SEEDS)
    if book.data.setdefault("seeds", seeds) != seeds:
        raise SystemExit(f"{book_path} trains on seeds {book.data['seeds']}, not {seeds}")
    method = {k: True for k, on in (method or {}).items() if on}
    if book.data.setdefault("method", method) != method:
        raise SystemExit(f"{book_path} learns with method {book.data['method']}, not {method}")
    passive = load_reference(root, reference) if reference else {}
    if method.get("track_record") and not all((sc, sd) in passive for sc, sd in schedule(seeds)):
        raise SystemExit("track_record needs --reference, a passive-player run covering every training seed")
    if (method.get("teacher") or method.get("contrast")) and passive and not all((root / "traces" / reference / f"original-ai-{sc}-{sd}.jsonl").exists()
                                         for sc, sd in schedule(seeds)):
        raise SystemExit("teacher and contrast need --reference with the original AI's traces on every training seed")
    if method.get("contrast") and not passive:
        raise SystemExit("contrast needs --reference")
    system = review_system(method)
    results, traces = root / "results" / run, root / "traces" / run
    results.mkdir(parents=True, exist_ok=True)
    curve_path = results / "curve.jsonl"
    rows = [json.loads(line) for line in curve_path.read_text().splitlines() if line] if curve_path.exists() else []
    plan = schedule(seeds)[: games or None]
    full = len(schedule(seeds))
    spent = sum(r["cost_usd"] for r in rows)
    for k in range(len(rows), len(plan)):
        if spent >= max_cost:
            log(f"stopping: estimated spend ${spent:.2f} reached --max-cost ${max_cost:.2f}")
            break
        scenario, seed = plan[k]
        player = LearningPlayer(client, book.lessons, fronts=bool(method.get("fronts")), plan=bool(method.get("plan")))
        player.config.update(lessons_book=book.data["name"], lessons_version=book.version, lessons_sha=book.sha())
        trace = traces / f"game-{k + 1:0{3 if full > 99 else 2}d}-{scenario}-{seed}.jsonl"
        log(f"== game {k + 1}/{full}: {scenario} seed {seed}, notebook v{book.version} ({len(book.lessons)} lessons)")
        r = run_episode(player, scenario, seed, limits or Limits(), trace_path=trace, on_end=player.end)
        if _calls_broken(r):
            _stop_broken(r, k + 1)
        behaviour = profile_file(trace)
        track = method.get("track_record")
        teach_trace = root / "traces" / str(reference) / f"original-ai-{scenario}-{seed}.jsonl"
        teach = teacher_text(teach_trace) if method.get("teacher") else None
        contrast = (contrast_text(behaviour, profile_file(teach_trace),
                                  [(x["behaviour"], x["turns"] - x["passive_turns"]) for x in rows if "passive_turns" in x]
                                  + [(behaviour, r.turns - passive[(scenario, seed)])])
                    if method.get("contrast") else None)
        text = review_text(k + 1, scenario, r.reason, r.turns, player, book.version, scoreboard(rows), teacher=teach,
                           contrast=contrast,
                           records=lesson_records(rows + [{"book_version_used": book.version, "turns": r.turns,
                                                           "passive_turns": passive[(scenario, seed)]}], book)
                           if track else None,                   # this game counts toward its lessons' record
                           mirror=mirror_text(behaviour, player) if method.get("mirror") else None,
                           passive_turns=passive[(scenario, seed)] if track else None)
        rev, error, rin, rout = review(review_client, text, system)
        used = book.version
        game = {"game": k + 1, "scenario": scenario, "reason": r.reason, "turns": r.turns}
        if rev:
            book.update(rev, game)
        play_cost = cost(r) or 0.0
        row = {"game": k + 1, "scenario": scenario, "seed": seed, "reason": r.reason,
               "tier": behaviour["tier"], "turns": r.turns, "cities_union": r.cities_union,
               "model_calls": r.model_calls, "failed_calls": r.failed_calls, "invalid_actions": r.invalid_actions,
               "fallback_actions": r.fallback_actions, "input_tokens": r.input_tokens, "output_tokens": r.output_tokens,
               "book_version_used": used, "book_version_after": book.version, "review_ok": rev is not None,
               "review_error": error, "review_input_tokens": rin, "review_output_tokens": rout,
               "cost_usd": round(play_cost + _price(rin, rout, client.model), 5),
               "behaviour": behaviour, "trace": str(trace.relative_to(root)),
               "run_date": datetime.date.today().isoformat(),
               "model_version": getattr(client, "model_version", None)}
        if (scenario, seed) in passive:
            row["passive_turns"] = passive[(scenario, seed)]
        rows.append(row)
        spent += row["cost_usd"]
        with curve_path.open("a") as f:
            f.write(json.dumps(row) + "\n")
        if status_every and (row["game"] % status_every == 0 or row["game"] == len(plan)):
            with (results / "status.md").open("a") as f:
                f.write(status_text(rows, book, status_every))
        p = row["behaviour"]
        log(f"   -> {r.reason} | turns {r.turns} | recruits {p['orders']['recruit']} drills {p['orders']['drill']} "
            f"attacks {p['attacks']} ({p['attack_wins']} won) | review {'ok' if rev else 'FAILED: ' + error} "
            f"| notebook v{book.version}")
    return rows


def _notebook_lines(title: str, lessons: list[str], openings: dict, records: dict | None) -> list[str]:
    lines = [title]
    for i, x in enumerate(lessons, 1):
        n, mean = (records or {}).get(x, (0, None))
        lines.append(f"{i}. {x}" + (f" [record: {n} games, {mean:+.1f} turns against no orders]" if n
                                    else " [record: no games yet]" if records is not None else ""))
    for m in ("standard", "alternate"):
        if openings.get(m):
            lines.append(f"Opening plan, {m} map: {openings[m]}")
    return lines


def round_review_text(round_no: int, played: list[dict], used: dict, champion: dict, verdict: str,
                      rounds: list[dict], records: dict | None) -> str:
    """The review after a round: the notebook those games used, the verdict, the notebook to improve, every game."""
    lines = [f"TRAINING ROUND {round_no}: {len(played)} games played with notebook v{used['version']}.",
             f"VERDICT: {verdict}", ""]
    lines += _notebook_lines(f"NOTEBOOK USED IN THESE GAMES (v{used['version']}):", used["lessons"],
                             used.get("openings", {}), records)
    if champion["version"] != used["version"]:
        lines += [""] + _notebook_lines(f"YOUR CURRENT NOTEBOOK, THE ONE TO IMPROVE (v{champion['version']}):",
                                        champion["lessons"], champion.get("openings", {}), records)
    if rounds:
        lines += ["", "EARLIER ROUNDS (score = mean turns against a player giving no orders, same games):"]
        lines += [f"round {r['round']}, notebook v{r['version']}: {r['score']:+.2f} "
                  f"({'kept' if r['accepted'] else 'rejected'})" for r in rounds[-10:]]
    seen_maps = set()
    for g in played:
        pl = g["player"]
        lines += ["", f"GAME {g['game']}, map: {g['scenario']}. RESULT: {g['reason']}, after {g['turns']} turns. "
                      f"A player giving no orders at all lasted {g['passive_turns']} turns in this same game."]
        if g["scenario"] not in seen_maps:
            seen_maps.add(g["scenario"])
            lines.append("VICTORY CONDITIONS: " + "; ".join(pl.conditions))
        if g.get("mirror"):
            lines.append("WHAT YOU ACTUALLY DID: " + g["mirror"])
        lines += turn_lines(pl, max_events=15)
    return "\n".join(lines)


def train_select(book_path: Path, run: str, client, review_client, root: Path = ROOT, round_size: int = 5,
                 games: int | None = None, limits: Limits | None = None, max_cost: float = 3.0, log=print,
                 seeds: list[int] | None = None, method: dict | None = None, reference: str | None = None,
                 status_every: int = 10, tolerance: float = 0.5) -> list[dict]:
    """Champion and challenger: the notebook plays a round of games; a new version replaces the champion unless
    its round score (turns against the passive player, same games) is more than `tolerance` below the
    champion's. The review then improves the champion. At the end the champion is the notebook kept."""
    book = LessonBook(book_path, model=client.model)
    if book.frozen:
        raise SystemExit(f"{book_path} is frozen: train a new notebook instead")
    seeds = list(seeds or book.data.get("seeds") or DEFAULT_SEEDS)
    if book.data.setdefault("seeds", seeds) != seeds:
        raise SystemExit(f"{book_path} trains on seeds {book.data['seeds']}, not {seeds}")
    method = {**{k: True for k, on in (method or {}).items() if on}, "select": True}
    if book.data.setdefault("method", method) != method or book.data.setdefault("round_size", round_size) != round_size:
        raise SystemExit(f"{book_path} learns with method {book.data['method']}, round size {book.data['round_size']}")
    if not reference:
        raise SystemExit("champion and challenger needs --reference, a passive-player run on the training seeds")
    passive = load_reference(root, reference)
    plan = schedule(seeds)[: games or None]
    if not all(g in passive for g in plan):
        raise SystemExit(f"--reference {reference} does not cover every training seed")
    system, schema = review_system(method), review_schema(method)
    results, traces = root / "results" / run, root / "traces" / run
    results.mkdir(parents=True, exist_ok=True)
    curve_path = results / "curve.jsonl"
    rows = [json.loads(x) for x in curve_path.read_text().splitlines() if x] if curve_path.exists() else []
    spent = sum(r["cost_usd"] for r in rows)
    played: list[dict] = []                              # this round's games, for the review
    full = len(schedule(seeds))
    for k in range(len(rows), len(plan)):
        if spent >= max_cost:
            log(f"stopping: estimated spend ${spent:.2f} reached --max-cost ${max_cost:.2f}")
            break
        scenario, seed = plan[k]
        opening = book.data.get("openings", {}).get(scenario) if method.get("openings") else None
        player = LearningPlayer(client, book.lessons, priority=bool(method.get("priority")), opening=opening)
        player.config.update(lessons_book=book.data["name"], lessons_version=book.version, lessons_sha=book.sha())
        trace = traces / f"game-{k + 1:0{3 if full > 99 else 2}d}-{scenario}-{seed}.jsonl"
        log(f"== game {k + 1}/{full}: {scenario} seed {seed}, notebook v{book.version}")
        r = run_episode(player, scenario, seed, limits or Limits(), trace_path=trace, on_end=player.end)
        if _calls_broken(r):
            _stop_broken(r, k + 1)
        behaviour = profile_file(trace)
        row = {"game": k + 1, "round": k // round_size + 1, "scenario": scenario, "seed": seed, "reason": r.reason,
               "tier": behaviour["tier"], "turns": r.turns, "passive_turns": passive[(scenario, seed)],
               "cities_union": r.cities_union, "model_calls": r.model_calls, "failed_calls": r.failed_calls,
               "invalid_actions": r.invalid_actions, "fallback_actions": r.fallback_actions,
               "input_tokens": r.input_tokens, "output_tokens": r.output_tokens, "book_version_used": book.version,
               "book_version_after": book.version, "review_ok": True, "review_error": "",
               "review_input_tokens": 0, "review_output_tokens": 0, "cost_usd": round(cost(r) or 0.0, 5),
               "behaviour": behaviour, "trace": str(trace.relative_to(root)),
               "run_date": datetime.date.today().isoformat(), "model_version": getattr(client, "model_version", None)}
        played.append({"game": k + 1, "scenario": scenario, "reason": r.reason, "turns": r.turns,
                       "passive_turns": passive[(scenario, seed)], "player": player,
                       "mirror": mirror_text(behaviour, player) if method.get("mirror") else None})
        if (k + 1) % round_size == 0 or k + 1 == len(plan):
            this = [x for x in rows if x["round"] == row["round"]] + [row]
            score = sum(x["turns"] - x["passive_turns"] for x in this) / len(this)
            used = {"version": book.version, "lessons": book.lessons, "openings": dict(book.data.get("openings", {})),
                    "strategy": book.data.get("strategy", ""), "score": score}
            champ = book.data.get("champion")
            if champ is None:
                accepted, verdict = True, f"your first notebook scored {score:+.2f} turns against no orders; it is your current notebook."
            else:
                accepted = score >= champ["score"] - tolerance
                verdict = (f"notebook v{book.version} scored {score:+.2f} against your current notebook's "
                           f"{champ['score']:+.2f}: " + ("it replaces it." if accepted else
                                                          "it did clearly worse and is set aside; improve your current notebook."))
            if accepted:
                book.data["champion"] = champ = used
            book.data.setdefault("rounds", []).append({"round": row["round"], "version": used["version"],
                                                        "score": round(score, 3), "accepted": accepted,
                                                        "champion": champ["version"], "after_game": k + 1})
            book.save()
            log(f"   round {row['round']}: v{used['version']} scored {score:+.2f} -> {'kept' if accepted else 'rejected'}; "
                f"champion v{champ['version']}")
            if k + 1 < len(plan):
                text = round_review_text(row["round"], played, used, champ, verdict, book.data["rounds"][:-1],
                                         lesson_records(rows + [row], book) if method.get("track_record") else None)
                rev, error, rin, rout = review(review_client, text, system, schema)
                if rev:
                    book.update(rev, {"game": k + 1, "scenario": scenario, "reason": r.reason, "turns": r.turns})
                elif not accepted:                       # no new version: play the champion again
                    _restore(book, champ, k + 1, f"review failed; champion v{champ['version']} restored")
                row.update(review_ok=rev is not None, review_error=error, review_input_tokens=rin,
                           review_output_tokens=rout, book_version_after=book.version,
                           cost_usd=round(row["cost_usd"] + _price(rin, rout, client.model), 5))
            played = []
        rows.append(row)
        spent += row["cost_usd"]
        with curve_path.open("a") as f:
            f.write(json.dumps(row) + "\n")
        if status_every and (row["game"] % status_every == 0 or row["game"] == len(plan)):
            with (results / "status.md").open("a") as f:
                f.write(status_text(rows, book, status_every))
    if len(rows) == len(schedule(seeds)) and book.data.get("champion"):
        ch = book.data["champion"]                       # the notebook kept is the champion, not the last version
        _restore(book, ch, len(rows), f"final notebook: champion v{ch['version']}")
        log(f"training done: kept champion v{ch['version']} as v{book.version}")
    return rows


def _restore(book: LessonBook, ch: dict, game: int, note: str) -> None:
    """A new version that is a copy of the champion, so every version number names what was played."""
    book.data["version"] += 1
    book.data["lessons"], book.data["openings"] = list(ch["lessons"]), dict(ch["openings"])
    book.data["strategy"] = ch.get("strategy", "")
    book.data["versions"].append({"version": book.version, "after_game": {"game": game, "scenario": "-",
                                  "reason": note, "turns": 0}, "diagnosis": "", "lessons": list(ch["lessons"]),
                                  "changes": [], "strategy": ch.get("strategy", ""), "note": note})
    book.save()


def journal(book: LessonBook, rows: list[dict]) -> str:
    """A readable record of how the notebook and the play changed, game by game."""
    out = [f"# Learning journal: `{book.data['name']}`", "",
           f"Model `{book.data.get('model', '')}`. {len(rows)} training games; notebook version {book.version}"
           f"{' (frozen, sha ' + book.data.get('frozen_sha', '') + ')' if book.frozen else ''}.", "",
           "## What it did, game by game", "",
           "| game | map | notebook | result | turns | recruits | drills | moves | attacks (won) | mean odds | "
           "cities peak / end | last-turn cash | refused |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        p = r["behaviour"]
        out.append(f"| {r['game']} | {r['scenario']} | v{r['book_version_used']} | {r['tier']}: {r['reason']} | "
                   f"{r['turns']} | {p['orders']['recruit']} | {p['orders']['drill']} | {p['orders']['move']} | "
                   f"{p['attacks']} ({p['attack_wins']}) | {p['mean_attack_odds'] if p['mean_attack_odds'] is not None else '-'}"
                   f"{'%' if p['mean_attack_odds'] is not None else ''} | {p['cities_peak']} / {p['cities_end']} | "
                   f"{p['last_turn_cash']} | {p['refused']} |")
    out += ["", "## How the notebook changed", ""]
    for v in book.data["versions"][1:]:
        g = v["after_game"]
        out += [f"### Version {v['version']}, after game {g['game']} ({g['scenario']}: {g['reason']}, {g['turns']} turns)",
                "", f"**Diagnosis.** {v['diagnosis']}", "", f"**Strategy for the next game.** {v['strategy']}", ""]
        if v["changes"]:
            out += ["**Changes:**", ""] + [f"- {c['kind']}: {c['lesson']} ({c['why']})" for c in v["changes"]] + [""]
        out += ["**Notebook:**", ""] + [f"{i}. {x}" for i, x in enumerate(v["lessons"], 1)] + [""]
    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["train", "freeze", "journal"])
    ap.add_argument("--book", required=True, type=Path, help="the notebook file, e.g. lessons/gemini-a.json")
    ap.add_argument("--run", help="results/<run> and traces/<run> for training")
    ap.add_argument("--games", type=int, help="play up to game N of the schedule (resumes where it stopped)")
    ap.add_argument("--seeds", type=parse_seeds, help="training seeds, e.g. 301-350 (default 201-208)")
    ap.add_argument("--mirror", action="store_true", help="show the review what the player actually did")
    ap.add_argument("--track-record", action="store_true", help="show each lesson's record against no orders")
    ap.add_argument("--actionable", action="store_true", help="ask for lessons as 'When ..., <orders>' rules")
    ap.add_argument("--reference", help="the passive player's run on the training seeds (for --track-record)")
    ap.add_argument("--select", type=int, metavar="N", help="champion and challenger in rounds of N games")
    ap.add_argument("--priority", action="store_true", help="ask for lessons in priority order")
    ap.add_argument("--openings", action="store_true", help="ask for an opening plan per map, shown on turn 1")
    ap.add_argument("--teacher", action="store_true", help="show the review the original AI's game on the same seed")
    ap.add_argument("--plan", action="store_true", help="the player plans each turn before ordering (execution aid)")
    ap.add_argument("--fronts", action="store_true", help="the player sees the front summary (execution aid)")
    ap.add_argument("--contrast", action="store_true", help="show the review its rates beside the original AI's, "
                                                            "and which of its rates went with lasting longer")
    ap.add_argument("--live", action="store_true", help="confirm paid model calls")
    ap.add_argument("--timeout", type=float, default=30.0)
    ap.add_argument("--max-output-tokens", type=int, default=2048, help="per player call (thinking models need more)")
    ap.add_argument("--max-cost", type=float, default=3.0, help="stop training once the estimate reaches this (USD)")
    args = ap.parse_args()
    book_path = args.book if args.book.is_absolute() else ROOT / args.book
    if args.command == "freeze":
        book = LessonBook(book_path)
        book.freeze()
        print(f"frozen {book_path} at version {book.version}, sha {book.sha()}")
        return
    if not args.run:
        sys.exit("--run is required")
    if args.command == "journal":
        rows = [json.loads(line) for line in (ROOT / "results" / args.run / "curve.jsonl").read_text().splitlines() if line]
        text = journal(LessonBook(book_path), rows)
        (ROOT / "results" / args.run / "journal.md").write_text(text + "\n")
        print(f"wrote results/{args.run}/journal.md")
        return
    if not args.live:
        sys.exit("Training makes paid calls: pass --live to confirm.")
    from .players.model_player import VertexClient
    client = VertexClient(timeout=args.timeout, max_output_tokens=args.max_output_tokens)
    review_client = VertexClient(timeout=max(60.0, args.timeout), max_output_tokens=max(4096, args.max_output_tokens))
    method = {"mirror": args.mirror, "track_record": args.track_record, "actionable": args.actionable,
              "priority": args.priority, "openings": args.openings, "teacher": args.teacher, "contrast": args.contrast,
              "plan": args.plan, "fronts": args.fronts}
    limits = Limits(engine_timeout=args.timeout + 30, decision_timeout=max(45.0, args.timeout + 15))
    if args.select:
        train_select(book_path, args.run, client, review_client, round_size=args.select, games=args.games,
                     limits=limits, max_cost=args.max_cost, seeds=args.seeds, method=method, reference=args.reference)
    elif args.priority or args.openings:
        sys.exit("--priority and --openings are only implemented with --select")
    else:
        train(book_path, args.run, client, review_client, games=args.games, limits=limits, max_cost=args.max_cost,
              seeds=args.seeds, method=method, reference=args.reference)


if __name__ == "__main__":
    main()
