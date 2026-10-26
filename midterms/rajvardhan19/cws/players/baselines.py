"""Cheap players: the original game's own Union AI, a random player and a passive one.

All three see only (observation, legal_actions) and return one action string,
the same contract as the model player. None of them touches the Game.
"""

import random

from ..engine import REBEL, UNION, starfin
from ..qb import QBRandom, S, cint, f32, qint
from .. import navy, railroad, smarts
from .view import View


class OriginalAI:
    """SUB smarts playing the Union, as it does when a human takes the Rebels.

    The decision code is cws/smarts.py, shared with the opponent. Differences
    from the original's computer Union, from the midterm's scope or the
    information boundary:

    - it uses fleets and trains under the human's rules (an ironclad costs
      200, not the computer's 100; ships join a fleet only in an own seaport);
    - two globals the screen never shows are approximated: `cityp(0)`
      (who last ran SUB navy) is taken to be the Rebels, and `grudge`
      (the computer's revenge order) is set when last turn's report shows a
      Rebel raid on Union commerce; the original also sets or clears it
      after naval battles and shore batteries (lines 1611, 1798, 1817),
      which this baseline ignores;
    - with a grudge against a fleet at sea it stays in port: the original
      sails to sea and fights (line 1639), but the human's Sail menu lists
      only seaports;
    - no `usadv` bonus: the original gives a computer Union 252 extra income
      a turn when the human plays the Rebels (lines 263, 749-751); here the
      human-side economy applies to every Union player alike;
    - it plans before the Rebels, as any Union player here does, instead of
      after them;
    - it draws its dice from its own generator, seeded from the episode seed
      (the model player needs none);
    - `occupied()` is rebuilt from the screen as the lowest-numbered army in
      each city, not the engine's stored pointer; the scratch slot
      armysize(0), invisible on screen, reads as 0 in randsel.
    """

    name = "original-ai"
    me, foe, bold = UNION, REBEL, 3

    def __init__(self, seed: float = 0) -> None:
        self.dice = QBRandom()
        self.dice.randomize(seed * 7 + 3)
        self._turn = None
        self._prev_control = None
        self.aggress = 0.0
        self.grudge = 0

    def act(self, obs: dict, legal: list[str]) -> str:
        self.obs, self.legal = obs, set(legal)
        if obs["turn"] != self._turn:
            self._turn = obs["turn"]
            self._start_turn(obs)
            self._plan = self._procedure()
        while True:
            try:
                action = next(self._plan)
            except StopIteration:
                return "end turn"
            if action in self.legal:
                return action

    def _start_turn(self, obs: dict) -> None:
        """aggress! as iterate (lines 1437-1440) and tupdate (2643) compute it for side = 2."""
        if obs["turn"] == 1:
            self.aggress = 0.0
        else:
            y = x = 0
            for a in sorted(obs["your_armies"], key=lambda a: a["id"]):
                y = cint(f32(y + .1 * (a["men"] // 100)))
            for a in sorted(obs["enemy_armies"], key=lambda a: a["id"]):
                x = cint(f32(x + .1 * (a["men"] // 100)))
            self.aggress = f32(y / x) if x > 0 else 1.0
            if self._prev_control is not None and self._prev_control < 11:
                self.aggress = f32(self.aggress + .7)
        self._prev_control = obs["treasury"]["Union"]["cities"]
        self.grudge = int(any(e["text"].startswith("Rebel raiders have sunk") for e in obs["last_turn_report"]))

    def _view(self) -> View:
        return View(self.obs)

    def _procedure(self):
        """smarts, line 2212 onward, one yielded action at a time."""
        rnd, me, foe = self.dice.rnd, self.me, self.foe
        b = self._view()
        for i in starfin(me):                            # Check Supply
            if b.armyloc[i] > 0 and b.supply[i] < 1:
                yield f"supply {i}"
        b = self._view()
        if 200 <= b.cash[me]:                            # Fortify Capital or Other City
            cap = b.capcity[me]
            target, go = 0, "city2"
            if not (b.occupied[cap] == 0 or b.fort[cap] > 1):
                target = cap
                go = "capital" if b.cityp[target] == me else "city2"
            while True:
                b = self._view()
                if go == "city2":
                    if f32(1 + rnd()) < f32(self.bold + self.aggress):
                        break
                    target = 0
                    for i in starfin(me):
                        x = b.armyloc[i]
                        if x == 0 or b.armymove[b.occupied[x]] < 0 or b.armymove[i] < 0 or b.fort[x] > 1:
                            continue
                        if smarts.void(b, x, foe) > b.armysize[i]:
                            target = x
                            break
                if target == 0 or b.fort[target] > 1:
                    break
                yield f"fortify {b.city[target]}"
                b = self._view()
                roll = rnd()                             # line 2251 rolls for every side (AND does not short-circuit)
                if b.navysize[1] < 1 and roll > S(.5):   # who = 1; the unset cash < 222 holds
                    break
                if f32(3 * rnd()) > f32(1 + self.aggress) and b.cash[me] >= 200:
                    go = "city2"
                    continue
                break
        slush = 0                                        # Recruit New Armies, lines 2255-2264
        b = self._view()
        while True:
            if b.navysize[1] < 1 and b.cash[1] > 100:    # line 2256: who = 1 builds a first ship
                yield from self._navy(1)
                b = self._view()
                if b.cash[me] < 100:
                    break
            if smarts.enufarmies(b, me) > f32(2 + 3 * foe + f32(3 * rnd())):
                break
            if b.navysize[me] < 5 and b.cash[me] > 100 and b.navyloc[me] != navy.AT_SEA:
                if b.cityp[b.navyloc[me]] == me:
                    slush = 100                          # kept back for ships
                    if b.cash[me] - slush < 100:
                        break
            yield "troops"
            while True:
                b = self._view()
                offered = [b.city.index(n) for n in self.obs["recruiting"]["offered"]]
                if not offered or b.cash[me] - slush < 100:
                    break
                pick = offered[smarts.randsel(b, offered, me, rnd)]
                if b.occupied[pick] == 0 and not any(b.armyloc[k] == 0 for k in starfin(me)):
                    break
                yield f"recruit {b.city[pick]}"
            break
        yield from self._naval_orders()                  # labels dock and movenavy
        b = self._view()                                 # Check to Combine
        eligible = sorted({b.armyloc[j] for j in starfin(me) if b.armyloc[j] > 0
                           and b.cityp[b.armyloc[j]] == me and b.occupied[b.armyloc[j]] != j
                           and b.armymove[j] == 0}, key=lambda c: b.city[c])
        if eligible:
            yield f"join {b.city[eligible[qint(f32(len(eligible) * rnd()))]]}"
        b = self._view()                                 # line 2301: railroad
        if not b.train_out:
            choice = railroad.computer_rail_choice(b, me, foe, b.rail_capacity)
            if choice:
                yield f"rail {choice[0]} {b.city[choice[1]]}"
        for i in starfin(me):                            # Top Priority: move orders
            b = self._view()
            dest = smarts.march_order(b, i, me, foe, rnd, self.aggress, self.bold)
            if dest:
                yield f"move {i} {b.city[dest]}"
        b = self._view()
        for i in starfin(me):                            # drill idle armies
            if b.armyloc[i] > 0 and b.armymove[i] == 0 and b.armyexper[i] < 6 and b.armyexper[i] < b.armylead[i]:
                yield f"drill {i}"


    def _naval_orders(self):
        """smarts labels dock and movenavy (lines 2265-2293), as the computer's Union plays them."""
        rnd, me = self.dice.rnd, self.me
        b = self._view()
        if b.navyloc[1] == 0 and b.navysize[1] < 1 and b.cityp[30] == 1 and b.cash[1] > 100:
            yield from self._navy(1)                     # line 2266 (side = 2): a fleet at a Union port
        elif b.navyloc[me] == navy.AT_SEA:
            if rnd() < S(.9):
                yield from self._navy(3)
            return
        elif not (b.cash[me] < 100 or b.navysize[me] > 9 or b.cityp[b.navyloc[me]] != me):
            yield from self._navy(1)
        b = self._view()                                 # movenavy
        loc = b.navyloc[me] if b.navysize[me] else 0
        if loc == 0:
            return
        if loc != navy.AT_SEA:
            if b.cityp[loc] in (me, 0):
                yield from self._navy(3)
                return
        else:
            if rnd() < S(.5):
                yield from self._navy(3)
            return
        if b.cityp[loc] != me:
            roll = rnd()
            yield from self._navy(2 if (b.occupied[loc] == 0 or roll > S(.3)) else 3)

    def _navy(self, chx: int):
        """SUB navy's computer modes (chx 1-5), turned into the human's Ships commands."""
        rnd, me, foe = self.dice.rnd, self.me, self.foe
        b = self._view()
        if b.navyloc[me] < 1:                            # lines 1473-1480
            chx = 1
        else:
            if b.commerce == foe and b.raider > 0:
                chx = 4
            if self.grudge > 0:
                chx = 3
        for _ in range(12):                              # label ahoy; each pass is one decision
            b = self._view()
            loc, n = b.navyloc[me], b.navysize[me]
            if chx == 1 and (b.cash[me] < 100 or n > 9):
                return
            if loc < 1 and chx == 3:
                chx = 1
            if loc not in (0, navy.AT_SEA) and n > 1 and b.cityp[loc] == 0:
                if smarts.void(b, b.navyloc[1], foe) < 100:
                    chx = 5
            if chx == 1:                                 # Build
                if loc == navy.AT_SEA or rnd() < f32(.07 * n):
                    return
                kind = "ironclad" if navy.ironclads_allowed(_Date(b)) and b.cash[me] >= 200 else "wooden"
                if loc == 0:
                    ports = [i for i in range(1, 41) if b.matrix[i][7] == 99 and b.cityp[i] == me
                             and b.navyloc[foe] != i]
                    choose = 1 + qint(f32(len(ports) * rnd()))
                    if not ports:
                        return
                    action = f"build {kind} at {b.city[ports[choose - 1]]}"
                else:
                    action = f"build {kind}"
            elif chx == 2:                               # Attack
                if loc == navy.AT_SEA or b.cityp[loc] == me:
                    return
                roll = rnd()
                if b.occupied[loc] > 0 and roll > S(.5):
                    rnd()                                # line 1582 rolls again on the second pass
                elif b.cityp[loc] == 0:
                    chx = 3
                    continue
                action = "fleet attack"
            elif chx == 3:                               # Sail
                dests = [i for i in range(1, 41) if b.matrix[i][7] > 90 and loc != i]
                if n < 1 or not dests:
                    return
                if self.grudge > 0:
                    dest = b.navyloc[foe]
                else:
                    choose = self._nest(b, dests)
                    dest = dests[choose - 1] if 1 <= choose <= len(dests) else 0
                if dest in (0, loc, navy.AT_SEA):
                    return
                action = f"fleet sail {b.city[dest]}"
            elif chx == 4:
                action = "fleet raid"
            else:
                action = "fleet invade"
            if action not in self.legal:                 # the human's rules forbid it here
                return
            yield action
            if chx != 1:
                return

    def _nest(self, b, dests: list[int]) -> int:
        """GOSUB nest with the baseline's dice; row 30 (array(30), always 0 in scope) means no move."""
        rnd, me, foe = self.dice.rnd, self.me, self.foe
        best = 0
        for i, target in enumerate(dests, 1):
            if b.cityp[target] == 0:
                continue
            if target == b.navyloc[foe]:
                roll = rnd()
                if b.navysize[me] >= b.navysize[foe] and roll > S(.1):
                    return i
            if b.cityp[target] != me:
                best = i
                if rnd() > S(.8):
                    return best
        return 1 + qint(f32(rnd() * len(dests))) if best == 0 else best


class _Date:
    def __init__(self, b) -> None:
        self.realism, self.year, self.month = b.realism, b.year, b.month


class RandomPlayer:
    """A floor: ends the turn with probability 1/5, otherwise any other legal action."""

    name = "random"

    def __init__(self, seed: float = 0) -> None:
        self.rng = random.Random(f"random-{seed}")

    def act(self, obs: dict, legal: list[str]) -> str:
        others = [a for a in legal if a != "end turn"]
        if not others or self.rng.random() < 0.2:
            return "end turn"
        return self.rng.choice(others)


class PassivePlayer:
    """A floor: never gives an order."""

    name = "passive"

    def __init__(self, seed: float = 0) -> None:
        pass

    def act(self, obs: dict, legal: list[str]) -> str:
        return "end turn"
