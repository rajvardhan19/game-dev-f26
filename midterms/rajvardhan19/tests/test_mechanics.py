"""Each mechanic against a result traced by hand from CWSTRAT.BAS.

The dice are scripted (cws.qb.ScriptedDice), so each test also states how
many rolls the source consumes; a port that rolls once too often fails.
"""

import unittest

from cws.engine import Game, REBEL, UNION
from cws.qb import ScriptedDice


def fresh(**changes) -> Game:
    g = Game()
    for name, value in changes.items():
        setattr(g, name, value)
    return g


class Battle(unittest.TestCase):
    """SUB battle, lines 845-1036, traced for one upset."""

    def setUp(self):
        g = Game()
        for i in range(1, 41):
            g.armyloc[i] = 0
        # attacker: slot 3, 10,000 men, leader 4, experience 1, supply 5
        g.armyloc[3], g.armysize[3], g.armylead[3], g.armyexper[3], g.supply[3] = 12, 100, 4, 1, 5
        # defender: slot 21, 30,000 men, leader 8, experience 1, supply 7, not moving, no fort
        g.armyloc[21], g.armysize[21], g.armylead[21], g.armyexper[21], g.supply[21] = 22, 300, 8, 1, 7
        g.armymove[21] = 0
        g.fort[22] = 0
        g.supply[1], g.supply[2] = 4, 0
        self.g = g

    def test_upset_traced_by_hand(self):
        g = self.g
        # Two grapple rolls: star = CINT(14*.05) = 1 <= 1 hits; fin = CINT(14*.99) = 14 > 13 misses.
        # Then two normal() draws of twelve rolls each; all .5 makes each draw its mean + .5*sd.
        g.dice = ScriptedDice([.05, .99] + [.5] * 24)
        vp = g.victory[UNION]
        win, lose = g.battle(3, 21)
        report = g.log[-1].data
        # x: CINT(.01*100)=1; ratio .33 > .2: CINT(1 + 1.2 + .3) = CINT(2.5) = 2 (half to even);
        # ratio <= .5: 2 - 2 = 0, floored to 1.
        self.assertEqual(report["attack"], 1)
        # x1: realism CINT(.02*300 + 2) = 8; +.3*8 +.3*1 -> CINT(10.7) = 11; R! = 3 > 1.5: +2 = 13.
        self.assertEqual(report["defend"], 13)
        self.assertEqual(report["odds_percent"], 7)          # INT(100 * 1/14)
        self.assertEqual((win, lose), (3, 21))
        # killd: pct .09*1.3=.117, xbar CINT(11.7)=12, vary CINT(12*.883)=11, 12+.5*SQR(11) -> 14
        # killa: pct .11, xbar 33, vary CINT(33*.89)=29, 33+.5*SQR(29) -> 36
        # blend: killa CINT(.8*36+.2*14)=32, killd CINT(.8*14+.2*32)=18
        self.assertEqual((report["attacker_loss"], report["defender_loss"]), (32, 18))
        self.assertEqual((g.armysize[3], g.armysize[21]), (68, 282))
        self.assertEqual(g.victory[UNION], vp + 1)
        self.assertEqual(g.dice.calls, 26)

    def test_line_947_decrements_armies_one_and_two(self):
        g = self.g
        g.dice = ScriptedDice([.05, .99] + [.5] * 24)
        g.battle(3, 21)
        # Not the combatants: slots 1 and 2, as written (supply(i) for i = 1 TO 2).
        self.assertEqual((g.supply[1], g.supply[2]), (3, 0))
        self.assertEqual((g.supply[3], g.supply[21]), (5, 7))

    def test_fort_doubles_a_resting_defender(self):
        g = self.g
        g.fort[22] = 1
        g.dice = ScriptedDice([.05, .99] + [.5] * 24)
        g.battle(3, 21)
        self.assertEqual(g.log[-1].data["defend"], 20)        # 13 * 2 = 26, capped at TCR 20

    def test_fort_ignored_for_a_defender_with_orders(self):
        g = self.g
        g.fort[22] = 1
        g.armymove[21] = 5                                    # line 913: armymove(defend) = 0 only
        g.dice = ScriptedDice([.05, .99] + [.5] * 24)
        g.battle(3, 21)
        self.assertEqual(g.log[-1].data["defend"], 13)


class Recruiting(unittest.TestCase):
    def test_newarmy_in_philadelphia(self):
        g = Game()
        g.dice = ScriptedDice([.5])
        slot = g.commander(UNION)
        self.assertEqual((slot, g.lname[slot]), (6, "Grant"))
        g.armyloc[slot] = 30
        cash = g.cash[UNION]
        g.newarmy(UNION, slot, 30)
        # supply CINT(3 + 5*.5) = CINT(5.5) = 6, +2 for the Union; size 3*50+33 = 183
        self.assertEqual((g.supply[slot], g.armysize[slot], g.armyexper[slot], g.armylead[slot]), (8, 183, 1, 8))
        self.assertEqual((g.armymove[slot], g.cash[UNION]), (-1, cash - 100))
        self.assertEqual(g.dice.calls, 1)

    def test_isolated_city_gives_a_third(self):
        g = Game()
        for c in g.neighbours(30):
            g.cityp[c] = REBEL
        g.dice = ScriptedDice([.5])
        slot = g.commander(UNION)
        g.armyloc[slot] = 30
        g.newarmy(UNION, slot, 30)
        self.assertEqual(g.armysize[slot], 183 // 3)

    def test_roll_consumes_one_die_per_city_until_full(self):
        g = Game()
        # First roll .9 > .8: at most 3 cities. Zeros then accept every Union city.
        g.dice = ScriptedDice([.9] + [0.0] * 40)
        offered = g.recruit_open(UNION)
        union_cities = [c for c in range(1, 41) if g.cityp[c] == UNION and g.cityo[c] != REBEL]
        self.assertEqual(sorted(offered), sorted(union_cities[:3]))
        self.assertEqual(g.dice.calls, 1 + union_cities[2])
        self.assertEqual(g.rflag, 3)
        g.dice = ScriptedDice([])                             # reopening uses the kept list
        self.assertEqual(g.recruit_open(UNION), offered)

    def test_empty_roll_is_not_kept(self):
        g = Game()
        g.dice = ScriptedDice([.1] + [.99] * 40)
        self.assertEqual(g.recruit_open(UNION), [])
        self.assertEqual(g.rflag, 0)


class Supply(unittest.TestCase):
    def test_resupply_buys_up_to_five(self):
        g = Game()
        g.cash[UNION], g.armysize[1], g.supply[1] = 500, 100, 1
        # x = CINT(500/100*10) = 50; 50 + 1 > 5 so x = 4; cost .1*4*100 = 40
        self.assertEqual(g.resupply_amount(1), 4)
        g.resupply(1)
        self.assertEqual((g.supply[1], g.cash[UNION]), (5, 460))

    def test_iterate_feeds_then_winter_costs_outside_ports(self):
        g = Game()
        g.dice = ScriptedDice([])
        g.month = 11                                          # iterate advances to January
        g.cash[UNION] = 1000
        before = g.supply[1]                                  # Washington is not a seaport (90)
        size = g.armysize[1]
        g.iterate()
        self.assertEqual((g.month, g.year), (1, 1862))
        self.assertEqual(g.supply[1], before + 1 - 1)
        self.assertEqual(g.cash[UNION], 1000 - sum(round(.2 * g.armysize[i]) for i in range(1, 21) if g.armyloc[i]))
        self.assertEqual(g.armysize[1], size)


class Victory(unittest.TestCase):
    def test_city_control_wins(self):
        g = Game()
        g.control[UNION] = g.vicflag[3]
        g.income[1] = g.income[2] = 100
        g.victor()
        self.assertEqual((g.result["winner"], g.result["reason"]), (UNION, "cities controlled"))

    def test_deadline_is_a_confederate_technical_victory(self):
        g = Game()
        g.month, g.year = g.vicflag[1], g.vicflag[2]
        g.income[1] = g.income[2] = 100
        v1 = g.victory[1]
        g.victor()
        self.assertEqual((g.result["winner"], g.result["reason"]), (REBEL, "time expired"))
        self.assertEqual(g.victory[1], round(.7 * v1))

    def test_annihilation_adds_three_hundred_then_one_hundred(self):
        # Lines 4397 and 4493: j = 7 adds 300 on detection and 100 more after the prompt.
        g = Game()
        for i in range(21, 41):
            g.armyloc[i] = 0
        g.income[1] = g.income[2] = 100
        v1 = g.victory[1]
        g.victor()
        self.assertEqual((g.result["winner"], g.result["condition"]), (UNION, 7))
        self.assertEqual(g.victory[1], v1 + 400)

    def test_union_strength_ratio(self):
        # Lines 4404-4407: for the Union, x / y > vicflag(6) with x, y the sides' total men.
        g = Game()
        g.income[1] = g.income[2] = 100
        g.armysize[1] = 3 * g.strength(REBEL) - sum(g.armysize[i] for i in range(2, 21) if g.armyloc[i])
        g.victor()
        self.assertIsNone(g.result)                       # exactly 3:1 is not "more than"
        g.armysize[1] += 1
        g.victor()
        self.assertEqual((g.result["winner"], g.result["condition"]), (UNION, 6))

    def test_union_capital_capture_needs_its_own_capital(self):
        g = Game()
        g.income[1] = g.income[2] = 100
        g.capcity[2] = 0
        g.capcity[1] = 0
        g.victor()
        self.assertIsNone(g.result)                       # line 4402: capcity(i) > 0 too
        g.capcity[1] = 39
        g.victor()
        self.assertEqual((g.result["winner"], g.result["condition"]), (UNION, 5))

    def test_the_deadline_is_checked_before_any_union_condition(self):
        # Line 4399 comes before 4400-4411 for i = 1, so a Union that also holds
        # 32 cities on the deadline still gets the Confederate technical victory.
        g = Game()
        g.income[1] = g.income[2] = 100
        g.month, g.year = g.vicflag[1], g.vicflag[2]
        g.control[1] = 35
        g.victor()
        self.assertEqual((g.result["winner"], g.result["condition"], g.result["checked_for"]), (REBEL, 2, UNION))

    def test_topbar_clamps_negative_points(self):
        g = Game()
        g.victory[2] = -40
        g.topbar()
        self.assertEqual(g.victory[2], 0)


if __name__ == "__main__":
    unittest.main()
