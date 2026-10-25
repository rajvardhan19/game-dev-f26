"""Regressions that were observed while building, each with the date it was found.

See docs/rule-source-map.md, "Regressions found", for the full account.
"""

import unittest
from pathlib import Path

from cws.data import DATA_DIR, tokens
from cws.engine import Game, REBEL, UNION
from cws.interface import CivilWarEpisode, PLAYER_ID
from cws.players.baselines import OriginalAI
from cws import smarts
from cws.qb import cint, f32


class LeadingBlankInQuotedField(unittest.TestCase):
    """2026-10-23: CITIES.GRD writes `30,520,45, "Phildelpha"`. Keeping the blank
    before the quote made every city " Phildelpha", so "recruit  Pittsburg" never
    matched its own legal action after whitespace normalisation and the original
    AI baseline lost every recruit."""

    def test_input_hash_skips_blanks_before_a_quote(self):
        self.assertIn("Phildelpha", tokens(DATA_DIR / "CITIES.GRD"))
        self.assertNotIn(" Phildelpha", tokens(DATA_DIR / "CITIES.GRD"))

    def test_recruit_round_trips_through_step(self):
        ep = CivilWarEpisode("standard")
        ep.reset(1)
        ep.step(PLAYER_ID, "troops")
        for action in ep.legal_actions(PLAYER_ID):
            if action.startswith("recruit "):
                self.assertTrue(ep.step(PLAYER_ID, action)["accepted"], action)
                break
        else:
            self.skipTest("this roll offered no city")

    def test_baseline_makes_no_invalid_moves(self):
        ep = CivilWarEpisode("standard")
        obs = ep.reset(1)
        ai = OriginalAI(1)
        while ep.outcome()["status"] == "ongoing" and ep.steps < 300:
            obs = ep.step(PLAYER_ID, ai.act(obs, ep.legal_actions(PLAYER_ID)))["observation"]
        self.assertEqual(ep.invalid_actions, 0)


class StackingPenaltyUsesOwnSide(unittest.TestCase):
    """2026-10-23, found by the QB64 differential run (seed 1, command 38):
    evaluate line 3019 reads `IF cityp(a) = 3 - side ...`: the computer avoids
    marching onto its own resting army. It was ported as the enemy's side."""

    def score_toward_richmond(self, g) -> int:
        seen, rolls = [], iter([0.5] * 200)
        smarts.PROBE = seen
        try:
            smarts.evaluate(g, 25, REBEL, UNION, lambda: next(rolls), 0.0, 3)
        finally:
            smarts.PROBE = None
        j = next(l.split()[2] for l in seen if l.startswith("EC 25 ") and l.split()[3] == "33")
        return int(next(l for l in seen if l.startswith(f"EV 25 {j} ")).split()[3])

    def test_penalty_applies_to_a_resting_friend(self):
        g = Game()
        # A Rebel army in Norfolk looks at Richmond, where Johnston (army 21, 30,000 men) rests.
        g.armyloc[25], g.armysize[25], g.armylead[25], g.supply[25] = 28, 100, 5, 5
        g.occupy(28)
        resting = self.score_toward_richmond(g)
        g.armymove[21] = 11                      # the same friend, now under orders
        moving = self.score_toward_richmond(g)
        self.assertEqual(moving - resting, g.armysize[21])


class DoublePrecisionThenSingle(unittest.TestCase):
    """2026-10-23, found by the QB64 differential run (seed 2, command 200):
    QB64 computes .8 * v + .3 * (income + control) in double and rounds once to
    SINGLE; rounding each product first gave 697 where the original gives 696."""

    def test_victory_points_round_once(self):
        g = Game()
        g.victory[1], g.income[1], g.control[1] = 742, 325, 18
        g.victory[2], g.income[2], g.control[2] = 100, 100, 10
        g._victory_points()
        self.assertEqual(g.victory[1], 696)
        self.assertEqual(cint(f32(.8 * 742 + .3 * 343)), 696)


if __name__ == "__main__":
    unittest.main()
