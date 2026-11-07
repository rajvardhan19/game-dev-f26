# Learning journal: `gemini-g`

Model `gemini-3.5-flash-lite`. 100 training games; notebook version 16 (frozen, sha 9e8dbf7a8ec6b980).

## What it did, game by game

| game | map | notebook | result | turns | recruits | drills | moves | attacks (won) | mean odds | cities peak / end | last-turn cash | refused |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | standard | v0 | decisive loss: Rebel victory: capital captured | 2 | 0 | 0 | 6 | 0 (0) | - | 13 / 12 | 562 | 1 |
| 2 | alternate | v1 | decisive loss: Rebel victory: cities controlled | 6 | 17 | 25 | 4 | 1 (1) | 58% | 11 / 8 | 361 | 5 |
| 3 | standard | v2 | decisive loss: Rebel victory: cities controlled | 18 | 28 | 33 | 4 | 1 (0) | 27% | 13 / 6 | 190 | 23 |
| 4 | alternate | v3 | decisive loss: Rebel victory: cities controlled | 17 | 39 | 36 | 3 | 1 (0) | 41% | 11 / 8 | 362 | 28 |
| 5 | standard | v4 | decisive loss: Rebel victory: capital captured | 11 | 16 | 21 | 6 | 2 (0) | 31% | 13 / 7 | 320 | 15 |
| 6 | alternate | v5 | decisive loss: Rebel victory: cities controlled | 13 | 32 | 40 | 5 | 3 (3) | 71% | 12 / 8 | 362 | 15 |
| 7 | standard | v6 | decisive loss: Rebel victory: share of total income | 6 | 14 | 20 | 5 | 0 (0) | - | 14 / 7 | 265 | 4 |
| 8 | alternate | v7 | decisive loss: Rebel victory: cities controlled | 9 | 23 | 33 | 7 | 1 (0) | 33% | 12 / 9 | 322 | 8 |
| 9 | standard | v8 | held out: Rebel victory: time expired | 24 | 23 | 27 | 6 | 0 (0) | - | 13 / 8 | 219 | 23 |
| 10 | alternate | v9 | decisive loss: Rebel victory: cities controlled | 13 | 36 | 32 | 6 | 2 (0) | 42% | 14 / 7 | 371 | 7 |
| 11 | standard | v10 | decisive loss: Rebel victory: capital captured | 4 | 10 | 9 | 5 | 2 (1) | 60% | 13 / 12 | 304 | 2 |
| 12 | alternate | v11 | held out: Rebel victory: time expired | 28 | 82 | 55 | 14 | 5 (0) | 19% | 15 / 11 | 369 | 29 |
| 13 | standard | v12 | decisive loss: Rebel victory: cities controlled | 7 | 17 | 25 | 6 | 0 (0) | - | 12 / 6 | 259 | 6 |
| 14 | alternate | v13 | decisive loss: Rebel victory: cities controlled | 5 | 14 | 13 | 5 | 0 (0) | - | 11 / 11 | 344 | 1 |
| 15 | standard | v14 | decisive loss: Rebel victory: cities controlled | 8 | 16 | 24 | 4 | 1 (0) | 33% | 12 / 7 | 239 | 9 |
| 16 | alternate | v15 | decisive loss: Rebel victory: cities controlled | 12 | 31 | 45 | 7 | 1 (0) | 44% | 13 / 8 | 335 | 12 |
| 17 | standard | v16 | decisive loss: Rebel victory: capital captured | 6 | 8 | 9 | 4 | 1 (0) | 40% | 13 / 10 | 487 | 2 |
| 18 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 10 / 7 | 1963 | 0 |
| 19 | standard | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 11 / 6 | 1330 | 0 |
| 20 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1974 | 0 |
| 21 | standard | v16 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 0 | 0 | 0 (0) | - | 11 / 4 | 1649 | 0 |
| 22 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1169 | 0 |
| 23 | standard | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1221 | 0 |
| 24 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1147 | 0 |
| 25 | standard | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1267 | 0 |
| 26 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1697 | 0 |
| 27 | standard | v16 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1480 | 0 |
| 28 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1146 | 0 |
| 29 | standard | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 11 / 6 | 1320 | 0 |
| 30 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1697 | 0 |
| 31 | standard | v16 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 963 | 0 |
| 32 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1415 | 0 |
| 33 | standard | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 11 / 6 | 1253 | 0 |
| 34 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1143 | 0 |
| 35 | standard | v16 | decisive loss: Rebel victory: cities controlled | 10 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1688 | 0 |
| 36 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1175 | 0 |
| 37 | standard | v16 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1446 | 0 |
| 38 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1417 | 0 |
| 39 | standard | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1375 | 0 |
| 40 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1655 | 0 |
| 41 | standard | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 11 / 4 | 1420 | 0 |
| 42 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 7 | 1145 | 0 |
| 43 | standard | v16 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1579 | 0 |
| 44 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 3 | 0 | 0 | 0 | 0 (0) | - | 10 / 7 | 882 | 0 |
| 45 | standard | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1263 | 0 |
| 46 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 10 / 7 | 1970 | 0 |
| 47 | standard | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 11 / 6 | 1307 | 0 |
| 48 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1146 | 0 |
| 49 | standard | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1132 | 0 |
| 50 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1148 | 0 |
| 51 | standard | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 963 | 0 |
| 52 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1691 | 0 |
| 53 | standard | v16 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 0 | 0 | 0 (0) | - | 11 / 4 | 1330 | 0 |
| 54 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 7 | 1147 | 0 |
| 55 | standard | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 11 / 6 | 1314 | 0 |
| 56 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 7 | 1137 | 0 |
| 57 | standard | v16 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1355 | 0 |
| 58 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 10 / 7 | 1678 | 0 |
| 59 | standard | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1183 | 0 |
| 60 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1979 | 0 |
| 61 | standard | v16 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 0 | 0 | 0 (0) | - | 11 / 4 | 1395 | 0 |
| 62 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1147 | 0 |
| 63 | standard | v16 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 0 | 0 | 0 (0) | - | 11 / 4 | 1393 | 0 |
| 64 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 7 | 1137 | 0 |
| 65 | standard | v16 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 0 | 0 | 0 (0) | - | 11 / 4 | 1605 | 0 |
| 66 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 10 / 9 | 1692 | 0 |
| 67 | standard | v16 | decisive loss: Rebel victory: cities controlled | 10 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1364 | 0 |
| 68 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1680 | 0 |
| 69 | standard | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 11 / 6 | 1184 | 0 |
| 70 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1146 | 0 |
| 71 | standard | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1321 | 0 |
| 72 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1149 | 0 |
| 73 | standard | v16 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 0 | 0 | 0 (0) | - | 11 / 7 | 1415 | 0 |
| 74 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1150 | 0 |
| 75 | standard | v16 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 0 | 0 | 0 (0) | - | 11 / 4 | 1455 | 0 |
| 76 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1984 | 0 |
| 77 | standard | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1191 | 0 |
| 78 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 2256 | 0 |
| 79 | standard | v16 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1339 | 0 |
| 80 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1658 | 0 |
| 81 | standard | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1025 | 0 |
| 82 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1702 | 0 |
| 83 | standard | v16 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 0 | 0 | 0 (0) | - | 11 / 4 | 1441 | 0 |
| 84 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1683 | 0 |
| 85 | standard | v16 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 0 | 0 | 0 (0) | - | 11 / 4 | 1402 | 0 |
| 86 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1932 | 0 |
| 87 | standard | v16 | decisive loss: Rebel victory: cities controlled | 10 | 0 | 0 | 0 | 0 (0) | - | 11 / 4 | 1671 | 0 |
| 88 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1169 | 0 |
| 89 | standard | v16 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1438 | 0 |
| 90 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1977 | 0 |
| 91 | standard | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 11 / 6 | 1183 | 0 |
| 92 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1976 | 0 |
| 93 | standard | v16 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 0 | 0 | 0 (0) | - | 11 / 6 | 1146 | 0 |
| 94 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 7 | 1137 | 0 |
| 95 | standard | v16 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1393 | 0 |
| 96 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1700 | 0 |
| 97 | standard | v16 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1223 | 0 |
| 98 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 0 | 0 (0) | - | 10 / 7 | 1146 | 0 |
| 99 | standard | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 0 | 0 (0) | - | 11 / 5 | 1264 | 0 |
| 100 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 0 | 0 | 0 (0) | - | 10 / 8 | 1412 | 0 |

## How the notebook changed

### Version 1, after game 1 (standard: Rebel victory: capital captured, 2 turns)

**Diagnosis.** We lost quickly because we scattered our forces with random moves instead of recruiting new troops to build strong armies, and we failed to defend Washington or attack enemy forces effectively.

**Strategy for the next game.** Next game, we will focus heavily on recruiting new troops, keeping our armies supplied and drilled, fortifying vital locations, and preventing the enemy from capturing Washington.

**Changes:**

- added: When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn. (We made zero recruits in the training game, falling far behind the computer and losing our starting strength.)
- added: When an army's supply is 1 or less, use supply to keep it from starving or losing strength. (Armies need constant supply to fight at full capacity and avoid attrition during marches.)
- added: When an army has no enemy adjacent and needs experience, use drill to raise its combat rating. (Drilling improves leader experience and army strength for upcoming battles.)
- added: When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength. (Fortifications are essential to withstand Confederate attacks and hold our territory.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army has no enemy adjacent and needs experience, use drill to raise its combat rating.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.

### Version 2, after game 2 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused heavily on recruiting and drilling inside our own secure cities instead of aggressively capturing enemy territory. While our army grew large, the Confederate forces methodically captured surrounding cities, out-maneuvering us and achieving victory through city control while we remained passive.

**Strategy for the next game.** We will continue to maintain our troop numbers and supply lines, but we must shift from endless drilling to active movement and capturing enemy cities to deny the Confederacy their territorial victory.

**Changes:**

- dropped: When an army has no enemy adjacent and needs experience, use drill to raise its combat rating. (Drilling constantly caused us to neglect city capture and offensive operations, leading to a loss by enemy city control.)
- added: When an army is adjacent to an undefended enemy city, use move to capture it immediately. (We must actively capture enemy territory to prevent the Confederacy from winning the city count victory condition.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.

### Version 3, after game 3 (standard: Rebel victory: cities controlled, 18 turns)

**Diagnosis.** This game was lost because we failed to capture and hold enemy territory while constantly neglecting defensive fortifications and allowing our armies to run out of supply, leading to attrition, defeats, and the gradual loss of our cities to Confederate counterattacks.

**Strategy for the next game.** In the next game, we will combine aggressive recruitment and strategic movement to capture enemy cities, while strictly maintaining supply lines and utilizing fortify to hold key positions against Confederate counteroffensives.

**Changes:**

- revised: When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn. (Maintained from previous notebook as recruiting is essential for maintaining force strength.)
- revised: When an army's supply is 1 or less, use supply to keep it from starving or losing strength. (Retained because starving armies repeatedly lost battles and disbanded during campaigns.)
- revised: When an army is adjacent to an undefended enemy city, use move to capture it immediately. (Kept to ensure we actively expand territory rather than remaining stagnant.)
- revised: When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength. (Kept to correct our complete lack of fortify orders in this game, which invited enemy breakthroughs.)
- added: When an army has low experience and is not immediately threatened, use drill to raise its combat readiness. (Added because we drilled frequently but lacked a disciplined rule for when to prioritize it over supplying or moving.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.
5. When an army has low experience and is not immediately threatened, use drill to raise its combat readiness.

### Version 4, after game 4 (alternate: Rebel victory: cities controlled, 17 turns)

**Diagnosis.** We focused almost exclusively on recruiting and drilling while remaining passive. By refusing to attack or capture enemy cities, we allowed the Confederacy to concentrate forces, outmaneuver us, and slowly overwhelm our isolated garrisons until we lost control of the map.

**Strategy for the next game.** Next game, we will continue steady recruitment and supply management, but we will aggressively use our armies to capture adjacent neutral and enemy cities rather than remaining completely idle on defense.

**Changes:**

- revised: When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn. (Maintained from previous notebook as it helps maintain army size, though we need to combine and use these forces actively rather than letting them sit.)
- revised: When an army's supply is 1 or less, use supply to keep it from starving or losing strength. (Retained to prevent crippling supply attrition on our core field armies.)
- revised: When an army is adjacent to an undefended enemy city, use move to capture it immediately. (Retained because our extreme passivity in this game directly caused the defeat; we must take empty cities to win.)
- revised: When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength. (Retained to ensure our defensive positions withstand enemy attacks.)
- revised: When an army has low experience and is not immediately threatened, use drill to raise its combat readiness. (Retained from previous notebook to ensure our forces are combat-effective.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.
5. When an army has low experience and is not immediately threatened, use drill to raise its combat readiness.

### Version 5, after game 5 (standard: Rebel victory: capital captured, 11 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while leaving our armies passive and out of supply, allowing the Confederate armies to concentrate, march unopposed, and eventually capture Washington. We failed to use our offensive power or fortify critical cities against enemy advances.

**Strategy for the next game.** We will continue to build up our forces through recruitment and maintain supply lines, but we will actively move armies to block Confederate advances, protect our capital, and capture vulnerable enemy cities instead of remaining idle.

**Changes:**

- added: When an enemy army threatens Washington or key supply centers, use move to intercept or fortify the city immediately. (We lost the game because the capital was left undefended against an advancing Confederate corps.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.
5. When an army has low experience and is not immediately threatened, use drill to raise its combat readiness.
6. When an enemy army threatens Washington or key supply centers, use move to intercept or fortify the city immediately.

### Version 6, after game 6 (alternate: Rebel victory: cities controlled, 13 turns)

**Diagnosis.** We built a large army through constant recruitment and kept our cash stable, but we failed to attack and capture enemy cities or use naval and rail options. Excessive drilling while the enemy maneuvered and captured our territory allowed the Confederates to surround us, blockade Philadelphia, and eventually overwhelm our isolated and unsupplied garrisons.

**Strategy for the next game.** We will continue our steady recruitment and supply management, but we will aggressively use move commands to take enemy territory, break blockades, and engage Confederate armies rather than passively drilling while the enemy surrounds and overwhelms us.

**Changes:**

- dropped: When an enemy army threatens Washington or key supply centers, use move to intercept or fortify the city immediately. (It was redundant with broader defensive and movement rules and had a limited single-game track record.)
- added: When enemy armies or fleets threaten core positions or blockade ports, use move or fleet orders to counter them immediately. (We suffered heavy blockade attrition and loss of territory in Philadelphia and along borders because we ignored fleet and active offensive/defensive movement.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.
5. When an army has low experience and is not immediately threatened, use drill to raise its combat readiness.
6. When enemy armies or fleets threaten core positions or blockade ports, use move or fleet orders to counter them immediately.

### Version 7, after game 7 (standard: Rebel victory: share of total income, 6 turns)

**Diagnosis.** We focused excessively on drilling and reinforcing scattered small armies while neglecting offensive movement, fortifying core positions, and protecting our capital. The Rebels outmaneuvered us, captured our vital cities, and eventually seized Washington, ending the game.

**Strategy for the next game.** We will aggressively recruit, maintain army supply, fortify threatened border cities, and actively move to capture enemy territory and counter Rebel incursions while defending our capital.

**Changes:**

- revised: When enemy armies or fleets threaten core positions or blockade ports, use move or fleet orders to counter them immediately. (We must aggressively counter enemy movements toward our capital and core cities rather than remaining static and drilling.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.
5. When an army has low experience and is not immediately threatened, use drill to raise its combat readiness.
6. When enemy armies or fleets threaten core positions or blockade ports, use move or fleet orders to counter them immediately.

### Version 8, after game 8 (alternate: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while neglecting aggressive territorial expansion and capturing enemy cities. The Rebel computer aggressively maneuvered and captured cities while we remained passive, leading to a loss of ground and income.

**Strategy for the next game.** We will maintain our focus on steady recruitment and supply management while increasing our offensive movements to capture enemy cities and actively counter Rebel incursions instead of over-drilling.

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.
5. When an army has low experience and is not immediately threatened, use drill to raise its combat readiness.
6. When enemy armies or fleets threaten core positions or blockade ports, use move or fleet orders to counter them immediately.

### Version 9, after game 9 (standard: Rebel victory: time expired, 24 turns)

**Diagnosis.** We survived the full 24 turns by continuously recruiting and supplying our core armies, but we failed to attack or expand our territory, ending with only 8 cities and letting the Rebels achieve time-expired victory control. We must aggressively capture enemy territory and fight battles rather than just drilling and waiting.

**Strategy for the next game.** Next game we will maintain our strong recruitment and supply habits while actively moving our armies out of passive defense to attack adjacent enemy cities, capture territory, and contest the Rebel victory conditions before time expires.

**Changes:**

- added: When an army is large and well-supplied adjacent to a weaker enemy-held city, use move to attack and capture enemy territory. (We made zero attacks in this game and lost on time because we did not capture enough cities to prevent a Rebel victory.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.
5. When an army has low experience and is not immediately threatened, use drill to raise its combat readiness.
6. When enemy armies or fleets threaten core positions or blockade ports, use move or fleet orders to counter them immediately.
7. When an army is large and well-supplied adjacent to a weaker enemy-held city, use move to attack and capture enemy territory.

### Version 10, after game 10 (alternate: Rebel victory: cities controlled, 13 turns)

**Diagnosis.** We raised a large number of troops and drilled constantly, but we barely moved or attacked enemy positions. This left the initiative to the Confederates, who systematically destroyed our isolated armies, seized our territory, and eventually captured our capital.

**Strategy for the next game.** We must combine steady recruitment and supply management with aggressive tactical movement. Instead of endlessly drilling while enemy forces concentrate against us, we will use our numerical strength to capture enemy cities and protect our capital.

**Changes:**

- revised: When an army is large and well-supplied adjacent to a weaker enemy-held city, use move to attack and capture enemy territory. (We failed to press our numerical advantage with offensive moves, allowing the computer to dictate the pace and overwhelm us.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.
5. When an army has low experience and is not immediately threatened, use drill to raise its combat readiness.
6. When enemy armies or fleets threaten core positions or blockade ports, use move or fleet orders to counter them immediately.
7. When an army is large and well-supplied adjacent to a weaker enemy-held city, use move to attack and capture enemy territory.

### Version 11, after game 11 (standard: Rebel victory: capital captured, 4 turns)

**Diagnosis.** We collapsed quickly because we left Washington completely undefended while launching deep offensives, allowing R.E. Lee to march straight in and capture our capital in September 1861. We also failed to secure our core border positions with fortifications and neglected supply lines.

**Strategy for the next game.** Next game we will aggressively recruit and drill our forces while strictly keeping a strong defensive army stationed in or immediately adjacent to Washington to prevent a capital capture, while slowly pushing out to secure border cities.

**Changes:**

- added: When Washington or the capital is vulnerable to nearby enemy forces, use move to position a defending army inside it immediately. (We lost the game in turn 4 because the capital was left completely open to R.E. Lee's march.)
- added: When an enemy army occupies a core adjacent city threatening our capital, use move to attack and clear it. (We failed to stop advancing Confederate columns near our core territory, leading directly to the loss of Washington.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.
5. When an army has low experience and is not immediately threatened, use drill to raise its combat readiness.
6. When enemy armies or fleets threaten core positions or blockade ports, use move or fleet orders to counter them immediately.
7. When Washington or the capital is vulnerable to nearby enemy forces, use move to position a defending army inside it immediately.
8. When an enemy army occupies a core adjacent city threatening our capital, use move to attack and clear it.

### Version 12, after game 12 (alternate: Rebel victory: time expired, 28 turns)

**Diagnosis.** In Training Game 12, we heavily prioritized recruiting and drilling while practically abandoning offensive movement (only 14 moves all game compared to the computer's 5.7 per turn). Although we successfully built a massive army of over 440,000 men and survived until the time expired by turtling, we failed to capture enemy territory or win battles, allowing the Confederacy to hold 27 cities and achieve a technical victory. We also spent 26 turns executing fleet attacks on Mobile without landing an invasion or moving out to capture surrounding ports.

**Strategy for the next game.** In the next game, we will continue our strong habits of recruiting and keeping armies supplied, but we will dramatically increase our offensive output. Instead of idling our massive armies and endlessly drilling or bombarding ports without following up, we will use move orders to capture empty enemy cities and launch coordinated attacks against outnumbered enemy garrisons to seize territory and deny the Confederacy a time-expired victory.

**Changes:**

- dropped: When Washington or the capital is vulnerable to nearby enemy forces, use move to position a defending army inside it immediately. (This was too narrow and redundant with general defensive and movement instructions.)
- dropped: When an enemy army occupies a core adjacent city threatening our capital, use move to attack and clear it. (Covered more comprehensively by broader offensive and tactical attack instructions.)
- added: When our army outnumbers the adjacent enemy city garrison and is fully supplied, use move to attack and capture the city. (We failed to attack enemy-held cities in this game, leading to time expiring while the enemy held too many cities for victory.)
- added: When a seaport enemy port has been bombarded by fleet attack and its garrison is weakened, use fleet invade to land forces and capture it. (We spent dozens of turns bombarding Mobile with fleet attack without ever following up with fleet invade to capture the port.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.
5. When an army has low experience and is not immediately threatened, use drill to raise its combat readiness.
6. When enemy armies or fleets threaten core positions or blockade ports, use move or fleet orders to counter them immediately.
7. When our army outnumbers the adjacent enemy city garrison and is fully supplied, use move to attack and capture the city.
8. When a seaport enemy port has been bombarded by fleet attack and its garrison is weakened, use fleet invade to land forces and capture it.

### Version 13, after game 13 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while ignoring offensive operations and city capture. The Rebel computer aggressively expanded, captured our capital, and controlled enough cities to win by turn 7.

**Strategy for the next game.** Next game, we will balance our recruitment and drilling with aggressive movement and attacks to capture enemy cities and prevent the Confederacy from seizing our capital.

**Changes:**

- revised: When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn. (Maintained from previous notebook as it helps maintain army sizes.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.
5. When an army has low experience and is not immediately threatened, use drill to raise its combat readiness.
6. When enemy armies or fleets threaten core positions or blockade ports, use move or fleet orders to counter them immediately.
7. When our army outnumbers the adjacent enemy city garrison and is fully supplied, use move to attack and capture the city.
8. When a seaport enemy port has been bombarded by fleet attack and its garrison is weakened, use fleet invade to land forces and capture it.

### Version 14, after game 14 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while ignoring offensive operations and fortification of key points. The Rebels outmaneuvered us, captured cities rapidly, and achieved a decisive victory within 5 turns.

**Strategy for the next game.** Next game we will maintain steady recruitment and supply management, but aggressively use move orders to capture enemy cities and confront rebel forces directly instead of over-drilling.

**Changes:**

- revised: When an army has low experience and is not immediately threatened, use drill to raise its combat readiness. (Drilling too frequently without pursuing attacks left us passive while the enemy claimed victory conditions.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.
5. When an army has low experience and is not immediately threatened, use drill to raise its combat readiness.
6. When enemy armies or fleets threaten core positions or blockade ports, use move or fleet orders to counter them immediately.
7. When our army outnumbers the adjacent enemy city garrison and is fully supplied, use move to attack and capture the city.
8. When a seaport enemy port has been bombarded by fleet attack and its garrison is weakened, use fleet invade to land forces and capture it.

### Version 15, after game 15 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused excessively on drilling and isolated recruitment while neglecting supply lines and coordinated offensives. Our armies ran out of supplies and suffered attrition, allowing the Confederate computer to steadily capture our core cities and overwhelm our positions.

**Strategy for the next game.** Next game, we will maintain rigorous supply management for all active armies, restrict attacks to high-odds situations with superior numbers, and balance recruitment with defensive fortifications to hold our core cities against Rebel counterattacks.

**Changes:**

- revised: When our army outnumbers the adjacent enemy city garrison by at least 2:1 and is fully supplied, use move to attack and capture the city. (We launched attacks with inadequate odds and inferior supply in past games, leading to heavy losses. Requiring a 2:1 advantage and full supply will ensure successful captures.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.
5. When an army has low experience and is not immediately threatened, use drill to raise its combat readiness.
6. When enemy armies or fleets threaten core positions or blockade ports, use move or fleet orders to counter them immediately.
7. When our army outnumbers the adjacent enemy city garrison by at least 2:1 and is fully supplied, use move to attack and capture the city.
8. When a seaport enemy port has been bombarded by fleet attack and its garrison is weakened, use fleet invade to land forces and capture it.

### Version 16, after game 16 (alternate: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** This game was lost because we over-relied on drilling while neglecting offensive maneuvers and city capture. Although we built up a large army of over 200,000 men, we rarely attacked or moved to take enemy territory, allowing the Confederacy to control the map, build up forces, and eventually crush our isolated and starving garrisons.

**Strategy for the next game.** In the next game, I will balance recruiting and drilling with aggressive movement and attacks. Rather than letting armies sit and drill indefinitely, I will use superior numbers to capture enemy cities, maintain supply lines, and prevent the Confederacy from dominating the map.

**Changes:**

- revised: When an army has low experience and is not immediately threatened, use drill to raise its combat readiness. (We drilled excessively (45 times) instead of taking the fight to the enemy, leading to a stagnant front and eventual defeat.)

**Notebook:**

1. When a city offers recruits, use recruit to strengthen existing armies or raise new ones every turn.
2. When an army's supply is 1 or less, use supply to keep it from starving or losing strength.
3. When an army is adjacent to an undefended enemy city, use move to capture it immediately.
4. When holding key border cities threatened by enemy forces, use fortify to double or triple defensive strength.
5. When an army has low experience and is not immediately threatened, use drill to raise its combat readiness.
6. When enemy armies or fleets threaten core positions or blockade ports, use move or fleet orders to counter them immediately.
7. When our army outnumbers the adjacent enemy city garrison by at least 2:1 and is fully supplied, use move to attack and capture the city.
8. When a seaport enemy port has been bombarded by fleet attack and its garrison is weakened, use fleet invade to land forces and capture it.

