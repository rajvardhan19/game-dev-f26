"""Navies and railroads, traced by hand from SUB navy (1471-1887) and SUB railroad (1969-2072).

Each test scripts the dice, so it also pins how many rolls the source uses.
"""

import unittest

from cws import navy, railroad
from cws.data import ALTERNATE
from cws.engine import Game, REBEL, UNION
from cws.interface import CivilWarEpisode, PLAYER_ID
from cws.qb import ScriptedDice

BALTIMORE, PHILADELPHIA, NEW_ORLEANS, MOBILE, SAVANNAH, CHARLESTON, NORFOLK = 2, 30, 27, 24, 34, 5, 28


class Fleets(unittest.TestCase):
    def test_opening_fleets_and_no_ironclads_in_1861(self):
        g = Game()
        self.assertEqual((g.fleet[1], g.navysize[1], g.navyloc[1]), ("WWWW", 4, PHILADELPHIA))
        self.assertEqual((g.fleet[2], g.navysize[2], g.navyloc[2]), ("W", 1, MOBILE))
        alt = Game(ALTERNATE)                            # ALTMAP.INI ships "IWWW"; lines 151-156 make it wooden
        self.assertEqual(alt.fleet[1], "WWWW")

    def test_barnacle_loses_the_last_ship(self):
        g = Game()
        g.fleet[1], g.navysize[1] = "IWW", 3
        navy.barnacle(g, 1)
        self.assertEqual((g.fleet[1], g.navysize[1]), ("IW", 2))
        g.fleet[1], g.navysize[1] = "I", 1
        navy.barnacle(g, 1)
        self.assertEqual((g.fleet[1], g.navysize[1], g.navyloc[1]), ("", 0, 0))

    def test_human_builds_a_wooden_ship_for_100_with_one_roll(self):
        g = Game()
        g.dice = ScriptedDice([.5])                     # line 1523 rolls even for the human
        cash = g.cash[1]
        g.human_navy([1])                                # Build; no Type menu before March 1862
        self.assertEqual((g.fleet[1], g.navysize[1], g.cash[1]), ("WWWWW", 5, cash - 100))
        self.assertEqual((g.cityp[0], g.dice.calls), (UNION, 1))   # line 1483: city 0's owner is set

    def test_human_ironclad_costs_200_and_goes_first(self):
        g = Game()
        g.month, g.year, g.cash[1] = 5, 1862, 500
        g.dice = ScriptedDice([.5])
        g.human_navy([1, 2])                             # Build, Type: Ironclad
        self.assertEqual((g.fleet[1], g.cash[1]), ("IWWWW", 300))

    def test_human_chooses_wooden_on_the_type_menu(self):
        g = Game()
        g.month, g.year, g.cash[1] = 5, 1862, 500        # ironclads allowed and cash >= 200: Type menu
        g.dice = ScriptedDice([.5])
        g.human_navy([1, 1])                             # Build, Type: Wooden
        self.assertEqual((g.fleet[1], g.navysize[1], g.cash[1], g.dice.calls), ("WWWWW", 5, 400, 1))

    def test_human_builds_a_new_fleet_in_a_chosen_shipyard(self):
        g = Game()
        g.fleet[1], g.navysize[1], g.navyloc[1] = "", 0, 0
        g.cityp[BALTIMORE] = g.cityp[NORFOLK] = UNION
        g.navyloc[2] = BALTIMORE                         # line 1553: no shipyard where the enemy fleet is
        g.dice = ScriptedDice([.5])
        cash = g.cash[1]
        g.human_navy([1, 1])                             # Build; Port row 1 of Norfolk, Philadelphia
        self.assertEqual(g.array[1:3], [NORFOLK, PHILADELPHIA])
        self.assertEqual((g.fleet[1], g.navysize[1], g.navyloc[1], g.cash[1]), ("W", 1, NORFOLK, cash - 100))
        self.assertIn("building NEW fleet in Norfolk", g.log[-1].text)

    def test_computer_ironclad_costs_100_and_it_keeps_building(self):
        g = Game()
        g.month, g.year, g.cash[2] = 5, 1862, 300
        g.dice = ScriptedDice([.5, .01])                 # builds once, then .01 < .07*2 ends the loop
        navy.navy(g, REBEL, 1)
        self.assertEqual((g.fleet[2], g.cash[2], g.dice.calls), ("IW", 200, 2))

    def test_bombarding_with_three_ships_rounds_half_to_even(self):
        g = Game()
        g.fleet[1], g.navysize[1], g.navyloc[1] = "WWW", 3, NEW_ORLEANS
        defender = 21
        g.armyloc[defender], g.armysize[defender], g.supply[defender] = NEW_ORLEANS, 100, 5
        g.occupy(NEW_ORLEANS)
        # pct = .005*3 + .02*.25 = .02, 2 killed; supply x = .5*3 + 1 = 2.5, which CINT makes 2
        g.dice = ScriptedDice([.9, .25])
        g.human_navy([2])
        self.assertEqual((g.armysize[defender], g.supply[defender]), (98, 3))

    def test_bombarding_an_occupied_port(self):
        g = Game()
        g.navyloc[1] = NEW_ORLEANS
        defender = 21
        g.armyloc[defender], g.armysize[defender], g.supply[defender] = NEW_ORLEANS, 100, 5
        g.occupy(NEW_ORLEANS)
        # .9 for line 1582 (rolled, unused by a human), then pct = .005*4 + .02*.5 = .03
        g.dice = ScriptedDice([.9, .5])
        g.human_navy([2])
        self.assertEqual((g.armysize[defender], g.supply[defender]), (97, 2))   # 3 killed, CINT(.5*4+1) supply
        self.assertEqual(g.nflag, 1)

    def test_an_empty_port_turns_neutral(self):
        g = Game()
        g.navyloc[1] = SAVANNAH
        g.fort[SAVANNAH] = 0
        vp = g.victory[1]
        g.dice = ScriptedDice([.9, .1])                  # .1 <= .25 + .07*4: the city falls
        g.human_navy([2])
        self.assertEqual((g.cityp[SAVANNAH], g.victory[1]), (0, vp + g.cityv[SAVANNAH]))

    def test_shore_batteries_sink_ships_until_a_fort_breaks(self):
        g = Game()
        g.navyloc[1] = CHARLESTON                        # fort 2, empty
        # .95 >= .7 + .03*(4 - 2): a ship sinks; .7 < .7 + .03*(3 - 2): the fort is damaged.
        # With the difference reversed (.64, then .67) the second roll would sink another ship.
        g.dice = ScriptedDice([.9, .95, .7])
        g.human_navy([2])
        self.assertEqual((g.navysize[1], g.fort[CHARLESTON], g.dice.calls), (3, 1, 3))

    def _duel(self, union: str, rebel: str, rolls: list[float], grudge: int) -> Game:
        """The Union fleet sails from Baltimore into the Rebel fleet at Philadelphia (labels pirate-hitme1)."""
        g = Game()
        g.grudge = grudge
        g.fleet[1], g.navysize[1], g.navyloc[1] = union, len(union), BALTIMORE
        g.fleet[2], g.navysize[2], g.navyloc[2] = rebel, len(rebel), PHILADELPHIA
        row = navy.sail_list(g, 1).index(PHILADELPHIA) + 1
        g.dice = ScriptedDice(rolls)
        g.human_navy([3, row])
        return g

    def test_an_ironclad_takes_20_hits_and_shoots_at_60_percent(self):
        # Union "I" against Rebel "W": RND <= .5 + .1 hits the Rebel. Fifteen rolls of .9 hit the
        # ironclad (it would sink at 10 if it had wooden hits); ten of .55 sink the Rebel ship
        # (.55 would be a Union loss if the .1 went the other way).
        vp2 = Game().victory[2]
        g = self._duel("I", "W", [.9] * 15 + [.55] * 10, grudge=0)
        self.assertEqual((g.navysize[2], g.navyloc[2], g.fleet[2], g.victory[2]), (0, 0, "", vp2 + 10))
        self.assertEqual((g.navysize[1], g.fleet[1], g.navyloc[1]), (1, "I", PHILADELPHIA))
        self.assertEqual((g.grudge, g.dice.calls), (1, 25))   # line 1798: who = side

    def test_an_attacking_fleet_can_be_eliminated(self):
        # Union "W" against Rebel "I": the Union hits only on RND <= .4, so .45 is a Union loss.
        vp1 = Game().victory[1]
        g = self._duel("W", "I", [.45] * 10, grudge=1)
        self.assertEqual((g.navysize[1], g.navyloc[1], g.fleet[1], g.victory[1]), (0, 0, "", vp1 + 10))
        self.assertEqual((g.navysize[2], g.navyloc[2]), (1, PHILADELPHIA))
        self.assertEqual((g.grudge, g.dice.calls), (0, 10))   # line 1817: who = side clears it

    def test_commerce_raiding_amount(self):
        g = Game()
        g.navyloc[1], g.commerce, g.income[2] = navy.AT_SEA, UNION, 400
        g.dice = ScriptedDice([.1, .5])                  # .1 < .88; raider = .05*4*(1+.5)*400 = 120
        navy.commerce_raiding(g)
        self.assertEqual((g.raider, g.grudge), (120, 1))  # line 2615: commerce = side

    def test_a_failed_raid_loses_a_ship_and_rolls_again(self):
        g = Game()
        g.navyloc[1], g.commerce, g.income[2] = navy.AT_SEA, UNION, 400
        # .95 >= .8 + .02*4: a ship is lost (lines 2617-2624) and, still at sea, the raid repeats;
        # .1 < .86, raider = .05*3*(1+.5)*400 = 90
        g.dice = ScriptedDice([.95, .1, .5])
        navy.commerce_raiding(g)
        self.assertEqual((g.navysize[1], g.fleet[1], g.raider, g.commerce, g.dice.calls), (3, "WWW", 90, UNION, 3))
        self.assertIn("raiders have lost a ship (3 remain)", " ".join(e.text for e in g.log))

    def test_a_raid_that_loses_the_last_ship_ends(self):
        g = Game()
        g.fleet[1], g.navysize[1], g.navyloc[1], g.commerce, g.income[2] = "W", 1, navy.AT_SEA, UNION, 400
        g.dice = ScriptedDice([.95])                     # .95 >= .82: the last ship goes, navyloc 0
        navy.commerce_raiding(g)
        self.assertEqual((g.navysize[1], g.navyloc[1], g.raider, g.commerce, g.dice.calls), (0, 0, 0, 0, 1))

    def _blockade(self, union_fleet: int, rebel_fleet: int) -> int:
        g = Game()
        g.dice = ScriptedDice([])
        g.month = 5                                      # iterate moves to July: no winter loss
        rebel = 21
        g.armyloc[rebel], g.supply[rebel], g.armysize[rebel] = MOBILE, 5, 100
        g.cash[2] = 0                                    # and no resupply
        g.navyloc[1], g.navyloc[2] = union_fleet, rebel_fleet
        g.iterate()
        return g.supply[rebel]

    def test_blockaded_armies_lose_supply(self):
        # Line 1424 tests the enemy's fleet, navyloc(3 - s), not the army's own.
        self.assertEqual(self._blockade(union_fleet=MOBILE, rebel_fleet=NEW_ORLEANS), 4)
        self.assertEqual(self._blockade(union_fleet=PHILADELPHIA, rebel_fleet=MOBILE), 5)


class ComputerFleet(unittest.TestCase):
    """GOSUB nest, lines 1846-1866: where the computer's fleet sails (chx = 3)."""

    def test_nest_prefers_an_enemy_port(self):
        g = Game()                                       # Rebel fleet (1 ship) at Mobile, Union (4) at Philadelphia
        dests = navy.sail_list(g, REBEL)
        g.set_array(dests)                               # Baltimore, Charleston, ..., Philadelphia (row 6), ...
        # Row 6 is the Union fleet: line 1853 rolls (.5) but 1 < 4 ships; line 1855 rolls (.5), not > .8.
        # No other row is an enemy city, so best = 6; the fleet is not at Philadelphia: no line 1865 roll.
        g.dice = ScriptedDice([.5, .5])
        self.assertEqual((dests[5], navy._nest(g, REBEL, len(dests)), g.dice.calls), (PHILADELPHIA, 6, 2))

    def test_the_rebel_fleet_at_philadelphia_stays_half_the_time(self):
        def sail(rolls):
            g = Game()
            g.fleet[1], g.navysize[1], g.navyloc[1] = "", 0, 0
            g.navyloc[2] = PHILADELPHIA
            g.dice = ScriptedDice(rolls)
            navy.navy(g, REBEL, 3)
            return g.navyloc[2], g.dice.calls
        # The eight other ports are Rebel or neutral Baltimore, so no row rolls and best = 0:
        # choose = 1 + INT(.55 * 8) = 5, New Orleans (Baltimore, Charleston, Jacksonville, Mobile, ...).
        self.assertEqual(sail([.55, .4]), (NEW_ORLEANS, 2))
        # Line 1865: .6 > .5 gives menu row 30; array(30) is 0, so line 1659 leaves the fleet in port.
        self.assertEqual(sail([.55, .6]), (PHILADELPHIA, 2))


class Railroads(unittest.TestCase):
    def test_train_capacity(self):
        g = Game()                                       # 600 + 5*(11 - 11) for the Union, 300 + 5*(23 - 11)
        self.assertEqual((railroad.traincapacity(g, 1), railroad.traincapacity(g, 2)), (600, 360))
        g.control[1] = 0
        self.assertEqual(railroad.traincapacity(g, 1), 600 - 55)
        g.control[1] = 200
        self.assertEqual(railroad.traincapacity(g, 1), 1200)          # capped at twice train(1)
        g.train[1], g.control[1] = 101, 0                # 101 - 55 = 46, below (2 * 101) \ 4 = 50
        self.assertEqual(railroad.traincapacity(g, 1), 50)

    def test_route_counts_two_rings_of_friendly_track(self):
        g = Game()
        self.assertGreater(railroad.route(g, UNION, 31), 1)            # Pittsburgh
        # Jefferson City: its one neighbour, St. Louis, is Union (+1), and St. Louis links on to
        # Union Springfield (+1; Paducah is neutral, Jefferson City itself is not counted).
        self.assertEqual(railroad.route(g, UNION, 18), 2)
        self.assertEqual(railroad.route(g, UNION, 19), 0)              # Knoxville: only Rebel Chattanooga

    def test_a_train_arrives_before_anyone_marches(self):
        ep = CivilWarEpisode("standard")
        ep.reset(3)
        self.assertTrue(ep.step(PLAYER_ID, "rail 2 Phildelpha")["accepted"])
        g = ep._game
        self.assertEqual((g.armyloc[2], g.armymove[2], g.rr[1]), (0, PHILADELPHIA, 2))
        self.assertFalse(any(a.startswith("rail ") for a in ep.legal_actions(PLAYER_ID)))   # one train a turn
        mark = len(g.log)
        ep.step(PLAYER_ID, "end turn")
        kinds = [e.kind for e in g.log[mark:]]
        arrival = next(i for i, e in enumerate(g.log[mark:]) if e.kind == "rail" and "arrived" in e.text)
        self.assertNotIn("move", kinds[:arrival])
        self.assertEqual((g.armyloc[2], g.rr[1]), (PHILADELPHIA, 0))


class Interface(unittest.TestCase):
    def test_one_fleet_action_a_turn(self):
        ep = CivilWarEpisode("standard")
        ep.reset(4)
        self.assertTrue(ep.step(PLAYER_ID, "fleet sail Baltimore")["accepted"])
        legal = ep.legal_actions(PLAYER_ID)
        self.assertFalse(any(a.startswith(("fleet ", "build ")) for a in legal))
        self.assertFalse(ep.step(PLAYER_ID, "fleet raid")["accepted"])
        ep.step(PLAYER_ID, "end turn")
        self.assertTrue(any(a.startswith("fleet ") for a in ep.legal_actions(PLAYER_ID)))

    def test_both_navies_are_visible_as_the_army_report_shows(self):
        obs = CivilWarEpisode("standard").reset(1)
        self.assertEqual(obs["navies"]["Rebel"], {"ships": 1, "ironclads": 0, "at": "Mobile"})
        self.assertEqual(obs["railroad"], {"capacity_men": 60000, "train": None})

    def test_army_on_a_train_is_still_listed(self):
        ep = CivilWarEpisode("standard")
        ep.reset(3)
        obs = ep.step(PLAYER_ID, "rail 2 Phildelpha")["observation"]
        army = next(a for a in obs["your_armies"] if a["id"] == 2)
        self.assertEqual((army["city"], army["order"]), (0, "on the train to Phildelpha"))
        self.assertEqual(obs["railroad"]["train"], {"army": 2, "to": "Phildelpha"})


if __name__ == "__main__":
    unittest.main()
