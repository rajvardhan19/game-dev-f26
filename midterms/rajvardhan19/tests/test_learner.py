"""The learning player, offline: its review sees only the screen, its notebook is bounded,
versioned and frozen before evaluation, and training records what it actually did.

A scripted client stands in for Gemini; nothing here is evidence about a live model.
"""

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from cws.behaviour import profile
from cws.evaluate import SUITE, price_for
from cws.learn import _price, journal, schedule, train
from cws.players.learner import LearningPlayer, LessonBook, MAX_CHARS, MAX_LESSONS, clean_review, review_text
from cws.players.model_player import FakeClient, ModelPlayer, render
from cws.runner import Limits, run_episode

REVIEW = {"diagnosis": "I never raised troops and the Rebels outgrew me.",
          "lessons": ["Call troops every turn and recruit with spare cash.", "Never leave a city empty."],
          "changes": [{"kind": "added", "lesson": "Call troops every turn and recruit with spare cash.",
                       "why": "the enemy raised three armies a turn"}],
          "strategy": "Recruit first, hold the border cities, attack only at good odds."}


def end_turns(n=60):
    return [{"actions": ["end turn"], "note": "hold"}] * n


class Notebook(unittest.TestCase):
    def test_review_is_cleaned_and_bounded(self):
        long = "x" * (MAX_CHARS + 50)
        out = clean_review({**REVIEW, "lessons": [long] + [f"lesson {i}" for i in range(20)] + ["Lesson 1"]})
        self.assertEqual(len(out["lessons"]), MAX_LESSONS)
        self.assertEqual(len(out["lessons"][0]), MAX_CHARS)
        self.assertEqual(sum(1 for x in out["lessons"] if x.lower() == "lesson 1"), 1)   # duplicates dropped
        for bad in ({"lessons": []}, {"lessons": "recruit"}, {"lessons": [3]}, []):
            with self.assertRaises(ValueError):
                clean_review(bad)

    def test_versions_are_kept_and_a_frozen_book_refuses(self):
        with tempfile.TemporaryDirectory() as tmp:
            book = LessonBook(Path(tmp) / "b.json")
            book.update(clean_review(REVIEW), {"game": 1, "scenario": "standard", "reason": "x", "turns": 5})
            again = LessonBook(Path(tmp) / "b.json")
            self.assertEqual((again.version, again.lessons), (1, REVIEW["lessons"]))
            self.assertEqual([v["version"] for v in again.data["versions"]], [0, 1])
            again.freeze()
            before = hashlib.sha256((Path(tmp) / "b.json").read_bytes()).hexdigest()
            with self.assertRaises(PermissionError):
                LessonBook(Path(tmp) / "b.json").update(clean_review(REVIEW), {})
            self.assertEqual(hashlib.sha256((Path(tmp) / "b.json").read_bytes()).hexdigest(), before)

    def test_lessons_reach_the_prompt_only_when_given(self):
        from cws.interface import CivilWarEpisode, PLAYER_ID
        ep = CivilWarEpisode("standard")
        obs = ep.reset(1)
        legal = ep.legal_actions(PLAYER_ID)
        self.assertNotIn("YOUR LESSONS", render(obs, legal, {}, None))
        text = render(obs, legal, {}, None, ["Recruit every turn."])
        self.assertTrue(text.startswith("YOUR LESSONS FROM EARLIER GAMES"))
        self.assertIn("1. Recruit every turn.", text)


class Review(unittest.TestCase):
    def test_review_shows_only_what_the_player_saw(self):
        player = LearningPlayer(FakeClient(end_turns()), ["Hold Washington."])
        seed = 777
        r = run_episode(player, "alternate", seed, Limits(), on_end=player.end)
        text = review_text(1, "alternate", r.reason, r.turns, player, 3, [])
        self.assertIn(r.reason, text)
        self.assertIn("FINAL POSITION", text)
        self.assertEqual(len(player.memory_turns), r.turns)              # the last turn's report is included
        self.assertNotIn(str(seed), text)
        for hidden in ("leader rating", "evaluate", "smarts", "dice", "seed"):          # own experience is on screen
            self.assertNotIn(hidden, text.lower())

    def test_the_last_turn_report_is_in_memory_and_the_trace(self):
        player = LearningPlayer(FakeClient(end_turns()), [])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "t.jsonl"
            run_episode(player, "alternate", 1, Limits(), trace_path=path, on_end=player.end)
            rows = [json.loads(l) for l in path.read_text().splitlines()]
        end = [r for r in rows if "game_end" in r]
        self.assertEqual(len(end), 1)
        self.assertTrue(any(e["kind"] == "game_over" for e in end[0]["report"]))
        self.assertTrue(any(e["kind"] == "game_over" for e in player.memory_turns[-1]["report"]))


class Behaviour(unittest.TestCase):
    def test_profile_counts_orders_and_attributes_battles(self):
        board = {"date": "d", "cash": 500, "vp": [0, 0], "owners": "UUR", "forts": "000",
                 "union": [[1, 1, 1000]], "rebel": [[21, 3, 2000]]}
        rows = [{"header": {"reason": "Rebel victory: cities controlled", "turns": 1, "date": "x"}},
                {"turn_start": 1, "board": board, "report": [], "leaders": ["Grant"]},
                {"turn": 1, "action": "recruit Cairo", "source": "model", "accepted": True, "text": ""},
                {"turn": 1, "action": "drill 1", "source": "model", "accepted": False, "text": ""},
                {"turn": 1, "action": "end turn", "source": "model", "accepted": True, "text": ""},
                {"game_end": 2, "board": dict(board, owners="URR", cash=300),
                 "report": [{"kind": "battle", "text": "Grant attacks Lee in Rome: Lee wins (attack 3 vs defend 9, odds 25%). x"},
                            {"kind": "battle", "text": "Lee attacks Grant in Cairo: Grant wins (attack 2 vs defend 8, odds 20%). x"}],
                 "leaders": ["Grant"]}]
        p = profile(rows)
        self.assertEqual((p["orders"]["recruit"], p["refused"], p["attacks"], p["attack_wins"], p["rebel_attacks"]),
                         (1, 1, 1, 0, 1))
        self.assertEqual((p["mean_attack_odds"], p["long_shot_attacks"], p["cities_lost"], p["last_turn_cash"]),
                         (25, 1, 1, 500))


class Training(unittest.TestCase):
    def test_training_seeds_are_disjoint_from_dev_and_eval(self):
        for scenario, split in SUITE.items():
            self.assertFalse(set(split["train"]) & (set(split["dev"]) | set(split["eval"])), scenario)
        self.assertEqual(schedule()[:2], [("standard", 201), ("alternate", 201)])

    def test_seed_blocks_are_checked_and_kept_per_notebook(self):
        from cws.learn import parse_seeds
        self.assertEqual(parse_seeds("301-303,310"), [301, 302, 303, 310])
        self.assertEqual(schedule(parse_seeds("301-350"))[-1], ("alternate", 350))
        self.assertEqual(len(schedule(parse_seeds("301-350"))), 100)
        with self.assertRaises(SystemExit):
            schedule([1, 2])                                             # evaluation seeds are refused
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            train(root / "b.json", "r", FakeClient(end_turns(200)), FakeClient([REVIEW]), root=root, games=1,
                  seeds=[301, 302], log=lambda *a: None)
            with self.assertRaises(SystemExit):                          # one notebook, one seed block
                train(root / "b.json", "r", FakeClient([]), FakeClient([]), root=root, games=2, seeds=[201],
                      log=lambda *a: None)

    def test_method_switches_change_only_what_the_review_is_shown(self):
        from cws.players.learner import REVIEW_SYSTEM, review_system
        self.assertEqual(review_system({}), REVIEW_SYSTEM)                 # gemini-a and gemini-b unchanged
        self.assertIn("When <something you can see on screen>", review_system({"actionable": True}))
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ref = root / "results" / "ref"
            ref.mkdir(parents=True)
            (ref / "results.jsonl").write_text("".join(
                json.dumps({"player": "passive", "scenario": sc, "seed": 301, "turns": 4}) + "\n"
                for sc in ("standard", "alternate")))
            reviews = FakeClient([REVIEW, REVIEW])
            method = {"mirror": True, "track_record": True, "actionable": True}
            rows = train(root / "c.json", "c", FakeClient(end_turns(200)), reviews, root=root, games=2,
                         seeds=[301], method=method, reference="ref", status_every=2, log=lambda *a: None)
            second = reviews.prompts[1]
            self.assertIn("WHAT YOU ACTUALLY DID", second)
            self.assertIn("[record: 1 games", second)                       # lessons written after game 1
            self.assertIn("no orders at all lasted 4 turns", second)
            self.assertIn("a player giving no orders lasted 4 turns", second)   # scoreboard line for game 1
            self.assertNotIn("301", second)                                 # the seed stays out of the review
            self.assertEqual([r["passive_turns"] for r in rows], [4, 4])
            self.assertIn("After game 2", (root / "results" / "c" / "status.md").read_text())
            with self.assertRaises(SystemExit):                             # one method per notebook
                train(root / "c.json", "c", FakeClient([]), FakeClient([]), root=root, games=3, seeds=[301, 302],
                      log=lambda *a: None)

    def test_teacher_shows_the_original_ai_on_the_same_game(self):
        from cws.players.baselines import OriginalAI
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ref = root / "results" / "ref"
            ref.mkdir(parents=True)
            (ref / "results.jsonl").write_text("".join(
                json.dumps({"player": "passive", "scenario": sc, "seed": 301, "turns": 4}) + "\n"
                for sc in ("standard", "alternate")))
            for sc in ("standard", "alternate"):
                run_episode(OriginalAI(301), sc, 301, trace_path=root / "traces" / "ref" / f"original-ai-{sc}-301.jsonl")
            reviews = FakeClient([REVIEW])
            train(root / "e.json", "e", FakeClient(end_turns(200)), reviews, root=root, games=1, seeds=[301],
                  method={"teacher": True}, reference="ref", status_every=0, log=lambda *a: None)
            text = reviews.prompts[0]
            self.assertIn("TEACHER'S GAME (the game's own computer as the Union, on this same game):", text)
            self.assertIn("Ordered ", text)
            self.assertNotIn("301", text)                                   # the seed stays out of the review
            with self.assertRaises(SystemExit):                             # no teacher traces, no teacher
                train(root / "e2.json", "e2", FakeClient([]), FakeClient([]), root=root, games=1, seeds=[302],
                      method={"teacher": True}, reference="ref", log=lambda *a: None)
            reviews = FakeClient([REVIEW])
            train(root / "f.json", "f", FakeClient(end_turns(200)), reviews, root=root, games=1, seeds=[301],
                  method={"contrast": True}, reference="ref", status_every=0, log=lambda *a: None)
            text = reviews.prompts[0]
            self.assertIn("CONTRAST (measured):", text)
            self.assertIn("(you | the computer's Union on the same game)", text)
            self.assertIn("Across your 1 games so far", text)
            self.assertNotIn("TEACHER'S GAME", text)

    def test_a_notebook_can_learn_with_plan_then_act(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rows = train(root / "g.json", "g", FakeClient(end_turns(400)), FakeClient([REVIEW]), root=root, games=1,
                         method={"plan": True}, log=lambda *a: None)
            header = json.loads((root / rows[0]["trace"]).read_text().splitlines()[0])["header"]
            self.assertTrue(header["config"]["player"]["plan"])
            self.assertEqual(LessonBook(root / "g.json").data["method"], {"plan": True})

    def test_training_stops_when_model_calls_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dead = FakeClient([ConnectionError("nodename nor servname provided")] * 400)
            with self.assertRaises(SystemExit):
                train(root / "x.json", "x", dead, FakeClient([REVIEW]), root=root, games=2, log=lambda *a: None)
            self.assertFalse((root / "results" / "x" / "curve.jsonl").exists()
                             and (root / "results" / "x" / "curve.jsonl").read_text().strip())   # nothing recorded
            self.assertEqual(LessonBook(root / "x.json").version, 0)

    def _select(self, round2_ref: int):
        """Two rounds of two games with a do-nothing player; round 1's reference is 0 turns, round 2's is set."""
        from cws.learn import train_select
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        (root / "results" / "ref").mkdir(parents=True)
        (root / "results" / "ref" / "results.jsonl").write_text("".join(
            json.dumps({"player": "passive", "scenario": sc, "seed": sd, "turns": 0 if sd == 301 else round2_ref}) + "\n"
            for sd in (301, 302) for sc in ("standard", "alternate")))
        review = dict(REVIEW, openings={"standard": "move 1 Manassas", "alternate": "move 2 Baltimore"})
        reviews = FakeClient([review])
        rows = train_select(root / "d.json", "d", FakeClient(end_turns(400)), reviews, root=root, round_size=2,
                            seeds=[301, 302], reference="ref", status_every=0, log=lambda *a: None,
                            method={"mirror": True, "track_record": True, "priority": True, "openings": True})
        return rows, LessonBook(root / "d.json"), reviews

    def test_a_challenger_that_does_clearly_worse_is_set_aside(self):
        rows, book, reviews = self._select(round2_ref=100)
        self.assertEqual([r["accepted"] for r in book.data["rounds"]], [True, False])
        self.assertEqual((book.lessons, book.data["openings"]), ([], {}))     # the kept notebook is champion v0
        self.assertIn("final notebook: champion v0", book.data["versions"][-1]["note"])
        self.assertEqual([r["book_version_used"] for r in rows], [0, 0, 1, 1])
        self.assertEqual(len(reviews.prompts), 1)                               # no review after the last round
        self.assertIn("VERDICT: your first notebook", reviews.prompts[0])
        self.assertIn("GAME 2, map: alternate", reviews.prompts[0])

    def test_a_challenger_that_holds_up_becomes_the_notebook_kept(self):
        rows, book, _ = self._select(round2_ref=0)
        self.assertEqual([r["accepted"] for r in book.data["rounds"]], [True, True])
        self.assertEqual(book.lessons, REVIEW["lessons"])
        self.assertEqual(book.data["openings"]["standard"], "move 1 Manassas")

    def test_opening_plan_shows_on_turn_one_and_priority_is_stated(self):
        from cws.interface import CivilWarEpisode, PLAYER_ID
        ep = CivilWarEpisode("standard")
        obs = ep.reset(1)
        legal = ep.legal_actions(PLAYER_ID)
        text = render(obs, legal, {}, None, ["Guard Washington."], priority=True, opening="move 1 Manassas")
        self.assertIn("in priority order: when two conflict, follow the earlier one", text)
        self.assertIn("YOUR OPENING PLAN FOR THIS MAP", text)
        ep.step(PLAYER_ID, "end turn")
        later = render(ep.observe(PLAYER_ID), ep.legal_actions(PLAYER_ID), {}, None, ["x"], opening="move 1 Manassas")
        self.assertNotIn("OPENING PLAN", later)

    def test_scoreboard_summarises_old_games_and_lists_recent_ones(self):
        from cws.learn import SCOREBOARD_RECENT, scoreboard
        beh = {"orders": {"recruit": 2, "drill": 1}, "attacks": 1, "attack_wins": 0, "cities_end": 5, "cities_peak": 9}
        rows = [{"game": i, "scenario": ("standard", "alternate")[i % 2], "book_version_used": i - 1,
                 "tier": "decisive loss", "turns": 5, "behaviour": beh} for i in range(1, 51)]
        lines = scoreboard(rows)
        self.assertEqual(len(lines), 2 + SCOREBOARD_RECENT)
        self.assertTrue(lines[0].startswith("games 1-30 on standard (15 games)"))
        self.assertTrue(lines[-1].startswith("game 50 "))

    def test_train_learns_after_each_game_and_records_behaviour(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            play = FakeClient(end_turns(200))
            reviews = FakeClient([REVIEW, "not json"])
            rows = train(root / "lessons" / "t.json", "learn-test", play, reviews, root=root, games=2,
                         log=lambda *a: None)
            self.assertEqual([r["book_version_used"] for r in rows], [0, 1])
            self.assertEqual([r["review_ok"] for r in rows], [True, False])   # a bad review changes nothing
            book = LessonBook(root / "lessons" / "t.json")
            self.assertEqual((book.version, book.lessons), (1, REVIEW["lessons"]))
            self.assertIn("YOUR LESSONS FROM EARLIER GAMES", play.prompts[-1])   # game 2 played with v1
            self.assertNotIn("YOUR LESSONS", play.prompts[0])
            self.assertTrue(all("behaviour" in r and (root / r["trace"]).exists() for r in rows))
            again = train(root / "lessons" / "t.json", "learn-test", play, reviews, root=root, games=2,
                          log=lambda *a: None)
            self.assertEqual(len(again), 2)                                  # resumes; nothing replayed
            self.assertIn("Version 1, after game 1", journal(book, rows))


class Prices(unittest.TestCase):
    def test_longest_model_prefix_wins(self):
        self.assertEqual(price_for("gemini-3.5-flash-lite")["output_per_m"], 2.50)   # not flash's 9.00
        self.assertEqual(price_for("gemini-3.5-flash")["output_per_m"], 9.00)
        self.assertEqual(price_for("gemini-3.7-flash")["output_per_m"], 3.75)
        self.assertIsNone(price_for("gemini-3.1-pro-preview"))
        self.assertAlmostEqual(_price(1_000_000, 1_000_000, "gemini-3.7-flash"), 4.50)
        self.assertEqual(_price(1_000_000, 1_000_000, "unpriced-model"), 0.0)


if __name__ == "__main__":
    unittest.main()
