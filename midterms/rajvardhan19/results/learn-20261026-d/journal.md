# Learning journal: `gemini-d`

Model `gemini-3.5-flash-lite`. 100 training games; notebook version 20 (frozen, sha 66a976c6197fdf1f).

## What it did, game by game

| game | map | notebook | result | turns | recruits | drills | moves | attacks (won) | mean odds | cities peak / end | last-turn cash | refused |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | standard | v0 | decisive loss: Rebel victory: capital captured | 3 | 0 | 4 | 3 | 1 (0) | 23% | 13 / 11 | 559 | 0 |
| 2 | alternate | v0 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 7 | 12 | 3 (0) | 43% | 13 / 10 | 977 | 6 |
| 3 | standard | v0 | decisive loss: Rebel victory: capital captured | 2 | 0 | 3 | 3 | 1 (0) | 27% | 12 / 10 | 527 | 0 |
| 4 | alternate | v0 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 3 | 6 | 2 (0) | 40% | 11 / 9 | 1091 | 2 |
| 5 | standard | v0 | decisive loss: Rebel victory: cities controlled | 11 | 0 | 19 | 7 | 0 (0) | - | 13 / 5 | 1514 | 7 |
| 6 | alternate | v1 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 22 | 0 | 0 (0) | - | 10 / 6 | 1280 | 2 |
| 7 | standard | v1 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 17 | 1 | 0 (0) | - | 12 / 5 | 451 | 10 |
| 8 | alternate | v1 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 13 | 2 | 0 (0) | - | 11 / 9 | 683 | 1 |
| 9 | standard | v1 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 18 | 1 | 0 (0) | - | 12 / 4 | 228 | 8 |
| 10 | alternate | v1 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 21 | 0 | 0 (0) | - | 10 / 7 | 1800 | 3 |
| 11 | standard | v2 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 15 | 2 | 0 (0) | - | 12 / 4 | 486 | 5 |
| 12 | alternate | v2 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 8 | 3 (0) | 30% | 12 / 9 | 1096 | 1 |
| 13 | standard | v2 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 14 | 3 | 1 (0) | 45% | 12 / 6 | 628 | 4 |
| 14 | alternate | v2 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 13 | 1 (0) | 10% | 14 / 10 | 661 | 1 |
| 15 | standard | v2 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 7 | 8 | 0 (0) | - | 12 / 5 | 469 | 3 |
| 16 | alternate | v3 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 24 | 0 | 0 (0) | - | 10 / 6 | 2057 | 6 |
| 17 | standard | v3 | decisive loss: Rebel victory: capital captured | 5 | 0 | 16 | 1 | 0 (0) | - | 12 / 10 | 291 | 3 |
| 18 | alternate | v3 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 25 | 1 | 1 (0) | 44% | 10 / 8 | 350 | 5 |
| 19 | standard | v3 | decisive loss: Rebel victory: cities controlled | 10 | 0 | 16 | 1 | 0 (0) | - | 12 / 6 | 588 | 9 |
| 20 | alternate | v3 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 24 | 0 | 0 (0) | - | 10 / 8 | 668 | 3 |
| 21 | standard | v4 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 19 | 1 | 0 (0) | - | 11 / 5 | 850 | 6 |
| 22 | alternate | v4 | decisive loss: Rebel victory: cities controlled | 4 | 3 | 26 | 0 | 0 (0) | - | 10 / 8 | 796 | 1 |
| 23 | standard | v4 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 17 | 1 | 0 (0) | - | 12 / 5 | 241 | 4 |
| 24 | alternate | v4 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 24 | 0 | 0 (0) | - | 10 / 8 | 896 | 2 |
| 25 | standard | v4 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 18 | 1 | 0 (0) | - | 12 / 5 | 240 | 7 |
| 26 | alternate | v5 | decisive loss: Rebel victory: cities controlled | 5 | 1 | 28 | 0 | 0 (0) | - | 10 / 9 | 1282 | 1 |
| 27 | standard | v5 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 18 | 1 | 0 (0) | - | 12 / 4 | 251 | 3 |
| 28 | alternate | v5 | decisive loss: Rebel victory: cities controlled | 8 | 6 | 27 | 2 | 0 (0) | - | 11 / 9 | 1089 | 1 |
| 29 | standard | v5 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 16 | 1 | 0 (0) | - | 12 / 5 | 466 | 11 |
| 30 | alternate | v5 | decisive loss: Rebel victory: cities controlled | 8 | 20 | 32 | 1 | 0 (0) | - | 10 / 8 | 341 | 6 |
| 31 | standard | v6 | decisive loss: Rebel victory: cities controlled | 10 | 1 | 17 | 1 | 0 (0) | - | 12 / 5 | 219 | 7 |
| 32 | alternate | v6 | decisive loss: Rebel victory: cities controlled | 7 | 8 | 30 | 0 | 0 (0) | - | 10 / 8 | 751 | 2 |
| 33 | standard | v6 | decisive loss: Rebel victory: cities controlled | 10 | 0 | 17 | 1 | 0 (0) | - | 12 / 5 | 431 | 7 |
| 34 | alternate | v6 | decisive loss: Rebel victory: cities controlled | 8 | 5 | 25 | 0 | 0 (0) | - | 10 / 7 | 332 | 5 |
| 35 | standard | v6 | decisive loss: Rebel victory: cities controlled | 10 | 0 | 17 | 1 | 0 (0) | - | 12 / 6 | 443 | 11 |
| 36 | alternate | v7 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 17 | 7 | 1 (0) | 50% | 11 / 8 | 1217 | 2 |
| 37 | standard | v7 | decisive loss: Rebel victory: cities controlled | 10 | 3 | 20 | 5 | 2 (0) | 32% | 12 / 3 | 162 | 6 |
| 38 | alternate | v7 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 25 | 10 | 3 (0) | 37% | 12 / 9 | 1663 | 1 |
| 39 | standard | v7 | decisive loss: Rebel victory: cities controlled | 8 | 6 | 19 | 4 | 0 (0) | - | 12 / 7 | 299 | 3 |
| 40 | alternate | v7 | decisive loss: Rebel victory: cities controlled | 5 | 2 | 19 | 6 | 2 (1) | 40% | 12 / 8 | 1178 | 3 |
| 41 | standard | v8 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 16 | 2 | 1 (0) | 23% | 12 / 4 | 234 | 5 |
| 42 | alternate | v8 | decisive loss: Rebel victory: cities controlled | 7 | 3 | 27 | 0 | 0 (0) | - | 10 / 8 | 1246 | 3 |
| 43 | standard | v8 | decisive loss: Rebel victory: cities controlled | 11 | 0 | 16 | 1 | 0 (0) | - | 12 / 6 | 523 | 11 |
| 44 | alternate | v8 | decisive loss: Rebel victory: cities controlled | 7 | 2 | 26 | 0 | 0 (0) | - | 10 / 7 | 1569 | 1 |
| 45 | standard | v8 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 18 | 1 | 0 (0) | - | 12 / 5 | 620 | 2 |
| 46 | alternate | v9 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 26 | 0 | 0 (0) | - | 10 / 8 | 1992 | 1 |
| 47 | standard | v9 | decisive loss: Rebel victory: cities controlled | 10 | 0 | 18 | 3 | 1 (1) | 66% | 12 / 5 | 384 | 12 |
| 48 | alternate | v9 | decisive loss: Rebel victory: cities controlled | 9 | 5 | 28 | 0 | 0 (0) | - | 10 / 9 | 1045 | 1 |
| 49 | standard | v9 | decisive loss: Rebel victory: cities controlled | 10 | 0 | 16 | 2 | 0 (0) | - | 12 / 4 | 418 | 6 |
| 50 | alternate | v9 | decisive loss: Rebel victory: cities controlled | 6 | 4 | 29 | 0 | 0 (0) | - | 10 / 7 | 1619 | 0 |
| 51 | standard | v10 | decisive loss: Rebel victory: share of total income | 8 | 0 | 16 | 5 | 3 (2) | 58% | 12 / 7 | 870 | 6 |
| 52 | alternate | v10 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 25 | 0 | 0 (0) | - | 10 / 8 | 845 | 1 |
| 53 | standard | v10 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 17 | 1 | 0 (0) | - | 12 / 5 | 261 | 1 |
| 54 | alternate | v10 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 29 | 0 | 0 (0) | - | 10 / 8 | 1414 | 0 |
| 55 | standard | v10 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 17 | 2 | 0 (0) | - | 12 / 5 | 196 | 2 |
| 56 | alternate | v11 | decisive loss: Rebel victory: share of total income | 6 | 4 | 27 | 0 | 0 (0) | - | 10 / 7 | 1105 | 1 |
| 57 | standard | v11 | decisive loss: Rebel victory: share of total income | 9 | 0 | 17 | 3 | 0 (0) | - | 12 / 7 | 203 | 8 |
| 58 | alternate | v11 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 29 | 0 | 0 (0) | - | 10 / 6 | 1639 | 0 |
| 59 | standard | v11 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 16 | 2 | 1 (0) | 45% | 12 / 5 | 653 | 6 |
| 60 | alternate | v11 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 28 | 2 | 1 (1) | 77% | 10 / 8 | 2056 | 1 |
| 61 | standard | v12 | decisive loss: Rebel victory: share of total income | 9 | 1 | 16 | 3 | 1 (0) | 30% | 12 / 6 | 238 | 9 |
| 62 | alternate | v12 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 25 | 0 | 0 (0) | - | 10 / 8 | 1147 | 1 |
| 63 | standard | v12 | decisive loss: Rebel victory: cities controlled | 10 | 0 | 16 | 3 | 1 (0) | 40% | 12 / 5 | 265 | 5 |
| 64 | alternate | v12 | decisive loss: Rebel victory: cities controlled | 6 | 3 | 29 | 0 | 0 (0) | - | 10 / 7 | 1302 | 1 |
| 65 | standard | v12 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 18 | 2 | 0 (0) | - | 12 / 5 | 395 | 1 |
| 66 | alternate | v13 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 28 | 1 | 0 (0) | - | 10 / 8 | 1968 | 0 |
| 67 | standard | v13 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 14 | 2 | 0 (0) | - | 11 / 5 | 754 | 0 |
| 68 | alternate | v13 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 28 | 0 | 0 (0) | - | 10 / 8 | 1480 | 0 |
| 69 | standard | v13 | decisive loss: Rebel victory: cities controlled | 13 | 0 | 17 | 1 | 0 (0) | - | 12 / 4 | 472 | 8 |
| 70 | alternate | v13 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 27 | 0 | 0 (0) | - | 10 / 8 | 1597 | 2 |
| 71 | standard | v14 | decisive loss: Rebel victory: cities controlled | 12 | 0 | 17 | 2 | 0 (0) | - | 12 / 6 | 341 | 8 |
| 72 | alternate | v14 | decisive loss: Rebel victory: share of total income | 9 | 3 | 25 | 0 | 0 (0) | - | 10 / 8 | 729 | 4 |
| 73 | standard | v14 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 17 | 5 | 3 (1) | 42% | 12 / 5 | 217 | 8 |
| 74 | alternate | v14 | decisive loss: Rebel victory: cities controlled | 6 | 6 | 32 | 0 | 0 (0) | - | 10 / 9 | 904 | 5 |
| 75 | standard | v14 | decisive loss: Rebel victory: cities controlled | 11 | 0 | 17 | 2 | 1 (0) | 27% | 12 / 5 | 285 | 6 |
| 76 | alternate | v15 | decisive loss: Rebel victory: cities controlled | 4 | 9 | 16 | 0 | 0 (0) | - | 10 / 8 | 334 | 0 |
| 77 | standard | v15 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 17 | 1 | 0 (0) | - | 12 / 6 | 657 | 6 |
| 78 | alternate | v15 | decisive loss: Rebel victory: cities controlled | 5 | 11 | 27 | 0 | 0 (0) | - | 10 / 9 | 352 | 4 |
| 79 | standard | v15 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 17 | 1 | 0 (0) | - | 12 / 6 | 468 | 5 |
| 80 | alternate | v15 | decisive loss: Rebel victory: cities controlled | 7 | 11 | 23 | 0 | 0 (0) | - | 10 / 9 | 585 | 4 |
| 81 | standard | v16 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 15 | 2 | 1 (0) | 27% | 12 / 5 | 277 | 5 |
| 82 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 26 | 0 | 0 (0) | - | 10 / 7 | 1149 | 0 |
| 83 | standard | v16 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 15 | 2 | 0 (0) | - | 12 / 4 | 329 | 8 |
| 84 | alternate | v16 | decisive loss: Rebel victory: cities controlled | 8 | 3 | 28 | 3 | 1 (0) | 36% | 10 / 6 | 1794 | 7 |
| 85 | standard | v16 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 17 | 1 | 0 (0) | - | 12 / 5 | 260 | 5 |
| 86 | alternate | v17 | decisive loss: Rebel victory: cities controlled | 4 | 12 | 21 | 1 | 0 (0) | - | 10 / 9 | 350 | 10 |
| 87 | standard | v17 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 15 | 4 | 1 (0) | 50% | 12 / 6 | 296 | 7 |
| 88 | alternate | v17 | decisive loss: Rebel victory: cities controlled | 5 | 3 | 27 | 2 | 0 (0) | - | 10 / 8 | 341 | 3 |
| 89 | standard | v17 | decisive loss: Rebel victory: capital captured | 11 | 0 | 17 | 7 | 1 (0) | 27% | 12 / 6 | 248 | 7 |
| 90 | alternate | v17 | decisive loss: Rebel victory: cities controlled | 9 | 6 | 35 | 1 | 1 (0) | 10% | 10 / 8 | 1324 | 3 |
| 91 | standard | v18 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 14 | 5 | 3 (1) | 39% | 12 / 5 | 350 | 3 |
| 92 | alternate | v18 | decisive loss: Rebel victory: cities controlled | 5 | 3 | 23 | 2 | 0 (0) | - | 10 / 9 | 1014 | 2 |
| 93 | standard | v18 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 20 | 1 | 0 (0) | - | 12 / 6 | 784 | 3 |
| 94 | alternate | v18 | decisive loss: Rebel victory: cities controlled | 5 | 7 | 20 | 0 | 0 (0) | - | 10 / 8 | 587 | 0 |
| 95 | standard | v18 | decisive loss: Rebel victory: capital captured | 9 | 0 | 16 | 5 | 0 (0) | - | 12 / 7 | 442 | 6 |
| 96 | alternate | v19 | decisive loss: Rebel victory: share of total income | 6 | 3 | 28 | 0 | 0 (0) | - | 10 / 8 | 1163 | 1 |
| 97 | standard | v19 | decisive loss: Rebel victory: cities controlled | 12 | 0 | 16 | 2 | 0 (0) | - | 12 / 5 | 347 | 15 |
| 98 | alternate | v19 | decisive loss: Rebel victory: cities controlled | 6 | 1 | 28 | 3 | 3 (1) | 55% | 10 / 9 | 1581 | 2 |
| 99 | standard | v19 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 19 | 1 | 0 (0) | - | 12 / 5 | 565 | 4 |
| 100 | alternate | v19 | decisive loss: Rebel victory: cities controlled | 3 | 5 | 17 | 0 | 0 (0) | - | 10 / 7 | 346 | 2 |

## How the notebook changed

### Version 1, after game 5 (standard: Rebel victory: cities controlled, 11 turns)

**Diagnosis.** The Union suffered repeated defeats because our armies attacked entrenched or superior Confederate forces at very low odds (around 20-40%), leading to massive casualties and the loss of the capital and key cities. Furthermore, armies were left to run out of supply without buying provisions or securing adjacent friendly cities, and too much time was wasted on idle drilling while the Rebels seized territory.

**Strategy for the next game.** Next game, we will focus on defensive consolidation, maintaining army supply lines, avoiding low-odds attacks on fortified enemy forces, and building up our economic and military strength safely.

**Changes:**

- dropped: When McDowell is available, advance immediately on Richmond. (Led directly to disastrous low-odds attacks against J.E. Johnston in Richmond.)
- added: When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn. (Armies repeatedly ran out of supplies and suffered severe attrition because supply orders were neglected or illegal due to timing.)
- added: When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured. (Prevents suicide attacks at 20-30% odds that drain Union manpower.)

**Notebook:**

1. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
2. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
3. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
4. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.

### Version 2, after game 10 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** In Games 6 through 10, the Union spent far too many turns endlessly drilling static armies while the Confederate computer relentlessly marched, captured cities, and overwhelmed our territory. Drilling gives experience, but it does not stop the enemy from seizing control of the map and winning via city dominance. We failed to actively contest enemy advances, utilize rail lines effectively, recruit new forces, or mount coordinated counter-offensives. To win, we must balance preparedness with active territorial defense and aggressive interception of advancing rebel armies.

**Strategy for the next game.** Next game, we will immediately secure key positions like Paducah and Washington, actively block or counter Rebel army movements instead of endlessly drilling in place, maintain active supply lines, and aggressively use our fleet to disrupt Confederate operations.

**Changes:**

- revised: When an adjacent enemy army threatens a friendly city with inferior defensive odds, do not remain idle; instead, move to intercept, reinforce, or fortify before the enemy captures the position. (Previous lesson overly encouraged passive drilling while the enemy captured the entire map.)
- dropped: When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids. (Replaced by a broader and more actionable naval engagement rule.)
- added: When recruit funds are available and strategic cities are losing friendly neighbors, use recruit to maintain field strength and garrison key hubs. (We failed to raise troops in recent games, letting our army sizes dwindle while the Confederacy grew.)

**Notebook:**

1. When an adjacent enemy army threatens a friendly city with inferior defensive odds, do not remain idle; instead, move to intercept, reinforce, or fortify before the enemy captures the position.
2. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
3. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.
4. When an enemy fleet is present in a port or blockading, use fleet sail or fleet attack to contest control rather than relying solely on passive positioning.
5. When recruit funds are available and strategic cities are losing friendly neighbors, use recruit to maintain field strength and garrison key hubs.

### Version 3, after game 15 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** Notebook v2 performed poorly (-1.00 score) because it forced defensive moves without sufficient numbers and engaged in counter-productive fleet attacks when blockaded or outmatched. In both standard and alternate maps, excessive marching into unfavorable combat odds depleted our armies while the Rebels consolidated their forces. Returning to a sound defensive posture, maintaining supply lines, and focusing on careful drilling rather than reckless attacks will improve our longevity.

**Strategy for the next game.** We will revert to our proven defensive strategy from notebook v1. On the standard map, we will drill our primary armies to build experience, construct wooden naval vessels to secure coastal superiority, and avoid unprofitable attacks against superior Rebel concentrations. We will maintain supply levels vigilantly and fortify critical positions to outlast the Confederate forces.

**Changes:**

- dropped: When an adjacent enemy army threatens a friendly city with inferior defensive odds, do not remain idle; instead, move to intercept, reinforce, or fortify before the enemy captures the position. (Led to chaotic, losing counter-attacks and failed defensive lunges that drained our troop strength.)
- dropped: When an enemy fleet is present in a port or blockading, use fleet sail or fleet attack to contest control rather than relying solely on passive positioning. (Resulted in disastrous fleet engagements and refused orders when blockaded or outgunned.)
- dropped: When recruit funds are available and strategic cities are losing friendly neighbors, use recruit to maintain field strength and garrison key hubs. (Distracted from crucial supply management and core defensive drilling priorities.)

**Notebook:**

1. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
2. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
3. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
4. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.

### Version 4, after game 20 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused heavily on drilling and static defense while failing to actively capture enemy territory, recruit new forces, or properly leverage our fleets and railways to shift the strategic balance. As a result, the Confederates outmaneuvered us and captured key cities.

**Strategy for the next game.** We will actively recruit new troops to expand our forces, secure key cities early by capturing objective points, maintain supply lines, and use our fleets and railways efficiently to counter Rebel movements.

**Changes:**

- added: When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling. (We failed to recruit enough troops throughout the games, leaving us outnumbered in cities and unable to hold territory.)

**Notebook:**

1. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
2. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
3. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
4. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
5. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.

### Version 5, after game 25 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** In these games, our excessive drilling of existing armies instead of actively recruiting new forces or aggressively advancing allowed the Confederate computer to steadily capture neutral and Union cities, eventually winning on city count. Our armies gained high experience levels, but remained passive while the enemy out-expanded us economically and territorially.

**Strategy for the next game.** For the next game, we will balance our focus between expanding our forces via recruitment in secure cities, cautiously advancing when odds favor us, and utilizing our naval fleet effectively to blockade enemy ports while maintaining strong defensive fortifications.

**Changes:**

- dropped: When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids. (This lesson remains active; no changes made to it.)

**Notebook:**

1. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
2. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
3. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
4. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
5. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.

### Version 6, after game 30 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** In these games, we overly focused on continuous drilling without aggressive expansion or sufficient defensive positioning, leading to the loss of key cities and our capital. While our recruitment efforts in the alternate map built up men, we failed to leverage our forces to capture Confederate territory or protect our supply lines, resulting in low supply states and ultimate defeat.

**Strategy for the next game.** We will maintain aggressive recruitment in secure cities and balanced drilling while immediately pivoting to intercept and defend against Confederate advances toward our capital and vital cities, ensuring our supply lines remain intact.

**Changes:**

- added: When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills. (In multiple games (e.g., Game 28 and 30), we lost the Union capital and key cities because our armies remained stationary drilling while the Confederates marched unopposed.)

**Notebook:**

1. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
2. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
3. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
4. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
5. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.
6. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.

### Version 7, after game 35 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** Across these games we relied far too heavily on endless drilling and building wooden ships while the Rebels aggressively seized cities and built up massive armies. On the standard map, moving Buell to Paducah triggered early friction, but we failed to capitalize or expand our forces through recruitment, leaving our armies outnumbered and outmaneuvered. On the alternate map, our failure to use aggressive moves and reinforcements allowed the Confederacy to secure territory unchecked. To win, we must actively recruit, consolidate forces, and contest enemy advances rather than endlessly drilling.

**Strategy for the next game.** We will immediately pivot from passive drilling to aggressive territorial retention and recruitment. On the standard map, we will secure Paducah early, recruit heavily in major industrial hubs, and actively use rail and move to intercept Rebel advances. On the alternate map, we will prioritize raising forces in key central cities and countering Confederate incursions rather than idling.

**Changes:**

- dropped: When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids. (Constantly sailing fleets into ports led to heavy ship losses early on and did not stop the Rebel land victory condition.)
- added: When an army is adjacent to a vulnerable enemy city with superior strength or favorable odds, use move to capture it rather than remaining idle. (We sat passively drilling while the Rebels captured city after city; we must take the offensive when odds are favorable.)
- added: When cash reserves exceed 400 and recruitment is available, use recruit in major cities to build up powerful regional field armies. (We accumulated surplus cash while our total troop count dwindled relative to the growing Confederate forces.)

**Notebook:**

1. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
2. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
3. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.
4. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.
5. When an army is adjacent to a vulnerable enemy city with superior strength or favorable odds, use move to capture it rather than remaining idle.
6. When cash reserves exceed 400 and recruitment is available, use recruit in major cities to build up powerful regional field armies.

### Version 8, after game 40 (-: review failed; champion v6 restored, 0 turns)

**Diagnosis.** 

**Strategy for the next game.** We will maintain aggressive recruitment in secure cities and balanced drilling while immediately pivoting to intercept and defend against Confederate advances toward our capital and vital cities, ensuring our supply lines remain intact.

**Notebook:**

1. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
2. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
3. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
4. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
5. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.
6. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.

### Version 9, after game 45 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** In these games, our armies spent too many turns continuously drilling while ignoring enemy advances and supply lines, leading to supply exhaustion, poor combat odds, and eventual collapse of our territory and capital. We must prioritize supplying armies before they starve, fortifying key cities, and concentrating for defense rather than endless drills.

**Strategy for the next game.** We will strictly monitor army supply levels to prevent starvation and zero-supply penalties, maintain defensive concentrations around vital cities and the capital, and expand recruitment when funds permit rather than over-drilling.

**Changes:**

- dropped: When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids. (Keeping standard lessons consistent with current record performance while reinforcing supply and defense priorities.)

**Notebook:**

1. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
2. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.
3. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
4. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
5. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
6. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.

### Version 10, after game 50 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** In these training games, our armies spent excessive turns drilling while the Confederacy aggressively captured strategic cities and accumulated superior numbers. On the alternate map, we neglected recruitment and expansion, leaving our forces too small to resist rebel advances. On the standard map, while we attempted an opening push into Paducah, our armies remained passive and failed to secure vital territory or prevent the loss of our capital. To succeed, we must balance drilling with aggressive recruitment, timely defensive concentrations, and proactive city captures.

**Strategy for the next game.** We will aggressively recruit in secure cities during the early turns to expand our troop numbers, maintain disciplined drilling for experienced units, and use rail and movement orders to quickly intercept rebel advances toward Washington and key supply centers.

**Changes:**

- revised: When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling. (We failed to recruit in alternate map games, leaving our total troop count severely stagnated while the enemy expanded.)
- revised: When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills. (We allowed rebel columns to capture Washington and Philadelphia while our armies were occupied drilling.)

**Notebook:**

1. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
2. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.
3. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
4. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
5. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
6. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.

### Version 11, after game 55 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** In these games, our excessive drilling without active expansion, recruitment, or aggressive defensive maneuvering allowed the Confederate computer to steadily accumulate cities, outnumber us, and achieve technical victories. While drilling increases experience, failing to recruit, expand, or properly counter enemy movements leaves our armies isolated, starved of supply, and eventually overwhelmed. We must balance experience building with proactive recruitment and decisive counter-attacks.

**Strategy for the next game.** Our strategy for the next games will focus on aggressive recruitment and reinforcement to counter Confederate numerical superiority, ensuring our armies are adequately supplied and positioned defensively rather than idling and drilling while the enemy captures cities.

**Changes:**

- revised: When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn. (Retained as a fundamental rule to prevent supply attrition and army destruction.)
- revised: When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills. (Retained to ensure defensive responsiveness against Confederate advances.)
- revised: When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling. (Retained to emphasize building troop numbers rather than endless drilling.)

**Notebook:**

1. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
2. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.
3. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
4. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
5. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
6. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.

### Version 12, after game 60 (alternate: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** In these games, our armies spent too much time continuously drilling instead of expanding our military forces via recruitment or actively capturing and defending territory. We accumulated large cash reserves while the Rebels steadily outgrew and out-flanked us, eventually capturing our capital or seizing enough cities for victory.

**Strategy for the next game.** We will balance our focus between maintaining sufficient military strength through recruitment and strategic positioning, avoiding prolonged inactivity or excessive drilling while ensuring critical supply lines and capitals are well defended.

**Changes:**

- revised: When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling. (We must prioritize building up our troop numbers and expanding our active armies rather than idling away turns drilling when cash is abundant.)

**Notebook:**

1. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
2. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
3. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.
4. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
5. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
6. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.

### Version 13, after game 65 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** In these training games, we continued to rely heavily on drilling core armies while neglecting territorial expansion and timely offensive maneuvers. Although drilling raises experience, it leaves our forces idle while the Confederacy captures critical cities and out-expands our income base. Our fleet engagements were handled reasonably well initially, but our failure to aggressively press territorial control and protect supply lines led to repeated defeats by city control or time.

**Strategy for the next game.** Next game, we will balance experience-building through drilling with proactive recruitment and decisive offensive and defensive maneuvers. We will prioritize securing key cities early, maintaining strong supply lines, and utilizing our fleet and rail network to respond rapidly to Confederate threats before they can overwhelm our income and territorial integrity.

**Changes:**

- revised: When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills. (Ensures we react promptly to enemy advances rather than passively drilling while losing territory.)
- revised: When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling. (Emphasizes force expansion over endless drilling to match Confederate numbers.)

**Notebook:**

1. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
2. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.
3. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
4. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
5. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
6. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.

### Version 14, after game 70 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** In Training Round 14, notebook v13 performed worse than our baseline notebook v9, averaging +1.00 compared to +2.80. Across our test games (Games 66-70), our armies relied too heavily on endless drilling while the Confederacy aggressively captured strategic cities and territory, leading to technical defeats. We must shift from passive drilling to active defense, fortifying vulnerable border positions, capturing enemy cities, and expanding our forces via recruitment.

**Strategy for the next game.** We will prioritize immediate defensive consolidation and strategic recruitment in the opening turns, fortifying key border cities to halt Confederate advances while using our naval fleet actively to contest enemy ports.

**Changes:**

- dropped: When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn. (Reordered priority to keep defensive concentration and recruitment rules ahead of routine supply maintenance.)

**Notebook:**

1. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.
2. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
3. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
4. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
5. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.
6. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.

### Version 15, after game 75 (standard: Rebel victory: cities controlled, 11 turns)

**Diagnosis.** In this round of games, our armies spent too much time drilling while the Confederacy aggressively captured territory and cities. On the standard map, our opening push to Paducah succeeded initially, but our main forces became bogged down in endless drilling rather than reinforcing key positions, leading to supply exhaustion and lost cities. On the alternate map, despite heavy recruitment, we failed to coordinate counterattacks effectively against Confederate advances. To achieve victory, we must balance experience-building drills with timely movement, aggressive defense of core supply hubs, a

**Strategy for the next game.** Our overall strategy for the next games is to balance essential force drilling with active territorial defense and prompt resupply. We will secure early footholds, avoid unfavorable attacks, and respond rapidly to Confederate incursions before they can overwhelm our cities.

**Changes:**

- revised: When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills. (Refined wording to emphasize immediate defensive concentration over drilling when vital hubs are threatened, based on prior stable performance.)
- revised: When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling. (Maintained emphasis on expansion via recruitment when safe, supporting steady troop growth.)

**Notebook:**

1. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.
2. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
3. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
4. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
5. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.
6. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.

### Version 16, after game 80 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** In these training games, our armies spent too much time drilling while rebel forces steadily captured strategic cities and accumulated control. On the alternate map we successfully expanded our military strength, but we failed to use movement orders to check rebel advances or counterattack effectively. On the standard map, we suffered from critical supply failures because we did not monitor or resupply armies promptly, leading to attrition and defeat.

**Strategy for the next game.** We will maintain a balanced approach of recruiting aggressively to build superior numbers, keeping our armies supplied and well-positioned, and utilizing movement and rail to counter rebel incursions rather than idling on drills while cities fall.

**Changes:**

- revised: When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills. (Retained from v14 as it remains fundamental for capital defense based on historical record.)
- revised: When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn. (Retained from v14 to prevent catastrophic supply attrition as seen in recent standard map games.)

**Notebook:**

1. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.
2. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
3. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
4. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
5. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
6. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.

### Version 17, after game 85 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** In these games, our excessive drilling without proactive offensive expansion allowed the Confederate computer to seize key cities and outnumber us. We also suffered from failing to supply armies promptly, leading to supply exhaustion and lost units.

**Strategy for the next game.** We will focus on stabilizing our supply lines, reinforcing our borders, and avoiding costly uncoordinated attacks while building up our forces for decisive counter-offensives.

**Changes:**

- revised: When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills. (Maintained from notebook v14 as it correctly prioritizes capital defense.)
- revised: When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn. (Maintained from notebook v14 to prevent catastrophic supply depletion.)

**Notebook:**

1. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.
2. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
3. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
4. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
5. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
6. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.

### Version 18, after game 90 (alternate: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** In this round of games, our armies were overly fixated on drilling instead of taking initiative, securing key cities, or responding to enemy captures. We allowed the Rebel computer to freely maneuver and seize cities, resulting in defeat by city control or capital capture. We also had issues with supply management where armies ran out of supply or were blockaded without prompt relief.

**Strategy for the next game.** For the next round, we will strictly adhere to our defensive concentration and timely resupply rules while ensuring our opening moves establish secure footholds without reckless attacks.

**Changes:**

- revised: When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills. (Kept from notebook v14 as it remains our most reliable foundational defensive rule.)

**Notebook:**

1. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.
2. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.
3. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
4. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
5. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
6. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.

### Version 19, after game 95 (standard: Rebel victory: capital captured, 9 turns)

**Diagnosis.** In this round of games, our armies spent too much time continuously drilling while the Confederacy aggressively attacked, captured key hubs, and outflanked our positions. Furthermore, we often neglected regular recruitment and reinforcement to keep our numbers high, leading to gradual attrition and eventual defeat. We must balance experience building with active recruitment, proper supply management, and timely defense of our capital and vital cities.

**Strategy for the next game.** We will prioritize a balanced opening: raise initial troops and reinforce secure cities early, maintain strong defensive lines around vital hubs, use supply management diligently, and avoid reckless attacks while building up our forces before attempting major pushes.

**Changes:**

- revised: When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling. (We failed to recruit aggressively enough in early turns, letting Confederate forces outnumber us over time.)

**Notebook:**

1. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.
2. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
3. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
4. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
5. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.
6. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.

### Version 20, after game 100 (-: final notebook: champion v14, 0 turns)

**Diagnosis.** 

**Strategy for the next game.** We will prioritize immediate defensive consolidation and strategic recruitment in the opening turns, fortifying key border cities to halt Confederate advances while using our naval fleet actively to contest enemy ports.

**Notebook:**

1. When an enemy army threatens our capital or critical supply hubs, use move or rail to concentrate our forces for defense rather than continuing routine drills.
2. When an idle army is in a secure city with recruitment available, use recruit to expand our military strength rather than only drilling.
3. When an army is adjacent to an enemy city with inferior numbers or unfavorable odds, do not move or attack; instead, drill or fortify until superior strength or supply is secured.
4. When a naval fleet is built, use fleet sail to clear or blockade enemy ports rather than engaging in unguided raids.
5. When a new army is raised with recruit, let it rest and do not order it to move on the same turn.
6. When an army has supply 1 or less, use supply <army> immediately before moving or ending the turn.

