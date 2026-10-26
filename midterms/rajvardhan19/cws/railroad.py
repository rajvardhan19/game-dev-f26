"""Railroads: SUB railroad (lines 1969-2072) and SUB traincapacity (4054-4061).

One train per side per turn. An army boards in a city with friendly rail links
(`route` > 1), travels to any friendly city whose own links pass the same test
(the track in between is not checked), and arrives at the start of that
turn's resolution, before any army marches (tupdate line 2408). While
aboard, its city is 0 and its order is the destination.
"""

from .qb import S, f32, idiv


def traincapacity(g, who: int) -> int:
    """SUB traincapacity: in hundreds of men. Note the base uses the human's side."""
    if g.realism == 0:
        return g.train[who]
    x = 23 if g.side == 2 else 11
    limit = g.train[who] + 5 * (g.control[who] - x)
    x = 2 * g.train[who]
    if limit > x:
        limit = x
    if limit < idiv(x, 4):
        limit = idiv(x, 4)
    return limit


def route(g, who: int, target: int) -> int:
    """GOSUB route, lines 2055-2066: friendly neighbours, and their friendly neighbours."""
    x = 0
    for j in range(1, 7):
        y = g.matrix[target][j]
        if y > 0 and g.cityp[y] == who:
            x += 1
            for m in range(1, 7):
                z = g.matrix[y][m]
                if z > 0 and z != target and g.cityp[z] == who:
                    x += 1
    return x


def destinations(g, who: int, frm: int) -> list[int]:
    """The cities newcity offers (own cities) that pass route at the far end, lines 2012-2019."""
    return [c for c in range(1, 41) if g.cityp[c] == who and c != frm and route(g, who, c) > 1]


def can_board(g, who: int, index: int) -> bool:
    """The human's checks, lines 2005-2011: idle, within capacity, links at the start."""
    return (g.rr[who] == 0 and g.armyloc[index] > 0 and g.armymove[index] == 0
            and g.armysize[index] <= traincapacity(g, who) and route(g, who, g.armyloc[index]) > 1)


def haul(g, who: int, index: int, dest: int) -> str:
    """Label haul, lines 2020-2032."""
    frm = g.armyloc[index]
    g.tracks[who] = frm
    g.rrfrom[who] = frm
    g.rr[who] = index
    g.armyloc[index] = 0
    g.armymove[index] = dest
    g.occupy(frm)
    text = f"{g.armyname[index]} is taking the train from {g.city[frm]} to {g.city[dest]}"
    g.say("rail", text, side=who, army=index, frm=frm, to=dest)
    return text


def arrive(g, who: int) -> None:
    """CASE IS > 0, lines 2034-2052: the train arrives."""
    g.occupy(g.rrfrom[who])
    index = g.rr[who]
    g.tracks[who] = g.armymove[index]
    g.rr[who] = 0
    g.armyloc[index] = g.armymove[index]
    g.armymove[index] = -1
    g.say("rail", f"Train with {g.armyname[index]} has arrived in {g.city[g.armyloc[index]]}",
          side=who, army=index, city=g.armyloc[index])
    if g.cityp[g.armyloc[index]] != who:
        g.capture(index, g.armyloc[index], who, 0)
    if g.occupied[g.armyloc[index]] > 0:
        return
    g.occupy(g.armyloc[index])


def computer_railroad(g, who: int) -> None:
    """SUB railroad for the computer: arrival if a train is out, else CASE 0's choice and haul."""
    if g.rr[who] > 0:
        arrive(g, who)
        return
    choice = computer_rail_choice(g, who, g.side, traincapacity(g, who))
    if choice:
        haul(g, who, *choice)


def computer_rail_choice(b, who: int, foe: int, limit: int) -> tuple[int, int] | None:
    """CASE 0 for the computer, lines 1971-2003: (army, destination) or None.

    `b` is the Game, or the Union baseline's View; `foe` is the original's
    `side` (the human, whose strength `void` measures); `limit` is the train
    capacity in hundreds.
    """
    from .smarts import void
    slots = range(1, 21) if who == 1 else range(21, 41)
    mx, index, target = 32767, 0, 0
    cap = b.capcity[who]
    for i in slots:
        if b.armyloc[i] == 0 or b.armymove[i] != 0:
            continue
        x = sum(1 for j in range(1, 7)
                if b.matrix[b.armyloc[i]][j] > 0 and b.cityp[b.matrix[b.armyloc[i]][j]] != who)
        if b.occupied[cap] > 0 and x > 1:
            continue                                     # a front-line army stays while the capital is held
        defend = void(b, b.armyloc[i], foe)
        if b.vicflag[5] > 0 and b.occupied[cap] == 0 and defend > mx:
            defend = mx - 1
        if defend < mx:
            target = b.armyloc[i]
            if route(b, who, target) > 1:
                mx, index = defend, i
    if index == 0 or f32(mx) > f32(.3 * b.armysize[index]):
        return None
    if b.armysize[index] > limit:
        return None
    frm = b.armyloc[index]
    x1 = 0
    for i in range(1, 41):
        if b.cityp[i] != who:
            continue
        defend = void(b, i, foe)
        if defend == 0 or defend > 3 * b.armysize[index]:
            continue
        if b.occupied[i] > 0:
            continue
        target = i
        if route(b, who, target) == 0:
            continue
        if foe == 1 and b.cityy[i] < b.cityy[frm]:
            x1 = i
        if foe == 2 and b.cityy[i] > b.cityy[frm]:
            x1 = i
        if b.fort[i] > 0 and b.occupied[i] == 0:
            x1 = i
            break
    if b.vicflag[5] > 0 and b.occupied[cap] == 0:
        if route(b, who, target) > 0:                    # as written: the last target, not the capital
            if void(b, cap, foe) > 0:
                x1 = cap
    return (index, x1) if x1 > 0 else None
