# Learning journal: `gemini-c`

Model `gemini-3.5-flash-lite`. 100 training games; notebook version 100 (frozen, sha 077d5b63649dbcc6).

## What it did, game by game

| game | map | notebook | result | turns | recruits | drills | moves | attacks (won) | mean odds | cities peak / end | last-turn cash | refused |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | standard | v0 | decisive loss: Rebel victory: capital captured | 6 | 0 | 10 | 10 | 3 (1) | 46% | 15 / 14 | 434 | 1 |
| 2 | alternate | v1 | decisive loss: Rebel victory: cities controlled | 5 | 7 | 4 | 10 | 1 (0) | 3% | 14 / 10 | 423 | 1 |
| 3 | standard | v2 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 16 | 2 | 0 (0) | - | 12 / 6 | 827 | 0 |
| 4 | alternate | v3 | decisive loss: Rebel victory: cities controlled | 4 | 11 | 10 | 1 | 0 (0) | - | 10 / 9 | 367 | 2 |
| 5 | standard | v4 | decisive loss: Rebel victory: cities controlled | 9 | 12 | 25 | 3 | 1 (0) | 45% | 13 / 7 | 358 | 10 |
| 6 | alternate | v5 | decisive loss: Rebel victory: cities controlled | 8 | 20 | 25 | 0 | 0 (0) | - | 10 / 8 | 376 | 2 |
| 7 | standard | v6 | decisive loss: Rebel victory: cities controlled | 11 | 15 | 25 | 4 | 2 (1) | 52% | 11 / 7 | 269 | 10 |
| 8 | alternate | v7 | decisive loss: Rebel victory: cities controlled | 9 | 15 | 26 | 9 | 2 (1) | 38% | 13 / 9 | 321 | 8 |
| 9 | standard | v8 | decisive loss: Rebel victory: cities controlled | 9 | 8 | 27 | 5 | 2 (0) | 42% | 11 / 6 | 633 | 8 |
| 10 | alternate | v9 | decisive loss: Rebel victory: cities controlled | 5 | 10 | 4 | 6 | 3 (1) | 39% | 11 / 10 | 696 | 0 |
| 11 | standard | v10 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 19 | 3 | 1 (0) | 45% | 11 / 6 | 570 | 3 |
| 12 | alternate | v11 | decisive loss: Rebel victory: cities controlled | 5 | 1 | 27 | 2 | 1 (0) | 30% | 10 / 8 | 1021 | 4 |
| 13 | standard | v12 | decisive loss: Rebel victory: cities controlled | 6 | 3 | 22 | 0 | 0 (0) | - | 11 / 6 | 392 | 1 |
| 14 | alternate | v13 | decisive loss: Rebel victory: cities controlled | 4 | 10 | 13 | 4 | 0 (0) | - | 12 / 10 | 380 | 1 |
| 15 | standard | v14 | decisive loss: Rebel victory: cities controlled | 11 | 17 | 29 | 3 | 2 (2) | 42% | 13 / 7 | 268 | 14 |
| 16 | alternate | v15 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 19 | 0 | 0 (0) | - | 10 / 8 | 706 | 0 |
| 17 | standard | v16 | decisive loss: Rebel victory: cities controlled | 14 | 15 | 22 | 6 | 5 (3) | 50% | 12 / 7 | 277 | 7 |
| 18 | alternate | v17 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 22 | 7 | 3 (2) | 38% | 11 / 9 | 1111 | 4 |
| 19 | standard | v18 | decisive loss: Rebel victory: capital captured | 10 | 10 | 24 | 6 | 2 (0) | 44% | 11 / 9 | 312 | 7 |
| 20 | alternate | v19 | decisive loss: Rebel victory: cities controlled | 10 | 23 | 7 | 10 | 3 (2) | 50% | 11 / 9 | 350 | 5 |
| 21 | standard | v20 | decisive loss: Rebel victory: cities controlled | 7 | 11 | 9 | 9 | 5 (0) | 26% | 11 / 5 | 247 | 11 |
| 22 | alternate | v21 | decisive loss: Rebel victory: cities controlled | 4 | 3 | 0 | 9 | 2 (0) | 23% | 13 / 9 | 921 | 1 |
| 23 | standard | v22 | decisive loss: Rebel victory: capital captured | 2 | 0 | 0 | 6 | 1 (0) | 27% | 13 / 11 | 633 | 0 |
| 24 | alternate | v23 | decisive loss: Rebel victory: cities controlled | 8 | 18 | 10 | 10 | 3 (1) | 47% | 13 / 9 | 366 | 2 |
| 25 | standard | v24 | decisive loss: Rebel victory: capital captured | 8 | 15 | 0 | 10 | 3 (1) | 27% | 12 / 9 | 287 | 4 |
| 26 | alternate | v25 | decisive loss: Rebel victory: cities controlled | 7 | 17 | 25 | 2 | 1 (1) | 57% | 11 / 8 | 362 | 4 |
| 27 | standard | v26 | decisive loss: Rebel victory: cities controlled | 6 | 1 | 12 | 7 | 2 (0) | 32% | 13 / 5 | 1069 | 0 |
| 28 | alternate | v27 | decisive loss: Rebel victory: cities controlled | 7 | 15 | 26 | 3 | 0 (0) | - | 11 / 8 | 345 | 8 |
| 29 | standard | v28 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 17 | 1 | 0 (0) | - | 11 / 5 | 354 | 7 |
| 30 | alternate | v29 | decisive loss: Rebel victory: cities controlled | 10 | 25 | 22 | 4 | 0 (0) | - | 10 / 9 | 366 | 13 |
| 31 | standard | v30 | decisive loss: Rebel victory: capital captured | 5 | 2 | 10 | 7 | 2 (0) | 45% | 13 / 8 | 587 | 4 |
| 32 | alternate | v31 | decisive loss: Rebel victory: cities controlled | 7 | 19 | 22 | 2 | 2 (1) | 51% | 10 / 8 | 349 | 6 |
| 33 | standard | v32 | decisive loss: Rebel victory: cities controlled | 7 | 4 | 20 | 1 | 0 (0) | - | 11 / 4 | 384 | 5 |
| 34 | alternate | v33 | decisive loss: Rebel victory: cities controlled | 5 | 3 | 0 | 4 | 3 (0) | 40% | 10 / 8 | 1020 | 1 |
| 35 | standard | v34 | decisive loss: Rebel victory: cities controlled | 14 | 16 | 19 | 9 | 1 (1) | 53% | 12 / 7 | 243 | 21 |
| 36 | alternate | v35 | decisive loss: Rebel victory: cities controlled | 4 | 9 | 9 | 1 | 0 (0) | - | 10 / 7 | 336 | 2 |
| 37 | standard | v36 | decisive loss: Rebel victory: cities controlled | 11 | 6 | 22 | 1 | 1 (0) | 50% | 11 / 6 | 489 | 9 |
| 38 | alternate | v37 | decisive loss: Rebel victory: share of total income | 6 | 4 | 15 | 7 | 5 (2) | 32% | 10 / 10 | 1530 | 2 |
| 39 | standard | v38 | decisive loss: Rebel victory: cities controlled | 10 | 9 | 7 | 9 | 4 (1) | 48% | 11 / 6 | 252 | 8 |
| 40 | alternate | v39 | decisive loss: Rebel victory: cities controlled | 8 | 15 | 25 | 8 | 2 (2) | 68% | 11 / 9 | 350 | 2 |
| 41 | standard | v40 | decisive loss: Rebel victory: cities controlled | 7 | 3 | 1 | 5 | 3 (1) | 28% | 11 / 4 | 515 | 1 |
| 42 | alternate | v41 | decisive loss: Rebel victory: cities controlled | 6 | 15 | 7 | 2 | 0 (0) | - | 10 / 9 | 335 | 3 |
| 43 | standard | v42 | decisive loss: Rebel victory: cities controlled | 10 | 2 | 11 | 5 | 2 (0) | 35% | 12 / 6 | 287 | 2 |
| 44 | alternate | v43 | decisive loss: Rebel victory: cities controlled | 4 | 4 | 5 | 5 | 3 (1) | 42% | 11 / 9 | 1007 | 1 |
| 45 | standard | v44 | decisive loss: Rebel victory: cities controlled | 12 | 17 | 24 | 10 | 3 (3) | 58% | 11 / 6 | 271 | 16 |
| 46 | alternate | v45 | decisive loss: Rebel victory: cities controlled | 5 | 14 | 9 | 1 | 0 (0) | - | 11 / 9 | 335 | 2 |
| 47 | standard | v46 | decisive loss: Rebel victory: cities controlled | 10 | 11 | 17 | 10 | 1 (0) | 9% | 11 / 6 | 250 | 10 |
| 48 | alternate | v47 | decisive loss: Rebel victory: cities controlled | 5 | 11 | 10 | 2 | 0 (0) | - | 11 / 9 | 549 | 2 |
| 49 | standard | v48 | decisive loss: Rebel victory: cities controlled | 7 | 7 | 1 | 6 | 2 (1) | 50% | 11 / 6 | 290 | 4 |
| 50 | alternate | v49 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 0 | 8 | 1 (0) | 37% | 12 / 7 | 1193 | 0 |
| 51 | standard | v50 | decisive loss: Rebel victory: cities controlled | 16 | 12 | 25 | 1 | 1 (1) | 46% | 11 / 5 | 245 | 14 |
| 52 | alternate | v51 | decisive loss: Rebel victory: cities controlled | 4 | 9 | 15 | 5 | 2 (0) | 34% | 11 / 9 | 347 | 5 |
| 53 | standard | v52 | decisive loss: Rebel victory: cities controlled | 8 | 3 | 20 | 2 | 0 (0) | - | 11 / 6 | 593 | 6 |
| 54 | alternate | v53 | decisive loss: Rebel victory: share of total income | 4 | 12 | 17 | 3 | 0 (0) | - | 12 / 10 | 386 | 2 |
| 55 | standard | v54 | decisive loss: Rebel victory: cities controlled | 11 | 10 | 21 | 7 | 1 (0) | 45% | 11 / 5 | 320 | 20 |
| 56 | alternate | v55 | decisive loss: Rebel victory: cities controlled | 4 | 9 | 0 | 4 | 2 (1) | 46% | 11 / 10 | 819 | 2 |
| 57 | standard | v56 | decisive loss: Rebel victory: cities controlled | 7 | 7 | 3 | 4 | 2 (0) | 35% | 12 / 5 | 245 | 3 |
| 58 | alternate | v57 | decisive loss: Rebel victory: cities controlled | 6 | 14 | 4 | 4 | 2 (2) | 46% | 11 / 8 | 297 | 4 |
| 59 | standard | v58 | decisive loss: Rebel victory: cities controlled | 10 | 9 | 7 | 5 | 0 (0) | - | 13 / 4 | 227 | 16 |
| 60 | alternate | v59 | decisive loss: Rebel victory: cities controlled | 5 | 5 | 19 | 2 | 0 (0) | - | 10 / 6 | 697 | 4 |
| 61 | standard | v60 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 9 | 3 (2) | 43% | 13 / 6 | 849 | 0 |
| 62 | alternate | v61 | decisive loss: Rebel victory: cities controlled | 4 | 3 | 22 | 1 | 0 (0) | - | 10 / 9 | 489 | 5 |
| 63 | standard | v62 | decisive loss: Rebel victory: cities controlled | 11 | 7 | 20 | 7 | 2 (0) | 27% | 13 / 6 | 203 | 9 |
| 64 | alternate | v63 | decisive loss: Rebel victory: cities controlled | 5 | 8 | 14 | 2 | 0 (0) | - | 11 / 9 | 820 | 5 |
| 65 | standard | v64 | decisive loss: Rebel victory: cities controlled | 8 | 5 | 16 | 7 | 2 (0) | 32% | 13 / 6 | 396 | 5 |
| 66 | alternate | v65 | decisive loss: Rebel victory: cities controlled | 9 | 6 | 27 | 6 | 2 (1) | 36% | 11 / 6 | 842 | 9 |
| 67 | standard | v66 | decisive loss: Rebel victory: cities controlled | 7 | 14 | 21 | 8 | 2 (1) | 42% | 13 / 6 | 215 | 10 |
| 68 | alternate | v67 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 0 | 12 | 0 (0) | - | 13 / 6 | 1356 | 0 |
| 69 | standard | v68 | decisive loss: Rebel victory: cities controlled | 16 | 12 | 18 | 24 | 10 (4) | 45% | 14 / 6 | 281 | 18 |
| 70 | alternate | v69 | decisive loss: Rebel victory: cities controlled | 12 | 28 | 31 | 6 | 2 (1) | 46% | 13 / 10 | 355 | 11 |
| 71 | standard | v70 | decisive loss: Rebel victory: cities controlled | 7 | 3 | 17 | 6 | 1 (1) | 57% | 13 / 6 | 341 | 3 |
| 72 | alternate | v71 | decisive loss: Rebel victory: cities controlled | 22 | 41 | 36 | 11 | 3 (0) | 36% | 13 / 10 | 352 | 16 |
| 73 | standard | v72 | decisive loss: Rebel victory: cities controlled | 16 | 18 | 21 | 11 | 5 (3) | 62% | 11 / 6 | 216 | 18 |
| 74 | alternate | v73 | decisive loss: Rebel victory: cities controlled | 7 | 2 | 0 | 9 | 2 (1) | 46% | 13 / 9 | 900 | 0 |
| 75 | standard | v74 | decisive loss: Rebel victory: cities controlled | 10 | 12 | 23 | 9 | 4 (2) | 54% | 13 / 6 | 303 | 4 |
| 76 | alternate | v75 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 10 | 2 (1) | 44% | 13 / 10 | 1304 | 0 |
| 77 | standard | v76 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 7 | 5 | 2 (0) | 28% | 13 / 6 | 1189 | 1 |
| 78 | alternate | v77 | decisive loss: Rebel victory: cities controlled | 6 | 12 | 9 | 6 | 2 (0) | 44% | 10 / 9 | 495 | 4 |
| 79 | standard | v78 | decisive loss: Rebel victory: cities controlled | 12 | 20 | 23 | 7 | 3 (1) | 47% | 12 / 6 | 251 | 17 |
| 80 | alternate | v79 | decisive loss: Rebel victory: cities controlled | 12 | 27 | 25 | 6 | 2 (0) | 30% | 11 / 8 | 348 | 8 |
| 81 | standard | v80 | decisive loss: Rebel victory: capital captured | 11 | 11 | 22 | 7 | 1 (0) | 40% | 11 / 9 | 962 | 12 |
| 82 | alternate | v81 | decisive loss: Rebel victory: cities controlled | 5 | 13 | 6 | 5 | 2 (0) | 22% | 12 / 9 | 388 | 3 |
| 83 | standard | v82 | decisive loss: Rebel victory: cities controlled | 7 | 3 | 9 | 5 | 2 (0) | 43% | 13 / 6 | 273 | 4 |
| 84 | alternate | v83 | decisive loss: Rebel victory: cities controlled | 13 | 16 | 32 | 4 | 3 (3) | 64% | 12 / 9 | 365 | 8 |
| 85 | standard | v84 | decisive loss: Rebel victory: capital captured | 2 | 0 | 0 | 4 | 0 (0) | - | 12 / 11 | 626 | 0 |
| 86 | alternate | v85 | decisive loss: Rebel victory: cities controlled | 8 | 14 | 33 | 1 | 0 (0) | - | 10 / 8 | 326 | 7 |
| 87 | standard | v86 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 0 | 8 | 3 (1) | 36% | 14 / 6 | 713 | 0 |
| 88 | alternate | v87 | decisive loss: Rebel victory: cities controlled | 12 | 29 | 36 | 3 | 0 (0) | - | 12 / 8 | 327 | 14 |
| 89 | standard | v88 | decisive loss: Rebel victory: capital captured | 2 | 0 | 0 | 5 | 1 (0) | 33% | 13 / 11 | 533 | 0 |
| 90 | alternate | v89 | decisive loss: Rebel victory: cities controlled | 8 | 18 | 28 | 7 | 2 (2) | 64% | 12 / 9 | 328 | 6 |
| 91 | standard | v90 | decisive loss: Rebel victory: capital captured | 4 | 2 | 0 | 7 | 2 (0) | 24% | 13 / 12 | 625 | 0 |
| 92 | alternate | v91 | decisive loss: Rebel victory: cities controlled | 6 | 13 | 17 | 0 | 0 (0) | - | 10 / 8 | 357 | 3 |
| 93 | standard | v92 | decisive loss: Rebel victory: capital captured | 2 | 0 | 0 | 5 | 1 (0) | 23% | 13 / 11 | 532 | 0 |
| 94 | alternate | v93 | decisive loss: Rebel victory: share of total income | 3 | 8 | 0 | 2 | 0 (0) | - | 10 / 8 | 345 | 4 |
| 95 | standard | v94 | decisive loss: Rebel victory: capital captured | 2 | 0 | 4 | 6 | 1 (0) | 23% | 13 / 11 | 532 | 0 |
| 96 | alternate | v95 | decisive loss: Rebel victory: cities controlled | 4 | 6 | 0 | 4 | 2 (1) | 44% | 10 / 9 | 625 | 1 |
| 97 | standard | v96 | decisive loss: Rebel victory: capital captured | 2 | 0 | 0 | 6 | 1 (0) | 23% | 13 / 12 | 533 | 0 |
| 98 | alternate | v97 | decisive loss: Rebel victory: cities controlled | 6 | 11 | 0 | 5 | 3 (1) | 38% | 10 / 8 | 574 | 0 |
| 99 | standard | v98 | decisive loss: Rebel victory: capital captured | 13 | 5 | 9 | 10 | 4 (4) | 53% | 14 / 7 | 239 | 1 |
| 100 | alternate | v99 | decisive loss: Rebel victory: cities controlled | 5 | 4 | 3 | 3 | 2 (0) | 44% | 10 / 7 | 884 | 2 |

## How the notebook changed

### Version 1, after game 1 (standard: Rebel victory: capital captured, 6 turns)

**Diagnosis.** The game was lost because we neglected to recruit troops to grow our armies while over-focusing on building ships and drilling, leaving our forces too small to hold territory against concentrated Confederate counter-attacks.

**Strategy for the next game.** Next game we will aggressively recruit to build up large armies, maintain proper supply lines, and use our superior numbers to push directly into enemy territory while safeguarding our capital.

**Changes:**

- added: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (We failed to recruit any new troops in the game, leaving our total manpower stagnant while the enemy grew stronger.)
- added: When an army is adjacent to an enemy-held city with inferior strength, use move <army> <city> to capture it. (We need clear, aggressive movement rules to secure territory and protect our capital.)
- added: When an army has 1 or less supply, use supply <army> before moving or fighting. (McClellan ran out of supplies in Louisville, severely hindering combat effectiveness.)
- added: When an army is idle in a safe city and needs experience, use drill <army>. (We wasted turns drilling active or vulnerable fronts instead of securing positions.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy-held city with inferior strength, use move <army> <city> to capture it.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.

### Version 2, after game 2 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We pushed isolated armies into enemy strongholds without checking defensive strength or ensuring numerical superiority, leading to the destruction of Buell's army at Nashville and Pope's armies in the west. We also neglected to build up our forces before advancing into hostile territory.

**Strategy for the next game.** We will focus on building up strong, supplied forces in secure rear areas before launching coordinated advances. We will avoid attacking fortified enemy positions with small or outnumbered armies and maintain our economic base.

**Changes:**

- revised: When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack. (We attacked into Nashville and other cities at terrible odds (3% and lower), causing our armies to be crushed. We must ensure superior strength before attacking.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.

### Version 3, after game 3 (standard: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We hoarded cash and spent all our time drilling instead of recruiting men or capturing enemy cities. The Rebels outmaneuvered us, captured our territory, and won by city count while we sat idle.

**Strategy for the next game.** We must stop over-drilling and start actively recruiting and attacking enemy positions to capture cities and prevent a Confederate victory.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.

### Version 4, after game 4 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while failing to capture enemy cities or aggressively expand our territory. Although our total troop count grew significantly, the Confederacy steadily captured cities and achieved their victory condition of controlling 28 cities.

**Strategy for the next game.** Next game we will aggressively march our reinforced armies into adjacent enemy cities to capture territory and prevent the Confederacy from reaching the city control threshold, balancing recruitment with constant offensive pressure.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.

### Version 5, after game 5 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused heavily on drilling and recruiting while ignoring supply management and strategic attacks. Several supply commands were refused because armies were out of position or funds were low, causing our armies to run out of supply and lose combat effectiveness against growing Confederate forces.

**Strategy for the next game.** We will maintain our focus on steady recruitment and selective attacks when we hold a 2:1 numerical advantage, while ensuring we carefully monitor our supply lines and treasury to keep our armies combat-effective.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.

### Version 6, after game 6 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused excessively on drilling and recruiting while completely neglecting offensive operations and map control. Although our troop numbers grew significantly, we allowed the Rebels to capture cities uncontested and dictate the strategic initiative, leading to a technical defeat via city count.

**Strategy for the next game.** We will continue to recruit and maintain our forces, but we must actively use move commands to attack vulnerable enemy-held cities and capture territory to prevent the Confederacy from winning through uncontested city control.

**Changes:**

- added: When an army has sufficient strength and is adjacent to a weakly held enemy city, use move <army> <city> to capture territory and expand our income. (We lost this game entirely because we never attacked or captured enemy cities, focusing too much on drilling while the enemy claimed 28 cities.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.
5. When an army has sufficient strength and is adjacent to a weakly held enemy city, use move <army> <city> to capture territory and expand our income.

### Version 7, after game 7 (standard: Rebel victory: cities controlled, 11 turns)

**Diagnosis.** We successfully recruited and built a large force, but we relied far too heavily on drilling while the Rebels actively captured our territory and blockaded Philadelphia. We failed to aggressively push out and defend our cities, allowing the Confederacy to slowly strangle our economy and achieve a city-count victory.

**Strategy for the next game.** Next game we will maintain our strong recruitment policy, but instead of spending all our turns drilling, we will use our superior numbers to aggressively attack rebel-held cities, keep our supply lines open, and prevent the enemy from surrounding and neutralizing our core economic ports.

**Changes:**

- dropped: When an army has sufficient strength and is adjacent to a weakly held enemy city, use move <army> <city> to capture territory and expand our income. (This was too vague and was subsumed by our general need to maintain a coherent offensive and defensive posture.)
- added: When an enemy fleet blockades one of our ports or threatens our income, use move <army> <city> to clear adjacent enemy forces and relieve the port. (In this game, the Rebel fleet blockaded Philadelphia and eventually neutralized it because our land forces did not clear out nearby enemy threats in time.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.
5. When an enemy fleet blockades one of our ports or threatens our income, use move <army> <city> to clear adjacent enemy forces and relieve the port.

### Version 8, after game 8 (alternate: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while failing to concentrate our superior numbers for decisive offensives or defensive consolidation. The Rebels used interior rail lines and aggressive counterattacks to steadily push us back and capture our vital cities.

**Strategy for the next game.** We will continue to systematically recruit in major cities and maintain supply lines while pressing our numerical advantage into targeted attacks on adjacent enemy-held cities.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.
5. When an enemy fleet blockades one of our ports or threatens our income, use move <army> <city> to clear adjacent enemy forces and relieve the port.

### Version 9, after game 9 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused too heavily on drilling while letting our army counts stagnate and allowing enemy forces to outmaneuver us. We neglected recruitment after the early game and failed to maintain proper supply lines, leading to isolated forces running out of supply, blockades at Philadelphia, and repeated failed attacks at poor odds.

**Strategy for the next game.** We will maintain a steady recruitment program to build numerical superiority, keep our armies well-supplied to avoid combat penalties, and concentrate our forces for decisive attacks against weakened enemy positions while protecting our vital cities and ports.

**Changes:**

- revised: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (We failed to recruit enough new armies in the mid-game, leaving us outnumbered in key sectors.)
- revised: When an army has 1 or less supply, use supply <army> before moving or fighting. (Our armies repeatedly went out of supply in Washington and elsewhere, severely hurting combat effectiveness.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.
5. When an enemy fleet blockades one of our ports or threatens our income, use move <army> <city> to clear adjacent enemy forces and relieve the port.

### Version 10, after game 10 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** The game was lost because we repeatedly attacked Confederate armies in cities without a clear 2:1 numerical advantage, resulting in costly defeats and lost momentum. Additionally, we neglected to fortify key positions and deal with enemy naval blockades promptly, which drained our forces and let the Rebels secure the city count victory.

**Strategy for the next game.** Next game, we will focus heavily on accumulating a 2:1 or greater force ratio before initiating any attacks on enemy-held cities. We will consistently recruit in high-value cities, keep our armies well-supplied, and use fortify on frontline cities to withstand Confederate pressure while we build up our overall strength.

**Changes:**

- added: When a critical frontier city is captured or vulnerable, use fortify <city> to double its defensive strength. (We lost control of key cities quickly because we never used the fortify command to make our defenses resilient against enemy counter-attacks.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.
5. When an enemy fleet blockades one of our ports or threatens our income, use move <army> <city> to clear adjacent enemy forces and relieve the port.
6. When a critical frontier city is captured or vulnerable, use fortify <city> to double its defensive strength.

### Version 11, after game 11 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused heavily on drilling and ship building while neglecting recruitment, leaving our forces too small to hold territory against the advancing Confederates. We lost key cities and income because we did not recruit new troops or adequately reinforce our armies.

**Strategy for the next game.** We will aggressively recruit new armies using our treasury funds, maintain sufficient supply lines, and use overwhelming local force to capture and hold enemy cities while securing our own.

**Changes:**

- dropped: When a critical frontier city is captured or vulnerable, use fortify <city> to double its defensive strength. (It had a poor record and did not prevent the loss of territory when our active army strength was too low.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.
5. When an enemy fleet blockades one of our ports or threatens our income, use move <army> <city> to clear adjacent enemy forces and relieve the port.

### Version 12, after game 12 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** In this game, we relied too heavily on drilling and spent most of our turns passing up offensive opportunities while the Confederate computer expanded rapidly, captured cities, and concentrated massive forces. We failed to recruit or launch coordinated attacks, leading to a quick loss of city control.

**Strategy for the next game.** Next game, we will shift focus from constant drilling to aggressive recruiting, moving, and capturing enemy cities to prevent the Confederacy from seizing the map early.

**Changes:**

- dropped: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (Kept the exact text, record remains stable.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.
5. When an enemy fleet blockades one of our ports or threatens our income, use move <army> <city> to clear adjacent enemy forces and relieve the port.

### Version 13, after game 13 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We relied excessively on drill commands while failing to recruit new armies or aggressively capture enemy cities. Although our troops gained experience, we lost crucial cities and allowed the Confederacy to steadily expand its territory and military strength until we were overwhelmed.

**Strategy for the next game.** In the next game, we will shift focus from constant drilling to aggressive recruitment and coordinated attacks on enemy cities to secure territory and protect our income.

**Changes:**

- revised: When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack. (We failed to execute offensive operations in this game, leading to passive defense and loss of territory.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.
5. When an enemy fleet blockades one of our ports or threatens our income, use move <army> <city> to clear adjacent enemy forces and relieve the port.

### Version 14, after game 14 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused heavily on recruiting and drilling inside our cities while allowing the Confederate armies to maneuver unchecked and capture our territory. We initiated almost no attacks and failed to contest key enemy movements, leading to a rapid loss of city control.

**Strategy for the next game.** Next game we will maintain our focus on steady recruitment and maintaining supply lines, while aggressively pressing attacks against vulnerable enemy-held cities instead of remaining passive.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.
5. When an enemy fleet blockades one of our ports or threatens our income, use move <army> <city> to clear adjacent enemy forces and relieve the port.

### Version 15, after game 15 (standard: Rebel victory: cities controlled, 11 turns)

**Diagnosis.** We focused heavily on drilling and recruiting but neglected strategic movement, fortifying, merging, and naval operations. Without expanding our territory or defending key cities, the Rebels steadily captured our towns and achieved victory.

**Strategy for the next game.** We will continue to recruit aggressively and maintain our supply lines while looking for advantageous attacks to expand our city control.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.
5. When an enemy fleet blockades one of our ports or threatens our income, use move <army> <city> to clear adjacent enemy forces and relieve the port.

### Version 16, after game 16 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused entirely on drilling existing armies and building wooden ships while completely ignoring recruitment and expansion. Without recruiting new forces to hold and capture territory, the Confederacy easily outmaneuvered us and seized our cities, leading to a rapid defeat.

**Strategy for the next game.** Next game, we will strictly follow our recruitment policy to build up our troop counts alongside drilling, and we will actively attack vulnerable enemy positions instead of remaining passive.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.
5. When an enemy fleet blockades one of our ports or threatens our income, use move <army> <city> to clear adjacent enemy forces and relieve the port.

### Version 17, after game 17 (standard: Rebel victory: cities controlled, 14 turns)

**Diagnosis.** We focused heavily on drilling and recruiting but failed to maintain sufficient supply for our main armies, causing them to repeatedly run out of supplies and lose combat effectiveness. Furthermore, we allowed the Rebel fleet to continually bombard Philadelphia and seize our northern territory without an effective naval or land counter-offensive.

**Strategy for the next game.** We will continue to recruit and drill our core armies while strictly monitoring supply lines to prevent armies from going out of supply. We will also prioritize offensive movements with overwhelming numerical advantage to secure enemy cities and protect our capital.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.
5. When an enemy fleet blockades one of our ports or threatens our income, use move <army> <city> to clear adjacent enemy forces and relieve the port.

### Version 18, after game 18 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused excessively on drilling and building ships while neglecting army recruitment and reinforcement. With a starting strength of only 39,100 men, we were heavily outnumbered and unable to sustain offensive pressure or defend key cities against growing Confederate forces.

**Strategy for the next game.** We will prioritize regular recruitment and reinforcement using our growing treasury to expand our total army strength, ensuring we outnumber the enemy before initiating attacks while maintaining proper supply lines.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an army is idle in a safe city and needs experience, use drill <army>.
5. When an enemy fleet blockades one of our ports or threatens our income, use move <army> <city> to clear adjacent enemy forces and relieve the port.

### Version 19, after game 19 (standard: Rebel victory: capital captured, 10 turns)

**Diagnosis.** We focused heavily on drilling while the enemy captured key positions and our capital. We failed to defend Washington or properly coordinate offensives, and our attacks were conducted at poor odds.

**Strategy for the next game.** We will prioritize defending our capital and core cities, maintain adequate supply for all active forces, recruit regularly to keep our strength up, and only attack when odds are heavily in our favor.

**Changes:**

- dropped: When an army is idle in a safe city and needs experience, use drill <army>. (Drilling too often left our armies unprepared to meet enemy advances and contributed to our defeat.)
- added: When an enemy army is adjacent to our capital or threatens our core cities, use move <army> <city> to intercept and defend. (We allowed the rebels to capture Washington because we lacked a direct defensive instruction for threatened core cities.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army is adjacent to our capital or threatens our core cities, use move <army> <city> to intercept and defend.
5. When our capital or a vital seaport is under direct threat or attack, use move <army> <city> to clear adjacent enemy forces.

### Version 20, after game 20 (alternate: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We successfully built up a massive army and grew our manpower to over 186,000, but we suffered from severe supply issues and constant rebel naval blockades on Philadelphia that cut off our capital's supply. We relied too much on drilling and failed to use our fleet to counter enemy blockades or project power, allowing the Confederates to control the pace and eventually claim 28 cities for victory.

**Strategy for the next game.** We will continue to aggressively recruit in our core cities and maintain our armies' supply lines, but we must prioritize building ships to contest enemy blockades on Philadelphia and maintain our income and supply flow to secure a victory.

**Changes:**

- added: When an enemy fleet is blockading our seaport, use build ironclad or build wooden to rebuild our fleet and use fleet sail to engage and break the blockade. (The rebel fleet continually blockaded Philadelphia, causing our armies to run out of supplies and losing us the game on city control.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army is adjacent to our capital or threatens our core cities, use move <army> <city> to intercept and defend.
5. When our capital or a vital seaport is under direct threat or attack, use move <army> <city> to clear adjacent enemy forces.
6. When an enemy fleet is blockading our seaport, use build ironclad or build wooden to rebuild our fleet and use fleet sail to engage and break the blockade.

### Version 21, after game 21 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We lost in 7 turns because our armies repeatedly attacked enemy forces at unfavorable odds (averaging 26%) without sufficient numerical superiority or supply. We neglected to consolidate or fortify key positions, drained our treasury with inefficient recruitment while running low on cash, and allowed enemy armies to outmaneuver and crush our scattered forces.

**Strategy for the next game.** Next game, we will focus on consolidating our forces before attacking, ensuring every offensive has at least a 2:1 advantage, keeping our armies well supplied, and avoiding reckless attacks against entrenched or superior enemy forces.

**Changes:**

- dropped: When an enemy fleet is blockading our seaport, use build ironclad or build wooden to rebuild our fleet and use fleet sail to engage and break the blockade. (Naval operations were a distraction from the land war and caused us to lose turns and control while our armies suffered on land.)
- added: When an army has multiple small friendly forces in the same city, use join <city> to consolidate them into a stronger single force before moving. (We kept separate small armies that fought individually and lost; we need to merge them to achieve superior combat strength.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army is adjacent to our capital or threatens our core cities, use move <army> <city> to intercept and defend.
5. When our capital or a vital seaport is under direct threat or attack, use move <army> <city> to clear adjacent enemy forces.
6. When an army has multiple small friendly forces in the same city, use join <city> to consolidate them into a stronger single force before moving.

### Version 22, after game 22 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** The Union forces engaged in uncoordinated attacks against superior Confederate numbers and fortifications without adequate supply lines, leading to catastrophic losses in Louisville and the rapid loss of core cities.

**Strategy for the next game.** Focus strictly on recruiting men to build up large armies, maintaining proper supply lines before advancing, and defending core territories without overextending into disadvantageous attacks against fortified Confederate positions.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army is adjacent to our capital or threatens our core cities, use move <army> <city> to intercept and defend.
5. When our capital or a vital seaport is under direct threat or attack, use move <army> <city> to clear adjacent enemy forces.
6. When an army has multiple small friendly forces in the same city, use join <city> to consolidate them into a stronger single force before moving.

### Version 23, after game 23 (standard: Rebel victory: capital captured, 2 turns)

**Diagnosis.** The game was lost in two turns because armies moved out without supporting supply lines or sufficient concentration, leaving Washington completely undefended against Jackson's rapid advance while offensive attacks like Buell into Louisville were launched at terrible odds (27%).

**Strategy for the next game.** Next game, prioritize keeping the capital heavily defended and supplied, avoid low-odds attacks, and build up solid forces through recruitment and consolidation before any offensive marches.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army is adjacent to our capital or threatens our core cities, use move <army> <city> to intercept and defend.
5. When our capital or a vital seaport is under direct threat or attack, use move <army> <city> to clear adjacent enemy forces.
6. When an army has multiple small friendly forces in the same city, use join <city> to consolidate them into a stronger single force before moving.

### Version 24, after game 24 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We successfully recruited and grew our army size, but we attacked with insufficient odds (averaging 47% success rate in battles) and failed to use supply and fortify commands when holding key positions. This allowed Confederate counterattacks to chip away at our forces and eventually overrun our lines.

**Strategy for the next game.** We will continue to aggressively recruit in available cities to build numerical superiority, but we will strictly wait for favorable 2:1 odds and ensure all attacking armies are fully supplied before engaging in combat.

**Changes:**

- revised: When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack. (We launched attacks at poor odds below 2:1 and suffered heavy casualties; we must strictly enforce the 2:1 ratio before attacking.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army is adjacent to our capital or threatens our core cities, use move <army> <city> to intercept and defend.
5. When our capital or a vital seaport is under direct threat or attack, use move <army> <city> to clear adjacent enemy forces.
6. When an army has multiple small friendly forces in the same city, use join <city> to consolidate them into a stronger single force before moving.

### Version 25, after game 25 (standard: Rebel victory: capital captured, 8 turns)

**Diagnosis.** We focused heavily on recruiting and scattered offensive advances without sufficient concentration or protecting our capital. While we successfully built up our total troop numbers, we allowed Stonewall Jackson to march completely unchecked into Washington and capture our capital in May 1862.

**Strategy for the next game.** We will continue aggressively recruiting and building our forces, but we must maintain a dedicated defensive garrison around Washington to prevent any surprise enemy captures of our capital while pushing our main armies forward.

**Changes:**

- revised: When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital. (Previous defense rules were too vague and did not trigger a specific interception when Washington itself was left undefended against Jackson's march.)
- added: When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately. (We lost the game entirely because we ignored Confederate movements targeting our capital while launching distant offensive pushes.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.

### Version 26, after game 26 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We captured Richmond early and grew our total troop count to over 160,000, but we spent almost every turn drilling instead of expanding our territory. Meanwhile, the Confederacy calmly swept across the western cities, seizing enough control points to trigger a technical victory. We neglected offensive movement and city capture.

**Strategy for the next game.** We must balance recruiting and reinforcement with aggressive forward movement. Instead of spending every turn drilling existing forces, we will direct our growing armies to capture neutral and enemy cities to prevent the Confederacy from securing a point-based victory.

**Changes:**

- added: When an idle army is fully supplied and not adjacent to a major threat, use move <army> <city> to capture adjacent neutral or enemy cities instead of drilling. (We lost this game because we drilled incessantly and let the AI capture enough cities to win on points, ignoring the core objective of seizing territory.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an idle army is fully supplied and not adjacent to a major threat, use move <army> <city> to capture adjacent neutral or enemy cities instead of drilling.

### Version 27, after game 27 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We performed poorly because we launched several uncoordinated attacks against defended cities with inferior odds, lost key territory, and spent too many turns drilling while the enemy consolidated strength and outflanked us.

**Strategy for the next game.** Next game, we will focus on building up our core armies, keeping them well-supplied, and strictly avoiding attacks unless we hold at least a 2:1 advantage. We will prioritize securing our heartland and recruiting heavily over premature offensives.

**Changes:**

- dropped: When an idle army is fully supplied and not adjacent to a major threat, use move <army> <city> to capture adjacent neutral or enemy cities instead of drilling. (Led to uncoordinated movements and failed attacks against enemy concentrations.)
- added: When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds. (Prevent us from throwing away men in unfavorable attacks like the ones against Columbus and Fort Donelson.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.

### Version 28, after game 28 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while allowing the Confederacy to capture key cities and build massive armies unchecked. Although our troop numbers grew, we failed to attack vulnerable enemy positions or project offensive power, letting the Rebels control the initiative and steadily capture our territory until achieving victory.

**Strategy for the next game.** We will continue to recruit and reinforce our armies while actively seeking out opportunities to attack isolated Confederate forces when we have superior numbers. We must balance our defensive posture in Washington and key cities with aggressive movements to capture enemy territory and prevent the Rebels from dictating the pace of the war.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.

### Version 29, after game 29 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused heavily on drilling rather than recruiting and expanding our territory or defending key lines, allowing the Confederates to overrun our cities and capture Washington. We failed to maintain our troop numbers and let our supply lines collapse.

**Strategy for the next game.** Next game, we will prioritize recruiting new troops, keeping our armies supplied, expanding our city control, and defending Washington aggressively against Rebel advances.

**Changes:**

- revised: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (We failed to recruit in this game and our troop numbers dwindled, making this essential for survival.)
- revised: When an army has 1 or less supply, use supply <army> before moving or fighting. (We repeatedly ran out of supplies and suffered attrition because armies were not supplied promptly.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.

### Version 30, after game 30 (alternate: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We focused heavily on recruiting and drilling large static armies while neglecting offensive expansion and city capture. Although our troop count grew significantly, we failed to press our advantage or attack enemy territory, allowing the Confederacy to steadily capture cities and achieve a time/city victory by October 1862.

**Strategy for the next game.** Next game, we will recruit and build up our forces early, but immediately transition to aggressive movement and attacks against vulnerable Confederate-held cities once our armies achieve numerical superiority, preventing the enemy from out-expanding us.

**Changes:**

- added: When our armies outnumber an adjacent enemy city's garrison 2:1 and have full supply, use move <army> <city> to capture enemy territory and increase our income. (We failed to press the attack in previous games, allowing the enemy to win by city count. We must actively capture enemy territory instead of only recruiting and drilling.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our armies outnumber an adjacent enemy city's garrison 2:1 and have full supply, use move <army> <city> to capture enemy territory and increase our income.

### Version 31, after game 31 (standard: Rebel victory: capital captured, 5 turns)

**Diagnosis.** We focused heavily on drilling rather than actively recruiting and reinforcing our armies. This left our troop numbers stagnant while the Rebels grew significantly, allowing them to outflank us, capture Washington, and secure a swift victory.

**Strategy for the next game.** Next game, we will prioritize regular recruitment in major cities to build up our manpower advantage, ensure adequate supply lines before every operation, and maintain a strong defensive posture around Washington to prevent any early capital losses while systematically pushing into enemy territory.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our armies outnumber an adjacent enemy city's garrison 2:1 and have full supply, use move <army> <city> to capture enemy territory and increase our income.

### Version 32, after game 32 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We built a large army through excessive recruiting and drilling, but failed to conduct offensive operations to capture enemy cities. Our passivity allowed the Confederate forces to concentrate, seize key territory, and achieve victory through city control.

**Strategy for the next game.** Next game we will maintain our focus on recruiting and supplying our forces while aggressively moving to attack adjacent enemy cities whenever we hold a numerical advantage, preventing the enemy from out-expanding us.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our armies outnumber an adjacent enemy city's garrison 2:1 and have full supply, use move <army> <city> to capture enemy territory and increase our income.

### Version 33, after game 33 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We spent almost all our actions drilling instead of recruiting, capturing cities, or maintaining supply lines. Our armies stagnated in place, allowing the Rebels to capture our territory, cut our income, and defeat us while we ran out of money and supplies.

**Strategy for the next game.** Next game, we will stop excessive drilling and focus heavily on recruiting fresh troops, keeping our armies supplied, and actively capturing adjacent enemy cities to maintain our income and territory.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our armies outnumber an adjacent enemy city's garrison 2:1 and have full supply, use move <army> <city> to capture enemy territory and increase our income.

### Version 34, after game 34 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We repeatedly ordered attacks into St. Louis against a fortified and numerically superior enemy force without adequate odds or supply, leading to repeated defeat and attrition. Meanwhile, we neglected naval building and failed to defend key intersections against enemy advances.

**Strategy for the next game.** We will build up our forces carefully, avoid attacking fortified cities without overwhelming superiority, reinforce our fleets to contest coastal movements, and maintain defensive positions while expanding income steadily.

**Changes:**

- revised: When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds. (We launched repeated unsuccessful attacks on St. Louis at 30-40 percent odds without waiting for sufficient advantages.)
- added: When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports. (We lost our initial fleet early and never rebuilt it, allowing the enemy naval actions to go uncontested.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 35, after game 35 (standard: Rebel victory: cities controlled, 14 turns)

**Diagnosis.** We focused heavily on drilling and recruiting but failed to manage supply properly, leaving McDowell stranded at zero supply in Washington for multiple turns. We also neglected joining and moving our armies aggressively to contest Rebel territory, allowing them to slowly capture cities and reach the victory threshold.

**Strategy for the next game.** We will aggressively combine our forces, maintain strict supply lines for armies defending key locations, and push outward to contest Rebel-held cities while keeping Washington heavily defended.

**Changes:**

- revised: When an army has 1 or less supply, use supply <army> before moving or fighting. (We failed to resupply McDowell when he repeatedly ran out of supply, causing massive penalties.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 36, after game 36 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while ignoring offensive operations. The Confederacy captured cities unchallenged and reached the 28-city victory threshold by October 1861. We must actively attack adjacent enemy-held cities when we have numerical superiority rather than endlessly drilling.

**Strategy for the next game.** We will aggressively recruit in large cities and launch coordinated attacks on vulnerable enemy-held adjacent cities instead of remaining idle and drilling, to prevent the Confederacy from capturing 28 cities.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 37, after game 37 (standard: Rebel victory: cities controlled, 11 turns)

**Diagnosis.** We focused heavily on drilling rather than expanding our territory or attacking enemy forces with decisive odds. We failed to leverage our cash reserves to recruit and reinforce properly, and our armies repeatedly ran out of supply without adequate offensive follow-up.

**Strategy for the next game.** We will prioritize aggressive recruitment using our cash reserves, maintain supply lines for all active armies, and avoid excessive drilling in favor of capturing and holding strategic cities.

**Changes:**

- revised: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (We held onto cash while our armies stagnated; we must consistently convert funds into troops.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 38, after game 38 (alternate: Rebel victory: share of total income, 6 turns)

**Diagnosis.** We focused excessively on drilling instead of aggressively recruiting and building our forces, allowing the Confederate army to concentrate superior strength and capture our capital.

**Strategy for the next game.** Next game, we will prioritize steady recruitment of new forces alongside defensive consolidation, avoiding idle drilling phases while the enemy builds overwhelming strength.

**Changes:**

- revised: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (We failed to recruit aggressively, leading to a critical shortage of manpower.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 39, after game 39 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We engaged in costly battles at low odds (~48% average win chance) and neglected fortification and joining small forces. As a result, our armies were repeatedly pushed back, attrition wore us down, and the Rebels steadily seized cities until securing a victory.

**Strategy for the next game.** Next game, we will maintain higher supply levels, avoid attacking at unfavorable odds, use join to consolidate forces into powerful armies, and prioritize defending our core cities while steadily expanding our territory.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 40, after game 40 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We lost our capital to a Confederate advance while focusing heavily on drilling and recruiting rather than defending core positions or responding to immediate threats. Our armies were large but poorly positioned, and we failed to maintain supply lines and city security.

**Strategy for the next game.** Next game, we will maintain rigorous defense of Washington, keep our armies supplied and concentrated, and aggressively defend our cities while continuing to build up our strength through recruitment and careful tactical movement.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 41, after game 41 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We engaged in attacks with insufficient numerical superiority, leading to heavy losses and allowing the Confederates to seize territory and eventually control over 32 cities. Our armies repeatedly initiated disadvantageous battles instead of consolidating and building up strength.

**Strategy for the next game.** We will maintain a defensive posture, prioritize reinforcing our core armies, avoid attacking unless we achieve overwhelming numerical superiority, and ensure all armies remain fully supplied before taking any aggressive action.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 42, after game 42 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while allowing the Confederacy to steadily capture key cities and outpace us in territory control. Although we built up a large army, our offensive pressure was insufficient and poorly timed, leading to a loss by city control threshold in early 1862.

**Strategy for the next game.** Next game, we will balance recruitment with aggressive regional expansion, actively securing neutral and enemy cities to prevent the Confederacy from winning the city-control threshold while maintaining sufficient defensive forces.

**Changes:**

- revised: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (Maintained as a foundational rule for economic conversion into military strength.)
- revised: When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack. (Kept to ensure we press attacks only when advantage is secured, avoiding attrition defeats.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 43, after game 43 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We lost control of key cities and suffered from poor supply management and low-odds attacks. Our main army frequently ran out of supply, drastically reducing combat effectiveness, while the Rebels concentrated superior forces and captured our territory.

**Strategy for the next game.** Next game, we will prioritize maintaining supply lines for all active armies, avoid attacking superior enemy forces without a 2:1 advantage, and steadily reinforce our main armies while protecting Washington and our core cities.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 44, after game 44 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We lost quickly because our forces were too small and fragmented, and we launched unfavorable attacks against defending armies without sufficient numerical superiority. Furthermore, we left our capital inadequately defended, allowing Jackson to capture Washington and trigger an immediate defeat.

**Strategy for the next game.** Next game, we will focus heavily on growing our troop numbers through consistent recruiting, consolidating forces before engaging in combat, strictly avoiding low-odds attacks, and keeping a strong garrison in Washington to protect our capital at all costs.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 45, after game 45 (standard: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** We lasted 12 turns, improving over baseline, but suffered from chronic supply issues (multiple armies going out of supply) and an inability to deal with enemy blockades and naval bombardments on Philadelphia. We fought successful tactical battles, but lack of supply and failure to secure key logistics cost us cities and eventually the game.

**Strategy for the next game.** Maintain aggressive recruitment to keep force numbers high, strictly monitor army supply lines to prevent attrition and penalties, and secure key transport nodes while defending against Rebel incursions.

**Changes:**

- revised: When an army has 1 or less supply, use supply <army> before moving or fighting. (We experienced multiple out-of-supply alerts that hampered combat effectiveness; supply must be prioritized earlier.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 46, after game 46 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** In Training Game 46 on the alternate map, we focused heavily on recruiting and drilling large numbers of troops while neglecting aggressive expansion, city capture, and defense of key positions. Although our troop count grew to nearly 130,000 men, the Confederate forces steadily captured cities and achieved victory through territorial dominance by turn 5. We failed to actively press the attack or secure territory.

**Strategy for the next game.** For the next game, we will maintain our steady recruitment and supply management while significantly increasing our offensive pressure. Instead of over-drilling static armies, we will use our numerical advantage to capture empty enemy cities, press attacks when holding superior odds, and aggressively contest Confederate territorial expansion to prevent them from reaching the 28-city threshold.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 47, after game 47 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We relied heavily on drilling and recruiting while our offensive actions were uncoordinated and frequently suffered from poor supply or unfavorable odds. Several armies ran out of supply in enemy territory, leading to severe attrition, and we failed to secure key cities or use rail and fleet movements effectively.

**Strategy for the next game.** Next game we will maintain strict control over army supply lines, avoid attacking fortified enemy positions at poor odds, and use rail transport and combined forces to secure vital strategic cities before engaging in major offensives.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 48, after game 48 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while allowing the Confederate army to steadily capture key cities and accumulate control. Although we built up our forces numerically, we failed to attack proactively or defend critical nodes effectively, leading to a loss of territory and a technical defeat on city control.

**Strategy for the next game.** Next game, we will maintain our steady recruitment and force consolidation while aggressively launching attacks when we hold numerical superiority, ensuring we contest city control and prevent the enemy from dominating the map.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.

### Version 49, after game 49 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused heavily on recruitment and sporadic attacks, but let armies run out of supply and failed to maintain proper supply lines or defensive positioning. Confederate forces exploited our lack of coordinated offensives and captured key northern cities while Jackson overran Philadelphia.

**Strategy for the next game.** We will maintain strict supply lines for all offensive armies, reinforce our major forces in the West and East, avoid low-odds attacks, and keep Washington heavily defended against Confederate incursions.

**Changes:**

- added: When an army is out of supply or has low supply near enemy territory, use supply <army> immediately to prevent combat penalties. (McClellan and other key armies suffered major combat penalties and inefficiencies due to running out of supply during critical offensives.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army is out of supply or has low supply near enemy territory, use supply <army> immediately to prevent combat penalties.

### Version 50, after game 50 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused too much on scattered offensive movements and naval building while neglecting recruitment and consolidation. Our attack on Springfield at 37% odds failed badly, and we failed to recruit new troops despite having ample funds, leading to a steady loss of cities and a quick Rebel victory.

**Strategy for the next game.** Next game we will aggressively recruit in available cities to build numerical superiority, maintain proper supply lines, consolidate our forces before attacking, and avoid low-odds attacks against superior or fortified enemy positions.

**Changes:**

- revised: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (We accumulated over $1,000 cash by the end of the game without recruiting enough troops to replace losses and hold cities.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army is out of supply or has low supply near enemy territory, use supply <army> immediately to prevent combat penalties.

### Version 51, after game 51 (standard: Rebel victory: cities controlled, 16 turns)

**Diagnosis.** We focused heavily on drilling and recruiting but failed to execute offensive campaigns or keep our armies supplied. Our armies ran out of supply constantly, reducing their combat power, and we suffered from poor coordination while the Confederacy systematically captured our cities and achieved victory.

**Strategy for the next game.** We will maintain our focus on steady recruitment, ensure all key armies are adequately supplied before undertaking operations, and coordinate our attacks only when possessing superior force ratios to steadily erode Confederate control.

**Changes:**

- revised: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (Maintained to ensure a steady influx of manpower into our forces.)
- revised: When an army has 1 or less supply, use supply <army> before moving or fighting. (Kept to prevent crippling supply shortages that plagued our frontline armies during this game.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army is out of supply or has low supply near enemy territory, use supply <army> immediately to prevent combat penalties.

### Version 52, after game 52 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while neglecting the defense of our capital and surrounding key cities. McClellan launched a disastrous low-odds attack against Jackson in Strasburg, and Buell similarly attacked A.S. Johnston at unfavorable odds in Louisville. Because our main forces were engaged elsewhere or tied up in drilling, Jackson marched completely unopposed into Washington, resulting in an immediate Rebel victory.

**Strategy for the next game.** Next game, we will prioritize maintaining a strong garrison in Washington at all times and strictly avoid attacking into fortified cities or superior forces without a 2:1 advantage. We will keep recruiting and supplying our forces regularly while ensuring our armies stay consolidated and ready to block Confederate advances toward our capital.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army is out of supply or has low supply near enemy territory, use supply <army> immediately to prevent combat penalties.

### Version 53, after game 53 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused excessively on drilling and building ships while failing to recruit aggressively, maintain supply lines, or capture enemy territory. As a result, the Confederacy outmaneuvered us, seized our cities, and achieved a technical victory.

**Strategy for the next game.** Next game we will aggressively recruit forces across all available cities, maintain continuous supply lines to our advancing armies, minimize unnecessary drilling, and push directly into enemy territory to capture cities and prevent Confederate expansion.

**Changes:**

- revised: When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition. (We encountered supply failures with McClellan and McDowell because we did not properly time our supply orders before running out.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 54, after game 54 (alternate: Rebel victory: share of total income, 4 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while ignoring enemy forces threatening our territory and capital. Jackson marched directly into Washington and captured our capital because we left it undefended and failed to intercept or position forces nearby.

**Strategy for the next game.** Next game, we will maintain our economic and recruiting growth while keeping defensive armies near Washington and core cities to prevent enemy capital captures and territory loss.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 55, after game 55 (standard: Rebel victory: cities controlled, 11 turns)

**Diagnosis.** We survived longer than the baseline by recruiting and keeping Washington fortified, but our armies frequently ran out of supply because we failed to use the supply command when funds were available, and many supply orders were refused due to being given on incorrect turns or when isolated.

**Strategy for the next game.** Next game we will maintain active supply lines, keep our main forces well-supplied and consolidated before attacking, and continue aggressive recruitment while fortifying Washington against Confederate advances.

**Changes:**

- revised: When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting. (We attempted to issue supply orders when armies were isolated or out of position, leading to refusals; this clarifies that supply lines must be intact.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 56, after game 56 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused heavily on recruitment and built a large force, but we failed to maintain adequate supply lines and attacked fortified enemy positions at poor odds. This led to defeat in detail and allowed the Confederacy to secure city dominance.

**Strategy for the next game.** We will build up our forces using steady recruitment, consolidate armies before engaging, and strictly verify superior odds and supply lines before ordering any attacks on enemy-held cities.

**Changes:**

- revised: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (Ensures continuous force growth while maintaining positive cash flow.)
- revised: When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack. (Prevents unfavorable assaults like our failed attack on St. Louis.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 57, after game 57 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We failed to consolidate our forces or maintain supply lines, launching disjointed attacks at low odds while the Rebels massed their strength and took our cities. We also wasted turns building wooden ships instead of reinforcing armies or fortifying key points.

**Strategy for the next game.** Next game, we will focus on concentrating our forces into powerful armies using join, keeping them fully supplied, and avoiding risky attacks while building up our defensive positions and recruiting steadily.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 58, after game 58 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused heavily on recruiting and building up our troop numbers, reaching over 140,000 men, but we neglected defensive positioning and city control. The Confederacy steadily outmaneuvered us and captured key cities, eventually reaching the threshold for a city-control victory while our offensive operations were too slow and reactive.

**Strategy for the next game.** We will continue to recruit aggressively to maintain numerical superiority, but we must be much more proactive in capturing and holding enemy cities to prevent the Confederacy from winning through city control.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 59, after game 59 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We suffered from severe supply issues and failed to adequately defend or retake lost territory, resulting in our armies running out of supply while the Rebels systematically captured our cities.

**Strategy for the next game.** We will focus on maintaining continuous supply lines to our front-line armies, avoiding unnecessary attrition, and aggressively consolidating and recruiting to defend key cities and our capital.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 60, after game 60 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We relied too heavily on drilling and recruiting without launching concerted offensive operations to capture enemy territory. While our forces grew, the Confederates steadily seized cities and surrounded us, leading to a loss of economic control and defeat.

**Strategy for the next game.** We will balance recruiting and force concentration with aggressive attacks on adjacent enemy cities to seize the initiative, capture territory, and prevent the Confederate computer from overwhelming us economically.

**Changes:**

- dropped: When our armies are idle and not adjacent to targets, use drill <army> to build experience. (Excessive drilling caused us to neglect offensive operations, allowing the enemy to capture cities unchecked and win the game.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 61, after game 61 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused heavily on movement and building wooden ships while completely neglecting recruitment, resulting in our army shrinking and failing to hold captured territory against the growing Rebel forces.

**Strategy for the next game.** We will prioritize regular recruitment in major cities alongside our movements to maintain our troop numbers, ensure all armies stay supplied, and capture key Confederate strongholds while defending our capital.

**Changes:**

- revised: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (We failed to recruit any troops this game, allowing the Rebel army to outnumber us massively by turn 6.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 62, after game 62 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused excessively on drilling instead of aggressively taking enemy territory or defending key locations, leading to a quick Confederate city-count victory while we remained passive.

**Strategy for the next game.** Next game, we will limit excessive drilling, actively recruit, and use our armies to capture adjacent enemy cities to prevent the Rebels from securing a fast victory through city dominance.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 63, after game 63 (standard: Rebel victory: cities controlled, 11 turns)

**Diagnosis.** We focused excessively on drilling and isolated supply management while failing to expand our recruitment base or press advantages. The Rebels steadily outgrew us in numbers and captured key cities, eventually overwhelming our defensive line.

**Strategy for the next game.** We will prioritize aggressive recruitment alongside careful supply management and high-odds attacks to gradually seize the initiative and push back Confederate forces.

**Changes:**

- revised: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (We must increase recruitment frequency to match growing Confederate strength instead of hoarding cash and over-drilling.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 64, after game 64 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused heavily on drilling armies while the Confederate forces aggressively maneuvered, captured key cities, and outpaced us in territorial control. Although our naval engagement successfully eliminated the Rebel fleet late in the game, our lack of offensive operations and failure to capture enemy territory allowed the Confederacy to secure a victory via city control within five turns.

**Strategy for the next game.** Next game we will maintain our recruitment and economic growth but prioritize aggressive movement and capturing adjacent enemy cities to prevent the Confederacy from securing a rapid territorial victory.

**Changes:**

- added: When our army is idle and adjacent to an undefended enemy city, use move <army> <city> to capture territory and increase our income. (We lost this game because we stayed passive and drilled instead of capturing cities, letting the Confederacy control 28 cities and win quickly.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When our army is idle and adjacent to an undefended enemy city, use move <army> <city> to capture territory and increase our income.

### Version 65, after game 65 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We repeatedly attacked fortified enemy positions or superior forces at poor odds (around 30% success rate) while neglecting supply lines, leading to widespread out-of-supply attrition and losing control of key cities.

**Strategy for the next game.** Prioritize reinforcing and supplying our main armies, avoid low-odds attacks against fortified Confederate positions, and focus on securing connected territory to maintain stable supply and income.

**Changes:**

- revised: When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds. (We attacked enemy cities with low odds and suffered heavy losses without taking territory.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an army is idle and adjacent to an undefended enemy city, use move <army> <city> to capture territory and increase our income.

### Version 66, after game 66 (alternate: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused heavily on drilling armies while accumulating capital, but neglected aggressive territory expansion and timely recruitment. The Confederates steadily outgrew us in territory and strength, eventually overwhelming our defensive positions.

**Strategy for the next game.** We will aggressively recruit in available cities, maintain our frontline forces, and actively expand our territory by capturing undefended or weakly held enemy cities while avoiding low-odds suicidal attacks.

**Changes:**

- revised: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (Ensures we keep pace with Confederate troop growth by continuously reinvesting idle capital into new strength.)
- revised: When an army is idle and adjacent to an undefended enemy city, use move <army> <city> to capture territory and increase our income. (We failed to capture enough enemy cities, allowing the Rebels to control the map; we must aggressively seize neutral and undefended enemy territory.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an army is idle and adjacent to an undefended enemy city, use move <army> <city> to capture territory and increase our income.

### Version 67, after game 67 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused heavily on drilling and recruiting while neglecting effective offensive maneuvers and timely resupply, leading to widespread supply shortages and allowing Confederate armies to systematically capture our cities.

**Strategy for the next game.** Next game, we will prioritize maintaining supply lines for active armies, reducing excessive drilling when campaigns are underway, and aggressively pressing our numerical advantage against vulnerable Confederate border cities.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an army is idle and adjacent to an undefended enemy city, use move <army> <city> to capture territory and increase our income.

### Version 68, after game 68 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We failed to recruit any new troops throughout the entire game, letting our total force shrink from 39,100 to 30,800 while the Confederacy built up to 54,600. Without replacements and reinforcements, our isolated armies were overwhelmed and flanked one by one.

**Strategy for the next game.** Next game we must aggressively use our treasury to recruit troops every turn in all available cities, maintaining force parity with the Confederacy while continuing to capture neutral cities and defend key positions.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an army is idle and adjacent to an undefended enemy city, use move <army> <city> to capture territory and increase our income.

### Version 69, after game 69 (standard: Rebel victory: cities controlled, 16 turns)

**Diagnosis.** We lost control of the map because our armies repeatedly attacked fortified positions or equal-strength defenders at poor odds (averaging 45%), bleeding men and falling out of supply. Although we recruited and kept our treasury stable, marching unsupported armies into enemy strongholds like Fort Donelson and Nashville without proper supply lines or numerical superiority led to heavy attrition and eventual collapse.

**Strategy for the next game.** Next game, we will prioritize maintaining supply lines for all active armies, strictly avoid attacking unless we hold a 2:1 advantage or better, and consolidate our forces into larger, unstoppable corps rather than launching piecemeal assaults.

**Changes:**

- revised: When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds. (We repeatedly threw McClellan and other armies against Beauregard at Fort Donelson and Nashville at poor odds, causing massive casualties and defeats.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an army is idle and adjacent to an undefended enemy city, use move <army> <city> to capture territory and increase our income.

### Version 70, after game 70 (alternate: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** We successfully recruited and built a large force, but spent too much time drilling instead of expanding our territory or pressing our numerical advantage. Our repeated low-odds attacks and lack of offensive momentum allowed the Confederacy to secure cities and win via control.

**Strategy for the next game.** Next game, we will balance recruiting and drilling with aggressive expansion into undefended enemy cities to outpace the Confederacy in territory control while avoiding low-odds attacks.

**Changes:**

- revised: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (Kept our foundational recruitment rule as it helps maintain force numbers.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an army is idle and adjacent to an undefended enemy city, use move <army> <city> to capture territory and increase our income.

### Version 71, after game 71 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused excessively on drilling while losing control of key cities and failing to properly manage supply or aggressive counter-offensives against advancing Confederate forces. Our armies ran out of supply and we lost critical territory.

**Strategy for the next game.** Next game we will balance our training with active territorial expansion and proper supply maintenance, ensuring we capture and hold cities to prevent the Confederacy from achieving an early city-count victory.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an army is idle and adjacent to an undefended enemy city, use move <army> <city> to capture territory and increase our income.

### Version 72, after game 72 (alternate: Rebel victory: cities controlled, 22 turns)

**Diagnosis.** We focused heavily on recruiting and drilling massive armies while ignoring supply lines and territorial expansion. Our armies frequently ran out of supply, fought at half strength, and lost battles even when numerically superior because we neglected supply lines and attacked fortified positions without proper preparation.

**Strategy for the next game.** We will maintain proper supply lines for all active armies, avoid attacking fortified enemy cities without overwhelming superiority, and aggressively capture neutral and undefended enemy cities to build our income and secure victory conditions.

**Changes:**

- revised: When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting. (We failed to keep our armies supplied, leading to crippling combat penalties and attrition during campaigns.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an army is idle and adjacent to an undefended enemy city, use move <army> <city> to capture territory and increase our income.

### Version 73, after game 73 (standard: Rebel victory: cities controlled, 16 turns)

**Diagnosis.** We lasted 16 turns through steady recruiting and building large stacks, but our armies frequently suffered from supply starvation in Washington and key positions. We failed to secure territory consistently, and our attacks into superior forces or fortified positions drained our manpower. Without naval operations or efficient rail deployment, the Confederacy steadily choked our income and outmaneuvered us.

**Strategy for the next game.** Next game, we will prioritize maintaining supply lines for active offensive stacks like Sherman's army, avoid reckless attacks on fortified positions, and systematically capture enemy cities to deny them the victory threshold while keeping Washington fully defended and supplied.

**Changes:**

- revised: When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies. (We successfully used recruitment to maintain high troop counts, but need to ensure it does not starve our cash reserves.)
- revised: When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting. (Too many armies starved in Washington and Louisville because supply orders were mistimed or omitted.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an army is idle and adjacent to an undefended enemy city, use move <army> <city> to capture territory and increase our income.

### Version 74, after game 74 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We struggled to maintain momentum and lost control of key western cities because our offensives against fortified or numerically superior Rebel armies (such as J.E. Johnston in Louisville) failed at poor odds. Meanwhile, we under-utilized supply lines and failed to reinforce and consolidate aggressively enough to match the Confederate buildup.

**Strategy for the next game.** We will focus on maintaining strong defensive positions in the West, ensuring our attacking forces heavily outnumber defenders before initiating combat, and continuously building up our economic and naval base.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an army is idle and adjacent to an undefended enemy city, use move <army> <city> to capture territory and increase our income.

### Version 75, after game 75 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We lasted 10 turns on standard, but lost control of too many cities as the Confederacy slowly choked our territory and achieved victory conditions. We spent too much time drilling instead of actively expanding and defending our cities, letting the Rebels capture vital income centers while our main forces sat idle.

**Strategy for the next game.** Next game, we will aggressively recruit and maintain active operations across the map to secure neutral and enemy cities early, preventing the AI from snowballing its city count while we waste turns drilling. We will keep supply lines stable and push forward decisively when we have numerical advantages.

**Changes:**

- revised: When an army is idle and adjacent to an undefended enemy or neutral city, use move <army> <city> to capture territory and increase our income. (We clarified the rule to include undefended enemy cities as well as neutral ones, ensuring we aggressively expand and contest city counts rather than idling.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an army is idle and adjacent to an undefended enemy or neutral city, use move <army> <city> to capture territory and increase our income.

### Version 76, after game 76 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** In this alternate map game, we advanced aggressively to capture border cities and even won some tactical engagements, but we completely neglected recruitment, reinforcement, and drilling. Our total troop count stagnated and dwindled from 39,100 down to 32,500 while the Rebel forces maintained superior strength and outnumbered us in key sectors, leading to a rapid loss of city control.

**Strategy for the next game.** Next game we will strictly balance our territorial advances with aggressive recruiting using our growing treasury, ensuring our army sizes outmatch the Confederate forces and we never neglect force augmentation.

**Changes:**

- dropped: When an army is idle and adjacent to an undefended enemy or neutral city, use move <army> <city> to capture territory and increase our income. (This instruction caused us to over-extend and neglect necessary force buildup, resulting in a disastrously short game.)
- added: When our treasury exceeds $300 and our active armies have fewer than 45,000 total men, use recruit <city> to expand our force pool. (We must consistently build up our troop numbers rather than just moving existing armies, otherwise the Confederacy overwhelms us in sheer numbers.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When our treasury exceeds $300 and our active armies have fewer than 45,000 total men, use recruit <city> to expand our force pool.

### Version 77, after game 77 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused heavily on drilling and minor movements while failing to recruit new troops or manage our economy effectively, leaving our active armies too weak and few to hold territory against advancing Confederate forces.

**Strategy for the next game.** Next game we will aggressively recruit forces to maintain numerical superiority, avoid low-odds attacks, and properly supply our armies while expanding our city control.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When our treasury exceeds $300 and our active armies have fewer than 45,000 total men, use recruit <city> to expand our force pool.

### Version 78, after game 78 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We expanded our army size significantly and managed a healthy treasury, but our attacks failed due to poor odds and attacking fortified enemy positions without sufficient numerical superiority. We also failed to secure territory effectively or prevent Rebel breakthroughs.

**Strategy for the next game.** We will focus on building up our forces while strictly avoiding low-odds attacks. We will use proper force concentration and supply management to ensure our offensives succeed with at least 2:1 numerical superiority.

**Changes:**

- dropped: When our treasury exceeds $300 and our active armies have fewer than 45,000 total men, use recruit <city> to expand our force pool. (This instruction had a poor record (-1.0 turns) and became obsolete as our forces quickly grew past 45,000 men in the early game.)
- added: When an enemy army occupies an adjacent city and our attacking army has less than 2:1 odds, use drill <army> or wait instead of launching costly failed attacks. (We lost several battles at poor odds (around 40% or lower) which drained our manpower and allowed the Rebels to secure victory.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an enemy army occupies an adjacent city and our attacking army has less than 2:1 odds, use drill <army> or wait instead of launching costly failed attacks.

### Version 79, after game 79 (standard: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** We focused heavily on drilling and recruiting but failed to maintain supply lines or consolidate forces, leading to armies running out of supply, losing naval dominance, and eventually being overwhelmed by concentrated Confederate offensives.

**Strategy for the next game.** We will strictly monitor army supply levels before initiating movements, actively rebuild and use our fleets to protect ports, consolidate small garrisons, and press attacks only when holding a clear 2:1 advantage.

**Changes:**

- revised: When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting. (We experienced widespread supply shortages across multiple armies that went unaddressed, causing severe attrition.)
- revised: When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports. (We completely neglected naval building and fleet operations, allowing the Rebels to blockade our ports and achieve dominance.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an enemy army occupies an adjacent city and our attacking army has less than 2:1 odds, use drill <army> or wait instead of launching costly failed attacks.

### Version 80, after game 80 (alternate: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while repeatedly launching low-odds attacks against defended positions or failing to press clear advantages, resulting in heavy casualties and zero successful attacks. Meanwhile, the Rebels steadily captured cities and achieved victory.

**Strategy for the next game.** We will build up our forces through steady recruiting and drilling, avoid attacking unless we have at least 2:1 odds, and maintain proper supply lines to contest rebel expansion and secure cities.

**Changes:**

- revised: When an enemy army occupies an adjacent city and our attacking army has less than 2:1 odds, use drill <army> or wait instead of launching costly failed attacks. (We continued to initiate poor-odds attacks in this game that drained our forces; we must strictly avoid attacking below 2:1 odds.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an enemy army occupies an adjacent city and our attacking army has less than 2:1 odds, use drill <army> or wait instead of launching costly failed attacks.

### Version 81, after game 81 (standard: Rebel victory: capital captured, 11 turns)

**Diagnosis.** We focused heavily on drilling and recruiting while allowing our main armies like Grant to become permanently blockaded and out of supply in Philadelphia, where they suffered constant bombardment attrition. Without a functioning fleet to clear the blockade or prompt supply management, our forces degraded in strength and failed to defend Washington, leading to a Rebel capture of the capital.

**Strategy for the next game.** Next game we will maintain active naval forces to prevent our ports from being blockaded, ensure our armies stay supplied, and aggressively maneuver to defend Washington while keeping our main forces concentrated rather than trapped.

**Changes:**

- dropped: When an enemy army occupies an adjacent city and our attacking army has less than 2:1 odds, use drill <army> or wait instead of launching costly failed attacks. (This lesson encouraged excessive drilling instead of proactive maneuvering and breaking blockades, contributing to our passivity.)
- added: When an enemy fleet blockades a port holding our army, use fleet sail to engage and break the blockade or build naval vessels to contest control. (We lost Grant's army in Philadelphia to permanent blockade attrition because we failed to rebuild our fleet and clear the enemy naval threat.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an enemy fleet blockades a port holding our army, use fleet sail to engage and break the blockade or build naval vessels to contest control.

### Version 82, after game 82 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** The Union suffered a quick defeat because armies attacked strong enemy positions without sufficient numerical or leadership advantage, leading to heavy losses (e.g., Buell attacking Nashville at 3% odds). Meanwhile, excessive drilling diverted turns from essential territorial expansion, and failure to reinforce key cities or maintain proper supply lines allowed the Rebels to capture critical territory and achieve victory by turn 5.

**Strategy for the next game.** Next game, we will focus on methodical expansion, building up large cohesive armies through recruiting and joining rather than premature attacking, avoiding low-odds engagements entirely, and securing our economic base by capturing and holding surrounding neutral and enemy cities.

**Changes:**

- revised: When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack. (We launched attacks at terrible odds (<50% or even 3%) which drained our forces and handed the initiative to the Rebels.)
- revised: When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds. (Too many turns were spent drilling while the enemy aggressively manoeuvred and captured cities; we must prioritize safety and superior concentration before striking.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an enemy fleet blockades a port holding our army, use fleet sail to engage and break the blockade or build naval vessels to contest control.

### Version 83, after game 83 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** In this game, our armies attacked into enemy-held cities at poor odds (around 43%) and lost multiple battles, leading to heavy casualties and loss of territory. We also failed to consistently recruit and supply our forces, causing armies to run out of supplies and attrition down our strength while the Rebels steadily expanded their control.

**Strategy for the next game.** Next game, we will focus heavily on reinforcing our armies through regular recruitment, strictly avoiding attacks unless we hold a clear 2:1 numerical advantage, and keeping our frontline armies well-supplied to prevent attrition and defeat in detail.

**Changes:**

- dropped: When an enemy fleet blockades a port holding our army, use fleet sail to engage and break the blockade or build naval vessels to contest control. (This lesson had a poor record (-1.0 turns) and distracted from land warfare priorities.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When our fleets are destroyed by enemy naval forces, use build wooden or build ironclad to rebuild our naval strength in seaports.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 84, after game 84 (alternate: Rebel victory: cities controlled, 13 turns)

**Diagnosis.** We lasted 13 turns on the alternate map, significantly outperforming the no-orders baseline of 6 turns, but we suffered a decisive defeat because we failed to build fleets to break the enemy naval blockade on Philadelphia and spent too many turns passively drilling instead of aggressively seizing enemy cities.

**Strategy for the next game.** Next game, we will aggressively recruit to maintain a strong numerical advantage, use naval forces to clear enemy blockades and protect our port income, and launch coordinated offensives against vulnerable Rebel cities rather than remaining idle.

**Changes:**

- revised: When enemy fleets blockade our seaports and cause attrition, use build wooden or build ironclad to construct naval forces and fleet sail to eliminate the blockade. (In this game, our fleet in Philadelphia was permanently blockaded and bombarded for multiple turns without a counter-strategy of rebuilding and sailing warships to clear the enemy navy.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When enemy fleets blockade our seaports and cause attrition, use build wooden or build ironclad to construct naval forces and fleet sail to eliminate the blockade.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 85, after game 85 (standard: Rebel victory: capital captured, 2 turns)

**Diagnosis.** The game was lost in two turns because the starting armies moved away from Washington, leaving the capital completely undefended while Confederate forces marched straight in and captured it immediately.

**Strategy for the next game.** Next game I will keep an army stationed in or immediately adjacent to Washington at all times to prevent early capital capture, while steadily recruiting and consolidating forces before attempting any aggressive expansion.

**Changes:**

- dropped: When enemy fleets blockade our seaports and cause attrition, use build wooden or build ironclad to construct naval forces and fleet sail to eliminate the blockade. (This lesson resulted in a severe negative turn record (-7.0) and distracted from vital land defense.)
- added: When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack. (Added to prevent the immediate early-game capital loss experienced in this match.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 86, after game 86 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused heavily on drilling and recruiting but failed to capture territory or challenge the Confederate expansion. With only one attack ordered over the entire game, the Rebels were free to capture cities unchecked, eventually reaching the victory threshold in July 1862.

**Strategy for the next game.** Next game we will maintain our economic and recruiting focus but aggressively use our forces to attack vulnerable enemy cities and prevent the Confederacy from easily claiming territory.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 87, after game 87 (standard: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused almost exclusively on moving and attacking at poor odds while neglecting recruitment and supply management. Our armies withered away through attrition and bad attacks against superior enemy forces, while the Confederacy built up massive strength and captured our cities.

**Strategy for the next game.** We will stop making reckless attacks at poor odds and prioritize recruiting fresh troops and maintaining proper supply lines. We will consolidate our forces and build up our strength before attempting to capture enemy territory.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 88, after game 88 (alternate: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while failing to conduct offensive operations or protect our supply lines. Our armies ran out of supply and were isolated, allowing the Confederate forces to pick them off one by one, leading to a decisive defeat.

**Strategy for the next game.** Next game, we will actively maintain supply lines for all active armies, coordinate regional attacks to capture enemy cities, and reduce excessive drilling in favor of advancing our lines and protecting our ports.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 89, after game 89 (standard: Rebel victory: capital captured, 2 turns)

**Diagnosis.** The game was lost in two turns because Confederate forces bypassed our front advances and captured an undefended Washington while our armies were marching away or positioned poorly. We neglected to recruit or keep defensive forces in the capital region, leading to a catastrophic and rapid loss.

**Strategy for the next game.** Next game we will strictly maintain a strong garrison in Washington at all times and refrain from reckless advances that leave our core territory completely undefended against fast Confederate counter-attacks.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 90, after game 90 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused heavily on drilling and recruiting while allowing the Confederates to steadily capture our cities and dominate the map. Although our army size grew, we failed to aggressively attack vulnerable enemy positions and protect our cities, leading to a loss of key territory and a Rebel victory by city count.

**Strategy for the next game.** Next game, we will balance recruiting and drilling with proactive offensive operations and timely reinforcement to prevent the Confederates from seizing critical cities and achieving a rapid victory.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 91, after game 91 (standard: Rebel victory: capital captured, 4 turns)

**Diagnosis.** We focused heavily on erratic offensive maneuvers instead of protecting our capital and building up economic and military strength. Jackson swept through our weak defenses and captured Washington directly while our armies were out of position.

**Strategy for the next game.** Next game, we will prioritize keeping Washington fully garrisoned and defended, avoiding reckless low-odds attacks, and methodically building up our economic and troop base through careful recruitment before pushing forward.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 92, after game 92 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused almost exclusively on recruiting and drilling while failing to use the move command to attack enemy cities or defend ours effectively. As a result, the Confederates steadily captured our territory and achieved victory.

**Strategy for the next game.** In the next game, we will maintain our recruitment and supply discipline while aggressively using the move command to seize enemy cities and contest Confederate territorial expansion.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 93, after game 93 (standard: Rebel victory: capital captured, 2 turns)

**Diagnosis.** The game was lost quickly because we launched a low-odds attack with Buell against a superior, reinforced enemy force in Louisville (23% odds), leaving Washington vulnerable and allowing Jackson to capture our capital on turn two.

**Strategy for the next game.** Next game, we will prioritize securing Washington, avoiding attacking strong enemy forces without at least 2:1 odds, and building up our forces through recruitment and consolidation before undertaking offensive operations.

**Changes:**

- added: When an enemy army occupies a fortified city with superior strength, use fortify or wait instead of ordering attacks at odds below 50%. (We attacked Louisville at 23% odds and suffered a disastrous defeat that enabled the enemy counter-offensive.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When an enemy army occupies a fortified city with superior strength, use fortify or wait instead of ordering attacks at odds below 50%.

### Version 94, after game 94 (alternate: Rebel victory: share of total income, 3 turns)

**Diagnosis.** The game was lost quickly because we failed to secure key strategic locations and allowed the enemy to capture major income-producing cities while our forces remained mostly idle in the rear instead of actively expanding our territory or defending critical ports.

**Strategy for the next game.** Next game, we will aggressively recruit to build up major field armies while actively using our fleets and rail transport to secure critical ports and cities before the Confederates can out-expand us economically.

**Changes:**

- dropped: When an enemy army occupies a fortified city with superior strength, use fortify or wait instead of ordering attacks at odds below 50%. (Dropped because it was redundant with lesson 7 and had a poor one-game record.)
- added: When a seaport is threatened by enemy fleets, use build wooden or build ironclad and fleet sail <port> to protect our maritime supply lines. (Added to address our complete lack of naval defense which allowed enemy fleets to neutralise Philadelphia and damage income.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.
10. When a seaport is threatened by enemy fleets, use build wooden or build ironclad and fleet sail <port> to protect our maritime supply lines.

### Version 95, after game 95 (standard: Rebel victory: capital captured, 2 turns)

**Diagnosis.** The game was lost in two turns because Confederate forces bypassed our front line to capture an undefended Washington while our armies were scattered and making low-odds attacks on fortified positions like Fort Donelson. We failed to keep a garrison in the capital or intercept incoming threats.

**Strategy for the next game.** Next game we will prioritize keeping a strong army stationed in or immediately adjacent to Washington to prevent swift decapitation strikes, avoid attacking fortified enemy positions without overwhelming odds, and steadily recruit forces to build up a secure defense before advancing.

**Changes:**

- dropped: When a seaport is threatened by enemy fleets, use build wooden or build ironclad and fleet sail <port> to protect our maritime supply lines. (It severely worsened our performance and distracted from vital land defense of the capital.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 96, after game 96 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** The game was lost quickly in 4 turns because our forces were thinly spread and attacked superior or well-defended positions without sufficient concentration. Although we built up overall troop numbers, we failed to properly combine armies or maintain proper support, allowing the Confederate forces to easily isolate and overwhelm our western positions while we shuffled troops indecisively.

**Strategy for the next game.** Next game, we will focus strictly on building up a few concentrated, powerful armies rather than moving small forces piecemeal. We will maintain strong defenses around Washington, avoid low-odds attacks against fortified or superior Confederate forces, and ensure our armies are fully supplied before any offensive operations.

**Changes:**

- revised: When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack. (We engaged in attacks at unfavorable odds (below 2:1) which resulted in heavy losses and failed assaults; we must strictly enforce the 2:1 ratio.)
- revised: When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds. (Attacking St. Louis prematurely without sufficient local advantage drained our manpower and cost us the initiative.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 97, after game 97 (standard: Rebel victory: capital captured, 2 turns)

**Diagnosis.** The game was lost quickly because we launched offensive attacks against fortified enemy forces at terrible odds (23%) and left Washington completely undefended, allowing Jackson to capture our capital on turn 2.

**Strategy for the next game.** We will prioritize keeping Washington fully garrisoned or immediately secured against enemy advances, avoid low-odds attacks on fortified cities, and focus on building our economic base and army strength through careful recruiting and defensive positioning.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 98, after game 98 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused heavily on recruiting and building up large armies, but our attacks were poorly timed and engaged superior enemy forces at low odds, leading to heavy losses. We also neglected naval management and allowed the enemy to blockade Philadelphia, cutting off supply and eventually losing the game.

**Strategy for the next game.** We will continue to build up our forces through steady recruitment while strictly avoiding attacks unless we hold a clear 2:1 numerical advantage. We will also pay closer attention to supply lines and naval defense to prevent blockades on key ports like Philadelphia.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 99, after game 99 (standard: Rebel victory: capital captured, 13 turns)

**Diagnosis.** We lost the game because the capital fell to Jackson's assault while our main armies were distracted or out of position, and we failed to keep sufficient defensive strength or fortifications in Washington.

**Strategy for the next game.** Next game we will maintain a strong permanent garrison in Washington, keep our main field armies supplied and concentrated, and strike only when we hold a clear numerical advantage.

**Changes:**

- revised: When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack. (We failed to keep Washington garrisoned, allowing Jackson to capture it.)

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

### Version 100, after game 100 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused too much on isolated recruiting and poorly coordinated attacks at low odds against fortified positions, resulting in heavy casualties. Meanwhile, the Confederate forces aggressively captured our western and northern cities while we drilled or failed to press our advantages, leading to a quick defeat in 5 turns.

**Strategy for the next game.** Next game, we will halt wasteful low-odds attacks, concentrate our forces into massive armies before attempting any offensive moves, and prioritize defensive positioning and steady reinforcement to check Confederate expansion.

**Notebook:**

1. When a city offers recruits and treasury exceeds $200, use recruit <city> to strengthen our armies.
2. When an army is adjacent to an enemy city and our strength outnumbers the defender by at least 2:1, use move <army> <city> to attack.
3. When an army has 1 or less supply and is connected to a friendly neighbouring city, use supply <army> before moving or fighting.
4. When an enemy army moves adjacent to Washington, use move <army> <city> to intercept and defend the capital.
5. When multiple small friendly forces occupy the same city, use join <city> to consolidate them into a single stronger army before moving.
6. When our capital is empty and an enemy force is within one movement, use move <army> <city> to secure Washington immediately.
7. When an army faces a fortified or superior enemy force in a city, use fortify <city> or wait for reinforcements instead of attacking at low odds.
8. When Washington is empty of combat forces, use recruit Washington or move an army into Washington to keep the capital secure against sudden attack.
9. When an army has 1 supply and is operating away from friendly cities, use supply <army> to prevent out-of-supply attrition.

