"""The runner's limits, terminal reasons and labels, with no model traffic."""

import json
import tempfile
import unittest
from pathlib import Path

from cws.client import EngineProcess, PlayerPort
from cws.players.baselines import OriginalAI, PassivePlayer
from cws.players.model_player import FakeClient, ModelPlayer
from cws.runner import Decision, Limits, run_episode


class Stubborn:
    """Proposes an illegal action forever."""
    name = "stubborn"

    def act(self, obs, legal):
        return "move 1 Richmond"


class Busy:
    """Never ends its turn: moves and cancels the same army."""
    name = "busy"

    def act(self, obs, legal):
        for a in legal:
            if a.startswith("cancel "):
                return a
        return next(a for a in legal if a.startswith("move "))


class Slow:
    name = "slow"
    uses_model = True

    def decide(self, obs, legal, memory):
        import time
        time.sleep(0.2)
        return Decision(["end turn"], "model", True, latency=0.2)


class Limits_(unittest.TestCase):
    def test_step_limit_ends_the_episode(self):
        r = run_episode(Busy(), "standard", 1, Limits(max_steps=12, max_actions_per_turn=1000))
        self.assertEqual(r.reason, "step limit")
        self.assertEqual(r.steps, 12)

    def test_turn_action_limit_ends_the_turn_and_is_labelled_fallback(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "t.jsonl"
            r = run_episode(Busy(), "standard", 1, Limits(max_actions_per_turn=5, max_steps=60), trace_path=path)
            entries = [json.loads(l) for l in path.read_text().splitlines()[1:]]
        fallbacks = [e for e in entries if e.get("source") == "fallback"]
        self.assertTrue(fallbacks)
        self.assertTrue(all(e["action"] == "end turn" and e["why"] == "turn action limit" for e in fallbacks))
        self.assertEqual(r.fallback_actions, len(fallbacks))
        self.assertFalse(any(e.get("source") == "scripted" and e["action"] == "end turn" for e in entries))

    def test_repeated_invalid_actions_fall_back_and_are_counted(self):
        r = run_episode(Stubborn(), "standard", 1, Limits(max_steps=40))
        self.assertGreater(r.invalid_actions, 0)
        self.assertGreater(r.fallback_actions, 0)
        self.assertEqual(r.invalid_actions + r.fallback_actions, r.steps)

    def test_model_call_limit(self):
        client = FakeClient([{"actions": ["end turn"], "note": ""}] * 50)
        r = run_episode(ModelPlayer(client, "obs-only"), "standard", 1, Limits(max_model_calls=3))
        self.assertEqual(r.reason, "model-call limit")
        self.assertEqual(r.model_calls, 3)

    def test_failed_calls_count_toward_the_budget(self):
        client = FakeClient([TimeoutError("deadline")] * 10)
        r = run_episode(ModelPlayer(client, "obs-only"), "standard", 1, Limits(max_model_calls=4))
        self.assertEqual((r.model_calls, r.failed_calls), (4, 4))
        self.assertEqual(r.reason, "model-call limit")

    def test_wall_clock_timeout_mid_game(self):
        # Slow ends a turn every 0.2 s (the war lasts about 8 turns); the clock must stop
        # it partway, not before the first decision.
        r = run_episode(Slow(), "standard", 1, Limits(max_wall_seconds=0.7))
        self.assertEqual(r.reason, "timeout: episode wall clock")
        self.assertGreaterEqual(r.steps, 2)
        self.assertLess(r.wall_seconds, 1.5)

    def test_watchdog_turns_a_hung_call_into_a_failed_call(self):
        class Hung:
            name, uses_model = "hung", True

            def decide(self, obs, legal, memory):
                import time
                time.sleep(5)
        r = run_episode(Hung(), "standard", 1, Limits(decision_timeout=0.1, max_model_calls=2))
        self.assertEqual((r.model_calls, r.failed_calls, r.reason), (2, 2, "model-call limit"))

    def test_a_crashing_baseline_ends_with_a_reason(self):
        class Broken:
            name = "broken"

            def act(self, obs, legal):
                raise KeyError("bug")
        r = run_episode(Broken(), "standard", 1)
        self.assertTrue(r.reason.startswith("player error: KeyError"), r.reason)

    def test_batch_stops_when_the_turn_resolves_whatever_the_spelling(self):
        # Review finding (blocking): "End turn" resolved the turn and the rest of the
        # batch ran blind in the next turn.
        client = FakeClient([{"actions": ["End turn", "move 1 Manassas", "end turn"], "note": ""},
                             {"actions": ["  TROOPS ", "recruit Pittsburg", "end turn"], "note": ""}])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "t.jsonl"
            run_episode(ModelPlayer(client, "obs-only"), "standard", 101, Limits(max_model_calls=2), trace_path=path)
            steps = [json.loads(l) for l in path.read_text().splitlines()[1:] if '"action"' in l]
        self.assertEqual([s["action"] for s in steps], ["End turn", "  TROOPS "])

    def test_terminal_reason_comes_from_the_game(self):
        r = run_episode(PassivePlayer(), "standard", 1)
        self.assertTrue(r.reason.startswith("Rebel victory: "))
        self.assertEqual(r.status, "terminal")


class ProcessBoundary(unittest.TestCase):
    def test_player_port_has_only_the_three_player_operations(self):
        with EngineProcess() as engine:
            engine.reset("standard", 1, 100)
            port = engine.port()
            self.assertIsInstance(port, PlayerPort)
            public = {n for n in dir(port) if not n.startswith("_")}
            self.assertEqual(public, {"observe", "legal_actions", "step", "player_id"})
            self.assertFalse(hasattr(port, "__dict__"))
            self.assertIn("end turn", port.legal_actions())
            for op in ("reset", "outcome", "trace"):         # the channel itself refuses runner operations
                with self.assertRaises(PermissionError):
                    port._call(op)

    def test_game_state_lives_in_another_process(self):
        with EngineProcess() as engine:
            engine.reset("standard", 1, 100)
            self.assertFalse(any(type(v).__name__ in ("Game", "CivilWarEpisode") for v in vars(engine).values()))
            self.assertIsNotNone(engine._proc.pid)

    def test_engine_gets_no_credentials(self):
        from cws.client import engine_environment
        env = engine_environment({"ANTHROPIC_API_KEY": "x", "GH_TOKEN": "x", "GOOGLE_APPLICATION_CREDENTIALS": "/k.json",
                                  "OPENAI_API_KEY": "x", "PATH": "/bin", "COURSE_MODEL": "m"})
        self.assertEqual(set(env), {"PATH", "COURSE_MODEL", "PYTHONPATH"})


class Labels(unittest.TestCase):
    def test_scripted_and_model_actions_are_labelled(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "t.jsonl"
            run_episode(OriginalAI(1), "alternate", 1, trace_path=path)
            sources = {json.loads(l).get("source") for l in path.read_text().splitlines()[1:]}
        self.assertEqual(sources - {None}, {"scripted"})


if __name__ == "__main__":
    unittest.main()
