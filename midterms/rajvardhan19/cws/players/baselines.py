"""Cheap players: the original game's own Union AI, a random player and a passive one.

All three see only (observation, legal_actions) and return one action string,
the same contract as the model player. None of them touches the Game.
"""

import random

from ..engine import REBEL, UNION, starfin
from ..qb import QBRandom, S, cint, f32, qint
from .. import smarts
from .view import View


class OriginalAI:
    """SUB smarts playing the Union, as it does when a human takes the Rebels.

    The decision code is cws/smarts.py, shared with the opponent. Differences
    from the original's computer Union, from the midterm's scope or the
    information boundary:

    - no navy or railroad to use;
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
                if rnd() > S(.5):                        # who = 1 branch of line 2251
                    break
                if f32(3 * rnd()) > f32(1 + self.aggress) and b.cash[me] >= 200:
                    go = "city2"
                    continue
                break
        b = self._view()                                 # Recruit New Armies
        if smarts.enufarmies(b, me) <= f32(2 + 3 * foe + f32(3 * rnd())):
            yield "troops"
            while True:
                b = self._view()
                offered = [b.city.index(n) for n in self.obs["recruiting"]["offered"]]
                if not offered or b.cash[me] < 100:
                    break
                pick = offered[smarts.randsel(b, offered, me, rnd)]
                if b.occupied[pick] == 0 and not any(b.armyloc[k] == 0 for k in starfin(me)):
                    break
                yield f"recruit {b.city[pick]}"
        b = self._view()                                 # Check to Combine
        eligible = sorted({b.armyloc[j] for j in starfin(me) if b.armyloc[j] > 0
                           and b.cityp[b.armyloc[j]] == me and b.occupied[b.armyloc[j]] != j
                           and b.armymove[j] == 0}, key=lambda c: b.city[c])
        if eligible:
            yield f"join {b.city[eligible[qint(f32(len(eligible) * rnd()))]]}"
        for i in starfin(me):                            # Top Priority: move orders
            b = self._view()
            dest = smarts.march_order(b, i, me, foe, rnd, self.aggress, self.bold)
            if dest:
                yield f"move {i} {b.city[dest]}"
        b = self._view()
        for i in starfin(me):                            # drill idle armies
            if b.armyloc[i] > 0 and b.armymove[i] == 0 and b.armyexper[i] < 6 and b.armyexper[i] < b.armylead[i]:
                yield f"drill {i}"


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
