"""Authoritative rules for the midterm scope of VGA Civil War Strategy v2.11.

Each method is a port of one SUB (or menu branch) of CWSTRAT.BAS, cited as
"line N" against source/CWSTRAT.BAS (unmodified copy, upstream commit dac8db1).
Arrays keep the source's 1-based indices; index 0 is the source's scratch
slot (combine uses armysize(0), for example) and is kept because other
routines read it. Union armies are slots 1-20, Confederate 21-40.

Out of scope, and therefore absent: navies, railroads, random events,
saving, two-player mode, graphics and sound. docs/rule-source-map.md lists
every omission and what it changes.
"""

import math
from dataclasses import dataclass, field

from .data import DATA_DIR, MapFiles, Reader, STANDARD
from .qb import QBRandom, S, cint, f32, idiv, qint

UNION, REBEL = 1, 2
FORCE = ("NEUTRAL", "Union", "Rebel")
MONTHS = ("", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")
CONDITIONS = {
    2: "time expired",
    3: "cities controlled",
    4: "share of total income",
    5: "capital captured",
    6: "army strength ratio",
    7: "enemy annihilated",
}


@dataclass
class Settings:
    """Options a player sets in the original's Utility menu (lines 479-703)."""

    side: int = UNION        # human side; the computer plays 3 - side
    difficult: int = 3       # Play Balance: 3 = Balanced
    realism: int = 1         # Realism + (CWS.CFG)
    jancam: int = 1          # January campaigns allowed (CWS.CFG)
    bold: int = 3            # computer aggression: 3 = NORMAL (CWS.CFG)
    randbal: int = 0         # Random Events OFF (Utility option 8, line 600)


def starfin(who: int) -> range:
    """SUB starfin, line 3816: army slots belonging to a side."""
    return range(1, 21) if who == UNION else range(21, 41)


def side_of(index: int) -> int:
    return UNION if index <= 20 else REBEL


@dataclass
class Event:
    kind: str
    text: str
    data: dict = field(default_factory=dict)


class Game:
    """One game. Holds every global the scoped routines read or write."""

    def __init__(self, map_files: MapFiles = STANDARD, settings: Settings | None = None,
                 dice=None) -> None:
        self.map_files = map_files
        self.settings = settings or Settings()
        self.dice = dice or QBRandom()
        self.log: list[Event] = []
        self._newgame()

    # ------------------------------------------------------------------ dice
    def rnd(self) -> float:
        return self.dice.rnd()

    def say(self, kind: str, text: str, **data) -> None:
        self.log.append(Event(kind, text, data))

    # ------------------------------------------------------------- new game
    def _newgame(self) -> None:
        """Lines 129-219: reset, filer(1), opening cash, cities, RANDOMIZE."""
        st = self.settings
        self.side, self.player = st.side, 1
        self.difficult, self.realism, self.jancam = st.difficult, st.realism, st.jancam
        self.bold, self.randbal = st.bold, st.randbal

        n = 41
        self.armysize = [0] * n
        self.armyloc = [0] * n
        self.armymove = [0] * n
        self.armylead = [0] * n
        self.armyexper = [0] * n
        self.supply = [0] * n
        self.armyname = [""] * n
        self.lname = [""] * n
        self.rating = [0] * n
        self.occupied = [0] * n
        self.city = ["NONE"] + [""] * 40
        self.cityx = [0] * n
        self.cityy = [0] * n
        self.cityv = [0] * n
        self.cityp = [0] * n
        self.cityo = [0] * n
        self.fort = [0] * n
        self.matrix = [[0] * 8 for _ in range(n)]
        self.cash = [0, 0, 0]
        self.control = [0, 0, 0]
        self.income = [0, 0, 0]
        self.victory = [0, 0, 0]
        self.capcity = [0, 0, 0]
        self.batwon = [0, 0, 0]
        self.casualty = [0, 0, 0]
        self.vicflag = [0] * 7
        self.aggress = 0.0          # aggress! starts at 0 until the first iterate
        self.rflag = 0
        self.rcity: list[int] = []
        self.turn = 1
        self.result: dict | None = None

        self._filer_load()
        # Line 160-161 would set randbal from the side; the scenario's
        # Utility setting (Random Events OFF) is applied after it.
        self.randbal = st.randbal
        if self.side == 1 and self.difficult < 3:          # line 163
            self.cash[2] += 600 - 100 * self.difficult
        if self.side == 2 and self.difficult > 3:          # line 164
            self.cash[1] += 100 * self.difficult
        for i in (1, 2):                                   # line 167, before RANDOMIZE
            self.income[i] = self.cash[i]
            self.cash[i] = cint(f32(self.cash[i] + f32(50 * self.rnd())))
        self._unionplus()                                  # line 204
        self._load_cities()                                # lines 206-217
        self.topbar()                                      # menu0 draws the topbar before turn 1

    def randomize(self, seed: float) -> None:
        """Line 219, RANDOMIZE TIMER: the episode seed stands in for TIMER."""
        self.dice.randomize(seed)

    def _unionplus(self) -> None:
        """Lines 749-752."""
        self.usadv = 120 * self.difficult
        if self.player == 2:
            self.usadv = 50 * self.difficult
        if self.realism > 0:
            self.usadv = cint(f32(.7 * self.usadv))

    def _filer_load(self) -> None:
        """SUB filer CASE 1, lines 1131-1188 (cws.cfg is replaced by Settings)."""
        lead = Reader(DATA_DIR / self.map_files.leaders)
        for i in range(1, 41):
            self.lname[i] = lead.take()
            self.rating[i] = lead.int()
        ini = Reader(DATA_DIR / self.map_files.ini)
        for _ in range(3 + 12):
            ini.take()                                     # force$ and month$ names
        self.month, self.year = ini.int(), ini.int()
        for i in range(1, 7):
            self.vicflag[i] = ini.int()
        self.vicflag[3] = cint(f32(.4 * self.vicflag[3]))   # line 1153
        for base in (0, 20):                               # Union then Rebel armies
            count = ini.int()
            for i in range(base + 1, base + count + 1):
                self.armyloc[i] = ini.int()
                self.armysize[i] = ini.int()
                self.armyexper[i] = ini.int()
                self.supply[i] = ini.int()
                self.occupied[self.armyloc[i]] = i
                self.armyname[i] = self.lname[i]
                self.armylead[i] = self.rating[i]
                self.lname[i] = ""
        self.cash[1], self.cash[2] = ini.int(), ini.int()
        self.ATKFAC, self.DEFAC, self.TCR = ini.int(), ini.int(), ini.int()
        for _ in range(4):
            ini.take()                                     # fleets: navies are out of scope
        self.capcity[1], self.capcity[2] = ini.int(), ini.int()

    def _load_cities(self) -> None:
        grd = Reader(DATA_DIR / self.map_files.cities)
        self.vptotal = self.usadv + 200                    # line 208
        for i in range(1, 41):
            grd.take()
            self.cityx[i], self.cityy[i] = grd.int(), grd.int()
            self.city[i] = grd.take()
            self.cityp[i], self.cityv[i] = grd.int(), grd.int()
            self.cityo[i] = self.cityp[i]
            self.occupy(i)
            for j in range(1, 8):
                self.matrix[i][j] = grd.int()
            self.fort[i] = grd.int()
            x = self.cityp[i]
            if x > 0:                                      # lines 213-214
                self.control[x] += 1
                self.victory[x] += self.cityv[i]
                self.cash[x] += self.cityv[i]
            self.vptotal += self.cityv[i]

    # ------------------------------------------------------- small helpers
    def occupy(self, x: int) -> None:
        """SUB occupy, line 3342: the lowest-numbered army in city x."""
        self.occupied[x] = 0
        for i in range(1, 41):
            if self.armyloc[i] == x:
                self.occupied[x] = i
                return

    def cutoff(self, who: int, target: int) -> int:
        """SUB cutoff, line 1121: neighbours of target that `who` owns."""
        a = 0
        for j in range(1, 7):
            y = self.matrix[target][j]
            if y > 0 and self.cityp[y] == who:
                a += 1
        return a

    def neighbours(self, c: int) -> list[int]:
        return [self.matrix[c][j] for j in range(1, 7) if self.matrix[c][j] > 0]

    def is_port(self, c: int) -> bool:
        return self.matrix[c][7] == 99

    def normal(self, xbar: int, vary: int) -> int:
        """SUB normal, line 1948: twelve uniform rolls, centred."""
        pct = 0.0
        for _ in range(12):
            pct = f32(pct + self.rnd())
        pct = f32(pct - 5.5)
        return cint(f32(xbar + pct * math.sqrt(vary)))     # SQR returns a double (qbmath.h func_sqr)

    # ---------------------------------------------------- player commands
    # Each returns the text the original prints at the bottom of the screen.

    def recruit_open(self, who: int) -> list[int]:
        """SUB recruit, lines 2074-2100: roll the cities offered this turn.

        For the human side the list is kept in rcity/rflag for the rest of
        the turn (lines 2078 and 2099). An empty roll is not kept (line 2098
        exits before 2099), so the human may open Troops again.
        """
        if self.cash[who] < 100:
            return []
        if who == self.side and self.rflag > 0:
            return self._sorted_by_name(self.rcity)
        size, chosen = 0, []
        mx = 4
        if self.rnd() > S(.8):
            mx -= 1
        if self.difficult < 3:
            mx += 1
        for i in range(1, 41):
            if self.control[who] > 0:
                pct = f32(.6 * mx / self.control[who])
            else:
                pct = S(.3)
            if size == 0 and i > 20:
                pct = S(.3)
            if size < 2 and i > 30:
                pct = S(.3)
            if self.occupied[i] > 0 and self.cityp[i] == who:
                pct = S(.4)
            roll = self.rnd()                              # consumed for every city
            if roll < pct and self.cityp[i] == who:
                if self.realism > 0 and self.cityo[i] == 3 - who:
                    continue
                size += 1
                chosen.append(i)
                if size > mx - 1:
                    break
        if size == 0:
            return []
        if who == self.side and self.rflag == 0:
            self.rcity, self.rflag = list(chosen), size
        return self._sorted_by_name(chosen)

    def _sorted_by_name(self, cities: list[int]) -> list[int]:
        """SUB bubble, line 2684: a stable sort of menu text."""
        return sorted(cities, key=lambda c: self.city[c])

    def commander(self, who: int) -> int:
        """SUB commander, line 2887: a free slot with a leader, else a generic one."""
        slots = starfin(who)
        for i in slots:
            if self.armyloc[i] == 0 and self.lname[i] != "":
                return i
        for i in slots:
            if self.armyloc[i] == 0:
                self.lname[i] = roman(i)
                self.rating[i] = cint(f32(1 + f32(8 * self.rnd())))
                return i
        return 0

    def levy(self, who: int, target: int) -> str:
        """One pass of recruit's levy loop, lines 2111-2145: one city, $100."""
        self.occupy(target)
        if self.occupied[target] > 0:
            return self._add_troops(who, self.occupied[target], target)
        empty = self.commander(who)
        if empty == 0:
            return f"No more {FORCE[who]} commanders available"
        self.armyloc[empty] = target
        self._playb(empty)
        return self.newarmy(who, empty, target)

    def _playb(self, empty: int) -> None:
        """Lines 2174-2177 (no effect at Balanced difficulty)."""
        if self.side == 1 and self.difficult < 3:
            self.armysize[empty] += 15 - 5 * self.difficult
        if self.side == 2 and self.difficult > 3:
            self.armysize[empty] += 5 * self.difficult - 15

    def _add_troops(self, who: int, i: int, target: int) -> str:
        """Label add2, lines 2125-2145."""
        x, note = 45, ""
        if self.realism > 0:
            x = 2 * self.cityv[self.armyloc[i]] + 20
            if self.cutoff(who, target) < 1:
                x, note = idiv(x, 3), " ISOLATED !"
        self.armysize[i] += x
        self._playb(0)
        self.cash[who] -= 100
        text = f"Army {i} {self.armyname[i]} in {self.city[self.armyloc[i]]} strength increased to {self.armysize[i]}00{note}"
        self.say("reinforce", text, side=who, army=i, city=target, added=x)
        return text

    def newarmy(self, who: int, empty: int, target: int) -> str:
        """SUB newarmy, line 1889."""
        self.supply[empty] = cint(f32(3 + f32(5 * self.rnd())))
        if who == 1:
            self.supply[empty] += 2
        self.armyexper[empty] = 2 if who == 2 else 1
        self.armylead[empty] = self.rating[empty]
        self.armyname[empty] = self.lname[empty]
        self.lname[empty] = ""
        x = 70
        if self.realism > 0:
            x = 3 * self.cityv[target] + 33
        if self.cutoff(who, target) < 1:
            x = idiv(x, 3)
        self.occupied[target] = empty
        self.armysize[empty] = x
        self.cash[who] -= 100
        self.armyloc[empty] = target
        self.armymove[empty] = -1
        text = f"Placing NEW army {empty} {self.armyname[empty]} in {self.city[target]} Size = {x}00"
        self.say("new_army", text, side=who, army=empty, city=target, size=x)
        return text

    def order_move(self, index: int, dest: int) -> str:
        """SUB armies, lines 797-822: give an army its destination."""
        self.armymove[index] = dest
        return f"Army {index} {self.armyname[index]} is moving from {self.city[self.armyloc[index]]} to {self.city[dest]}"

    def january_blocked(self, who: int, dest: int) -> bool:
        """Line 814: no campaigns into another side's city in January."""
        return self.month < 3 and self.jancam == 0 and self.cityp[dest] != who

    def cancel(self, index: int) -> str:
        """SUB cancel, line 2697."""
        dest = self.armymove[index]
        self.armymove[index] = 0
        return f"{self.armyname[index]} has cancelled move to {self.city[dest]}"

    def fortify(self, who: int, target: int, refresh: bool = True) -> str:
        """SUB fortify, lines 1295-1329 (cost 200, maximum level 2).

        The human menu re-reads the occupant (line 1314); smarts uses the
        stored pointer (line 2246), so it passes refresh=False.
        """
        if refresh:
            self.occupy(target)
        x = self.occupied[target]
        self.fort[target] += 1
        self.cash[who] -= 200
        self.armymove[x] = -1
        text = f"{self.city[target]} fortifications increased to {self.fort[target]}"
        self.say("fortify", text, side=who, city=target, level=self.fort[target])
        return text

    def resupply_amount(self, index: int) -> int:
        """SUB resupply, lines 3602-3611: how much supply would be bought."""
        who = side_of(index)
        if self.realism > 0 and self.cutoff(who, self.armyloc[index]) < 1:
            return 0
        x = 0
        if self.armysize[index] > 0:
            x = cint(f32(self.cash[who] / self.armysize[index] * 10))
        y = x + self.supply[index]
        if y > 5:
            x = 5 - self.supply[index]
        return x

    def resupply(self, index: int) -> str:
        who = side_of(index)
        if self.realism > 0 and self.cutoff(who, self.armyloc[index]) < 1:
            return f"{FORCE[who]} army in {self.city[self.armyloc[index]]} is CUT OFF !"
        x = self.resupply_amount(index)
        if x < 1:
            text = f"Not enough funds in the Treasury to supply {self.armyname[index]}"
        else:
            self.supply[index] += x
            self.cash[who] = cint(f32(self.cash[who] - .1 * x * self.armysize[index]))
            text = f"{self.armyname[index]} has received supplies"
            self.say("supply", text, side=who, army=index, amount=x)
        if self.cash[who] < 0:
            self.cash[who] = 0
        return text

    def drill(self, index: int) -> str:
        """Commands > Army Drill, lines 459-469."""
        self.armyexper[index] += 1
        self.armymove[index] = -1
        return f"{self.armyname[index]} has drilled to reach experience level {self.armyexper[index]}"

    def combine_cities(self, who: int) -> list[int]:
        """SUB combine, lines 1043-1049: cities with a second idle army."""
        out = []
        for i in range(1, 41):
            if self.cityp[i] == who and self.occupied[i] > 0:
                for j in starfin(who):
                    if self.armyloc[j] == i and self.occupied[i] != j and self.armymove[j] == 0:
                        out.append(i)
                        break
        return self._sorted_by_name(out)

    def combine(self, who: int, target: int) -> str:
        """SUB combine, label join, lines 1058-1118."""
        self.armysize[0] = self.armylead[0] = self.armyexper[0] = 0
        self.armyloc[0] = target
        self.armyname[0] = ""
        self.supply[0] = self.armymove[0] = 0
        best, x, spin = 0, 0, 0
        notes = []
        for j in starfin(who):
            if self.armymove[j] != 0 or self.armyloc[j] != target or self.armysize[j] == 0:
                continue
            if self.armysize[0] + self.armysize[j] > 1250:
                notes.append(f"Cannot combine {self.armyname[j]}... TOO LARGE")
                continue
            if self.armylead[j] > x:
                x = self.armylead[j]
                self.armyname[0] = self.armyname[j]
                self.armylead[0] = self.armylead[j]
                best = j
            self.armysize[0] += self.armysize[j]
            if self.armysize[0] < 1:
                continue
            pct = f32(self.armysize[j] / self.armysize[0])
            spin += 1
            self.armyexper[0] = cint(f32(f32(f32(1 - pct) * self.armyexper[0]) + f32(pct * self.armyexper[j])))
            self.supply[0] += self.supply[j]
            if self.supply[0] > 10:
                self.supply[0] = 10
            self.armysize[j] = self.armyloc[j] = self.armyexper[j] = self.armymove[j] = 0
            self.lname[j] = self.armyname[j]
            self.armylead[j] = self.supply[j] = 0
            self.armyname[j] = ""
        if spin == 0:
            if who != self.side:
                return ""
            return f"No valid armies to combine at this time in {self.city[target]}"
        self.armysize[best] = self.armysize[0]
        self.armylead[best] = self.armylead[0]
        self.armyexper[best] = self.armyexper[0]
        self.supply[best] = self.supply[0]
        self.armyloc[best] = target
        self.armyname[best] = self.armyname[0]
        self.lname[best] = ""
        if spin > 1:
            self.armymove[best] = -1
            text = f"New army {best} of {self.armysize[best]}00 is commanded by {self.armyname[best]}"
            self.say("combine", f"Combining {FORCE[who]} armies in {self.city[target]}. {text}",
                     side=who, army=best, city=target)
        else:
            text = "Only 1 eligible army -- cannot combine at this time"
        self.occupied[target] = best
        return "; ".join(notes + [text])

    # ------------------------------------------------------------ the turn
    def end_turn(self) -> None:
        """END TURN (lines 351-354) then newmonth (lines 251-283)."""
        self.newmonth()
        self.victor()                                      # line 278
        if self.result is None:
            self.topbar()                                  # back at menu0, line 287

    def newmonth(self) -> None:
        """Everything END TURN does before SUB victor."""
        self.rflag = 0
        self.rcity = []
        from . import smarts
        self.say("turn", f"--------> EVENTS FOR {MONTHS[self.month]} {self.year} --------")
        smarts.smarts(self)                                # tupdate line 2395
        self._tupdate_resolve()
        self.control[1] = self.control[2] = 0              # lines 256-273
        for i in (1, 2):
            self.income[i] = 0
            self.cash[i] = min(max(self.cash[i], 0), 19999)
        if self.player == 1 and self.side == 2:
            self.income[1] += self.usadv
        for i in range(1, 41):
            if self.cityp[i] > 0:
                x = self.cityp[i]
                self.control[x] += 1
                self.income[x] += self.cityv[i]
            self.armymove[i] = 0
        for i in (1, 2):
            if self.capcity[i] > 0:
                self.income[i] += 100
            self.cash[i] += self.income[i]
        self.vptotal = self.income[1] + self.income[2]
        self.turn += 1

    def topbar(self) -> None:
        """SUB topbar, line 3970: the main menu clamps negative victory points."""
        for i in (1, 2):
            if self.victory[i] < 0:
                self.victory[i] = 0

    def _initiative(self) -> list[int]:
        """tupdate lines 2411-2432: who moves first."""
        brray = [999] * 41
        for i in range(1, 41):
            brray[i] = 999
            if self.armymove[i] < 0:
                self.armymove[i] = 0
            if self.armyloc[i] > 0 and self.armymove[i] > 0:
                brray[i] = qint(f32(4 + f32(4 * self.rnd()))) * 100 + i
            if self.supply[i] < 1 and self.armymove[i] > 0:
                brray[i] = 900 + i
            # SELECT CASE armysize(i): only the first case (> 400) can match.
            if self.armysize[i] > 400 and brray[i] < 900:
                brray[i] += 100
            roll = self.rnd()                              # consumed for every slot
            if brray[i] != 999 and self.armylead[i] > f32(10 * roll):
                brray[i] -= 100 * idiv(self.armylead[i], 2)
                if brray[i] < 100:
                    brray[i] = 100 + i
        order = sorted(brray[1:])
        return [b - 100 * qint(f32(b / 100)) for b in order if b != 999]

    def _tupdate_resolve(self) -> None:
        """tupdate lines 2434-2648: moves, battles, iterate, victory points."""
        # win and lose are tupdate locals: a skipped battle reuses the last pair.
        self._win = self._lose = 0
        from . import smarts
        for active in self._initiative():
            s = side_of(active)
            if smarts.PROBE is not None:
                smarts.PROBE.append(f"GO {active} {self.armymove[active]}")
            if self.armymove[active] < 1:
                continue
            self.supply[active] -= 1
            if self.supply[active] < 0:
                self.supply[active] = 0
                self.say("supply_out", f"{self.armyname[active]} is out of supplies !", army=active)
            origin = self.armyloc[active]
            self._animate_leave(active)
            target = self.armymove[active]
            self._fought = 0
            self.say("move", f"{self.armyname[active]} is moving to {self.city[target]}",
                     side=s, army=active, frm=origin, to=target)
            occ = self.occupied[target]
            hostile = occ > 0 and not ((s == 1 and occ < 21) or (s == 2 and occ > 20))
            outcome = self._attack(active, origin, target, s) if hostile else "arrive"
            if outcome == "arrive":
                self._arrive(active, target, s, self._fought)
        self.iterate()
        self._victory_points()

    def _attack(self, active: int, origin: int, target: int, s: int) -> str:
        """Labels enemy, kickbutt, deadmeat, crushed and holdon, lines 2460-2553.

        Returns "arrive" (label easy), "withdrew" or "destroyed".
        """
        self._fought = 0
        while True:
            defend = self.occupied[target]
            if self.armysize[defend] > 0:
                self._win, self._lose = self.battle(active, defend)
                self._fought = 1
            win, lose = self._win, self._lose
            if self.armyexper[win] < 10:
                self.armyexper[win] += 1
            if self.armysize[lose] < 2:                    # crushed, line 2468
                self.say("crushed", f"{self.armyname[lose]}'s army is crushed in {self.city[target]}",
                         army=lose, city=target)
                self._eliminate(lose, active, s)
                if self.armyloc[active] == 0:
                    return "destroyed"
            elif win != active:                            # attacker withdraws, 2477-2494
                self.armyloc[active] = target              # animate(active, 1) re-reads the target
                self._animate_leave(active)
                self.armyloc[active] = origin
                self.occupied[origin] = active
                self.armymove[active] = -2
                self.say("withdraw", f"{self.armyname[active]} withdrew to {self.city[origin]}",
                         army=active, city=origin)
                if f32(11 * self.rnd()) > self.armylead[defend] and self.armymove[defend] > 0:
                    self.armymove[defend] = -2
                return "withdrew"
            else:                                          # defender retreats, 2496-2530
                move2 = self._retreat_destination(defend, target, s)
                if move2 == 0:                             # deadmeat
                    self.say("surrender", f"{self.armyname[defend]} surrenders to {self.armyname[active]} in {self.city[target]}",
                             army=defend, city=target)
                    self._eliminate(defend, active, s)
                else:
                    self.armyloc[defend] = move2
                    self.occupied[move2] = defend
                    self.armymove[defend] = -2
                    self.say("retreat", f"{self.armyname[defend]} is withdrawing to {self.city[move2]}",
                             army=defend, city=move2)
            self.occupy(target)                            # holdon, line 2551
            if self.occupied[target] == 0:
                return "arrive"
            self.say("defenders", f"There are still defenders in {self.city[target]}", city=target)

    def _animate_leave(self, index: int) -> None:
        """SUB animate, lines 772-778: the city left behind re-reads its occupant."""
        frm = self.armyloc[index]
        self.armyloc[index] = 0
        self.occupy(frm)
        self.armyloc[index] = frm

    def _retreat_destination(self, defend: int, target: int, s: int) -> int:
        """SUB retreat (line 3617) then the automatic choice, lines 2502-2514.

        The human's own retreat menu (more than one friendly neighbour) is
        answered with ESC, which falls through to the automatic rule: design
        choice, see the rule map.
        """
        who = side_of(defend)
        options = [c for c in self.neighbours(self.armyloc[defend]) if self.cityp[c] == who]
        if who == self.side and len(options) == 1:
            return options[0]
        best = flee = 0
        for i in range(1, 7):
            x = self.matrix[target][i]
            if x > 0 and self.cityp[x] == 3 - s and self.cityv[x] > best:
                if best == 0:
                    flee, best = i, self.cityv[x]
                elif self.occupied[x] == 0:
                    flee, best = i, self.cityv[x]
        return self.matrix[target][flee] if flee else 0

    def _eliminate(self, index: int, active: int, s: int) -> None:
        """Labels deadmeat/crushed, lines 2532-2548."""
        self.victory[3 - s] += 25
        self.armyloc[index] = 0
        self.lname[index] = self.armyname[index] = ""
        self.armysize[index] = self.armylead[index] = 0
        self.armyexper[index] = self.armymove[index] = self.supply[index] = 0
        self.supply[active] += self.supply[index]
        if self.supply[active] > 10:
            self.supply[active] = 10

    def _arrive(self, active: int, target: int, s: int, flag: int) -> None:
        """Labels easy and horde, lines 2555-2590."""
        self.armyloc[active] = target
        self.armymove[active] = -2
        self.occupy(target)
        if self.cityp[target] != s:
            c = target
            # A human capture of an unopposed fortified city asks "Raze ?";
            # the interface always answers No (design). The computer razes
            # southern forts it takes without a battle (lines 2575-2586).
            if self.player == 1 and s != self.side and self.fort[c] > 0 and flag == 0:
                if self.realism > 0 and self.cityy[c] > 150:
                    self.fort[c] = 0
                    self.say("raze", f"{self.armyname[active]} has destroyed the forts at {self.city[c]}", city=c)
            self.capture(active, c, s, flag)
        while self.supply[active] < 10:
            self.supply[active] += 1
            if not self.rnd() > S(.8):
                break

    def capture(self, active: int, c: int, s: int, flag: int) -> None:
        """SUB capture, line 2827."""
        self.cityp[c] = s
        self.victory[s] += self.cityv[c]
        self.say("capture", f"{self.armyname[active]} has captured {self.city[c]}", side=s, city=c)
        if c == self.capcity[3 - s]:
            self.victory[s] += 100
            self.victory[3 - s] -= 100
            self.say("capital", f"{FORCE[3 - s]} CAPITAL captured !", side=s, city=c)
            self.capcity[3 - s] = 0
        if self.fort[c] > 0 and flag > 0:
            self.fort[c] -= 1

    def battle(self, attack: int, defend: int) -> tuple[int, int]:
        """SUB battle, lines 845-1036."""
        A = self.armysize
        if A[defend] < 1:
            A[defend] = 1
        if A[attack] < 1:
            A[attack] = 1
        tcr = self.TCR
        ratio = f32(A[attack] / A[defend])                 # comparisons cast both sides to float

        x = cint(f32(.01 * A[attack]))
        x = min(x, tcr)
        if ratio > S(.2):
            x = cint(f32(x + .3 * self.armylead[attack] + .3 * self.armyexper[attack]))
            x = min(x, tcr)
        if self.armyexper[attack] > 8:
            x = min(x + 1, tcr)
        if A[attack] < 15:
            x = min(cint(f32(.5 * x)), tcr)
        if ratio <= S(.5):
            x = max(x - 2, 1)
        if ratio > 3:
            x = min(x + 2, tcr)
        if ratio > 10:
            x = tcr
        if ratio <= S(.2):
            x = 1
        if self.supply[attack] < 1:
            x = cint(f32(.5 * x))
        if x < 1:
            x = 1
        if attack < 21 and self.side == 2 and self.difficult > 3:
            x += 2 * self.difficult - 6
        if attack > 20 and self.side == 1 and self.difficult < 3:
            x += 6 - 2 * self.difficult
        x = min(x, tcr)

        x1 = cint(f32(.013 * A[defend] + 1))
        if self.realism == 1:
            x1 = cint(f32(.02 * A[defend] + 2))
            if x1 > 20:
                x1 = 20
        if f32(A[defend] / A[attack]) > S(.2):
            x1 = cint(f32(x1 + .3 * self.armylead[defend] + .3 * self.armyexper[defend]))
            x1 = min(x1, tcr)
        if self.armyexper[defend] > 8:
            x1 = min(x1 + 1, tcr)
        if A[defend] < 15:
            x1 = cint(f32(.5 * x1))
        r = f32(A[defend] / A[attack])                     # R! is SINGLE
        if r > 10:
            x1 = tcr
        elif r > S(1.5):
            x1 += 2
        elif r < S(.5):                                    # CASE IS < .2 is unreachable
            x1 = cint(f32(.8 * x1))
        x1 = min(max(x1, 1), tcr)
        if self.supply[defend] < 1:
            x1 = cint(f32(.5 * x1))
        if x1 < 1:
            x1 = 1
        if defend < 21 and self.side == 2 and self.difficult > 3:
            x1 += 2 * self.difficult - 6
        if defend > 20 and self.side == 1 and self.difficult < 3:
            x1 += 6 - 2 * self.difficult
        fort = self.fort[self.armyloc[defend]]
        if self.armymove[defend] == 0:
            x1 = x1 * (1 + fort)
        x1 = min(x1, tcr)

        scale = max(x, x1) + 1
        odds = f32(x / (x + x1))
        shown = max(qint(f32(100 * odds)), 1)
        for i in (1, 2):                                   # line 947: armies 1 and 2, as written
            if self.supply[i] > 0:
                self.supply[i] -= 1
        while True:                                        # label grapple
            star = cint(f32(scale * self.rnd()))
            fin = cint(f32(scale * self.rnd()))
            hit = 1 if star <= x else 0
            hit1 = 1 if fin <= x1 else 0
            if hit != hit1:
                break
        win, lose = (attack, defend) if hit == 1 else (defend, attack)
        from . import smarts
        if smarts.PROBE is not None:
            smarts.PROBE.append(f"BT {attack} {defend} {x} {x1} {win}")

        pct = f32(.01 * self.DEFAC - .03 * fort)
        if win == attack:
            pct = f32(1.3 * pct)
        if A[defend] > 300:                                # CASE IS > 800 is unreachable
            pct = f32(.9 * pct)
        xbar = cint(f32(A[attack] * pct))
        vary = cint(f32(xbar * f32(1 - pct)))
        killd = self.normal(xbar, vary)

        pct = f32(.01 * self.ATKFAC + .02 * fort)
        if win == defend:
            pct = f32(1.5 * pct)
        if A[attack] > 300:
            pct = f32(.9 * pct)
        xbar = cint(f32(A[defend] * pct))
        vary = cint(f32(xbar * f32(1 - pct)))
        killa = self.normal(xbar, vary)

        killa = cint(f32(.8 * killa + .2 * killd))
        if killa < 1:
            killa = 1
        killd = cint(f32(.8 * killd + .2 * killa))
        if killd < 1:
            killd = 1
        if killa > 9 * killd:
            killa = 9 * killd
        if killd > 5 * killa:
            killd = 5 * killa
        if killa >= A[attack]:
            killa = A[attack] - 1
        if killd >= A[defend]:
            killd = A[defend] - 1

        where = self.armyloc[defend]
        report = {
            "city": where, "attacker": attack, "defender": defend,
            "attacker_size": A[attack], "defender_size": A[defend],
            "attack": x, "defend": x1, "odds_percent": shown,
            "attacker_loss": killa, "defender_loss": killd,
            "winner": win, "loser": lose,
        }
        A[attack] -= killa
        A[defend] -= killd
        if A[defend] < 1:
            A[defend] = 1
        s = 2 if attack > 2 else 1                         # line 1028, as written
        self.casualty[s] += killa
        self.casualty[3 - s] += killd
        s = 2 if win > 20 else 1
        self.batwon[s] += 1
        self.victory[s] += 1
        # The battle panel (lines 875, 921, 930), the result line (967) and the loss line (1003-1009).
        self.say("battle", f"{self.armyname[attack]} attacks {self.armyname[defend]} in {self.city[where]}: "
                           f"{self.armyname[win]} wins (attack {x} vs defend {x1}, odds {shown}%). Attacker lost "
                           f"{killa}00 of {report['attacker_size']}00, defender lost {killd}00 of "
                           f"{report['defender_size']}00", **report)
        return win, lose

    def iterate(self) -> None:
        """SUB iterate, lines 1406-1441: calendar, supply and attrition."""
        self.month += 2
        if self.month > 12:
            self.month = 1
            self.year += 1
        s = 1
        for i in range(1, 41):
            if self.armyloc[i] < 1:
                continue
            if i > 20:
                s = 2
            if self.cash[s] >= f32(.2 * self.armysize[i]):
                a = 1
                if self.realism > 0:
                    a = self.cutoff(s, self.armyloc[i])
                if a > 0:
                    self.supply[i] += 1
                    self.cash[s] = cint(f32(self.cash[s] - .2 * self.armysize[i]))
            if (self.month < 7 or self.month > 10) and self.matrix[self.armyloc[i]][7] < 99:
                self.supply[i] -= 1
            if self.supply[i] < 1:
                self.supply[i] = 0
                self.say("supply_out", f"{self.armyname[i]} is out of supplies", army=i)
                if self.rnd() > S(.8) and self.armysize[i] > 50:
                    self.armysize[i] = cint(f32(.9 * self.armysize[i]))
        y = 0
        for i in range(1, 21):
            y = cint(f32(y + .1 * self.armysize[i]))
        x = 0
        for i in range(21, 41):
            x = cint(f32(x + .1 * self.armysize[i]))
        if self.side == 2 and x > 0:
            self.aggress = f32(y / x)
        else:
            self.aggress = 1.0
        if self.side == 1 and y > 0:
            self.aggress = f32(x / y)
        elif self.side == 1:
            self.aggress = 1.0

    def _victory_points(self) -> None:
        """tupdate lines 2641-2648."""
        v, inc, ctl = self.victory, self.income, self.control
        v[1] = cint(f32(.8 * v[1] + .3 * (inc[1] + ctl[1])))
        if ctl[1] > 29:
            v[1] += 50
            if ctl[1] > 34:
                v[1] += 100
        if self.side == 2 and ctl[1] < 11:
            self.aggress = f32(self.aggress + .7)
        if v[1] < 1:
            v[1] = 0
        v[2] = cint(f32(.8 * v[2] + .3 * (inc[2] + ctl[2])))
        if ctl[2] > 29:
            v[2] += 50
            if ctl[2] > 34:
                v[2] = v[1] + 100                          # as written: victory(1)
        if self.side == 1 and ctl[2] < 11:
            self.aggress = f32(self.aggress + .7)

    def strength(self, who: int) -> int:
        return sum(self.armysize[j] for j in starfin(who) if self.armyloc[j] > 0)

    def victor(self) -> None:
        """SUB victor, lines 4385-4512. The end-game prompt is answered Yes."""
        x, y = self.strength(1), self.strength(2)
        for i in (1, 2):
            j = 0
            if (i == 1 and y == 0) or (i == 2 and x == 0):
                j = 7
                self.victory[i] += 300
            elif self.year >= self.vicflag[2] and self.month >= self.vicflag[1] and self.vicflag[2] > 0:
                j = 2
            elif self.control[i] >= self.vicflag[3] and self.vicflag[3] > 0:
                j = 3
            elif (self.vicflag[4] > 0 and
                  f32(self.income[i] / (self.income[1] + self.income[2])) >= f32(.01 * self.vicflag[4])):
                j = 4
            elif self.vicflag[5] > 0 and self.capcity[3 - i] == 0 and self.capcity[i] > 0:
                j = 5
            elif self.vicflag[6] > 0:
                if i == 1:
                    if y == 0:
                        j = 7
                    elif f32(x / y) > self.vicflag[6]:
                        j = 6
                else:
                    if x == 0:
                        j = 7
                    elif f32(y / x) > self.vicflag[6]:
                        j = 6
            if j == 0:
                continue
            if j == 7:
                self.victory[i] += 100
            winner = REBEL if j == 2 else i
            if j == 2:                                     # "Confederates will win a technical victory"
                for k in (1, 2):
                    self.victory[k] = cint(f32(.7 * self.victory[k]))
            self.result = {
                "winner": winner, "condition": j, "reason": CONDITIONS[j],
                "checked_for": i, "victory": [self.victory[1], self.victory[2]],
            }
            self.say("game_over", f"{FORCE[winner].upper()} VICTORY: {CONDITIONS[j]}", **self.result)
            return


def roman(target: int) -> str:
    """SUB roman, line 3639: generic leader names."""
    name = "Union " if target <= 20 else "Rebel "
    if target > 20:
        target -= 20
    if target > 10:
        name += "X"
        target -= 10
    if target < 4:
        name += "I" * target
    elif target == 4:
        name += "IV"
    elif target <= 8:
        name += "V" + "I" * (target - 5)
    elif target == 9:
        name += "IX"
    elif target == 10:
        name += "X"
    return name
