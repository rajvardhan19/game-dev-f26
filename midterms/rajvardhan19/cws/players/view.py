"""A board rebuilt from a Union observation, for the original-AI baseline.

It has the attribute names cws/smarts.py reads, filled only from the
observation. Enemy leader, experience and supply are masked: reading one
raises HiddenInformation, so the baseline provably plays on what a human
Union player can see. Enemy orders are 0, which is the truth at the time the
Union decides (newmonth clears every order, line 267, and the computer
plans only after the Union ends its turn).
"""

from ..engine import UNION, REBEL

_OWNER = {"NEUTRAL": 0, "Union": UNION, "Rebel": REBEL}


class HiddenInformation(LookupError):
    pass


class Masked(list):
    def __init__(self, values, hidden):
        super().__init__(values)
        self.hidden = set(hidden)

    def __getitem__(self, i):
        if i in self.hidden:
            raise HiddenInformation(f"slot {i} is not visible to the Union")
        return super().__getitem__(i)


class View:
    def __init__(self, obs: dict) -> None:
        n = 41
        self.matrix = [[0] * 8 for _ in range(n)]
        self.cityp, self.cityv, self.fort, self.cityy = [0] * n, [0] * n, [0] * n, [0] * n
        self.city = ["NONE"] + [""] * 40
        for c in obs["cities"]:
            i = c["id"]
            self.city[i] = c["name"]
            self.cityp[i] = _OWNER[c["owner"]]
            self.cityv[i], self.fort[i], self.cityy[i] = c["value"], c["fort"], c["y"]
            for j, m in enumerate(c["neighbors"], 1):
                self.matrix[i][j] = m
        self.armysize, self.armyloc, self.armymove = [0] * n, [0] * n, [0] * n
        lead, exper, supply = [0] * n, [0] * n, [0] * n
        for a in obs["your_armies"]:
            i = a["id"]
            self.armysize[i], self.armyloc[i] = a["men"] // 100, a["city"]
            lead[i], exper[i], supply[i] = a["leader"], a["experience"], a["supply"]
            order = a["order"]
            if order.startswith("moving to "):
                self.armymove[i] = self._city_id(order[len("moving to "):])
            elif order != "none":
                self.armymove[i] = -1
        enemy = []
        for a in obs["enemy_armies"]:
            i = a["id"]
            self.armysize[i], self.armyloc[i] = a["men"] // 100, a["city"]
            enemy.append(i)
        self.armylead = Masked(lead, enemy)
        self.armyexper = Masked(exper, enemy)
        self.supply = Masked(supply, enemy)
        self.occupied = [0] * n
        for i in sorted(range(1, 41), reverse=True):     # SUB occupy: lowest-numbered army wins
            if self.armyloc[i] > 0:
                self.occupied[self.armyloc[i]] = i
        self.capcity = [0, 0, 0]
        for c in obs["cities"]:
            if c["capital_of"]:
                self.capcity[_OWNER[c["capital_of"]]] = c["id"]
        r = obs["victory_rules"]
        self.vicflag = [0, r["deadline_month"], r["deadline_year"], r["cities"],
                        r["income_percent"], r["capital"], r["strength_ratio"]]
        self.cash = [0, obs["treasury"]["Union"]["cash"], obs["treasury"]["Rebel"]["cash"]]
        self.control = [0, obs["treasury"]["Union"]["cities"], obs["treasury"]["Rebel"]["cities"]]
        self.realism = int(obs["settings"]["realism"])
        self.jancam = int(obs["settings"]["january_campaigns"])
        self.month = obs["month_number"]

    def _city_id(self, name: str) -> int:
        return self.city.index(name)

    def cutoff(self, who: int, target: int) -> int:
        return sum(1 for j in range(1, 7)
                   if self.matrix[target][j] > 0 and self.cityp[self.matrix[target][j]] == who)

    def neighbours(self, c: int) -> list[int]:
        return [m for m in self.matrix[c][1:7] if m > 0]
