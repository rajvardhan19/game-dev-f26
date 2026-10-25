"""Whole episodes: a successful path, terminal outcomes, and baseline separation."""

import unittest

from cws.interface import CivilWarEpisode, PLAYER_ID
from cws.players.baselines import OriginalAI, PassivePlayer, RandomPlayer
from cws.players.view import HiddenInformation, View


def play(scenario, seed, player):
    ep = CivilWarEpisode(scenario)
    obs = ep.reset(seed)
    while ep.outcome()["status"] == "ongoing":
        obs = ep.step(PLAYER_ID, player.act(obs, ep.legal_actions(PLAYER_ID)))["observation"]
    return ep.outcome()


class SuccessfulPaths(unittest.TestCase):
    def test_union_wins_on_income_alternate_seed_9(self):
        out = play("alternate", 9, OriginalAI(9))
        self.assertEqual((out["winner"], out["reason"]), ("Union", "Union victory: share of total income"))
        self.assertEqual((out["turn"], out["steps"], out["invalid_actions"]), (4, 37, 0))

    def test_union_takes_richmond_standard_seed_8(self):
        out = play("standard", 8, OriginalAI(8))
        self.assertEqual(out["reason"], "Union victory: capital captured")
        self.assertEqual(out["turn"], 9)

    def test_deadline_ends_a_long_game(self):
        out = play("standard", 1, OriginalAI(1))
        self.assertEqual(out["reason"], "Rebel victory: time expired")
        self.assertEqual(out["date"], "March 1865")


class Separation(unittest.TestCase):
    """The original AI is a real competitor: it beats the floors on the same seeds."""

    def test_original_ai_outranks_random_and_passive(self):
        from cws.evaluate import rank
        for scenario in ("standard", "alternate"):
            for seed in (1, 2, 3):
                ai, rnd, idle = (play(scenario, seed, P(seed)) for P in (OriginalAI, RandomPlayer, PassivePlayer))
                self.assertGreater(rank(ai), rank(rnd), (scenario, seed))
                self.assertGreater(rank(ai), rank(idle), (scenario, seed))

    def test_victory_point_share_is_not_the_score(self):
        # Why the outcome tier is primary: a player conquered in 1862 can end
        # with a higher VP share than one that held out until 1865.
        from cws.evaluate import rank
        ai, idle = play("standard", 3, OriginalAI(3)), play("standard", 3, PassivePlayer(3))
        self.assertLess(ai["score"], idle["score"])
        self.assertGreater(rank(ai), rank(idle))


class BaselineBoundary(unittest.TestCase):
    def test_view_refuses_hidden_enemy_fields(self):
        obs = CivilWarEpisode("standard").reset(1)
        v = View(obs)
        self.assertEqual(v.armysize[21], 300)                # visible: the enemy's size
        for field in (v.armylead, v.armyexper, v.supply):
            with self.assertRaises(HiddenInformation):
                field[21]
        self.assertEqual(v.armylead[1], 4)                   # own leader is known

    def test_baseline_is_reproducible_per_seed(self):
        self.assertEqual(play("standard", 4, OriginalAI(4)), play("standard", 4, OriginalAI(4)))


if __name__ == "__main__":
    unittest.main()
