"""The machine-playable interface: the midterm brief's five operations.

The episode holds the authoritative Game. A player gets copies of
observations and a list of action strings, never the Game. In a live run the
episode lives in a separate process (cws/server.py) and the player's side
of the runner holds only cws/client.py's PlayerPort.

What the Union may know is what the original shows a human Union player
(evidence in docs/rule-source-map.md, "Information boundary"): every city's
owner, value and forts (map and City Report, lines 3480-3500); both sides'
cash, income and victory points (City Report line 3496, topbar line 3973,
Army Report line 3437); its own armies in full (Army Report line 3460); and
each enemy army's number, name, size and city (Army Report line 3459 prints
no more for the enemy), plus whether it is out of supply (the map's "S"
glyph, placearmy line 1961). Hidden: enemy leader ratings, experience,
supply levels and orders; the dice; the opponent's routines.

Action vocabulary (design, see the rule map): one string per menu choice
the original offers, listed only when it would change the game now.
"""

from .engine import FORCE, MONTHS, UNION, Event, Game, starfin
from .qb import cint, f32
from .scenarios import SCENARIOS

PLAYER_ID = "union"
# "plan" stands for the map arrows smarts draws for each computer order before resolution
# (icon kinds 1 and 9, lines 2334-2335); the original prints its text only above Fast display speed.
VISIBLE_EVENTS = {
    "turn", "plan", "move", "battle", "withdraw", "retreat", "surrender", "crushed",
    "capture", "capital", "raze", "defenders", "supply_out", "new_army", "reinforce",
    "fortify", "combine", "supply", "game_over",
}


class CivilWarEpisode:
    def __init__(self, scenario: str = "standard", max_steps: int = 600) -> None:
        if scenario not in SCENARIOS:
            raise ValueError(f"unknown scenario {scenario!r}; choose from {sorted(SCENARIOS)}")
        self.scenario = SCENARIOS[scenario]
        self.max_steps = max_steps
        self.reset(None)

    # ------------------------------------------------------------- runner
    def reset(self, seed: float | None = None) -> dict:
        self.seed = seed
        self._game = Game(self.scenario.map_files, self.scenario.settings)
        if seed is not None:
            self._game.randomize(seed)
        self.steps = 0
        self.invalid_actions = 0
        self.trace: list[dict] = []
        self._report: list[dict] = []
        self._messages: list[str] = []
        self._log_mark = len(self._game.log)
        return self.observe(PLAYER_ID)

    def outcome(self) -> dict:
        g = self._game
        result = {"steps": self.steps, "invalid_actions": self.invalid_actions,
                  "turn": g.turn, "date": f"{MONTHS[g.month]} {g.year}",
                  "victory_points": {"Union": g.victory[1], "Rebel": g.victory[2]},
                  "score": union_share(g), "cities": {"Union": g.control[1], "Rebel": g.control[2]}}
        if g.result:
            winner = FORCE[g.result["winner"]]
            result.update(status="terminal", winner=winner,
                          reason=f"{winner} victory: {g.result['reason']}")
        elif self.steps >= self.max_steps:
            result.update(status="terminal", winner=None, reason="step limit")
        else:
            result.update(status="ongoing", winner=None, reason="")
        return result

    # ------------------------------------------------------------- player
    def observe(self, player_id: str) -> dict:
        _check_player(player_id)
        g = self._game
        me, foe = UNION, 3 - UNION
        cities = [{
            "id": c, "name": g.city[c], "owner": FORCE[g.cityp[c]], "value": g.cityv[c],
            "fort": g.fort[c], "port": g.is_port(c), "neighbors": g.neighbours(c),
            "x": g.cityx[c], "y": g.cityy[c],
            "capital_of": next((FORCE[s] for s in (1, 2) if g.capcity[s] == c), None),
        } for c in range(1, 41)]
        own = [{
            "id": i, "name": g.armyname[i], "men": g.armysize[i] * 100, "city": g.armyloc[i],
            "city_name": g.city[g.armyloc[i]], "leader": g.armylead[i],
            "experience": g.armyexper[i], "supply": g.supply[i], "order": _order(g, i),
        } for i in starfin(me) if g.armyloc[i] > 0]
        enemy = [{
            "id": i, "name": g.armyname[i], "men": g.armysize[i] * 100, "city": g.armyloc[i],
            "city_name": g.city[g.armyloc[i]], "out_of_supply": g.supply[i] < 1,
        } for i in starfin(foe) if g.armyloc[i] > 0]
        deadline = (g.vicflag[1], g.vicflag[2])
        return {
            "you": FORCE[me], "opponent": f"{FORCE[foe]} (the original computer player)",
            "date": f"{MONTHS[g.month]} {g.year}", "turn": g.turn,
            "turns_left": _turns_left(g.month, g.year, *deadline),
            "treasury": {s: {"cash": g.cash[i], "income": g.income[i], "cities": g.control[i]}
                         for i, s in ((1, "Union"), (2, "Rebel"))},
            "victory_points": {"Union": g.victory[1], "Rebel": g.victory[2],
                               "union_share_percent": union_share(g)},
            "victory_conditions": _conditions(g),
            "victory_rules": {"deadline_month": g.vicflag[1], "deadline_year": g.vicflag[2],
                              "cities": g.vicflag[3], "income_percent": g.vicflag[4],
                              "capital": g.vicflag[5], "strength_ratio": g.vicflag[6]},
            "month_number": g.month,
            "settings": {"realism": bool(g.realism), "january_campaigns": bool(g.jancam),
                         "balance": "Balanced" if g.difficult == 3 else g.difficult,
                         "opponent_aggression": _BOLD[g.bold]},
            "cities": cities,
            "your_armies": own,
            "enemy_armies": enemy,
            "recruiting": {"rolled": g.rflag > 0,
                           "offered": [g.city[c] for c in g._sorted_by_name(g.rcity)] if g.rflag > 0 else []},
            "last_turn_report": list(self._report),
            "this_turn_messages": list(self._messages),
        }

    def legal_actions(self, player_id: str) -> list[str]:
        _check_player(player_id)
        g = self._game
        if self.outcome()["status"] == "terminal":
            return []
        me = UNION
        acts: list[str] = []
        if g.cash[me] >= 100 and g.rflag == 0:
            acts.append("troops")
        if g.rflag > 0 and g.cash[me] >= 100:
            free_slot = any(g.armyloc[k] == 0 for k in starfin(me))
            for c in g._sorted_by_name(g.rcity):
                if free_slot or any(g.armyloc[k] == c for k in starfin(me)):
                    acts.append(f"recruit {g.city[c]}")
        for i in starfin(me):
            if g.armyloc[i] > 0 and g.armymove[i] == 0:
                for c in g.neighbours(g.armyloc[i]):
                    if not g.january_blocked(me, c):
                        acts.append(f"move {i} {g.city[c]}")
        for i in starfin(me):
            if g.armyloc[i] > 0 and g.armymove[i] > 0:
                acts.append(f"cancel {i}")
        if g.cash[me] >= 200:
            seen = set()
            for i in starfin(me):
                c = g.armyloc[i]
                if c > 0 and g.fort[c] < 2 and c not in seen:
                    seen.add(c)
                    acts.append(f"fortify {g.city[c]}")
        for c in g.combine_cities(me):
            if _combine_count(g, me, c) >= 2:
                acts.append(f"join {g.city[c]}")
        for i in starfin(me):
            if g.armyloc[i] > 0 and g.supply[i] <= 1 and g.resupply_amount(i) >= 1:
                acts.append(f"supply {i}")
        for i in starfin(me):
            if (g.armyloc[i] > 0 and g.armymove[i] == 0 and g.armyexper[i] <= 5
                    and g.armyexper[i] < g.armylead[i]):
                acts.append(f"drill {i}")
        acts.append("end turn")
        return acts

    def step(self, player_id: str, action: object) -> dict:
        _check_player(player_id)
        if self.outcome()["status"] == "terminal":
            return {"accepted": False, "text": "The episode is over.", "observation": self.observe(player_id)}
        if not isinstance(action, str):
            action = f"<not text: {type(action).__name__}>"   # a malformed reply is an invalid action
        action = " ".join(action.split())
        self.steps += 1
        legal = {a.lower(): a for a in self.legal_actions(player_id)}
        chosen = legal.get(action.lower())
        if chosen is None:
            self.invalid_actions += 1
            text = "That action is not available now."
        else:
            text = self._apply(chosen)
        self.trace.append({"step": self.steps, "turn": self._game.turn, "action": chosen or action,
                           "accepted": chosen is not None, "text": text})
        return {"accepted": chosen is not None, "text": text, "observation": self.observe(player_id)}

    # ----------------------------------------------------------- internal
    def _apply(self, action: str) -> str:
        g, me = self._game, UNION
        verb, _, rest = action.partition(" ")
        if action == "end turn":
            mark = len(g.log)
            g.end_turn()
            self._report = [_event_dict(e) for e in g.log[mark:] if e.kind in VISIBLE_EVENTS]
            self._messages = []
            return f"Turn resolved. It is now {MONTHS[g.month]} {g.year}."
        if verb == "troops":
            offered = g.recruit_open(me)
            text = ("Recruiting offered in: " + ", ".join(g.city[c] for c in offered)) if offered \
                else "No cities offer recruits this time."
        elif verb == "recruit":
            text = g.levy(me, _city_id(g, rest))
        elif verb == "move":
            army, _, dest = rest.partition(" ")
            text = g.order_move(int(army), _city_id(g, dest))
        elif verb == "cancel":
            text = g.cancel(int(rest))
        elif verb == "fortify":
            text = g.fortify(me, _city_id(g, rest))
        elif verb == "join":
            text = g.combine(me, _city_id(g, rest))
        elif verb == "supply":
            text = g.resupply(int(rest))
        elif verb == "drill":
            text = g.drill(int(rest))
        else:                                              # unreachable: only listed actions arrive
            raise ValueError(action)
        self._messages.append(text)
        return text


_BOLD = {0: "PASSIVE", 1: "TIMID", 2: "CAUTIOUS", 3: "NORMAL", 4: "BOLD", 5: "RECKLESS"}


def union_share(g: Game) -> int:
    """topbar lines 3970-3981: the Union's percentage of all victory points."""
    total = max(g.victory[1], 0) + max(g.victory[2], 0)
    return cint(f32(100 * (max(g.victory[1], 0) / total))) if total > 0 else 0


def _order(g: Game, i: int) -> str:
    m = g.armymove[i]
    if m > 0:
        return f"moving to {g.city[m]}"
    return "resting this turn" if m < 0 else "none"


def _combine_count(g: Game, who: int, target: int) -> int:
    """How many armies SUB combine would merge, respecting its 1,250 cap."""
    total = count = 0
    for j in starfin(who):
        if g.armymove[j] != 0 or g.armyloc[j] != target or g.armysize[j] == 0:
            continue
        if total + g.armysize[j] > 1250:
            continue
        total += g.armysize[j]
        count += 1
    return count


def _city_id(g: Game, name: str) -> int:
    for c in range(1, 41):
        if g.city[c].lower() == name.lower():
            return c
    raise ValueError(name)


def _turns_left(month: int, year: int, end_month: int, end_year: int) -> int:
    n = 0
    while not (year >= end_year and month >= end_month) and n < 200:
        month += 2
        if month > 12:
            month, year = 1, year + 1
        n += 1
    return n


def _conditions(g: Game) -> list[str]:
    v = g.vicflag
    out = [f"time: the Confederacy wins a technical victory in {MONTHS[v[1]]} {v[2]}"]
    if v[3] > 0:
        out.append(f"control {v[3]} of 40 cities")
    if v[4] > 0:
        out.append(f"earn {v[4]}% of total income")
    if v[5] > 0:
        out.append("capture the enemy capital while holding your own")
    if v[6] > 0:
        out.append(f"field more than {v[6]}:1 the enemy's total strength")
    out.append("destroy every enemy army")
    return out


def _event_dict(e: Event) -> dict:
    return {"kind": e.kind, "text": e.text}


def _check_player(player_id: str) -> None:
    if player_id != PLAYER_ID:
        raise ValueError(f"The playing agent is the Union, {PLAYER_ID!r}; the Rebels are the built-in opponent.")
