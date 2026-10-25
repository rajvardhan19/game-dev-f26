"""The five operations: legal and illegal actions, the information boundary, invariants."""

import copy
import json
import random
import unittest

from cws.engine import UNION, REBEL, starfin
from cws.interface import PLAYER_ID, CivilWarEpisode
from cws.players.baselines import OriginalAI, RandomPlayer

ROLLS = ("troops", "end turn")      # the only actions that roll dice before an outcome is shown


def state_snapshot(ep: CivilWarEpisode) -> str:
    g = ep._game
    keys = ("armysize", "armyloc", "armymove", "armylead", "armyexper", "supply", "cityp", "fort",
            "cash", "control", "income", "victory", "capcity", "rflag", "month", "year")
    return json.dumps({k: getattr(g, k) for k in keys}) + str(g.dice.state)


class LegalAndIllegal(unittest.TestCase):
    def setUp(self):
        self.ep = CivilWarEpisode("standard")
        self.obs = self.ep.reset(7)

    def test_opening_actions(self):
        legal = self.ep.legal_actions(PLAYER_ID)
        self.assertIn("troops", legal)
        self.assertIn("move 1 Manassas", legal)
        self.assertIn("fortify Washington", legal)
        self.assertEqual(legal[-1], "end turn")
        self.assertFalse(any(a.startswith("recruit ") for a in legal), "recruit cities exist only after troops")

    def test_illegal_action_is_refused_counted_and_changes_nothing(self):
        before = state_snapshot(self.ep)
        for bad in ("move 1 Richmond", "recruit Washington", "fortify Richmond", "drill 21",
                    "attack", "", "MOVE 99 Atlanta"):
            res = self.ep.step(PLAYER_ID, bad)
            self.assertFalse(res["accepted"], bad)
        self.assertEqual(state_snapshot(self.ep), before)
        self.assertEqual(self.ep.invalid_actions, 7)
        self.assertEqual(self.ep.steps, 7)

    def test_malformed_reply_is_an_invalid_action_not_a_crash(self):
        res = self.ep.step(PLAYER_ID, {"move": 1})
        self.assertFalse(res["accepted"])
        self.assertEqual(self.ep.invalid_actions, 1)

    def test_case_and_spacing_are_normalised(self):
        res = self.ep.step(PLAYER_ID, "  MOVE 1   manassas ")
        self.assertTrue(res["accepted"])
        self.assertEqual(self.ep._game.armymove[1], 22)

    def test_every_listed_action_is_accepted_and_changes_state(self):
        rng = random.Random(3)
        for _ in range(60):
            if self.ep.outcome()["status"] == "terminal":
                break
            legal = self.ep.legal_actions(PLAYER_ID)
            action = rng.choice(legal)
            before = state_snapshot(self.ep)
            res = self.ep.step(PLAYER_ID, action)
            self.assertTrue(res["accepted"], action)
            if action not in ROLLS or action == "end turn":
                self.assertNotEqual(state_snapshot(self.ep), before, action)

    def test_resting_army_cannot_move(self):
        self.ep.step(PLAYER_ID, "fortify Washington")
        self.assertFalse(any(a.startswith("move 1 ") for a in self.ep.legal_actions(PLAYER_ID)))
        self.assertFalse(self.ep.step(PLAYER_ID, "move 1 Manassas")["accepted"])

    def test_wrong_player_is_rejected(self):
        with self.assertRaises(ValueError):
            self.ep.observe("rebel")

    def test_terminal_episode_refuses_everything(self):
        ep = CivilWarEpisode("standard")
        ep.reset(1)
        while ep.outcome()["status"] == "ongoing":
            ep.step(PLAYER_ID, "end turn")
        out = ep.outcome()
        self.assertEqual(out["status"], "terminal")
        self.assertTrue(out["reason"].startswith(("Rebel victory", "Union victory")))
        self.assertEqual(ep.legal_actions(PLAYER_ID), [])
        steps = ep.steps
        self.assertFalse(ep.step(PLAYER_ID, "end turn")["accepted"])
        self.assertEqual(ep.steps, steps)


class InformationBoundary(unittest.TestCase):
    HIDDEN_ENEMY_KEYS = {"leader", "experience", "supply", "order"}

    def test_enemy_armies_show_only_what_the_army_report_prints(self):
        obs = CivilWarEpisode("standard").reset(5)
        for army in obs["enemy_armies"]:
            self.assertEqual(set(army), {"id", "name", "men", "city", "city_name", "out_of_supply"})
            self.assertFalse(self.HIDDEN_ENEMY_KEYS & set(army))
        for army in obs["your_armies"]:
            self.assertTrue(self.HIDDEN_ENEMY_KEYS <= set(army))

    def test_no_dice_seed_or_engine_internals_in_the_observation(self):
        ep = CivilWarEpisode("standard")
        obs = ep.reset(123.25)
        text = json.dumps(obs)
        for secret in ("123.25", str(ep._game.dice.state)):
            self.assertNotIn(secret, text)

        def keys(node):
            if isinstance(node, dict):
                for k, v in node.items():
                    yield k
                    yield from keys(v)
            elif isinstance(node, list):
                for v in node:
                    yield from keys(v)
        internal = {"seed", "dice", "rnd", "aggress", "brray", "rating", "lname", "rcity", "armymove"}
        self.assertFalse(internal & set(keys(obs)))

    def test_two_seeds_give_identical_observations_before_any_roll(self):
        # Week 3 discernment test: same state, two seeds. If anything differs
        # before a die is rolled, the seed has leaked and the build is rejected.
        script = ["move 1 Manassas", "drill 2", "fortify Columbus", "move 4 Jeff. City", "cancel 1"]
        for a, b in ((1, 2), (17, 99.5), (3, 4)):
            ea, eb = CivilWarEpisode("standard"), CivilWarEpisode("standard")
            self.assertEqual(ea.reset(a), eb.reset(b))
            self.assertEqual(ea.legal_actions(PLAYER_ID), eb.legal_actions(PLAYER_ID))
            for action in script:
                ra, rb = ea.step(PLAYER_ID, action), eb.step(PLAYER_ID, action)
                self.assertTrue(ra["accepted"], action)
                self.assertEqual(ra, rb, action)
                self.assertEqual(ea.legal_actions(PLAYER_ID), eb.legal_actions(PLAYER_ID))

    def test_no_die_is_rolled_before_a_roll(self):
        # Stronger than comparing observations: a die rolled and not shown would still move the counter.
        ep = CivilWarEpisode("standard")
        ep.reset(5)
        dice = ep._game.dice
        before = dice.calls
        for action in ["move 1 Manassas", "drill 2", "fortify Columbus", "move 4 Jeff. City", "cancel 1"]:
            ep.legal_actions(PLAYER_ID)
            ep.observe(PLAYER_ID)
            self.assertTrue(ep.step(PLAYER_ID, action)["accepted"], action)
        ep.legal_actions(PLAYER_ID)
        self.assertEqual(dice.calls, before)
        ep.step(PLAYER_ID, "troops")
        self.assertGreater(dice.calls, before)

    def test_the_seed_does_matter_after_a_roll(self):
        results = {json.dumps(CivilWarEpisode("standard").reset(s)) for s in (1, 2)}
        self.assertEqual(len(results), 1)
        after = set()
        for s in (1, 2, 3):
            ep = CivilWarEpisode("standard")
            ep.reset(s)
            after.add(json.dumps(ep.step(PLAYER_ID, "end turn")["observation"]))
        self.assertGreater(len(after), 1)

    def test_legal_actions_name_only_visible_things(self):
        ep = CivilWarEpisode("standard")
        obs = ep.reset(9)
        names = {c["name"] for c in obs["cities"]}
        own = {a["id"] for a in obs["your_armies"]}
        for action in ep.legal_actions(PLAYER_ID):
            verb, _, rest = action.partition(" ")
            if verb in ("move", "cancel", "supply", "drill"):
                self.assertIn(int(rest.split()[0]), own)
            if verb in ("move",):
                self.assertIn(rest.split(" ", 1)[1], names)

    def test_observation_is_a_copy(self):
        ep = CivilWarEpisode("standard")
        obs = ep.reset(2)
        obs["your_armies"][0]["men"] = 999999
        obs["cities"][0]["owner"] = "Union"
        self.assertNotEqual(ep.observe(PLAYER_ID)["your_armies"][0]["men"], 999999)
        self.assertEqual(ep._game.cityp[1], REBEL)


class Invariants(unittest.TestCase):
    """Rule invariants checked after every step of whole episodes."""

    def check(self, g):
        for who in (UNION, REBEL):
            self.assertGreaterEqual(g.cash[who], 0)
            self.assertLessEqual(g.cash[who], 19999 + 2000)
            for i in starfin(who):
                if g.armyloc[i] > 0:
                    self.assertGreaterEqual(g.armysize[i], 1)
                    self.assertTrue(1 <= g.armyloc[i] <= 40)
                    self.assertGreaterEqual(g.supply[i], 0)
                    self.assertLessEqual(g.armyexper[i], 10)
        for c in range(1, 41):
            self.assertIn(g.fort[c], (0, 1, 2))
            self.assertIn(g.cityp[c], (0, 1, 2))
        self.assertLessEqual(g.control[1] + g.control[2], 40)
        self.assertGreaterEqual(g.victory[1], 0)
        self.assertTrue(1 <= g.month <= 12)

    def test_invariants_hold_through_whole_games(self):
        for scenario in ("standard", "alternate", "reckless"):
            for seed in (1, 2):
                for player in (RandomPlayer(seed), OriginalAI(seed)):
                    ep = CivilWarEpisode(scenario)
                    obs = ep.reset(seed)
                    while ep.outcome()["status"] == "ongoing":
                        when = (ep._game.month, ep._game.year)
                        res = ep.step(PLAYER_ID, player.act(obs, ep.legal_actions(PLAYER_ID)))
                        obs = res["observation"]
                        self.check(ep._game)
                        g = ep._game
                        if res["text"].startswith("Turn resolved"):
                            # Each turn is two months; December wraps to January (iterate, line 1411).
                            m, y = when[0] + 2, when[1]
                            if m > 12:
                                m, y = 1, y + 1
                            self.assertEqual((g.month, g.year), (m, y))
                            for who in (UNION, REBEL):          # after a turn, armies stand in their own cities
                                for i in starfin(who):
                                    if g.armyloc[i] > 0:
                                        self.assertEqual(g.cityp[g.armyloc[i]], who, (scenario, seed, i))


if __name__ == "__main__":
    unittest.main()
