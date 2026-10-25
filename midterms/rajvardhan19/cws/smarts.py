"""The original computer opponent: SUB smarts (line 2212), evaluate (2961), void (4514).

In the source, `side` is the human's side and `3 - side` the computer's.
These helpers take both explicitly (`me`, `foe`) so the same code can also
drive the Union baseline (cws/players/original_ai.py), which is the
original's own Union AI, the one a player meets after choosing the Rebels.

The decision helpers read only a "board": the Game itself for the opponent,
or a View built from a player's observation for the baseline. A View raises
if asked for something the observation does not contain.
"""

from .engine import REBEL, UNION, starfin
from .qb import S, cint, f32, idiv, qint

PROBE: list | None = None   # tools/qb64-harness/debug_compare.py collects decision lines here


def void(b, a: int, foe: int) -> int:
    """SUB void: enemy strength next to city a, plus a tenth of the ring beyond."""
    y = 0
    for j in range(1, 7):
        x = b.matrix[a][j]
        if x == 0:
            break
        if b.cityp[x] == foe and b.occupied[x] > 0:
            y += b.armysize[b.occupied[x]]
        for k in range(1, 7):
            m = b.matrix[x][k]
            if m == 0 or m == a:
                continue
            if b.cityp[m] == foe and b.occupied[m] > 0:
                y = cint(f32(y + .1 * b.armysize[b.occupied[m]]))
    return y


def evaluate(b, index: int, me: int, foe: int, rnd, aggress: float, bold: int) -> int:
    """SUB evaluate: the neighbour (1-6) army `index` should march to, or 0."""
    frm = b.armyloc[index]
    x = 200
    if aggress > 1.5:
        x = 80
        if aggress > 2:
            x = 20
            if aggress > 3:
                x = 5
    defend = void(b, frm, foe)
    if defend == 0:
        x = 0
    if bold > 1:
        x = cint(f32(.5 * x))
    best = b.armysize[index]
    array = [0] + [-1] * 6
    for j in range(1, 7):
        a = b.matrix[frm][j]
        if a > 0 and b.occupied[a] > 0:
            best -= b.armysize[b.occupied[a]]
    best = cint(f32(.01 * best))
    if bold > 0:
        best += 20 * bold

    mx = 6
    for j in range(1, 7):
        a = b.matrix[frm][j]
        if a == 0:
            mx = j - 1
            break
        c = b.occupied[a]
        if PROBE is not None:
            PROBE.append(f"EC {index} {j} {a} {c} {b.armysize[c]}")
        if c == 0 and any(b.armyloc[k] > 0 and b.armymove[k] == a for k in starfin(me)):
            continue                                     # a friend is already heading there
        y = cint(f32(best - x * b.fort[frm] - b.cityv[frm] + f32(30 * rnd())))
        if b.fort[frm] > 0 and index == b.occupied[frm]:
            y -= 25
            if b.realism > 0:
                y -= 50
        if a == b.capcity[foe] and b.vicflag[5] > 0:
            y += 200
        if b.cityp[a] != me:
            y += 5 * b.cityv[a] + 10 * b.fort[a]
        if b.cityp[a] == foe:
            if c == 0:
                y += 10 * b.cityv[a]
            else:
                x1 = 2 if b.fort[a] == 1 else 1          # "IF fort(a) = 3" is nested and unreachable
                odds = f32(b.armysize[index] / (x1 * b.armysize[c])) if b.armysize[c] > 0 else 5.0
                if b.armysize[index] < 15:
                    y -= 300
                    odds = S(.1)
                if bold < 3 and b.armysize[index] < 40 and odds < S(.8):
                    y = 0
                if b.realism > 0:
                    y -= 15
                if odds < S(.5):
                    y -= 200
                roll = rnd()                             # consumed even when bold > 0
                if bold == 0 and roll > S(.9):
                    y += 10 * (b.armylead[index] - b.armylead[c] + b.armyexper[index] - b.armylead[index])
                if b.supply[index] < 1:
                    y -= 100
                v = f32(odds + .5 * bold)                # SELECT CASE compares as SINGLE
                if v < S(.3):
                    y = -9999
                elif v < S(.5):
                    y -= 300
                elif v <= S(.8):
                    y -= 20
                elif v <= S(1.2):
                    y -= 5
                elif v <= S(1.5):
                    y += 10
                else:
                    y = cint(f32(y + .5 * (b.armysize[index] - b.armysize[c]) + f32(50 * rnd())))
        # label ourn
        if b.cityp[a] == me and c > 0 and b.armymove[c] == 0:   # 3 - side: do not pile onto a resting friend
            y -= b.armysize[c]
        if foe == UNION and b.cityy[a] < b.cityy[frm]:
            y += 2
        if foe == REBEL and b.cityy[a] > b.cityy[frm]:
            y += 2
        for k in range(1, 7):
            m = b.matrix[a][k]
            if m == 0:
                continue
            if b.cityp[m] == 0:
                y += 3 * b.cityv[m] + 4 * b.fort[m]
            if b.cityp[m] == foe:
                y += 3 * b.cityv[m] + 4 * b.fort[m]
            if b.cityp[m] == foe and c > 0:
                rnd()                                    # odds! = 5 - 4 * RND, overwritten at once
                odds = f32(b.armysize[index] / b.armysize[c]) if b.armysize[c] > 0 else 5.0
                if odds < 1:
                    y -= 2
            if b.cityp[m] == b.capcity[foe]:             # compares an owner with a city: as written
                y += 50
        array[j] = y
        if PROBE is not None:
            PROBE.append(f"EV {index} {j} {y}")

    x, best = 0, 0
    for j in range(1, mx + 1):
        if array[j] < 0:
            continue
        if array[j] > x:
            x, best = array[j], j
    if defend > b.armysize[index] and array[best] < 50:
        best = 0
    return best


def enufarmies(b, me: int) -> int:
    """GOSUB enufarmies, lines 2354-2364."""
    y = 0
    for i in starfin(3 - me):
        if b.armyloc[i] > 0:
            y = cint(f32(y + .1 * b.armysize[i]))
    x = z = 0
    for i in starfin(me):
        if b.armyloc[i] > 0:
            x += 1
            z = cint(f32(z + .1 * b.armysize[i]))
    if y > z:
        x -= 2
    if y > 2 * z:
        x = 0
    return x


def randsel(b, cities: list[int], me: int, rnd) -> int:
    """GOSUB randsel, lines 2146-2173: which offered city the computer levies in.

    `cities` is the offered list in menu order; returns its 0-based index.
    """
    size = len(cities)
    choose = 0
    for i, target in enumerate(cities, 1):
        x = b.occupied[target]
        if (x == 0) != (b.armysize[x] < 155):             # QBasic XOR of two comparisons
            choose = i
    if choose == 0:
        choose = 1 + qint(f32(rnd() * size))
    if b.realism > 0:
        x = 0
        for i, target in enumerate(cities, 1):
            if b.occupied[target] == 0:
                y = 3 * b.cityv[target] + 33
            else:
                y = 2 * b.cityv[target] + 20
            if b.cutoff(me, target) < 1:
                y = idiv(y, 3)
            roll = rnd()
            if y > x and roll > S(.5):
                x, choose = y, i
    if b.cash[me] < 100:
        choose = size
    return choose - 1


def march_order(b, i: int, me: int, foe: int, rnd, aggress: float, bold: int) -> int:
    """One pass of smarts' "Top Priority" loop, lines 2305-2337: a destination or 0."""
    target = b.armyloc[i]
    if b.armyloc[i] < 1 or b.armymove[i] < 0:
        return 0
    x = b.armysize[i]
    roll = rnd()
    if b.supply[i] < 1 and roll > S(.1):
        return 0
    defend = void(b, target, foe)
    if defend > 0 and target == b.capcity[me] and b.occupied[target] == i:
        return 0                                         # hold the capital
    if target == b.capcity[me] and b.vicflag[5] != 0:
        for j in range(1, 7):
            if void(b, b.matrix[target][j], foe) > 0:
                return 0
    best = evaluate(b, i, me, foe, rnd, aggress, bold)
    if best == 0:
        return 0
    dest = b.matrix[target][best]
    if PROBE is not None:
        PROBE.append(f"MV {i} {dest}")
    if b.cityp[dest] == me:
        y = b.occupied[dest]
        if y > 0 and b.armymove[y] == x:                 # "crossing moves": compares with armysize, as written
            return 0
    if b.month == 1 and b.jancam == 0 and b.cityp[dest] != me:
        return 0
    return dest


def smarts(g) -> None:
    """SUB smarts for the computer side, without navies, railroads or events."""
    who, foe = 3 - g.side, g.side
    rnd = g.rnd
    slots = starfin(who)
    # events: Random Events are OFF (randbal = 0), so SUB events returns at line 3057.

    for i in slots:                                      # Check Supply, line 2221
        if g.armyloc[i] > 0 and g.supply[i] < 1:
            g.resupply(i)

    cost = 200
    if cost <= g.cash[who]:                              # Fortify Capital or Other City
        target = 0
        cap = g.capcity[who]
        go = "city2"
        if not (g.occupied[cap] == 0 or g.fort[cap] > 1):
            target = cap
            go = "capital" if g.cityp[target] == who else "city2"
        while True:
            if go == "city2":
                if f32(1 + rnd()) < f32(g.bold + g.aggress):
                    break
                target = 0
                for i in slots:
                    x = g.armyloc[i]
                    if x == 0 or g.armymove[g.occupied[x]] < 0 or g.armymove[i] < 0:
                        continue
                    if g.fort[x] > 1:
                        continue
                    if void(g, x, foe) > g.armysize[i]:
                        target = g.armyloc[i]
                        break
            # label capital
            if target == 0 or g.fort[target] > 1:
                break
            g.fortify(who, target, refresh=False)
            roll = rnd()
            if who == UNION and roll > S(.5):            # navysize(1) < 1 and the unset cash < 222 hold
                break
            again = f32(3 * rnd()) > f32(1 + g.aggress)
            if again and g.cash[who] >= cost:
                go = "city2"
                continue
            break

    # Recruit New Armies, label signup
    if enufarmies(g, who) <= f32(2 + 3 * foe + f32(3 * rnd())):
        cities = g.recruit_open(who)
        while cities and g.cash[who] >= 100:             # label levy
            pick = cities[randsel(g, cities, who, rnd)]
            g.occupy(pick)
            if g.occupied[pick] == 0 and not any(g.armyloc[k] == 0 for k in slots):
                break                                    # no commander: the computer stops
            g.levy(who, pick)

    # Give Move Orders to Each Army, label movearmy
    eligible = g.combine_cities(who)
    if eligible:
        g.combine(who, eligible[qint(f32(len(eligible) * rnd()))])

    for i in slots:
        dest = march_order(g, i, who, foe, rnd, g.aggress, g.bold)
        if dest:
            g.armymove[i] = dest
            g.say("plan", f"{g.armyname[i]} plans to move from {g.city[g.armyloc[i]]} to {g.city[dest]}",
                  side=who, army=i, frm=g.armyloc[i], to=dest)

    for i in slots:                                      # drill idle armies, lines 2340-2351
        if g.armymove[i] == 0 and g.armyexper[i] < 6 and g.armyexper[i] < g.armylead[i]:
            g.armyexper[i] += 1
            g.armymove[i] = -1
