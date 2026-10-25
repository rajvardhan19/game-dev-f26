"""The model player with a scripted client: no network, no credentials.

These test the application around the model (prompt contents, parsing,
failure handling, labels). They are not evidence about any live model.
"""

import json
import tempfile
import unittest
from pathlib import Path

from cws.interface import CivilWarEpisode, PLAYER_ID
from cws.players.model_player import SYSTEM, FakeClient, ModelPlayer, render
from cws.runner import Limits, run_episode


def episode_obs(seed=1):
    ep = CivilWarEpisode("standard")
    return ep, ep.reset(seed)


class Prompt(unittest.TestCase):
    def test_prompt_lists_legal_actions_and_no_hidden_fields(self):
        ep, obs = episode_obs()
        legal = ep.legal_actions(PLAYER_ID)
        text = render(obs, legal, {"feedback": []}, None)
        self.assertTrue(text.endswith("\n".join(legal)))
        g = ep._game
        for i in range(21, 41):
            if g.armyloc[i]:
                line = next(l for l in text.splitlines() if l.startswith(f"{i} {g.armyname[i]} |"))
                self.assertEqual(line.count("|"), 3, "enemy line carries men, city and supply flag only")
        self.assertNotIn(str(g.dice.state), text)
        self.assertNotIn("evaluate", SYSTEM.lower())

    def test_history_appears_only_in_history_mode(self):
        replies = [{"actions": ["end turn"], "note": "hold the line"}] * 2
        for memory, expect in (("history", True), ("obs-only", False)):
            client = FakeClient(list(replies))
            run_episode(ModelPlayer(client, memory), "standard", 1, Limits(max_model_calls=2))
            self.assertEqual("YOUR MEMORY OF EARLIER TURNS" in client.prompts[1], expect, memory)
            self.assertEqual("hold the line" in client.prompts[1], expect, memory)


class Replies(unittest.TestCase):
    def test_batch_is_submitted_in_order_and_stops_at_first_illegal(self):
        client = FakeClient([
            {"actions": ["move 1 Manassas", "move 1 Baltimore", "end turn"], "note": "x"},
            {"actions": ["end turn"], "note": "y"},
        ])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "t.jsonl"
            r = run_episode(ModelPlayer(client, "obs-only"), "standard", 1, Limits(max_model_calls=2), trace_path=path)
            steps = [json.loads(l) for l in path.read_text().splitlines()[1:] if "action" in json.loads(l)]
        self.assertEqual([(s["action"], s["accepted"]) for s in steps[:3]],
                         [("move 1 Manassas", True), ("move 1 Baltimore", False), ("end turn", True)])
        self.assertTrue(all(s["source"] == "model" for s in steps))
        self.assertEqual(r.invalid_actions, 1)

    def test_bad_json_is_a_failed_call_and_never_a_move(self):
        client = FakeClient(["not json", {"actions": "end turn", "note": ""}, {"note": "no actions"}] + [
            {"actions": ["end turn"], "note": ""}] * 3)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "t.jsonl"
            r = run_episode(ModelPlayer(client, "obs-only"), "standard", 1, Limits(max_model_calls=4), trace_path=path)
            entries = [json.loads(l) for l in path.read_text().splitlines()[1:]]
        calls = [e for e in entries if "call" in e]
        self.assertEqual([c["ok"] for c in calls[:3]], [False, False, False])
        self.assertEqual(r.failed_calls, 3)
        fallback = [e for e in entries if e.get("source") == "fallback"]
        self.assertEqual([f["why"] for f in fallback], ["repeated failures"])

    def test_feedback_after_rejection_reaches_the_next_prompt(self):
        client = FakeClient([{"actions": ["move 1 Atlanta"], "note": ""}, {"actions": ["end turn"], "note": ""}])
        run_episode(ModelPlayer(client, "obs-only"), "standard", 1, Limits(max_model_calls=2))
        self.assertIn("'move 1 Atlanta' was rejected", client.prompts[1])

    def test_tokens_and_latency_are_recorded(self):
        client = FakeClient([{"actions": ["end turn"], "note": ""}] * 3)
        r = run_episode(ModelPlayer(client, "obs-only"), "standard", 1, Limits(max_model_calls=3))
        self.assertGreater(r.input_tokens, 0)
        self.assertGreater(r.output_tokens, 0)
        self.assertEqual(r.config["player"]["provider"], "fake")


class NoTools(unittest.TestCase):
    def test_vertex_request_has_no_tools_and_one_attempt(self):
        """Read the adapter's request without sending it."""
        import inspect
        from cws.players import model_player
        src = inspect.getsource(model_player.VertexClient)
        self.assertIn("AutomaticFunctionCallingConfig(disable=True)", src)
        self.assertIn("HttpRetryOptions(attempts=1)", src)
        self.assertNotIn("tools=", src)


class VertexAdapterWithFakeSDK(unittest.TestCase):
    """VertexClient against a stand-in google.genai module: the request it builds and how it parses."""

    def setUp(self):
        import sys
        import types as pytypes
        self.sent = {}
        test = self

        class Obj:
            def __init__(self, **kw):
                self.__dict__.update(kw)

        class FinishReason:
            STOP = "STOP"
            MAX_TOKENS = "MAX_TOKENS"

        class Models:
            def generate_content(self, model, contents, config):
                test.sent.update(model=model, contents=contents, config=config)
                return Obj(text=test.reply_text, model_version="gemini-test-001",
                           candidates=[Obj(finish_reason=test.finish)],
                           usage_metadata=Obj(prompt_token_count=1200, candidates_token_count=40,
                                              thoughts_token_count=60))

        class Client:
            def __init__(self, **kw):
                test.sent["client"] = kw
                self.models = Models()

        gtypes = pytypes.SimpleNamespace(HttpOptions=Obj, HttpRetryOptions=Obj, GenerateContentConfig=Obj,
                                         AutomaticFunctionCallingConfig=Obj, FinishReason=FinishReason)
        genai = pytypes.ModuleType("google.genai")
        genai.Client, genai.types = Client, gtypes
        google = pytypes.ModuleType("google")
        google.genai = genai
        self.saved = {k: sys.modules.get(k) for k in ("google", "google.genai")}
        sys.modules["google"], sys.modules["google.genai"] = google, genai
        import os
        self.env = {k: os.environ.get(k) for k in ("GOOGLE_CLOUD_PROJECT", "GOOGLE_CLOUD_LOCATION", "COURSE_MODEL")}
        os.environ.update(GOOGLE_CLOUD_PROJECT="p", GOOGLE_CLOUD_LOCATION="us-central1", COURSE_MODEL="gemini-test")
        self.reply_text, self.finish = json.dumps({"actions": ["end turn"], "note": "n"}), "STOP"

    def tearDown(self):
        import os
        import sys
        for k, v in self.saved.items():
            if v is None:
                sys.modules.pop(k, None)
            else:
                sys.modules[k] = v
        for k, v in self.env.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v

    def test_request_shape_and_parsing(self):
        from cws.players.model_player import SCHEMA, VertexClient
        client = VertexClient(timeout=30)
        reply = client.generate("system", "prompt", SCHEMA)
        cfg = self.sent["config"]
        self.assertEqual(self.sent["model"], "gemini-test")
        self.assertFalse(hasattr(cfg, "tools"))
        self.assertTrue(cfg.automatic_function_calling.disable)
        self.assertEqual(self.sent["client"]["http_options"].retry_options.attempts, 1)
        self.assertEqual(self.sent["client"]["http_options"].timeout, 30000)
        self.assertEqual((reply["input_tokens"], reply["output_tokens"], reply["complete"]), (1200, 100, True))
        self.assertEqual(client.model_version, "gemini-test-001")

    def test_truncated_reply_is_a_failed_call(self):
        from cws.players.model_player import ModelPlayer, VertexClient
        self.finish = "MAX_TOKENS"
        ep, obs = episode_obs()
        d = ModelPlayer(VertexClient()).decide(obs, ep.legal_actions(PLAYER_ID), {"turns": [], "feedback": []})
        self.assertFalse(d.ok)
        self.assertEqual(d.actions, [])
        self.assertIn("incomplete", d.error)


if __name__ == "__main__":
    unittest.main()
