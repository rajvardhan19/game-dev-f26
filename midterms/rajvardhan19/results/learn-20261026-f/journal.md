# Learning journal: `gemini-f`

Model `gemini-3.5-flash-lite`. 100 training games; notebook version 100 (frozen, sha b268f897393d855e).

## What it did, game by game

| game | map | notebook | result | turns | recruits | drills | moves | attacks (won) | mean odds | cities peak / end | last-turn cash | refused |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | standard | v0 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 10 | 5 | 1 (0) | 27% | 12 / 6 | 639 | 2 |
| 2 | alternate | v1 | decisive loss: Rebel victory: cities controlled | 8 | 18 | 22 | 7 | 4 (1) | 34% | 12 / 10 | 376 | 6 |
| 3 | standard | v2 | decisive loss: Rebel victory: cities controlled | 13 | 16 | 20 | 16 | 3 (2) | 65% | 13 / 6 | 284 | 17 |
| 4 | alternate | v3 | decisive loss: Rebel victory: cities controlled | 4 | 12 | 16 | 2 | 2 (0) | 22% | 10 / 9 | 345 | 5 |
| 5 | standard | v4 | decisive loss: Rebel victory: cities controlled | 12 | 10 | 26 | 5 | 1 (0) | 27% | 13 / 6 | 245 | 9 |
| 6 | alternate | v5 | decisive loss: Rebel victory: share of total income | 16 | 22 | 36 | 9 | 5 (1) | 25% | 13 / 9 | 275 | 9 |
| 7 | standard | v6 | decisive loss: Rebel victory: cities controlled | 10 | 13 | 29 | 4 | 1 (0) | 28% | 13 / 7 | 263 | 8 |
| 8 | alternate | v7 | decisive loss: Rebel victory: share of total income | 11 | 18 | 21 | 9 | 4 (2) | 42% | 11 / 9 | 273 | 14 |
| 9 | standard | v8 | decisive loss: Rebel victory: cities controlled | 13 | 13 | 21 | 7 | 2 (0) | 33% | 13 / 6 | 390 | 10 |
| 10 | alternate | v9 | decisive loss: Rebel victory: share of total income | 8 | 13 | 0 | 13 | 5 (2) | 38% | 14 / 9 | 730 | 1 |
| 11 | standard | v10 | decisive loss: Rebel victory: cities controlled | 9 | 10 | 20 | 5 | 1 (0) | 33% | 11 / 5 | 220 | 4 |
| 12 | alternate | v11 | decisive loss: Rebel victory: cities controlled | 10 | 29 | 36 | 5 | 0 (0) | - | 13 / 8 | 335 | 5 |
| 13 | standard | v12 | decisive loss: Rebel victory: cities controlled | 9 | 14 | 15 | 9 | 1 (0) | 27% | 12 / 7 | 255 | 11 |
| 14 | alternate | v13 | decisive loss: Rebel victory: cities controlled | 6 | 12 | 22 | 3 | 4 (2) | 50% | 10 / 8 | 354 | 4 |
| 15 | standard | v14 | decisive loss: Rebel victory: cities controlled | 9 | 13 | 20 | 13 | 2 (0) | 34% | 12 / 5 | 306 | 11 |
| 16 | alternate | v15 | decisive loss: Rebel victory: cities controlled | 8 | 19 | 2 | 5 | 3 (1) | 45% | 11 / 10 | 437 | 3 |
| 17 | standard | v16 | decisive loss: Rebel victory: share of total income | 10 | 14 | 27 | 13 | 6 (1) | 27% | 13 / 7 | 230 | 12 |
| 18 | alternate | v17 | decisive loss: Rebel victory: share of total income | 9 | 20 | 22 | 8 | 4 (0) | 10% | 12 / 8 | 353 | 9 |
| 19 | standard | v18 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 15 | 8 | 1 (0) | 23% | 12 / 4 | 1444 | 6 |
| 20 | alternate | v19 | decisive loss: Rebel victory: cities controlled | 7 | 13 | 9 | 3 | 2 (2) | 62% | 11 / 9 | 328 | 2 |
| 21 | standard | v20 | decisive loss: Rebel victory: cities controlled | 11 | 12 | 17 | 8 | 3 (1) | 34% | 13 / 6 | 253 | 9 |
| 22 | alternate | v21 | decisive loss: Rebel victory: share of total income | 5 | 8 | 3 | 8 | 3 (1) | 56% | 10 / 9 | 523 | 2 |
| 23 | standard | v22 | decisive loss: Rebel victory: capital captured | 6 | 12 | 7 | 5 | 1 (0) | 46% | 11 / 8 | 270 | 7 |
| 24 | alternate | v23 | decisive loss: Rebel victory: cities controlled | 6 | 9 | 24 | 3 | 1 (0) | 44% | 10 / 8 | 514 | 2 |
| 25 | standard | v24 | decisive loss: Rebel victory: capital captured | 18 | 12 | 25 | 5 | 1 (1) | 33% | 12 / 9 | 421 | 11 |
| 26 | alternate | v25 | decisive loss: Rebel victory: cities controlled | 11 | 29 | 36 | 8 | 2 (2) | 69% | 13 / 8 | 356 | 5 |
| 27 | standard | v26 | decisive loss: Rebel victory: cities controlled | 9 | 13 | 22 | 3 | 2 (1) | 50% | 11 / 8 | 264 | 8 |
| 28 | alternate | v27 | decisive loss: Rebel victory: cities controlled | 5 | 12 | 11 | 5 | 3 (2) | 63% | 10 / 7 | 346 | 5 |
| 29 | standard | v28 | decisive loss: Rebel victory: cities controlled | 10 | 12 | 20 | 6 | 3 (0) | 44% | 11 / 5 | 323 | 7 |
| 30 | alternate | v29 | decisive loss: Rebel victory: cities controlled | 4 | 12 | 6 | 1 | 0 (0) | - | 10 / 9 | 349 | 3 |
| 31 | standard | v30 | decisive loss: Rebel victory: cities controlled | 9 | 8 | 0 | 12 | 3 (1) | 55% | 13 / 5 | 210 | 5 |
| 32 | alternate | v31 | decisive loss: Rebel victory: cities controlled | 8 | 10 | 17 | 8 | 1 (0) | 40% | 10 / 7 | 466 | 4 |
| 33 | standard | v32 | decisive loss: Rebel victory: cities controlled | 9 | 11 | 15 | 11 | 3 (2) | 42% | 11 / 7 | 255 | 6 |
| 34 | alternate | v33 | decisive loss: Rebel victory: cities controlled | 7 | 17 | 10 | 7 | 4 (3) | 44% | 11 / 10 | 365 | 4 |
| 35 | standard | v34 | decisive loss: Rebel victory: cities controlled | 8 | 4 | 13 | 12 | 4 (1) | 48% | 13 / 7 | 269 | 2 |
| 36 | alternate | v35 | decisive loss: Rebel victory: share of total income | 6 | 12 | 28 | 4 | 3 (0) | 42% | 10 / 8 | 343 | 5 |
| 37 | standard | v36 | decisive loss: Rebel victory: cities controlled | 13 | 7 | 13 | 6 | 2 (0) | 46% | 11 / 6 | 277 | 12 |
| 38 | alternate | v37 | decisive loss: Rebel victory: cities controlled | 6 | 9 | 14 | 6 | 5 (2) | 51% | 10 / 9 | 343 | 2 |
| 39 | standard | v38 | decisive loss: Rebel victory: cities controlled | 12 | 5 | 15 | 12 | 4 (2) | 58% | 13 / 6 | 737 | 12 |
| 40 | alternate | v39 | decisive loss: Rebel victory: cities controlled | 17 | 31 | 38 | 5 | 1 (0) | 21% | 12 / 9 | 351 | 26 |
| 41 | standard | v40 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 10 | 6 | 2 (0) | 34% | 13 / 5 | 1188 | 3 |
| 42 | alternate | v41 | decisive loss: Rebel victory: cities controlled | 5 | 7 | 6 | 6 | 3 (1) | 46% | 10 / 7 | 456 | 1 |
| 43 | standard | v42 | decisive loss: Rebel victory: capital captured | 8 | 7 | 0 | 19 | 6 (1) | 30% | 11 / 6 | 243 | 3 |
| 44 | alternate | v43 | decisive loss: Rebel victory: cities controlled | 9 | 16 | 17 | 6 | 5 (2) | 50% | 11 / 9 | 371 | 4 |
| 45 | standard | v44 | decisive loss: Rebel victory: cities controlled | 16 | 21 | 22 | 9 | 1 (1) | 46% | 11 / 7 | 278 | 18 |
| 46 | alternate | v45 | decisive loss: Rebel victory: cities controlled | 5 | 6 | 4 | 0 | 0 (0) | - | 10 / 8 | 452 | 0 |
| 47 | standard | v46 | decisive loss: Rebel victory: cities controlled | 13 | 17 | 17 | 5 | 1 (0) | 40% | 12 / 5 | 190 | 9 |
| 48 | alternate | v47 | decisive loss: Rebel victory: cities controlled | 8 | 20 | 24 | 11 | 1 (1) | 80% | 11 / 8 | 361 | 12 |
| 49 | standard | v48 | decisive loss: Rebel victory: cities controlled | 10 | 15 | 12 | 12 | 2 (0) | 29% | 11 / 6 | 261 | 10 |
| 50 | alternate | v49 | decisive loss: Rebel victory: cities controlled | 5 | 14 | 24 | 1 | 1 (0) | 40% | 10 / 9 | 343 | 2 |
| 51 | standard | v50 | decisive loss: Rebel victory: cities controlled | 10 | 7 | 22 | 5 | 1 (0) | 27% | 12 / 5 | 315 | 14 |
| 52 | alternate | v51 | decisive loss: Rebel victory: cities controlled | 5 | 8 | 4 | 3 | 1 (0) | 42% | 10 / 9 | 350 | 0 |
| 53 | standard | v52 | decisive loss: Rebel victory: cities controlled | 13 | 15 | 20 | 8 | 1 (0) | 28% | 13 / 4 | 632 | 14 |
| 54 | alternate | v53 | decisive loss: Rebel victory: cities controlled | 8 | 18 | 0 | 9 | 6 (2) | 37% | 13 / 8 | 364 | 4 |
| 55 | standard | v54 | decisive loss: Rebel victory: cities controlled | 12 | 16 | 23 | 5 | 2 (1) | 53% | 11 / 7 | 200 | 13 |
| 56 | alternate | v55 | decisive loss: Rebel victory: cities controlled | 6 | 11 | 24 | 0 | 0 (0) | - | 10 / 9 | 552 | 5 |
| 57 | standard | v56 | decisive loss: Rebel victory: cities controlled | 11 | 12 | 19 | 5 | 1 (1) | 57% | 14 / 6 | 272 | 5 |
| 58 | alternate | v57 | decisive loss: Rebel victory: cities controlled | 3 | 6 | 4 | 0 | 0 (0) | - | 10 / 8 | 351 | 0 |
| 59 | standard | v58 | decisive loss: Rebel victory: cities controlled | 12 | 10 | 23 | 4 | 2 (1) | 38% | 11 / 6 | 237 | 8 |
| 60 | alternate | v59 | decisive loss: Rebel victory: cities controlled | 12 | 33 | 35 | 7 | 0 (0) | - | 13 / 8 | 292 | 12 |
| 61 | standard | v60 | decisive loss: Rebel victory: capital captured | 5 | 6 | 5 | 5 | 1 (1) | 50% | 12 / 11 | 281 | 3 |
| 62 | alternate | v61 | decisive loss: Rebel victory: cities controlled | 17 | 31 | 29 | 3 | 3 (3) | 61% | 11 / 9 | 364 | 9 |
| 63 | standard | v62 | decisive loss: Rebel victory: cities controlled | 11 | 10 | 9 | 4 | 0 (0) | - | 11 / 6 | 181 | 9 |
| 64 | alternate | v63 | decisive loss: Rebel victory: cities controlled | 3 | 6 | 0 | 7 | 1 (0) | 30% | 13 / 10 | 586 | 1 |
| 65 | standard | v64 | decisive loss: Rebel victory: cities controlled | 17 | 12 | 27 | 5 | 4 (2) | 61% | 11 / 5 | 254 | 9 |
| 66 | alternate | v65 | decisive loss: Rebel victory: cities controlled | 6 | 16 | 22 | 0 | 0 (0) | - | 10 / 8 | 330 | 2 |
| 67 | standard | v66 | decisive loss: Rebel victory: cities controlled | 13 | 13 | 26 | 0 | 0 (0) | - | 11 / 6 | 236 | 6 |
| 68 | alternate | v67 | decisive loss: Rebel victory: cities controlled | 4 | 12 | 18 | 0 | 0 (0) | - | 10 / 9 | 345 | 3 |
| 69 | standard | v68 | decisive loss: Rebel victory: capital captured | 12 | 10 | 26 | 1 | 1 (1) | 66% | 11 / 7 | 344 | 6 |
| 70 | alternate | v69 | decisive loss: Rebel victory: cities controlled | 9 | 13 | 27 | 0 | 0 (0) | - | 10 / 7 | 369 | 1 |
| 71 | standard | v70 | decisive loss: Rebel victory: cities controlled | 14 | 14 | 25 | 2 | 1 (1) | 78% | 11 / 7 | 257 | 17 |
| 72 | alternate | v71 | decisive loss: Rebel victory: cities controlled | 7 | 19 | 26 | 0 | 0 (0) | - | 10 / 9 | 341 | 5 |
| 73 | standard | v72 | decisive loss: Rebel victory: capital captured | 11 | 16 | 27 | 5 | 3 (1) | 48% | 11 / 8 | 281 | 10 |
| 74 | alternate | v73 | decisive loss: Rebel victory: cities controlled | 6 | 18 | 20 | 2 | 1 (1) | 37% | 10 / 8 | 351 | 9 |
| 75 | standard | v74 | decisive loss: Rebel victory: cities controlled | 12 | 7 | 24 | 2 | 1 (1) | 66% | 11 / 6 | 270 | 4 |
| 76 | alternate | v75 | decisive loss: Rebel victory: cities controlled | 5 | 13 | 0 | 5 | 3 (0) | 43% | 10 / 8 | 327 | 0 |
| 77 | standard | v76 | decisive loss: Rebel victory: cities controlled | 9 | 12 | 0 | 10 | 5 (1) | 46% | 11 / 7 | 293 | 4 |
| 78 | alternate | v77 | decisive loss: Rebel victory: share of total income | 12 | 20 | 28 | 7 | 2 (2) | 52% | 11 / 8 | 266 | 8 |
| 79 | standard | v78 | decisive loss: Rebel victory: cities controlled | 7 | 9 | 0 | 6 | 2 (0) | 44% | 11 / 6 | 256 | 5 |
| 80 | alternate | v79 | decisive loss: Rebel victory: cities controlled | 4 | 3 | 6 | 0 | 0 (0) | - | 10 / 8 | 809 | 0 |
| 81 | standard | v80 | decisive loss: Rebel victory: cities controlled | 11 | 7 | 26 | 3 | 2 (1) | 58% | 11 / 7 | 418 | 12 |
| 82 | alternate | v81 | decisive loss: Rebel victory: cities controlled | 6 | 12 | 28 | 1 | 0 (0) | - | 10 / 8 | 606 | 3 |
| 83 | standard | v82 | decisive loss: Rebel victory: cities controlled | 11 | 3 | 22 | 2 | 0 (0) | - | 11 / 6 | 371 | 6 |
| 84 | alternate | v83 | decisive loss: Rebel victory: share of total income | 4 | 12 | 17 | 3 | 1 (1) | 55% | 10 / 10 | 347 | 7 |
| 85 | standard | v84 | decisive loss: Rebel victory: cities controlled | 8 | 12 | 1 | 13 | 2 (0) | 20% | 11 / 6 | 285 | 10 |
| 86 | alternate | v85 | decisive loss: Rebel victory: share of total income | 10 | 11 | 6 | 8 | 7 (0) | 32% | 10 / 8 | 886 | 2 |
| 87 | standard | v86 | decisive loss: Rebel victory: cities controlled | 16 | 11 | 0 | 12 | 3 (0) | 31% | 11 / 4 | 448 | 5 |
| 88 | alternate | v87 | decisive loss: Rebel victory: cities controlled | 11 | 24 | 27 | 1 | 1 (0) | 44% | 10 / 9 | 344 | 8 |
| 89 | standard | v88 | decisive loss: Rebel victory: cities controlled | 14 | 9 | 22 | 3 | 2 (1) | 61% | 11 / 5 | 765 | 16 |
| 90 | alternate | v89 | decisive loss: Rebel victory: cities controlled | 4 | 12 | 13 | 1 | 0 (0) | - | 10 / 9 | 360 | 3 |
| 91 | standard | v90 | decisive loss: Rebel victory: cities controlled | 16 | 11 | 22 | 7 | 3 (2) | 60% | 12 / 7 | 270 | 11 |
| 92 | alternate | v91 | decisive loss: Rebel victory: cities controlled | 4 | 12 | 13 | 1 | 0 (0) | - | 10 / 9 | 342 | 4 |
| 93 | standard | v92 | decisive loss: Rebel victory: cities controlled | 10 | 14 | 25 | 6 | 1 (0) | 8% | 12 / 7 | 210 | 13 |
| 94 | alternate | v93 | decisive loss: Rebel victory: cities controlled | 5 | 13 | 0 | 3 | 1 (0) | 37% | 10 / 8 | 343 | 1 |
| 95 | standard | v94 | decisive loss: Rebel victory: cities controlled | 9 | 13 | 16 | 10 | 2 (0) | 32% | 13 / 6 | 175 | 9 |
| 96 | alternate | v95 | decisive loss: Rebel victory: cities controlled | 4 | 10 | 3 | 5 | 2 (0) | 40% | 10 / 8 | 347 | 3 |
| 97 | standard | v96 | decisive loss: Rebel victory: capital captured | 5 | 12 | 0 | 6 | 1 (0) | 18% | 13 / 12 | 295 | 4 |
| 98 | alternate | v97 | decisive loss: Rebel victory: cities controlled | 5 | 12 | 1 | 8 | 1 (0) | 21% | 13 / 10 | 337 | 2 |
| 99 | standard | v98 | decisive loss: Rebel victory: capital captured | 6 | 2 | 5 | 9 | 3 (1) | 38% | 12 / 8 | 926 | 0 |
| 100 | alternate | v99 | decisive loss: Rebel victory: cities controlled | 6 | 17 | 20 | 7 | 2 (1) | 51% | 13 / 10 | 381 | 3 |

## How the notebook changed

### Version 1, after game 1 (standard: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We lost quickly because we spent too much time drilling and building ships instead of recruiting new troops and capturing enemy cities. The computer opponent actively marched and took territory, while our passive stance allowed the Confederates to outnumber us locally, seize our cities, and choke our income.

**Strategy for the next game.** Next game we will aggressively recruit forces, maintain our supply lines, and actively maneuver against enemy-held cities to outpace the Confederate expansion.

**Changes:**

- added: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (We completely failed to recruit troops in our first game, falling far behind the computer's rate and losing ground.)
- added: When an army is adjacent to a weakly held enemy city with favorable odds, issue a move order to capture it. (We spent too many turns drilling instead of attacking or taking territory, leading to a rapid defeat.)
- added: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Our armies ran out of supplies by late 1861 because we never purchased supply tokens.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to a weakly held enemy city with favorable odds, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.

### Version 2, after game 2 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We successfully built up a large troop count through constant recruiting and maintained a healthy treasury, but our army failed to capture enough cities because we neglected offensive movement and wasted actions on excessive drilling while the Rebels steadily claimed territory.

**Strategy for the next game.** We will continue our steady recruitment and supply management while strictly limiting excessive drilling. We will focus our movement orders on attacking weakly defended cities with high odds to rapidly expand our city count and deny the Rebels territory.

**Changes:**

- revised: When an army is adjacent to an enemy city with favorable odds above 50 percent, issue a move order to capture it. (We attacked at poor odds too often and lost battles; we need to pick favorable engagements to seize territory without heavy losses.)
- dropped: When an experienced commander's army rests, issue a drill order to raise its experience. (Drilling too often distracted us from capturing cities and expanding our territorial control, leading to a loss by city count.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 50 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.

### Version 3, after game 3 (standard: Rebel victory: cities controlled, 13 turns)

**Diagnosis.** We focused too much on drilling and moving isolated armies while neglecting regional concentration and maintaining army supply lines. The Rebels concentrated large forces like A.S. Johnston and R.E. Lee to overwhelm our smaller detachments and capture our key cities, while we frequently ran out of supply and suffered repeated refusals for supply orders.

**Strategy for the next game.** Next game, we will focus heavily on keeping our main armies well-supplied and consolidated into large forces, avoiding isolated advances, and recruiting aggressively to match Confederate numbers while defending our capital and key industrial centers.

**Changes:**

- added: When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking. (We repeatedly suffered from starving armies like McDowell's and McClellan's getting stuck without supplies, leading to severe losses during enemy attacks.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 50 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.

### Version 4, after game 4 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused heavily on recruiting and drilling separate armies while neglecting coordinated offensives and territory capture. The Confederates aggressively seized cities and advanced while we remained passive, leading to a loss of key cities and control.

**Strategy for the next game.** Next game we will balance recruitment with aggressive moves on adjacent enemy cities to seize territory and income, avoiding excessive drilling that leaves us passive while the enemy captures the map.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (Maintained from notebook v3 as it successfully built up our forces across games.)
- revised: When an army is adjacent to an enemy city with favorable odds above 50 percent, issue a move order to capture it. (Maintained from notebook v3 to ensure we push for objective city captures rather than endlessly drilling.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Kept from notebook v3 to prevent attrition and keep combat readiness high.)
- revised: When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking. (Retained from notebook v3 to ensure survival of isolated forces.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 50 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.

### Version 5, after game 5 (standard: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** We focused too much on drilling and too little on recruiting, aggressive movement, and fleet operations, allowing the Rebels to outpace us in city control and military strength. Furthermore, attacking fortified positions at poor odds drained our armies without gaining territory.

**Strategy for the next game.** Next game, we will prioritize steady recruitment of new forces, keep our armies supplied before launching attacks, avoid low-odds assaults on fortified cities, and actively use our fleet to protect our ports and disrupt the enemy.

**Changes:**

- added: When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it. (We failed to utilize our fleet against enemy bombardments and blockades, losing Philadelphia to neutrality.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 50 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
5. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.

### Version 6, after game 6 (alternate: Rebel victory: share of total income, 16 turns)

**Diagnosis.** We focused too much on drilling and accumulated large idle forces while failing to capture enemy cities or counter the rebel naval blockade at Philadelphia. When armies ran out of supply, we repeatedly ordered attacks instead of retreating to friendly cities or using the supply command, leading to disastrous defeats and severe attrition.

**Strategy for the next game.** Next game, we will aggressively recruit in available cities, immediately engage and clear enemy fleets blockading our ports, keep our armies supplied before they hit zero, and advance to capture enemy-held cities with favorable odds rather than endlessly drilling.

**Changes:**

- revised: When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking. (We failed to follow this in Game 6 by ordering zero-supply armies like Grant to attack strong enemy positions, causing massive losses.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 50 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
5. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.

### Version 7, after game 7 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** The Confederacy won because our armies repeatedly launched low-odds attacks against fortified positions like Harper Ferry while leaving key units unsupplied and idle in the field. We relied too heavily on drilling instead of marching to capture cities, leading to a steady loss of territory and income.

**Strategy for the next game.** Next game, we will focus on maintaining positive supply lines, avoiding attacks on fortified cities unless odds exceed 50 percent, and aggressively capturing neutral or weakly held cities to secure our income and territory.

**Changes:**

- dropped: When an army's odds of success are below 50 percent, do not issue a move order to attack, but instead issue a drill or fortify order. (This lesson encouraged excessive passivity and low-odds attacks without restricting movement properly, contributing to poor tactical outcomes.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 50 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
5. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.

### Version 8, after game 8 (alternate: Rebel victory: share of total income, 11 turns)

**Diagnosis.** We focused heavily on drilling and recruiting while letting our frontline armies languish with poor movement and low attack rates, allowing the Rebels to seize the initiative, capture our key cities, and blockade our ports. Our lack of offensive pressure and failure to eliminate threats led to a gradual loss of income and territory.

**Strategy for the next game.** Next game we will maintain steady recruitment while aggressively moving armies with good odds to capture enemy cities, avoiding excessive drilling that stalls our advance and surrenders the initiative.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (Maintained from previous notebook version as it has a strong positive record (+4.9 turns).)
- revised: When an army is adjacent to an enemy city with favorable odds above 50 percent, issue a move order to capture it. (Retained to encourage active and successful offensives instead of passive drilling.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Kept to prevent attrition and supply failures that hurt our armies in past games.)
- revised: When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking. (Retained to ensure unsupported units fall back rather than getting crushed.)
- revised: When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it. (Kept to deal with port blockades that drain our supply lines.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 50 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
5. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.

### Version 9, after game 9 (standard: Rebel victory: cities controlled, 13 turns)

**Diagnosis.** We focused far too much on drilling and recruitment while neglecting to capture enemy cities or defend properly. Our attack rate was only 0.15 per turn compared to the computer's 3.90, and we won zero attacks because we kept attacking entrenched or superior forces with unfavorable odds. Consequently, the Rebels steadily expanded and overwhelmed us by March 1863.

**Strategy for the next game.** Next game, we will aggressively push offensive moves when odds exceed 50 percent, reduce excessive drilling, and maintain strict control over army supply lines to capture and hold vital territory.

**Changes:**

- revised: When an army is adjacent to an enemy city with favorable odds above 50 percent, issue a move order to capture it. (We failed to press attacks and lost because we initiated too few offensive actions at poor odds.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Keeping supply stable is critical to avoid combat penalties during engagements.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 50 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
5. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.

### Version 10, after game 10 (alternate: Rebel victory: share of total income, 8 turns)

**Diagnosis.** We expanded our army sizes well and accumulated strong cash reserves, but we suffered severe losses by attacking enemy forces without sufficient numerical superiority or leader advantage. Furthermore, we failed to deal with the enemy fleet blockading Philadelphia, which damaged our city and turned it neutral.

**Strategy for the next game.** Next game, we will prioritize raising troops in safe interior cities, maintaining supply lines, and engaging in naval defense of our ports while strictly avoiding low-odds attacks until our armies possess overwhelming numerical superiority.

**Changes:**

- revised: When an army is adjacent to an enemy city with favorable odds above 60 percent, issue a move order to capture it. (We lost too many battles and men fighting at 40-50 percent odds. Raising the threshold to 60 percent ensures we only attack when heavily favored.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 60 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
5. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.

### Version 11, after game 11 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** In this game we heavily over-relied on drilling while neglecting offensive maneuvers and supply lines, causing our armies to repeatedly run out of food and suffer attrition. The Rebels systematically outmaneuvered and defeated our isolated forces, capturing key cities and squeezing our income until we lost.

**Strategy for the next game.** Next game we will curb excessive drilling, maintain strict control over army supply lines, and push forward only when attack odds are decisively in our favor above 60 percent to steadily capture and hold territory.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (Maintained from previous notebook as the foundational rule for building our force size.)
- revised: When an army is adjacent to an enemy city with favorable odds above 60 percent, issue a move order to capture it. (Kept to prevent low-odds suicide attacks that drain our manpower.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Retained because repeated supply failures crippled our combat strength in this game.)
- revised: When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking. (Kept to ensure starving armies fall back instead of fighting at a severe disadvantage.)
- revised: When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it. (Maintained to protect our seaports and commerce from enemy blockades.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 60 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
5. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.

### Version 12, after game 12 (alternate: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We focused almost entirely on recruiting and drilling while performing almost no offensive moves or supplying our armies, allowing the Rebels to seize territory and capture cities while our forces sat idle or suffered from supply shortages.

**Strategy for the next game.** Next game, we will balance recruiting and drilling with active offensive movements to capture enemy cities and maintain proper supply lines for our advancing armies.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (Kept as it has a solid record and ensures our forces continue to grow.)
- revised: When an army is adjacent to an enemy city with favorable odds above 60 percent, issue a move order to capture it. (Kept to ensure we press the advantage and take territory rather than just drilling.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 60 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
5. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.

### Version 13, after game 13 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused heavily on drilling rather than maintaining offensive pressure or capturing empty or weakly held cities. Our attacks had poor odds because we moved small or unjoined forces against well-defended enemy locations without sufficient numerical advantage or supply.

**Strategy for the next game.** We will prioritize active movement to capture unoccupied or poorly defended cities, ensure our attacking armies have clear numerical and supply superiority before engaging, and maintain aggressive recruitment to pressure the Confederate capital.

**Changes:**

- dropped: When an army's experience is below the leader's rating, issue a drill order to improve combat performance. (Over-drilling contributed to a passive posture and allowed the Rebels to dictate the initiative and accumulate territory.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 60 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
5. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.

### Version 14, after game 14 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused too much on drilling and accumulated large idle forces while the Confederate computer aggressively captured cities and maneuvered to take territory. Although our army size grew, we failed to press our advantages with sufficient move orders to secure key cities, leading to a loss of control on the map.

**Strategy for the next game.** We will continue to recruit and supply our forces robustly, but we must translate our growing manpower into proactive move orders to capture cities and contest Rebel advances rather than relying excessively on drilling.

**Changes:**

- added: When an army has finished drilling or resting and is adjacent to an undefended or vulnerable enemy city, issue a move order to capture it immediately. (We fell behind in city counts because we kept armies stationary drilling instead of pushing them forward to take enemy territory.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 60 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
5. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
6. When an army has finished drilling or resting and is adjacent to an undefended or vulnerable enemy city, issue a move order to capture it immediately.

### Version 15, after game 15 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We lost quickly because our armies ran out of supply and were caught attacking at poor odds against larger Rebel concentrations, while we spent too many turns drilling instead of consolidating or supplying.

**Strategy for the next game.** Next game we will maintain strict control over army supply lines, avoid attacking into superior enemy defenses without favorable odds above 60 percent, and keep our main forces concentrated and supplied.

**Changes:**

- dropped: When an army has finished drilling or resting and is adjacent to an undefended or vulnerable enemy city, issue a move order to capture it immediately. (It failed to prevent our armies from attacking at poor odds and running out of supply.)
- added: When an army has low supply or is preparing for an offensive, issue a supply order rather than a drill order. (We lost several armies to supply exhaustion while spending too many actions on drilling.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 60 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
5. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
6. When an army has low supply or is preparing for an offensive, issue a supply order rather than a drill order.

### Version 16, after game 16 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused heavily on recruitment and built up a large troop count, but we suffered from poor attack timing. We initiated attacks with unfavorable odds, and we failed to maintain consistent supply lines, leaving armies vulnerable to counterattacks and attrition. Meanwhile, the computer aggressively captured cities and applied pressure.

**Strategy for the next game.** We will continue to aggressively recruit to maintain numerical superiority, but we will strictly monitor supply and only attack when odds exceed 60 percent to avoid disastrous defeats.

**Changes:**

- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (We encountered supply shortages and failed to resupply promptly during critical turns, leading to combat penalties.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 60 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
5. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
6. When an army has low supply or is preparing for an offensive, issue a supply order rather than a drill order.

### Version 17, after game 17 (standard: Rebel victory: share of total income, 10 turns)

**Diagnosis.** We lost control of our supply lines and economy while repeatedly attacking or drilling instead of securing adjacent cities and maintaining army supply. Armies frequently ran out of supply, leading to reduced combat effectiveness and defeat, culminating in the loss of Washington.

**Strategy for the next game.** We will prioritize maintaining supply lines for all active armies, restrict drilling until logistics are secure, and systematically capture adjacent neutral and enemy cities with favorable odds.

**Changes:**

- revised: When an army is out of supply or low on supply, issue a supply order rather than a drill order. (The previous lesson was too narrow and allowed excessive drilling while key armies suffered supply starvation in the field.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army is adjacent to an enemy city with favorable odds above 60 percent, issue a move order to capture it.
3. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
4. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
5. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
6. When an army is out of supply or low on supply, issue a supply order rather than a drill order.

### Version 18, after game 18 (alternate: Rebel victory: share of total income, 9 turns)

**Diagnosis.** We focused heavily on drilling rather than capturing enemy territory, and we repeatedly launched hopeless attacks against heavily defended enemy cities with severe odds disadvantages, draining our manpower without achieving territorial gains.

**Strategy for the next game.** Next game, we will stop wasteful drilling and reckless low-odds attacks, maintain proper supply lines, and only advance on enemy cities when we hold a clear and overwhelming local numerical superiority.

**Changes:**

- revised: When an army is adjacent to an enemy city and our strength outnumbers the enemy by at least 2 to 1, issue a move order to capture it. (We kept attacking heavily fortified cities at terrible odds (under 20%), resulting in massive casualties and zero wins; we need strict numerical superiority before moving to attack.)
- dropped: When an army has favorable odds above 60 percent, issue a move order to capture it. (Replaced by a stricter, more reliable threshold rule based on force ratio to avoid disastrous attacks on fortified positions.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an army is adjacent to an enemy city and our strength outnumbers the enemy by at least 2 to 1, issue a move order to capture it.
6. When an army is out of supply or low on supply, issue a supply order rather than a drill order.

### Version 19, after game 19 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** This game went poorly because we failed to recruit new troops and reinforce our armies while spending most of our turns drilling and letting our forces dwindle in size and supply. The Confederacy outproduced and outflanked us while our armies remained static or starved.

**Strategy for the next game.** Next game we will aggressively recruit to match Rebel numbers, maintain supply lines to prevent attrition, and launch coordinated attacks with superior strength rather than defaulting to excessive drilling.

**Changes:**

- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (We failed to issue supply orders when armies were starving, leading to severe supply penalties and losses.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an army is adjacent to an enemy city and our strength outnumbers the enemy by at least 2 to 1, issue a move order to capture it.
6. When an army is out of supply or low on supply, issue a supply order rather than a drill order.

### Version 20, after game 20 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused heavily on recruiting and drilling, but neglected aggressive movement and city capture. The computer expanded rapidly and secured 28 cities while we remained passive, resulting in a technical defeat through city control.

**Strategy for the next game.** We will continue to recruit and maintain supply, but we must shift our primary focus to attacking adjacent enemy cities with superior numbers to capture territory and prevent the Confederate victory condition.

**Changes:**

- dropped: When an army's experience is below the leader's rating, issue a drill order to improve combat performance. (We overused drilling while neglecting map control and city capture, losing the game on city count.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an army is adjacent to an enemy city and our strength outnumbers the enemy by at least 2 to 1, issue a move order to capture it.
6. When an army is out of supply or low on supply, issue a supply order rather than a drill order.

### Version 21, after game 21 (standard: Rebel victory: cities controlled, 11 turns)

**Diagnosis.** We focused heavily on drilling rather than expanding our territory or defending our capital. Excessive drilling drained turns while Rebel armies seized cities and ultimately captured Washington, leading to a technical defeat.

**Strategy for the next game.** We will halt excessive drilling, maintain active recruitment, keep our supply lines secure, and aggressively defend Washington and key cities while pressing the offensive when we outnumber the enemy.

**Changes:**

- added: When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies. (We lost Washington because Jackson advanced unhindered while our forces spent turns drilling in the interior.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an army is adjacent to an enemy city and our strength outnumbers the enemy by at least 2 to 1, issue a move order to capture it.
6. When an army is out of supply or low on supply, issue a supply order rather than a drill order.
7. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.

### Version 22, after game 22 (alternate: Rebel victory: share of total income, 5 turns)

**Diagnosis.** We focused heavily on recruitment and built up a strong manpower base, but our attacks were poorly timed against fortified or superior enemy positions, leading to costly defeats. Meanwhile, the Confederate forces concentrated strength, overwhelmed our northern positions, and secured key cities to trigger early victory conditions.

**Strategy for the next game.** Next game, we will continue aggressive recruitment and force concentration, but we must strictly avoid attacking fortified enemy positions unless we achieve overwhelming odds and proper supply superiority. We will prioritize defending key strongpoints and maintaining steady logistics.

**Changes:**

- revised: When an army is adjacent to an enemy city and our strength outnumbers the enemy by at least 2 to 1 and the enemy is not fortified, issue a move order to capture it. (We lost several attacks against defended and fortified enemy cities because basic numerical advantage wasn't enough when factoring in defender bonuses.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an army is adjacent to an enemy city and our strength outnumbers the enemy by at least 2 to 1 and the enemy is not fortified, issue a move order to capture it.
6. When an army is out of supply or low on supply, issue a supply order rather than a drill order.
7. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.

### Version 23, after game 23 (standard: Rebel victory: capital captured, 6 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while allowing Confederate forces under Jackson to slip through and capture key cities like Philadelphia and eventually our capital Washington. Our failure to aggressively intercept and destroy enemy columns, combined with neglecting defensive positioning, left our core territory vulnerable to a rapid Confederate breakthrough.

**Strategy for the next game.** We will continue to build our numbers through steady recruitment while maintaining army supply, but we will shift from excessive drilling and passive defense to actively intercepting and destroying enemy forces that threaten our capital and core cities.

**Changes:**

- dropped: When an army is adjacent to an enemy city and our strength outnumbers the enemy by at least 2 to 1 and the enemy is not fortified, issue a move order to capture it. (This lesson had no meaningful track record and did not help prevent the enemy from outmaneuvering us.)
- added: When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them. (Added to ensure we actively block and counter Confederate raiding forces before they capture critical cities and our capital.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When an army is out of supply or low on supply, issue a supply order rather than a drill order.
7. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.

### Version 24, after game 24 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused heavily on drilling and recruiting while allowing the Confederate forces to aggressively capture cities, surround our ports, and outnumber us in key regional battles. Our lack of strategic movement and naval action allowed the enemy to control 28 cities and secure a technical victory.

**Strategy for the next game.** We will aggressively recruit in core cities, actively use our fleet to break blockades and contest enemy naval movements, and employ coordinated moves and attacks to retake lost territory before the enemy achieves critical mass.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (Maintained from previous notebook to ensure steady force growth.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When an army is out of supply or low on supply, issue a supply order rather than a drill order.
7. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.

### Version 25, after game 25 (standard: Rebel victory: capital captured, 18 turns)

**Diagnosis.** We relied too heavily on drilling distant armies rather than aggressively recruiting and expanding our territory, allowing the Confederacy to outpace us in city control and eventually capture our capital.

**Strategy for the next game.** We will focus on aggressive recruitment in major cities, maintain robust supply lines for our frontline forces, and aggressively intercept Confederate advances to protect our capital and core territory.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (Maintained from previous notebook to ensure steady force growth.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Kept to prevent armies from fighting at half strength or starving.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When an army is out of supply or low on supply, issue a supply order rather than a drill order.
7. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.

### Version 26, after game 26 (alternate: Rebel victory: cities controlled, 11 turns)

**Diagnosis.** We successfully built up a large army and survived longer than previous games, but we heavily neglected naval operations and offensive strategy. While we recruited and drilled extensively, we failed to counter enemy naval blockades or launch meaningful campaigns to capture enemy cities, eventually allowing the Rebels to surround and capture our capital.

**Strategy for the next game.** Next game, we will maintain our strong recruitment and supply management, but we will actively build and sail our fleet to clear enemy blockades and prevent them from starving our coastal forces while launching concerted offensives to capture enemy cities.

**Changes:**

- added: When our port is blockaded by an enemy fleet, issue a fleet sail order to clear the blockade and restore supply lines. (We suffered repeated blockades on our ports without deploying naval forces to counter them, which crippled our army supplies.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When an army is out of supply or low on supply, issue a supply order rather than a drill order.
7. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
8. When our port is blockaded by an enemy fleet, issue a fleet sail order to clear the blockade and restore supply lines.

### Version 27, after game 27 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused heavily on drilling armies rather than expanding territory or capturing key objective cities, allowing the Confederates to steadily out-expand us and claim victory via city control. Our attacks were also infrequent and often poorly timed against well-defended positions.

**Strategy for the next game.** Next game, we will reduce unnecessary drilling, keep our armies well-supplied, and actively push out to capture and secure enemy cities to prevent the Confederacy from winning on city count.

**Changes:**

- added: When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling. (We drilled too much and attacked too little in this game, losing the city control race to the computer.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When an army is out of supply or low on supply, issue a supply order rather than a drill order.
7. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
8. When our port is blockaded by an enemy fleet, issue a fleet sail order to clear the blockade and restore supply lines.
9. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.

### Version 28, after game 28 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while allowing the Rebels to capture our capital and vital cities. Our armies were fragmented, and we failed to intercept enemy advances toward Washington, leading to a quick defeat.

**Strategy for the next game.** We will prioritize defending our capital and core cities, intercepting advancing Rebel armies immediately, and maintaining solid supply lines while continuing steady recruitment.

**Changes:**

- dropped: When an army is out of supply or low on supply, issue a supply order rather than a drill order. (This lesson was redundant with lesson 2.)
- dropped: When our port is blockaded by an enemy fleet, issue a fleet sail order to clear the blockade and restore supply lines. (This lesson overlapped too much with lesson 4 regarding enemy fleets.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.

### Version 29, after game 29 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We focused excessively on drilling while allowing Confederate forces to seize key cities and isolate our armies. We engaged in unfavourable attacks without sufficient concentration of force, and failed to maintain adequate supply lines or protect our ports from blockades.

**Strategy for the next game.** We will prioritize securing our cities and supply lines, aggressively eliminate enemy fleets blockading our ports, and coordinate concentrated attacks on weakened enemy positions while minimizing unproductive drilling.

**Changes:**

- revised: When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking. (We lost multiple armies and battles due to moving and attacking while out of supply. Retreating to safety is vital when supply fails.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.

### Version 30, after game 30 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused excessively on recruiting and drilling while remaining largely idle, allowing the Confederacy to capture key cities unopposed and achieve a quick victory by controlling 28 cities.

**Strategy for the next game.** Next game, we will immediately pivot from passive drilling and heavy recruitment to proactive offensive operations, attacking adjacent enemy cities and intercepting enemy advances to secure territory before the Rebels overwhelm us.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.

### Version 31, after game 31 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused heavily on recruitment and isolated counter-attacks, but neglected securing our logistics and expanding naval dominance. Allowing enemy forces like Jackson to persistently harass Harper Ferry and letting our armies run out of supply crippled our offense. Meanwhile, the Confederacy outmaneuvered us and seized key regional cities, leading to a swift collapse.

**Strategy for the next game.** Next game, we will maintain rigorous supply lines for all advancing armies, protect our core cities from Confederate incursions without overextending, and systematically recruit to maintain force parity while eliminating enemy fleets.

**Changes:**

- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (We failed to issue supply orders promptly during critical turns in 1861 and 1862, causing multiple armies to run out of supplies and stall.)
- revised: When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking. (McClellan's army became stranded in Nashville without supplies and was forced to retreat under adverse conditions; immediate withdrawal is vital.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.

### Version 32, after game 32 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused heavily on drilling and passive recruitment while allowing Confederate forces to seize key western cities and blockade our ports. Our attacks lacked sufficient numerical superiority and coordination, leading to high casualties, the loss of Grant's army, and a quick Rebel victory in July 1862.

**Strategy for the next game.** Next game, we will prioritize aggressive movement and attacking vulnerable enemy positions rather than excessive drilling, while keeping our armies properly supplied and defending core cities.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.

### Version 33, after game 33 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused heavily on drilling distant armies while enemy forces outmaneuvered us, captured key cities, and ultimately seized our capital. Our supply lines frequently collapsed, leaving armies unable to fight effectively. We must prioritize recruiting, maintaining army supply, and intercepting enemy threats to core territory rather than idling.

**Strategy for the next game.** Next game, we will keep our armies supplied and concentrated around core territories, actively recruit to build our strength, and immediately intercept any Confederate advances toward our capital or key cities rather than spending turns drilling.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.

### Version 34, after game 34 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** The Confederate forces successfully captured core cities and outmaneuvered our scattered armies, while our attempts to attack fortified positions resulted in heavy losses. Although we expanded our military strength through recruitment and won several defensive engagements, failing to maintain cohesive lines and attacking heavily defended enemy positions like Nashville drained our forces and allowed the Rebels to achieve victory.

**Strategy for the next game.** We will continue to aggressively recruit in all available cities while maintaining sufficient cash reserves. We will prioritize reinforcing threatened core territory, keeping our armies well-supplied, and launching attacks only against weakly held adjacent enemy cities to steadily erode Confederate control without risking disastrous assaults on heavily fortified positions.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.

### Version 35, after game 35 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused too heavily on drilling and allowed enemy forces to seize the initiative and accumulate cities. Our attacks were poorly timed and lost due to low odds and lack of concentrated force, leading to a loss of supply and territory.

**Strategy for the next game.** We will increase recruitment to build up our forces, minimize unnecessary drilling, and concentrate our attacks on weak or isolated enemy positions to reclaim territory.

**Changes:**

- revised: When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling. (We attacked with unfavorable odds during this game, so we must be stricter about attacking only weakly held cities with supplied armies.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.

### Version 36, after game 36 (alternate: Rebel victory: share of total income, 6 turns)

**Diagnosis.** In this alternate map game, we relied too heavily on drilling while the Confederate computer aggressively captured territory, attacked our positions, and blockaded and neutralized Philadelphia with naval bombardments. We failed to maintain offensive momentum, neglected naval defense entirely, and launched poorly supported attacks that resulted in heavy defeats.

**Strategy for the next game.** Next game, we will aggressively recruit to build up our forces, maintain naval strength to protect our ports against enemy fleets, and launch coordinated attacks with supplied armies rather than wasting turns on excessive drilling.

**Changes:**

- added: When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports. (We ignored naval defense completely this game, allowing the Confederate fleet to bombard Philadelphia into neutrality and blockade our forces without resistance.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.
8. When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports.

### Version 37, after game 37 (standard: Rebel victory: cities controlled, 13 turns)

**Diagnosis.** We focused heavily on drilling distant armies while losing key territory and cities to Confederate counterattacks. Our lack of offensive initiative allowed the Rebels to concentrate forces, outnumber us locally, and capture our cities while we suffered supply shortages and low win rates in battle.

**Strategy for the next game.** Next game, we will prioritize active recruitment and capturing adjacent vulnerable enemy cities while maintaining supply lines, avoiding excessive drilling that leaves our armies out of position and vulnerable to Confederate advances.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.
8. When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports.

### Version 38, after game 38 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We relied too heavily on drilling while the Rebel forces aggressively captured key cities and pushed our lines back. Our armies lacked coordination, leading to unfavorable attacks like the one against Nashville, and we failed to secure enough territory to meet victory conditions.

**Strategy for the next game.** Next game, we will reduce unnecessary drilling and focus on aggressive recruitment, seizing neutral or weakly held enemy cities to maintain territorial dominance, and keeping our armies well-supplied and concentrated for effective offensives.

**Changes:**

- added: When an adjacent enemy city is weakly defended and our attacking force has superior numbers and supply, issue a move order to capture it rather than drilling. (We lost this game because we spent too many turns drilling instead of pressing the attack on vulnerable enemy cities.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.
8. When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports.
9. When an adjacent enemy city is weakly defended and our attacking force has superior numbers and supply, issue a move order to capture it rather than drilling.

### Version 39, after game 39 (standard: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** We focused too much on drilling and building ships early on rather than maintaining a steady pace of recruitment and pressing attacks when we had numerical advantages. This allowed the Confederate armies to outgrow us in strength and gradually overwhelm our positions.

**Strategy for the next game.** Next game, we will prioritize continuous recruitment in available cities and direct aggressive movements against weakly defended enemy positions, while avoiding excessive drilling that leaves our frontlines under-resourced.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.
8. When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports.
9. When an adjacent enemy city is weakly defended and our attacking force has superior numbers and supply, issue a move order to capture it rather than drilling.

### Version 40, after game 40 (alternate: Rebel victory: cities controlled, 17 turns)

**Diagnosis.** We relied heavily on drilling and recruiting while neglecting aggressive offensive movements and proper supply management. Grant's army repeatedly fell out of supply and was eventually destroyed in Decatur, allowing the Rebels to secure the map and achieve victory.

**Strategy for the next game.** Next game, we will maintain rigorous supply lines for all active armies, avoid letting combat units sit idle drilling when enemy territory can be seized, and aggressively advance to capture enemy cities while keeping our forces concentrated and well-supplied.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.
8. When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports.
9. When an adjacent enemy city is weakly defended and our attacking force has superior numbers and supply, issue a move order to capture it rather than drilling.

### Version 41, after game 41 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We lost quickly because we attacked into enemy-held cities with insufficient strength and inferior odds, failing to build up our forces or use recruitment while over-relying on drilling. The computer vastly out-recruited us and out-maneuvered us while our armies starved for supply and were crushed in detail.

**Strategy for the next game.** Next game we will aggressively recruit to match the computer's numbers, avoid attacking into fortified cities without overwhelming local superiority, keep our armies supplied, and use the railroad to concentrate force where needed.

**Changes:**

- revised: When an adjacent enemy city is defended and our attacking force has inferior or equal numbers, issue a move order to fortify or join rather than attacking at poor odds. (We repeatedly threw small armies at enemy cities at 30-40% odds and lost battles and troops.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.
8. When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports.
9. When an adjacent enemy city is defended and our attacking force has inferior or equal numbers, issue a move order to fortify or join rather than attacking at poor odds.

### Version 42, after game 42 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while allowing Confederate armies under A.S. Johnston and Beauregard to seize key nodes like St. Louis, Indianapolis, and Louisville unopposed or at poor tactical odds. Although we eventually recaptured Louisville, our failure to concentrate forces and block enemy advances early allowed the Confederacy to overwhelm our regional defenses and achieve a rapid city-control victory.

**Strategy for the next game.** Next game we will maintain aggressive recruitment while prioritizing concentrated moves to block enemy advances into our core cities, avoiding uncoordinated attacks against defended enemy positions.

**Changes:**

- revised: When an adjacent enemy city is defended by equal or greater forces, issue a move order to join or fortify rather than attacking at poor odds. (We launched several costly attacks at inferior odds during this game which drained our manpower without securing decisive territory.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly held and we have a supplied army available, issue a move order to attack and capture it rather than drilling.
8. When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports.
9. When an adjacent enemy city is defended by equal or greater forces, issue a move order to join or fortify rather than attacking at poor odds.

### Version 43, after game 43 (standard: Rebel victory: capital captured, 8 turns)

**Diagnosis.** We focused heavily on erratic offensive moves into enemy-held territory with poor odds, while neglecting to defend our capital and supply lines. This allowed Confederate forces to flank us, cut our supplies, and eventually capture Washington.

**Strategy for the next game.** Next game, we will prioritize defending Washington and core cities, maintaining solid supply lines for all moving armies, avoiding suicidal low-odds attacks, and building up a stable economic and recruitment base before advancing.

**Changes:**

- added: When an enemy force threatens the capital, issue a move order to garrison Washington immediately rather than launching distant offensive campaigns. (We lost the game because the capital was left vulnerable and captured while our armies chased distant objectives.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is defended by equal or greater forces, issue a move order to join or fortify rather than attacking at poor odds.
8. When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports.
9. When an enemy force threatens the capital, issue a move order to garrison Washington immediately rather than launching distant offensive campaigns.

### Version 44, after game 44 (alternate: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** The Confederate forces concentrated their large armies and launched aggressive offensives that overwhelmed our isolated garrisons. Despite building up our total troop count, we spent too many turns drilling and recruiting instead of fortifying key cities or consolidating our armies via join orders to meet the Rebel advance with adequate strength.

**Strategy for the next game.** Next game, we will prioritize consolidating our forces into large, effective armies using join orders and defending our key cities with fortify orders rather than scattering our strength into small garrisons that are easily defeated by concentrated Rebel attacks.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is defended by equal or greater forces, issue a move order to join or fortify rather than attacking at poor odds.
8. When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports.
9. When an enemy force threatens the capital, issue a move order to garrison Washington immediately rather than launching distant offensive campaigns.

### Version 45, after game 45 (standard: Rebel victory: cities controlled, 16 turns)

**Diagnosis.** We focused heavily on drilling and routine recruiting while allowing the Confederate armies to systematically capture our core cities and reduce our territory to 7 cities by November 1863. Our lack of decisive offensive action and failure to intercept or counter enemy advances allowed the Rebels to seize the initiative and win via city control.

**Strategy for the next game.** Next game, we will aggressively counter enemy movements into our territory, prioritize defending and recapturing key cities, and limit excessive drilling in favor of active maneuvering and reinforcement.

**Changes:**

- dropped: When our armies are not actively engaged in combat or moving, issue a drill order to steadily increase their experience up to the leader's rating. (Excessive drilling consumed actions that should have been spent on movement, defense, and recapturing lost territory, contributing to our loss of cities.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is defended by equal or greater forces, issue a move order to join or fortify rather than attacking at poor odds.
8. When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports.
9. When an enemy force threatens the capital, issue a move order to garrison Washington immediately rather than launching distant offensive campaigns.

### Version 46, after game 46 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused entirely on recruiting and drilling while issuing zero move or attack orders. This left us completely passive, allowing the Confederacy to capture our cities unopposed and outpace us in territory and income until they secured a quick victory.

**Strategy for the next game.** We will maintain our steady recruitment and economic growth, but we will actively issue move and attack orders against vulnerable enemy cities to capture territory, deny the Rebels economic advantage, and contest control of the map.

**Changes:**

- revised: When an adjacent enemy city is weakly defended or our forces outnumber them locally, issue a move order to attack and capture it rather than only recruiting. (Lesson 7 previously told us only to fortify or join when facing equal or greater forces, but gave no positive instruction to attack, which led to our total lack of movement this game.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly defended or our forces outnumber them locally, issue a move order to attack and capture it rather than only recruiting.
8. When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports.
9. When an enemy force threatens the capital, issue a move order to garrison Washington immediately rather than launching distant offensive campaigns.

### Version 47, after game 47 (standard: Rebel victory: cities controlled, 13 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while remaining largely passive, allowing the Confederacy to capture key cities and gradually overwhelm us. Our lack of aggressive counter-attacks and failure to properly contest enemy movements led to a steady loss of territory and ultimate defeat.

**Strategy for the next game.** Next game, we will maintain our focus on steady recruitment and supply management while increasing offensive pressure on weakly defended enemy cities to prevent the Confederacy from securing a territorial majority.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly defended or our forces outnumber them locally, issue a move order to attack and capture it rather than only recruiting.
8. When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports.
9. When an enemy force threatens the capital, issue a move order to garrison Washington immediately rather than launching distant offensive campaigns.

### Version 48, after game 48 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused heavily on drilling and recruiting while allowing the Confederate armies to concentrate, maneuver freely, and capture core cities and ports. Our lack of active campaigning and failure to aggressively contest enemy troop movements and key territory led to being outmaneuvered and overwhelmed.

**Strategy for the next game.** Next game, we will balance our recruitment and drilling with aggressive counter-attacks against vulnerable Confederate forces, immediately contesting enemy advances on our cities and preventing them from dominating the map.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (Ensures consistent reinforcement while maintaining high overall troop levels.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Prevents attrition and keeps frontline forces operational.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly defended or our forces outnumber them locally, issue a move order to attack and capture it rather than only recruiting.
8. When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports.
9. When an enemy force threatens the capital, issue a move order to garrison Washington immediately rather than launching distant offensive campaigns.

### Version 49, after game 49 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We suffered a decisive loss because our armies repeatedly attacked fortified enemy positions at poor odds and ran out of supply, while failing to consolidate or properly defend Washington and our core cities. We engaged in piecemeal assaults that bled our strength and allowed the Confederates to capture our capital.

**Strategy for the next game.** Next game, we will prioritize maintaining supply lines for all active armies, avoid low-odds attacks against defended cities, and ensure Washington and our core territories are heavily garrisoned and fortified against Confederate advances.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them.
6. When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies.
7. When an adjacent enemy city is weakly defended or our forces outnumber them locally, issue a move order to attack and capture it rather than only recruiting.
8. When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports.
9. When an enemy force threatens the capital, issue a move order to garrison Washington immediately rather than launching distant offensive campaigns.

### Version 50, after game 50 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused overwhelmingly on recruiting and drilling while ignoring offensive movement, allowing the AI to capture critical cities unchecked. Despite having 166,400 men, we made only one attack and one move order across five turns, resulting in an overwhelming defeat in terms of city control.

**Strategy for the next game.** We will continue to recruit and maintain supply, but we must shift from endless drilling to aggressive forward movement and attacking adjacent enemy-held cities to seize territory before the Confederacy achieves victory by city control.

**Changes:**

- dropped: When an enemy army moves into an adjacent city threatening our capital or core territory, issue a move order to intercept and engage them. (Redundant with core engagement instructions and did not prevent our passivity.)
- dropped: When the capital or a key city is threatened by adjacent enemy forces, issue a move order to reinforce it rather than drilling distant armies. (Did not address our failure to capture enemy territory.)
- dropped: When our ports are threatened by enemy naval vessels or bombardment, issue a build ironclad or build wooden order to rebuild our fleet and protect our seaports. (Naval building wasn't the core bottleneck for winning alternate maps.)
- dropped: When an enemy force threatens the capital, issue a move order to garrison Washington immediately rather than launching distant offensive campaigns. (We failed to launch any offensive campaigns at all, leading to defeat by city count.)
- added: When our forces outnumber an adjacent enemy army or city garrison, issue a move order to attack rather than drilling continuously. (We drilled 24 times and attacked only once despite massive troop advantages, losing the game entirely on city counts.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an adjacent enemy city is weakly defended or our forces outnumber them locally, issue a move order to attack and capture it rather than only recruiting.
6. When our forces outnumber an adjacent enemy army or city garrison, issue a move order to attack rather than drilling continuously.

### Version 51, after game 51 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We focused heavily on drilling and allowed several armies to run out of supplies while failing to capture and hold key cities. Meanwhile, the Confederate computer expanded its territory rapidly and overwhelmed our isolated positions.

**Strategy for the next game.** Next game, we will prioritize maintaining army supply lines, keep our forces concentrated to capture and hold territory, and recruit steadily without over-drilling under-supplied units.

**Changes:**

- dropped: When our forces outnumber an adjacent enemy army or city garrison, issue a move order to attack rather than drilling continuously. (This instruction was redundant with our general attack lesson and caused confusion when armies needed supply first.)
- added: When an army is out of supply or at 0 supply, issue a supply order before attempting any move or drill commands. (In this game, multiple armies fell to 0 supply and suffered attrition because we drilled or moved instead of resupplying them.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an adjacent enemy city is weakly defended or our forces outnumber them locally, issue a move order to attack and capture it rather than only recruiting.
6. When an army is out of supply or at 0 supply, issue a supply order before attempting any move or drill commands.

### Version 52, after game 52 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused heavily on recruiting and drilling but failed to capture and hold key cities or merge our smaller armies into powerful forces. The Rebel armies marched aggressively and seized territory while our isolated forces were pushed back in local engagements. We must combine forces and press attacks with overwhelming local strength.

**Strategy for the next game.** We will combine our starting forces into larger armies, aggressively capture adjacent enemy cities to expand our income and territory, maintain adequate supply lines, and steadily recruit to outnumber the Confederacy.

**Changes:**

- added: When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army. (We had many small, vulnerable separate armies that lost local engagements; we need to merge them to match enemy concentration.)
- dropped: When an army is out of supply or at 0 supply, issue a supply order before attempting any move or drill commands. (It was redundant with lesson 2 and had a poor record in our recent games.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When an adjacent enemy city is weakly defended or our forces outnumber them locally, issue a move order to attack and capture it rather than only recruiting.

### Version 53, after game 53 (standard: Rebel victory: cities controlled, 13 turns)

**Diagnosis.** We focused heavily on drilling and recruiting while remaining almost completely passive, launching very few attacks and letting the Rebels capture our cities unmolested. Our lack of offensive operations allowed the computer to seize territory, cut off our supply lines, and steadily choke us out.

**Strategy for the next game.** We will aggressively expand our forces, maintain active regional attacks against weak enemy positions to keep our city count high, and safeguard our supply lines to prevent attrition.

**Changes:**

- revised: When an adjacent enemy city is weakly defended or our forces outnumber them locally, issue a move order to attack and capture it rather than only recruiting. (We failed to attack enough, resulting in a passive defense that let the enemy control the board.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When an adjacent enemy city is weakly defended or our forces outnumber them locally, issue a move order to attack and capture it rather than only recruiting.

### Version 54, after game 54 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused heavily on constant recruiting and isolated attacks with inferior odds, leading to high casualties and eventual defeat. We neglected drilling and consolidating our forces into large armies, allowing Confederate commanders to outmatch us piecemeal.

**Strategy for the next game.** We will focus on building up large, well-drilled armies through consolidation and regular drilling, avoiding attacking fortified or superior Confederate forces until we hold a decisive numerical advantage.

**Changes:**

- revised: When our forces do not outnumber the enemy locally by at least 2:1, issue a drill order instead of a move order to attack. (We launched too many low-odds attacks and lost battles repeatedly. We need to build experience and wait for overwhelming strength.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces do not outnumber the enemy locally by at least 2:1, issue a drill order instead of a move order to attack.

### Version 55, after game 55 (standard: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** We focused heavily on drilling and recruiting, which raised our troop counts, but we neglected active movement and capturing enemy cities. Consequently, the Confederacy steadily expanded its city control while our forces remained static, leading to a loss of economic advantage and eventual defeat.

**Strategy for the next game.** We will continue to recruit and supply our main armies, but we must actively advance and attack when we have numerical superiority to capture enemy cities, reverse our economic decline, and prevent Confederate victory.

**Changes:**

- revised: When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities. (The previous lesson told us to drill instead of attack, which caused us to remain completely passive while the Rebels seized all the cities.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.

### Version 56, after game 56 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused almost entirely on recruiting and drilling, issuing zero move orders to attack enemy cities or expand our territory. While our troop count grew to over 100,000, the Confederate forces methodically captured our cities and achieved a technical victory by controlling 28 cities.

**Strategy for the next game.** We will continue recruiting and managing supply while strictly enforcing offensive move orders when local superiority is achieved, ensuring we capture enemy cities rather than only drilling.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.

### Version 57, after game 57 (standard: Rebel victory: cities controlled, 11 turns)

**Diagnosis.** We focused excessively on drilling and neglected aggressive expansion and capturing enemy territory. While our forces gained experience, our city count dwindled from 11 down to 6, allowing the Confederacy to achieve a territorial victory. We need to balance force maintenance with seizing and holding strategic cities.

**Strategy for the next game.** We will shift from over-drilling to an aggressive expansion strategy. We will recruit steadily, keep our armies supplied, and actively march on enemy-held cities to prevent the Confederacy from securing a territorial victory.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (Maintained from previous notebook as a foundational rule for building force structure.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Kept to prevent armies from running completely out of supplies during campaigns.)
- revised: When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking. (Kept to ensure starving or isolated forces are not wasted in combat.)
- revised: When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it. (Retained to keep our ports clear and protect our supply lines.)
- revised: When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army. (Kept to build stronger field armies instead of splitting force strength.)
- revised: When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities. (Retained to encourage necessary territorial capture instead of endless drilling.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.

### Version 58, after game 58 (alternate: Rebel victory: cities controlled, 3 turns)

**Diagnosis.** In this game, we heavily focused on recruiting and drilling while completely neglecting movement and attacks. This allowed the Confederate computer to capture our cities freely and overwhelm us through territorial expansion, resulting in a swift defeat after only 3 turns.

**Strategy for the next game.** Next game, we will maintain our focus on recruiting and supplying our forces while actively utilizing move and attack orders to contest enemy-held cities and prevent the computer from easily capturing our territory.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.

### Version 59, after game 59 (standard: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** We focused heavily on drilling rather than maintaining our offensive or expanding our economic base through recruiting. This allowed the Confederacy to seize key cities, outgrow us in strength, and blockade our ports, cutting down our income and leading to defeat.

**Strategy for the next game.** We will increase recruitment frequency in all available northern cities, maintain strict supply lines, and push offensives only when we hold a decisive local numerical superiority.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (We fell behind the Confederate troop growth rate because we did not recruit aggressively enough in standard cities.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.

### Version 60, after game 60 (alternate: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** We raised a large army by recruiting heavily, but we drilled excessively instead of attacking or taking initiative. The computer out-moved and out-attacked us while our forces sat idle, leading to a slow positional squeeze and defeat.

**Strategy for the next game.** We will continue to recruit and maintain supply, but we must drastically reduce drilling and increase aggressive movement and attacks on adjacent enemy cities to seize the initiative.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (Kept as a proven foundation for building our forces.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Kept to prevent supply attrition and avoid surrenders.)
- revised: When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking. (Kept to preserve isolated forces.)
- revised: When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it. (Kept to deal with blockades.)
- revised: When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army. (Kept to prevent weak, fragmented armies.)
- revised: When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities. (Kept to shift our focus from endless drilling to active attacks.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.

### Version 61, after game 61 (standard: Rebel victory: capital captured, 5 turns)

**Diagnosis.** We focused too heavily on isolated drills and slow expansions while ignoring the Confederate threat to Washington. Jackson marched through Harpers Ferry and captured our capital, resulting in a swift defeat.

**Strategy for the next game.** Next game we will maintain defensive cover over Washington while steadily recruiting and consolidating our forces in the West before launching concentrated offensives.

**Changes:**

- added: When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital. (We lost the game immediately because Jackson captured Washington while our armies were elsewhere.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.

### Version 62, after game 62 (alternate: Rebel victory: cities controlled, 17 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while remaining largely idle on the strategic map, allowing the Confederate forces to capture key cities unhindered and ultimately take Washington. Our lack of active movement and failure to defend our capital led to a decisive defeat.

**Strategy for the next game.** Next game, we will aggressively recruit and immediately push our forces out to capture and hold enemy cities while maintaining a strong defense around Washington to prevent the loss of our capital.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (Maintained to continue building forces, but we must pair it with aggressive movement.)
- revised: When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital. (Retained because failing to defend Washington directly caused our defeat this game.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.

### Version 63, after game 63 (standard: Rebel victory: cities controlled, 11 turns)

**Diagnosis.** This game was lost because armies advanced into enemy territory without securing lines of communication, leading to chronic out-of-supply states (especially McClellan in Knoxville). Cash reserves dwindled as cities were lost, preventing adequate supply purchases and recruitment. We drilled frequently but failed to maintain operational logistics, allowing the Confederacy to capture key cities and eventually win via city control.

**Strategy for the next game.** Next game we will strictly monitor army supply lines before advancing into enemy territory. We will prioritize keeping our armies supplied and consolidated, avoiding isolated forward moves that leave forces cut off, while continuing steady recruitment and defensive positioning.

**Changes:**

- revised: When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking. (Updated to clarify retreating to safety instead of making unsupported attacks when out of supply.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.

### Version 64, after game 64 (alternate: Rebel victory: cities controlled, 3 turns)

**Diagnosis.** In Training Game 64 on the alternate map, we lasted only 3 turns before the Confederacy achieved a rapid victory. We attempted to advance early and attack Louisville at poor odds (30%), which resulted in a heavy defeat and the loss of key northern cities like Indianapolis and Cincinnati. Our forces were spread too thin, and we failed to consolidate and drill our armies before initiating offensive operations.

**Strategy for the next game.** For the next game, we will prioritize building a strong economic and defensive foundation, steadily recruiting troops, using drill orders to maximize army quality, and strictly avoiding unfavorable attacks until we achieve overwhelming local numerical superiority.

**Changes:**

- added: When an army has not engaged in battle recently and leader rating permits, issue a drill order to build combat experience. (We failed to drill our forces entirely this game, leaving our troops inexperienced against seasoned Confederate commanders.)
- added: When planning an attack against an enemy-held city, verify that our combat odds exceed 50% before issuing a move order. (Our attack on Louisville at 30% odds severely crippled our army and triggered a cascade of enemy counter-attacks that cost us the game.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has not engaged in battle recently and leader rating permits, issue a drill order to build combat experience.
9. When planning an attack against an enemy-held city, verify that our combat odds exceed 50% before issuing a move order.

### Version 65, after game 65 (standard: Rebel victory: cities controlled, 17 turns)

**Diagnosis.** We spent excessive turns drilling instead of consolidating forces and capturing enemy cities. While our individual armies gained experience, we neglected strategic movement and allowed the Rebels to concentrate superior forces, outmaneuver us, and gradually capture our territory.

**Strategy for the next game.** Next game we will aggressively consolidate our forces using join orders, maintain steady recruitment and supply lines, and push outward to capture enemy cities rather than remaining static and drilling indefinitely.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (Maintained from previous notebook as a reliable foundation for force generation.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Essential to prevent armies from becoming stranded or defeated due to supply exhaustion.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has not engaged in battle recently and leader rating permits, issue a drill order to build combat experience.
9. When planning an attack against an enemy-held city, verify that our combat odds exceed 50% before issuing a move order.

### Version 66, after game 66 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We relied excessively on recruiting and drilling while completely neglecting strategic movement and offensive operations. Although our troop numbers and finances grew, we initiated zero attacks and allowed the Confederate forces to capture key cities and dictate the pace of the war, resulting in a swift defeat.

**Strategy for the next game.** Next game, we will continue our steady recruitment and sensible drilling, but we will actively issue move orders to attack vulnerable enemy cities and defend our territory, ensuring we contest control of the map rather than remaining completely passive.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (Maintained from previous notebook as it correctly directs force expansion.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Retained to ensure armies remain supplied for upcoming operations.)
- revised: When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking. (Kept to prevent attrition and destruction of isolated forces.)
- revised: When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it. (Preserved for naval security and maintaining open ports.)
- revised: When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army. (Kept to avoid small fragmented forces and build effective field armies.)
- revised: When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities. (Critical correction: we must transition from passive drilling to active capturing of enemy cities.)
- revised: When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital. (Retained to guarantee capital defense against Confederate advances.)
- revised: When an army has not engaged in battle recently and leader rating permits, issue a drill order to build combat experience. (Kept to improve combat power, but balanced with actual movement orders.)
- revised: When planning an attack against an enemy-held city, verify that our combat odds exceed 50% before issuing a move order. (Retained to ensure attacks are only launched with favorable odds.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has not engaged in battle recently and leader rating permits, issue a drill order to build combat experience.
9. When planning an attack against an enemy-held city, verify that our combat odds exceed 50% before issuing a move order.

### Version 67, after game 67 (standard: Rebel victory: cities controlled, 13 turns)

**Diagnosis.** We relied heavily on drilling and recruiting while executing zero move orders, which allowed the Confederate forces to capture cities unchecked, surround us, and ultimately secure a city-control victory.

**Strategy for the next game.** Next game we must actively issue move orders to counter Confederate expansions and capture key enemy cities rather than exclusively drilling and recruiting while remaining stationary.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (Maintained from previous notebook as it accurately reflects our standing recruitment instructions.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Kept to ensure armies maintain operational capability.)
- revised: When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking. (Kept to prevent stranded armies from being destroyed.)
- revised: When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it. (Retained to ensure port blockades are challenged.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has not engaged in battle recently and leader rating permits, issue a drill order to build combat experience.
9. When planning an attack against an enemy-held city, verify that our combat odds exceed 50% before issuing a move order.

### Version 68, after game 68 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused almost entirely on recruiting and drilling while issuing zero movement or attack orders, allowing the Confederacy to capture cities unopposed and achieve a territorial victory.

**Strategy for the next game.** We will actively use move orders to capture and defend cities instead of only recruiting and drilling, ensuring we contest Confederate territorial expansion.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has not engaged in battle recently and leader rating permits, issue a drill order to build combat experience.
9. When planning an attack against an enemy-held city, verify that our combat odds exceed 50% before issuing a move order.

### Version 69, after game 69 (standard: Rebel victory: capital captured, 12 turns)

**Diagnosis.** We focused heavily on drilling rather than expanding our territory or engaging the enemy, which allowed the Confederates to steadily capture cities and outmaneuver us. When the enemy bypassed our static positions and marched on Washington, our capital fell because we lacked active defense and offensive pressure.

**Strategy for the next game.** Next game, we will balance recruitment and supply maintenance with proactive offensive operations to capture enemy cities, while keeping our main forces positioned to protect Washington and intercept Confederate advances early.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle. (Maintained to ensure continuous troop growth.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Kept to prevent supply attrition losses.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has not engaged in battle recently and leader rating permits, issue a drill order to build combat experience.
9. When planning an attack against an enemy-held city, verify that our combat odds exceed 50% before issuing a move order.

### Version 70, after game 70 (alternate: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused entirely on recruiting and drilling while completely neglecting offensive movement, fortifying, and naval operations. Because we never attacked or captured enemy cities, the Rebels expanded unchecked, seized our territory, and eventually overwhelmed us.

**Strategy for the next game.** We will continue our steady recruitment and supply management, but we must actively use move orders to capture enemy cities and press the offensive rather than solely drilling and staying passive.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has not engaged in battle recently and leader rating permits, issue a drill order to build combat experience.
9. When planning an attack against an enemy-held city, verify that our combat odds exceed 50% before issuing a move order.

### Version 71, after game 71 (standard: Rebel victory: cities controlled, 14 turns)

**Diagnosis.** We focused heavily on drilling and recruiting while neglecting offensive momentum. During the winter months our armies ran out of supply and we failed to issue timely supply orders, leading to zero supply status and vulnerable forces. Furthermore, our lack of aggressive moves allowed the Confederates to slowly choke our territory and take cities.

**Strategy for the next game.** Next game we will maintain aggressive recruitment, ensure winter supply lines are actively managed without missing turns, and push outward to capture enemy cities rather than remaining purely static.

**Changes:**

- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (We failed to resupply armies before winter exhaustion hit in several turns, causing them to sit at 0 supply.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has not engaged in battle recently and leader rating permits, issue a drill order to build combat experience.
9. When planning an attack against an enemy-held city, verify that our combat odds exceed 50% before issuing a move order.

### Version 72, after game 72 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused excessively on recruiting and drilling while completely neglecting offensive move orders. Although our troop numbers grew significantly, the computer captured cities unchecked, resulting in a swift defeat by city control thresholds.

**Strategy for the next game.** We must balance recruiting and drilling with active move orders to capture enemy cities and contest Confederate expansion, rather than remaining entirely passive.

**Changes:**

- added: When an army has full supply and outnumbers the adjacent enemy, issue a move order to capture unoccupied or weakly held enemy cities. (We lost this game because we never issued a single move order to capture enemy cities, allowing the Confederacy to win unopposed.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has not engaged in battle recently and leader rating permits, issue a drill order to build combat experience.
9. When planning an attack against an enemy-held city, verify that our combat odds exceed 50% before issuing a move order.
10. When an army has full supply and outnumbers the adjacent enemy, issue a move order to capture unoccupied or weakly held enemy cities.

### Version 73, after game 73 (standard: Rebel victory: capital captured, 11 turns)

**Diagnosis.** We heavily relied on drilling while neglecting offensive maneuvers and failing to protect Washington adequately, allowing the Confederate forces to capture our capital.

**Strategy for the next game.** We will maintain aggressive recruiting, avoid excessive drilling that stalls our fronts, and prioritize the defense of Washington while seeking favorable attack opportunities.

**Changes:**

- revised: When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital. (We failed to properly intercept Jackson before he seized Washington in late 1862.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength rather than idle.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety rather than attacking.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has not engaged in battle recently and leader rating permits, issue a drill order to build combat experience.
9. When planning an attack against an enemy-held city, verify that our combat odds exceed 50% before issuing a move order.
10. When an army has full supply and outnumbers the adjacent enemy, issue a move order to capture unoccupied or weakly held enemy cities.

### Version 74, after game 74 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while leaving enemy forces largely unchecked. This allowed the Confederacy to steadily capture territory and reach the 28-city victory threshold by turn 6. We failed to aggressively advance and seize enemy cities or defend our own properly.

**Strategy for the next game.** Next game, we will combine steady recruitment with aggressive forward movement to capture and hold enemy territory, preventing the Confederacy from quietly accumulating cities and winning on points.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength. (Streamlined wording for direct action.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Clarified command usage for low supply.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has not engaged in battle recently and leader rating permits, issue a drill order to build combat experience.
9. When planning an attack against an enemy-held city, verify that our combat odds exceed 50% before issuing a move order.
10. When an army has full supply and outnumbers the adjacent enemy, issue a move order to capture unoccupied or weakly held enemy cities.

### Version 75, after game 75 (standard: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** We focused heavily on drilling rather than capturing and holding cities, allowing the Confederacy to steadily expand its city control and economy while we remained passive. We also failed to secure our supply lines properly, leading to recurring supply shortages that handicapped our armies.

**Strategy for the next game.** Next game we will curb unnecessary drilling and actively push our superior numbers into adjacent enemy or neutral cities to secure territory, while keeping supply lines robust and fleets active.

**Changes:**

- dropped: When an army has not engaged in battle recently and leader rating permits, issue a drill order to build combat experience. (Excessive drilling distracted us from capturing cities and winning the strategic map.)
- dropped: When planning an attack against an enemy-held city, verify that our combat odds exceed 50% before issuing a move order. (This instruction was redundant with our local numerical advantage attack rule.)
- added: When a friendly city is empty or weakly held and adjacent enemy armies are advancing, issue a move order to reinforce and block them. (We lost too many cities simply because we did not contest Rebel movements into our territory.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has full supply and outnumbers the adjacent enemy, issue a move order to capture unoccupied or weakly held enemy cities.
9. When a friendly city is empty or weakly held and adjacent enemy armies are advancing, issue a move order to reinforce and block them.

### Version 76, after game 76 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused heavily on recruiting new troops and building raw numbers, but repeatedly launched attacks at unfavourable odds (under 43% average) against enemy forces positioned in cities, resulting in heavy defeats and a loss of territorial control.

**Strategy for the next game.** We will continue to build our forces via recruiting and consolidating, but we will strictly avoid attacking entrenched enemy cities unless we hold a clear 2:1 local numerical advantage with full supply.

**Changes:**

- dropped: When a friendly city is empty or weakly held and adjacent enemy armies are advancing, issue a move order to reinforce and block them. (It had a negative record (-2.0 turns) and did not prevent enemy advances.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has full supply and outnumbers the adjacent enemy, issue a move order to capture unoccupied or weakly held enemy cities.

### Version 77, after game 77 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused heavily on recruiting and isolated attacks without maintaining proper supply lines or guarding our capital. When the Rebel army advanced on Washington, our forces were out of position and lacked supply, leading to the loss of our capital and defeat.

**Strategy for the next game.** We will maintain strict supply lines for all advancing armies, keep a strong defensive force near Washington to prevent capital loss, and only launch attacks when we have a clear 2:1 local advantage with full supply.

**Changes:**

- revised: When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital. (We failed to protect Washington in this game because armies were engaged elsewhere without enough supply to respond in time.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has full supply and outnumbers the adjacent enemy, issue a move order to capture unoccupied or weakly held enemy cities.

### Version 78, after game 78 (alternate: Rebel victory: share of total income, 12 turns)

**Diagnosis.** We focused heavily on recruiting and drilling large armies but completely neglected strategic movement, naval operations, and territorial expansion. While our troop numbers grew, we allowed the Confederacy to seize key cities and eventually outflank us, leading to a loss of income and eventual defeat.

**Strategy for the next game.** We will combine steady recruitment and supply maintenance with aggressive tactical movement to capture enemy cities, secure our borders, and press the offensive against Confederate territory.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength. (Maintained to ensure a steady flow of manpower for our armies.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Essential for preventing attrition losses among our active field armies.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
6. When our forces outnumber the enemy locally by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
7. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
8. When an army has full supply and outnumbers the adjacent enemy, issue a move order to capture unoccupied or weakly held enemy cities.

### Version 79, after game 79 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We suffered a decisive loss because our armies advanced into enemy territory without sufficient numerical superiority or supply, resulting in costly failed attacks and the loss of key cities. Furthermore, we neglected troop training and failed to maintain economic momentum.

**Strategy for the next game.** We will focus on steady recruitment, aggressive force consolidation, maintaining robust supply lines, and systematic drilling of our armies before launching overwhelming attacks on weakened Confederate positions.

**Changes:**

- dropped: When an army has 0 supply or is cut off from a friendly neighbouring city, issue a move order to retreat to safety. (It duplicated supply management rules and did not prevent attrition losses effectively during combat retreats.)
- added: When an army is idle in a safe city and its experience is below the leader's rating, issue a drill order to build combat experience. (Contrast analysis shows that successful games involve consistent drilling to increase army combat effectiveness.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When our forces outnumber the adjacent enemy by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities.
6. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
7. When an army has full supply and outnumbers the adjacent enemy, issue a move order to capture unoccupied or weakly held enemy cities.
8. When an army is idle in a safe city and its experience is below the leader's rating, issue a drill order to build combat experience.

### Version 80, after game 80 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while executing zero move orders, allowing the Rebels to freely capture cities and build up territory unchecked until we were overwhelmed.

**Strategy for the next game.** We will actively use move orders to capture empty or weakly defended enemy cities instead of only drilling and recruiting, ensuring we contest map control from the start.

**Changes:**

- dropped: When our forces outnumber the adjacent enemy by at least 2:1 and have full supply, issue a move order to attack adjacent enemy cities. (This lesson had a poor record and contributed to our passive play by setting an overly restrictive threshold for attacking.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an army has full supply and outnumbers the adjacent enemy, issue a move order to capture unoccupied or weakly held enemy cities.
6. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
7. When an army is idle in a safe city and its experience is below the leader's rating, issue a drill order to build combat experience.

### Version 81, after game 81 (standard: Rebel victory: cities controlled, 11 turns)

**Diagnosis.** We focused excessively on drilling while neglecting strategic movement, consolidation, and timely supply lines. Our armies lacked coordination, leading to isolated attacks and supply starvation while the Confederacy expanded its territory unchecked.

**Strategy for the next game.** We will prioritize keeping our main armies well-supplied and consolidated while systematically advancing on enemy cities rather than wasting turns on excessive drilling and isolated movements.

**Changes:**

- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Keeping armies supplied prevents catastrophic losses and enables successful offensives, which we failed to maintain in this game.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an army has full supply and outnumbers the adjacent enemy, issue a move order to capture unoccupied or weakly held enemy cities.
6. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
7. When an army is idle in a safe city and its experience is below the leader's rating, issue a drill order to build combat experience.

### Version 82, after game 82 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused almost exclusively on drilling armies rather than expanding territory or contesting the enemy. While our troops gained experience, the Confederacy captured cities unhindered, out-maneuvered us, and achieved a quick victory by controlling the map.

**Strategy for the next game.** We must balance recruiting and drilling with aggressive movement. Instead of sitting back and repeatedly drilling, we will use our superior numbers to capture and hold enemy cities to deny the Confederacy the victory threshold.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an army has full supply and outnumbers the adjacent enemy, issue a move order to capture unoccupied or weakly held enemy cities.
6. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
7. When an army is idle in a safe city and its experience is below the leader's rating, issue a drill order to build combat experience.

### Version 83, after game 83 (standard: Rebel victory: cities controlled, 11 turns)

**Diagnosis.** We relied excessively on drilling and building ships instead of recruiting new troops and capturing enemy cities. While our drill experience grew, our lack of aggressive expansion allowed the Confederacy to outproduce and overrun us, eventually capturing Washington and securing victory.

**Strategy for the next game.** Next game we will aggressively recruit forces across all available cities, keep our armies supplied, and actively move to capture enemy territory rather than sitting idle to drill.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength. (We failed to recruit enough forces this game, leading to a severe manpower deficit against the Rebel armies.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an army has full supply and outnumbers the adjacent enemy, issue a move order to capture unoccupied or weakly held enemy cities.
6. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
7. When an army is idle in a safe city and its experience is below the leader's rating, issue a drill order to build combat experience.

### Version 84, after game 84 (alternate: Rebel victory: share of total income, 4 turns)

**Diagnosis.** The Confederate forces captured Washington and secured a decisive victory in October 1861 because our armies were kept drilling and expanding locally rather than aggressively engaging and defending key territories, allowing enemy columns to march on our capital.

**Strategy for the next game.** Next game we will aggressively move our recruited and consolidated forces to capture enemy cities, maintain active defense around Washington, and minimize idle drilling to pressure the Confederate lines before they can advance on our capital.

**Changes:**

- dropped: When an army is idle in a safe city and its experience is below the leader's rating, issue a drill order to build combat experience. (Excessive drilling caused us to neglect attacks and movement, resulting in a swift defeat when the enemy advanced.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army has full supply and outnumbers the adjacent enemy, issue a move order to capture unoccupied or weakly held enemy cities.

### Version 85, after game 85 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We lost this game because our attacks were launched at poor odds (averaging 20%) and we failed to manage army supply effectively, leading to several out-of-supply states that crippled combat effectiveness. We also did not fortify or drill enough to maintain strong defensive positions, letting the Confederate armies outnumber and overwhelm us.

**Strategy for the next game.** Next game, we will focus on careful supply management, building up larger concentrated armies via joining, and only attacking when we hold a clear numerical and defensive advantage to prevent disastrous defeats.

**Changes:**

- revised: When an army has full supply and outnumbers the adjacent enemy by at least 2:1, issue a move order to capture unoccupied or weakly held enemy cities. (We attacked at terrible odds (20% average) in this game and lost every battle; we must ensure numerical superiority before attacking.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army has full supply and outnumbers the adjacent enemy by at least 2:1, issue a move order to capture unoccupied or weakly held enemy cities.

### Version 86, after game 86 (alternate: Rebel victory: share of total income, 10 turns)

**Diagnosis.** We focused too much on costly offensive attacks against superior Confederate forces and fortified positions like Louisville without sufficient numerical advantage. Meanwhile, an enemy fleet blockaded Philadelphia, cutting off our port and starving McDowell's army.

**Strategy for the next game.** Next game, we will prioritize building a strong naval defense to break blockades, avoid attacking fortified enemy concentrations without overwhelming numerical superiority, and steadily expand our secure city control.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength. (Retained as it helps maintain army numbers, though we must shift focus from drilling to effective campaigning.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Essential to keep armies in the field from starving, especially when blockaded.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army has full supply and outnumbers the adjacent enemy by at least 2:1, issue a move order to capture unoccupied or weakly held enemy cities.

### Version 87, after game 87 (standard: Rebel victory: cities controlled, 16 turns)

**Diagnosis.** We suffered a decisive loss because our armies repeatedly attacked fortified enemy positions at poor odds and ran out of supply, while the Rebel navy blockaded Philadelphia and attrition reduced our city count below the threshold.

**Strategy for the next game.** We will focus on maintaining steady recruitment, keeping our armies well-supplied, promptly eliminating enemy blockades in our ports, and only attacking adjacent enemy forces when we have overwhelming numerical superiority and no enemy fortifications.

**Changes:**

- added: When an army is blockaded in a port city by an enemy fleet, issue a move order to evacuate the port before the city falls neutral. (We lost Philadelphia and Burnside's army to a prolonged enemy fleet bombardment and blockade because we failed to retreat in time.)
- revised: When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city. (Previous attacks failed because we attacked enemies enjoying city and fort defensive multipliers at unfavorable odds.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army is blockaded in a port city by an enemy fleet, issue a move order to evacuate the port before the city falls neutral.
7. When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city.

### Version 88, after game 88 (alternate: Rebel victory: cities controlled, 11 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while remaining largely static, allowing the Rebels to methodically capture territory and accumulate cities until they reached the victory threshold in 11 turns. We initiated almost no offensive moves or strategic expansions.

**Strategy for the next game.** We will continue to maintain our core economic and supply discipline while increasing offensive pressure against vulnerable Confederate-held cities to prevent them from securing a territorial victory.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army is blockaded in a port city by an enemy fleet, issue a move order to evacuate the port before the city falls neutral.
7. When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city.

### Version 89, after game 89 (standard: Rebel victory: cities controlled, 14 turns)

**Diagnosis.** We accumulated surplus cash and drilled excessively while losing ground and cities. Failing to maintain supply lines and coordinate offensive attacks allowed Confederate forces to steadily capture our territory and achieve victory by July 1863.

**Strategy for the next game.** We will focus on maintaining steady recruitment, ensuring all combat armies remain well-supplied, and launching coordinated offensive moves against weakened enemy-held cities rather than over-drilling.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength. (Maintained from previous record to ensure consistent troop replenishment.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Kept to prevent armies from running out of supplies during critical campaigns.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army is blockaded in a port city by an enemy fleet, issue a move order to evacuate the port before the city falls neutral.
7. When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city.

### Version 90, after game 90 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while remaining largely idle, allowing the Confederate army to aggressively capture our cities and ultimately seize Washington, ending the game in a decisive defeat.

**Strategy for the next game.** We must balance building up our military forces with proactive offensive movements and defense of our capital to prevent the Confederacy from capturing key cities and winning early.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army is blockaded in a port city by an enemy fleet, issue a move order to evacuate the port before the city falls neutral.
7. When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city.

### Version 91, after game 91 (standard: Rebel victory: cities controlled, 16 turns)

**Diagnosis.** We relied too heavily on drilling and defensive holding while the Confederacy slowly strangled our economy and outpaced us in city control and military expansion. Our moves and attacks were too infrequent to contest enemy advances effectively.

**Strategy for the next game.** We will increase our rate of recruitment and aggressive movement to challenge Confederate control of cities early, while maintaining supply and consolidating our armies to prevent them from wearing us down defensively.

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army is blockaded in a port city by an enemy fleet, issue a move order to evacuate the port before the city falls neutral.
7. When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city.

### Version 92, after game 92 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused heavily on recruiting and drilling while failing to take offensive action, conducting only a single move order over four turns. The Rebels aggressively seized territory and cities unopposed while we idly drilled, leading to a swift defeat by city control.

**Strategy for the next game.** We must break our habit of endless drilling and aggressively use our recruited forces to march on adjacent enemy and neutral cities. Securing territory is vital to preventing the Rebels from winning via city control targets.

**Changes:**

- dropped: When an army is blockaded in a port city by an enemy fleet, issue a move order to evacuate the port before the city falls neutral. (This situation rarely arises and did not contribute to our overall performance across recent games.)
- added: When an idle army can march into an adjacent unoccupied enemy or neutral city, issue a move order to capture it. (We lost this game entirely because we failed to capture and contest cities, sitting idle instead of seizing territory.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city.
7. When an idle army can march into an adjacent unoccupied enemy or neutral city, issue a move order to capture it.

### Version 93, after game 93 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We focused heavily on drilling armies while losing cities and territory to the advancing Confederates. Our offensive moves lacked sufficient force concentration, leading to heavy losses and lost cities, while the enemy systematically captured our territory and ultimately achieved a city-control victory.

**Strategy for the next game.** We will prioritize aggressive expansion and securing neutral or enemy cities while maintaining proper supply lines, reducing excessive drilling, and concentrating our forces to block Confederate advances and protect our economic core.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength. (Maintained from previous notebook to ensure steady manpower growth.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Retained to prevent supply exhaustion seen in our armies during this game.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city.
7. When an idle army can march into an adjacent unoccupied enemy or neutral city, issue a move order to capture it.

### Version 94, after game 94 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused heavily on internal recruitment and accumulation of forces but failed to protect our capital and execute coordinated, overwhelming attacks. The Confederacy quickly outmaneuvered us, captured Washington, and sealed our defeat by taking control of the map's key cities while our large armies remained passive or engaged in unfavorable battles.

**Strategy for the next game.** We will aggressively expand our forces and secure nearby neutral cities while maintaining strict defensive coverage around Washington. We will avoid attacking fortified or numerically superior enemy positions without overwhelming force ratios, consolidating our armies into powerful regional commands before launching offensive operations.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength. (Maintained from previous notebook to ensure steady force growth.)
- revised: When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness. (Retained to prevent attrition and keep field armies operational.)
- revised: When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army. (Kept to ensure we build cohesive high-command strike forces.)
- revised: When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it. (Maintained to protect our seaports from blockades and supply drains.)
- revised: When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital. (Critical defensive priority highlighted by losing Washington this game.)
- revised: When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city. (Kept to enforce favorable combat ratios instead of attacking at low odds.)
- revised: When an idle army can march into an adjacent unoccupied enemy or neutral city, issue a move order to capture it. (Retained to ensure steady territorial expansion.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city.
7. When an idle army can march into an adjacent unoccupied enemy or neutral city, issue a move order to capture it.

### Version 95, after game 95 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused too heavily on continuous drilling and piecemeal attacks against fortified or superior forces, which drained our treasury and resulted in heavy battle losses. Meanwhile, we neglected defensive fortication and strategic maneuvering, allowing Confederate forces to outmaneuver us and capture key cities.

**Strategy for the next game.** Next game, we will prioritize capturing neutral and empty cities, maintaining positive cash flow, and consolidating large forces before launching attacks, avoiding speculative drills and costly low-odds battles.

**Changes:**

- dropped: When an army has high experience and no immediate enemy threat, issue a drill order to maximize combat readiness. (Excessive drilling consumed actions and funds while our actual combat performance and city control deteriorated.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city.
7. When an idle army can march into an adjacent unoccupied enemy or neutral city, issue a move order to capture it.

### Version 96, after game 96 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused heavily on recruitment and drilling while failing to concentrate superior force for attacks, resulting in poor combat odds and lost battles. Meanwhile, Confederate armies aggressively maneuvered and seized key cities, achieving victory by overwhelming our controlled territory.

**Strategy for the next game.** Next game we will maintain our steady recruitment and reinforcement, consolidate our armies into powerful forces before engaging, and strictly attack only when holding a clear numerical and positional advantage.

**Changes:**

- revised: When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city. (We attacked with low odds (under 50%) and lost valuable battles; we must strictly enforce favorable odds and avoid attacking defended positions blindly.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city.
7. When an idle army can march into an adjacent unoccupied enemy or neutral city, issue a move order to capture it.

### Version 97, after game 97 (standard: Rebel victory: capital captured, 5 turns)

**Diagnosis.** The Confederate forces exploited our weak defenses in the East by moving R.E. Lee directly into Washington and capturing our capital while our main armies were distracted or out of supply in the West and Shenandoah Valley. Our attacks failed due to poor odds and lack of sufficient force concentration, and we neglected capital defense and supply lines.

**Strategy for the next game.** We will maintain aggressive recruitment and careful supply management while keeping a strong defensive force near Washington to intercept any Confederate approach on the capital, ensuring our core territory remains secure before attempting major offensives in the West.

**Changes:**

- revised: When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital. (We failed to protect Washington from R.E. Lee in November, leading directly to the loss of the capital and the game.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city.
7. When an idle army can march into an adjacent unoccupied enemy or neutral city, issue a move order to capture it.

### Version 98, after game 98 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We expanded rapidly and built a large force, but attacked a strongly fortified Chattanooga at 21% odds without sufficient advantage, suffering a severe repulse. Meanwhile, the Rebels captured key cities and outmaneuvered us.

**Strategy for the next game.** We will maintain aggressive recruitment, consolidate forces, and avoid attacking fortified enemy positions unless we have an overwhelming numerical and supply advantage.

**Changes:**

- dropped: When an army has been repulsed in battle, issue a drill order to restore its readiness. (Drilling after a defeat did not prevent further losses; keeping pressure or consolidating is better.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army threatens Washington or an adjacent city, issue a move order to intercept and defend the capital.
6. When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city.
7. When an idle army can march into an adjacent unoccupied enemy or neutral city, issue a move order to capture it.

### Version 99, after game 99 (standard: Rebel victory: capital captured, 6 turns)

**Diagnosis.** We failed to protect Washington, allowing J.E. Johnston to march in and capture our capital on turn 6. While we maintained cash and recruited early, we neglected to leave an army defending the capital region or intercept advancing rebel corps, leading to a quick loss despite holding a strong economic position.

**Strategy for the next game.** We will continue to build our financial reserve and recruit steadily, but we will maintain a dedicated defensive force near Washington and Baltimore to prevent Confederate flanking maneuvers from seizing our capital early in the war.

**Changes:**

- revised: When an enemy army moves within one city of Washington, issue a move order to intercept and defend the capital. (We failed to protect the capital in game 99 because our previous rule was too passive, only reacting when Washington itself was directly threatened.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves within one city of Washington, issue a move order to intercept and defend the capital.
6. When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city.
7. When an idle army can march into an adjacent unoccupied enemy or neutral city, issue a move order to capture it.

### Version 100, after game 100 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused heavily on recruiting and drilling behind our lines while the Confederate forces actively captured our key cities and pushed deep into the North, eventually achieving a city-control victory.

**Strategy for the next game.** Next game we will aggressively deploy our armies to capture and hold regional cities to prevent Confederate expansion, limiting their ability to reach the 28-city victory threshold while maintaining necessary recruits and supplies.

**Changes:**

- revised: When a city offers recruits and treasury allows, issue a recruit order to expand our military strength. (Maintained from previous notebook as recruiting is essential for baseline numbers.)

**Notebook:**

1. When a city offers recruits and treasury allows, issue a recruit order to expand our military strength.
2. When an army's supply drops to 1 or lower, issue a supply order to maintain combat effectiveness.
3. When multiple idle armies occupy the same city, issue a join order to consolidate our forces into a powerful army.
4. When an enemy fleet is present in one of our ports, issue a fleet sail order to engage and eliminate it.
5. When an enemy army moves within one city of Washington, issue a move order to intercept and defend the capital.
6. When an army has full supply and outnumbers the adjacent enemy by at least 2:1 and the enemy has no fort, issue a move order to capture the city.
7. When an idle army can march into an adjacent unoccupied enemy or neutral city, issue a move order to capture it.

