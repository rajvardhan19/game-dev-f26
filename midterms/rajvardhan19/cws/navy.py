"""Navies: SUB navy (lines 1471-1887), barnacle (836), ships (3799) and commerce raiding.

`navyloc(who)` is a city, 0 for no fleet, or 99 for "at sea raiding commerce".
`fleet$(who)` lists the ships: "W" wooden, appended at the end; "I" ironclad,
added at the front. So losses (barnacle drops the last ship) take wooden ships
first, and a fleet's combat strength is set by its last ship.

`navy(g, who, chx, answers)` keeps the original's control flow: `chx` > 0 is
the computer's mode (1 build, 2 attack, 3 sail, 4 raid, 5 invasion); `chx` = 0
is the human's menu, whose choices arrive as `answers` (menu rows, as the
harness feeds SUB menu). Naval combat's Attack/Retreat menu is answered Attack
for the human, the choice the computer always makes (design, rule map).
"""

from .qb import S, cint, f32, qint

AT_SEA = 99


class MenuExhausted(RuntimeError):
    """The original would wait for a keypress here; the interface never lets it."""


def barnacle(g, who: int) -> None:
    """SUB barnacle, line 836: lose the last ship."""
    g.navysize[who] -= 1
    if g.navysize[who] > 0:
        g.fleet[who] = g.fleet[who][:g.navysize[who]]
    else:
        g.fleet[who] = ""
        g.navyloc[who] = 0
        g.navysize[who] = 0


def ships(g) -> None:
    """SUB ships, line 3799: drawing, plus one rule: no ships means no fleet."""
    for s in (1, 2):
        if g.navysize[s] == 0 or g.navyloc[s] == 0:
            g.navyloc[s] = 0


def sail3(g) -> None:
    """Label sail3, lines 1881-1885: whoever is at sea is raiding."""
    g.commerce = 0
    for k in (1, 2):
        if g.navyloc[k] == AT_SEA:
            g.commerce = k


def ironclads_allowed(g) -> bool:
    """Line 1526: with Realism, no ironclads before March 1862."""
    return not (g.realism > 0 and (g.year < 1862 or (g.year == 1862 and g.month < 3)))


def port_list(g, who: int) -> list[int]:
    """Lines 1552-1554: shipyards for a new fleet (own seaports without the enemy fleet)."""
    return [i for i in range(1, 41)
            if g.matrix[i][7] == 99 and g.cityp[i] == who and g.navyloc[3 - who] != i]


def sail_list(g, who: int) -> list[int]:
    """Lines 1634-1636: every seaport but the one the fleet is in."""
    return [i for i in range(1, 41) if g.matrix[i][7] > 90 and g.navyloc[who] != i]


def name(g, loc: int) -> str:
    return "at sea" if loc == AT_SEA else g.city[loc]


def navy(g, who: int, chx: int, answers=()) -> None:
    from .smarts import void
    queue = list(answers)

    def menu() -> int:
        if not queue:
            raise MenuExhausted("navy menu needs an answer")
        return queue.pop(0)

    side = g.side
    if chx > 0:                                          # lines 1473-1480
        if g.navyloc[who] < 1:
            chx = 1
        else:
            if g.commerce == 3 - who and g.raider > 0:
                chx = 4
            if g.grudge > 0:
                chx = 3
    choose = 0
    state = "ahoy"
    while True:
        if state == "ahoy":                              # lines 1482-1510
            cost = 100
            g.cityp[0] = who                             # as written: the owner of city 0
            if chx == 1 and (g.cash[who] < cost or g.navysize[who] > 9):
                return
            loc = g.navyloc[who]
            if loc != AT_SEA:
                if g.cash[who] < cost or g.navysize[who] > 9 or g.cityp[loc] != who:
                    choose = 23
                if g.cityp[loc] != 3 - who:
                    choose = 22
            else:
                choose = 24
            if loc < 1 and chx == 3:
                chx = 1
            if loc != AT_SEA:
                if who == 1 and g.navysize[who] > 1 and g.cityp[loc] == 0:
                    defend = void(g, g.navyloc[1], side)
                    if chx > 0 and defend < 100:
                        chx = 5
                if g.realism == 0 and who == 2 and g.navysize[who] > 1 and g.cityp[loc] == 0:
                    defend = void(g, g.navyloc[1], side)
                    if chx > 0 and defend < 100:
                        chx = 5
            if chx > 0:
                choose = chx
            else:
                if g.nflag > 0 and choose != 1:
                    return
                if not queue:                            # the human leaves the Ships menu
                    return
                choose = menu()
            state = "anchor"
            continue

        # label anchor: SELECT CASE choose
        if choose == 1:                                  # Build Ship, lines 1514-1578
            if g.cash[who] < cost or g.navyloc[who] == AT_SEA:
                state = "ahoy"
                continue
            if chx == 1 and g.navysize[who] > 9:
                return
            if chx == 0 and g.navysize[who] > 9:
                state = "ahoy"
                continue
            if chx == 0 and g.navyloc[who] > 0:
                if g.cityp[g.navyloc[who]] != who or g.matrix[g.navyloc[who]][7] < 99:
                    state = "ahoy"
                    continue
            roll = g.rnd()                               # line 1523: rolled for every builder
            if chx == 1 and roll < f32(.07 * g.navysize[who]):
                return
            kind = "W"
            if ironclads_allowed(g) and g.cash[who] >= 2 * cost:
                if who == side:
                    choose = menu()                      # Type: 1 Wooden, 2 Ironclad
                    if choose < 1:
                        state = "ahoy"
                        continue
                    if choose == 2:
                        kind, cost = "I", 2 * cost
                else:
                    kind = "I"                           # the computer's ironclad still costs 100
            g.navysize[who] += 1                         # label noiron
            g.fleet[who] = g.fleet[who] + kind if kind == "W" else kind + g.fleet[who]
            if g.navysize[who] > 1:                      # label add2ship
                g.cash[who] -= cost
                g.say("navy", f"{_force(who)} navy increased to {g.navysize[who]}", side=who)
                ships(g)
                state = "ahoy"
                continue
            while True:                                  # label ships
                ports = port_list(g, who)
                g.set_array(ports)
                if chx == 1:
                    choose = 1 + qint(f32(len(ports) * g.rnd()))
                if len(ports) < 1:
                    g.navysize[who] = 0
                    g.fleet[who] = ""
                    return
                if chx == 0:
                    choose = menu()
                if choose >= 1:
                    break
            g.navyloc[who] = g.array[choose]
            g.cash[who] -= cost
            g.navysize[who] = 1
            ships(g)
            g.say("navy", f"{_force(who)} is building NEW fleet in {g.city[g.navyloc[who]]}", side=who)
            state = "ahoy"
            continue

        if choose == 2:                                  # Attack City, lines 1579-1628
            if g.navyloc[who] == AT_SEA:
                state = "ahoy"
                continue
            if chx == 2 and g.cityp[g.navyloc[who]] == who:
                return
            roll = g.rnd()                               # line 1582: rolled even for the human
            if chx == 2 and g.occupied[g.navyloc[who]] > 0 and roll > S(.5):
                chx = 3                                  # GOTO anchor with choose still 2: bombards anyway
                continue
            if chx == 2 and g.cityp[g.navyloc[who]] == 0:
                chx = 3
                state = "ahoy"
                continue
            if g.navyloc[who] < 1:
                return
            if who == side:
                g.nflag = 1
            if g.cityp[g.navyloc[who]] != 3 - who:
                state = "ahoy"
                continue
            target = g.navyloc[who]
            g.say("navy", f"{_force(who)} fleet bombards {g.city[target]}", side=who, city=target)
            index = g.occupied[target]
            if index > 0:
                pct = f32(.005 * g.navysize[who] + .02 * g.rnd())
                killd = cint(f32(g.armysize[index] * pct))
                if killd < 1:
                    killd = 1
                x = cint(f32(.5 * g.navysize[who] + 1))
                if x > g.supply[index]:
                    x = g.supply[index]
                g.supply[index] -= x
                g.armysize[index] -= killd
                if g.armysize[index] < 1:
                    g.armysize[index] = 1
                g.say("navy", f"{g.armyname[index]} suffered {100 * killd} casualties", army=index)
                return
            while g.fort[target] > 0:                    # label deserted
                if g.rnd() < f32(.7 + .03 * (g.navysize[who] - g.fort[target])):
                    g.fort[target] -= 1                  # label hurt1
                    g.say("navy", f"{g.city[target]} fortifications damaged", city=target)
                    return
                barnacle(g, who)
                g.say("navy", f"{_force(g.cityp[target])} shore battery sunk an attacking ship! "
                              f"{g.navysize[who]} ship(s) left!", city=target)
                if g.navysize[who] < 1:
                    g.navyloc[who] = 0
                    g.fleet[who] = ""
                    g.say("navy", f"{_force(who)} fleet eliminated", side=who)
                    g.victory[3 - who] += 5
                    if who == side:
                        g.grudge = 0
                    sail3(g)
                    return
            if g.rnd() > f32(.25 + .07 * g.navysize[who]):   # label blast
                g.say("navy", f"Citizens of {g.city[target]} stand firm against the attack", city=target)
                return
            if g.navyloc[who] == g.capcity[3 - who]:
                g.say("navy", "The CAPITAL steadfastly stands loyal", city=target)
                return
            g.cityp[target] = 0
            g.say("navy", f"{g.city[target]} is now  NEUTRAL", city=target)
            g.victory[who] += g.cityv[target]
            return

        if choose == 3:                                  # Sail, lines 1629-1690
            g.navysize[who] = len(g.fleet[who])
            if g.navysize[who] < 1 and chx > 0:
                return
            if g.navyloc[who] < 1 or g.navysize[who] < 1:
                g.say("navy", "No ships remain")
                state = "ahoy"
                continue
            dests = sail_list(g, who)
            g.set_array(dests)
            if chx == 3:
                if not dests:
                    return
                if g.grudge > 0:
                    choose = 1
                    g.array[1] = g.navyloc[3 - who]
                else:
                    choose = _nest(g, who, len(dests))
                    if choose <= 0:
                        return
            else:
                choose = menu()
                if choose < 1:
                    return
            dest = g.array[choose]                       # label admiral
            if dest == g.navyloc[who] or dest < 1:
                return
            if g.navysize[who] < 1:
                raise RuntimeError("line 1655 jumps into the build code; unreachable here")
            if who == side:
                g.nflag = 1
            g.say("navy", f"{_force(who)} fleet of {g.navysize[who]} ship(s) is sailing from "
                          f"{name(g, g.navyloc[who])} to {'Raid Commerce' if dest == AT_SEA else g.city[dest]}",
                  side=who)
            g.navyloc[who] = dest
            if g.navyloc[1] == g.navyloc[2]:
                _pirate(g, who, chx)
                return
            sail3(g)
            return

        if choose == 4:                                  # Raid Commerce, lines 1691-1720
            g.navysize[who] = len(g.fleet[who])
            if g.navysize[who] < 1 and chx > 0:
                return
            if g.navysize[who] < 1 or g.commerce == who:
                state = "ahoy"
                continue
            if who == side:
                g.nflag = 1
            g.say("navy", f"{_force(who)} fleet of {g.navysize[who]} ship(s) is sailing to RAID "
                          f"{_force(3 - who)} COMMERCE !", side=who)
            g.navyloc[who] = AT_SEA
            g.commerce = who
            if g.navyloc[1] == g.navyloc[2]:
                _pirate(g, who, chx)
            return

        if choose == 5:                                  # Invasion, lines 1721-1731
            empty = g.commander(who)
            if chx > 0 and empty == 0:
                raise RuntimeError("line 1723 loops forever when no commander is free")
            barnacle(g, who)
            c = g.navyloc[who]
            g.newarmy(who, empty, c)
            g.cash[who] += 100                           # compensates newarmy's charge
            g.capture(empty, c, who, 0)
            g.armysize[empty] = 35
            if who == side:
                g.nflag = 1
            return

        return                                           # CASE ELSE: leave the menu


def _nest(g, who: int, size: int) -> int:
    """GOSUB nest, lines 1846-1866: where the computer's fleet sails."""
    best = 0
    for i in range(1, size + 1):
        target = g.array[i]
        if g.cityp[target] == 0:
            continue
        if target == g.navyloc[3 - who]:
            roll = g.rnd()
            if g.navysize[who] >= g.navysize[3 - who] and roll > S(.1):
                return i
        if g.cityp[target] != who:
            best = i
            if g.rnd() > S(.8):
                return best
    choose = 1 + qint(f32(g.rnd() * size)) if best == 0 else best
    if who == 2 and g.navyloc[2] == 30:
        if g.rnd() > S(.5):
            return 30                                    # a menu row, not city 30: reads array(30)
    return choose


def _pirate(g, who: int, chx: int) -> None:
    """Labels pirate to hitme1, lines 1739-1821: ship against ship until one fleet is gone."""
    g.say("naval_battle", f"NAVAL COMBAT: Union {g.navysize[1]} ship(s), Confederates {g.navysize[2]} ship(s)")
    hit = [0, 10, 10]
    for k in (1, 2):
        if g.fleet[k][-1:] == "I":
            hit[k] = 20
    while True:                                          # firemore (Attack is always chosen)
        pct = 0.0
        a = g.fleet[who][-1:]
        if a != g.fleet[3 - who][-1:]:
            pct = S(.1) if a == "I" else S(-.1)
        loser = 3 - who if g.rnd() <= f32(.5 + pct) else who
        hit[loser] -= 1
        if hit[loser] > 0:
            continue
        barnacle(g, loser)
        g.say("naval_battle", f"{_force(loser)} ship SUNK!", side=loser)
        if g.navysize[loser] < 1:
            g.navyloc[loser] = 0
            g.fleet[loser] = ""
            g.victory[loser] += 10                       # as written: the defeated side gains 10
            if loser != who:
                g.grudge = 1 if who == g.side else 0
            else:
                g.grudge = 1 if who != g.side else 0
            g.say("naval_battle", f"{_force(loser)} fleet {'DEFEATED' if loser != who else 'has been ELIMINATED'}",
                  side=loser)
            sail3(g)
            return
        hit[loser] = 20 if g.fleet[loser][-1:] == "I" else 10


def commerce_raiding(g) -> None:
    """tupdate label allthru, lines 2603-2633."""
    while True:
        if g.navysize[g.commerce] < 1:
            g.commerce = 0
        if g.commerce == 0:
            return
        c = g.commerce
        if g.rnd() < f32(.8 + .02 * g.navysize[c]):
            g.raider = cint(f32(.05 * g.navysize[c] * f32(1 + g.rnd()) * g.income[3 - c]))
            if g.raider < 1:
                g.raider = 1
            share = g.raider / g.income[3 - c] if g.income[3 - c] else float("inf")   # QB64: x/0 is infinite
            if f32(share) > S(.3):
                g.raider = cint(f32(.3 * g.income[3 - c]))
            g.say("raid", f"{_force(c)} raiders have sunk ${g.raider} of {_force(3 - c)} commerce", side=c,
                  amount=g.raider)
            if c == g.side:
                g.grudge = 1
            return
        g.raider = 0
        barnacle(g, c)
        g.say("raid", f"{_force(c)} raiders have lost a ship ({g.navysize[c]} remain)", side=c)
        if g.navyloc[c] > 0:
            continue
        g.commerce = 0
        return


def _force(who: int) -> str:
    return ("NEUTRAL", "Union", "Rebel")[who]
