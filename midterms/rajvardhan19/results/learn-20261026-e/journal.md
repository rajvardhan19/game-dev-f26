# Learning journal: `gemini-e`

Model `gemini-3.5-flash-lite`. 100 training games; notebook version 100 (frozen, sha ea436d9d292b000d).

## What it did, game by game

| game | map | notebook | result | turns | recruits | drills | moves | attacks (won) | mean odds | cities peak / end | last-turn cash | refused |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | standard | v0 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 9 | 8 | 1 (0) | 23% | 13 / 4 | 941 | 3 |
| 2 | alternate | v1 | decisive loss: Rebel victory: cities controlled | 6 | 2 | 17 | 0 | 0 (0) | - | 10 / 8 | 1203 | 4 |
| 3 | standard | v2 | decisive loss: Rebel victory: capital captured | 6 | 0 | 6 | 9 | 2 (2) | 42% | 13 / 9 | 342 | 8 |
| 4 | alternate | v3 | decisive loss: Rebel victory: cities controlled | 6 | 11 | 0 | 8 | 3 (1) | 50% | 13 / 9 | 343 | 1 |
| 5 | standard | v4 | decisive loss: Rebel victory: capital captured | 5 | 0 | 15 | 1 | 0 (0) | - | 12 / 9 | 655 | 0 |
| 6 | alternate | v5 | decisive loss: Rebel victory: cities controlled | 5 | 11 | 20 | 0 | 0 (0) | - | 10 / 9 | 411 | 0 |
| 7 | standard | v6 | decisive loss: Rebel victory: cities controlled | 13 | 6 | 26 | 4 | 0 (0) | - | 11 / 6 | 397 | 7 |
| 8 | alternate | v7 | decisive loss: Rebel victory: cities controlled | 8 | 7 | 25 | 2 | 2 (0) | 42% | 10 / 8 | 453 | 0 |
| 9 | standard | v8 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 6 | 8 | 3 (0) | 30% | 13 / 5 | 380 | 7 |
| 10 | alternate | v9 | decisive loss: Rebel victory: cities controlled | 3 | 4 | 0 | 2 | 0 (0) | - | 10 / 8 | 958 | 1 |
| 11 | standard | v10 | decisive loss: Rebel victory: cities controlled | 17 | 9 | 14 | 12 | 2 (1) | 53% | 14 / 6 | 183 | 8 |
| 12 | alternate | v11 | decisive loss: Rebel victory: share of total income | 7 | 0 | 0 | 17 | 1 (0) | 3% | 14 / 12 | 1852 | 1 |
| 13 | standard | v12 | decisive loss: Rebel victory: capital captured | 2 | 0 | 0 | 6 | 0 (0) | - | 13 / 12 | 662 | 0 |
| 14 | alternate | v13 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 14 | 10 | 2 (1) | 34% | 16 / 9 | 1679 | 5 |
| 15 | standard | v14 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 13 | 6 | 2 (0) | 32% | 13 / 5 | 314 | 7 |
| 16 | alternate | v15 | decisive loss: Rebel victory: cities controlled | 7 | 3 | 5 | 9 | 1 (0) | 21% | 14 / 11 | 1760 | 0 |
| 17 | standard | v16 | decisive loss: Rebel victory: capital captured | 2 | 0 | 0 | 6 | 1 (0) | 30% | 13 / 12 | 532 | 1 |
| 18 | alternate | v17 | decisive loss: Rebel victory: cities controlled | 6 | 10 | 6 | 8 | 1 (0) | 30% | 12 / 9 | 360 | 4 |
| 19 | standard | v18 | decisive loss: Rebel victory: cities controlled | 8 | 3 | 8 | 8 | 1 (0) | 23% | 13 / 6 | 285 | 6 |
| 20 | alternate | v19 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 2 | 12 | 2 (1) | 36% | 14 / 10 | 1094 | 0 |
| 21 | standard | v20 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 0 | 6 | 2 (0) | 32% | 13 / 6 | 512 | 3 |
| 22 | alternate | v21 | decisive loss: Rebel victory: cities controlled | 5 | 12 | 5 | 7 | 1 (0) | 12% | 13 / 10 | 363 | 3 |
| 23 | standard | v22 | decisive loss: Rebel victory: capital captured | 2 | 0 | 0 | 6 | 1 (0) | 27% | 13 / 11 | 633 | 0 |
| 24 | alternate | v23 | decisive loss: Rebel victory: cities controlled | 4 | 6 | 13 | 6 | 1 (0) | 8% | 13 / 10 | 622 | 5 |
| 25 | standard | v24 | decisive loss: Rebel victory: capital captured | 5 | 0 | 0 | 8 | 2 (0) | 34% | 13 / 10 | 798 | 4 |
| 26 | alternate | v25 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 3 | 10 | 6 (2) | 32% | 11 / 10 | 1274 | 1 |
| 27 | standard | v26 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 6 | 9 | 2 (0) | 30% | 13 / 6 | 659 | 2 |
| 28 | alternate | v27 | decisive loss: Rebel victory: cities controlled | 13 | 3 | 25 | 21 | 5 (1) | 35% | 16 / 10 | 2514 | 5 |
| 29 | standard | v28 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 0 | 9 | 2 (0) | 32% | 13 / 6 | 739 | 5 |
| 30 | alternate | v29 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 17 | 8 | 1 (0) | 14% | 13 / 10 | 1205 | 3 |
| 31 | standard | v30 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 13 | 10 | 5 (2) | 37% | 13 / 5 | 1185 | 6 |
| 32 | alternate | v31 | decisive loss: Rebel victory: cities controlled | 3 | 4 | 0 | 10 | 1 (0) | 30% | 14 / 10 | 830 | 1 |
| 33 | standard | v32 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 3 | 7 | 2 (0) | 42% | 13 / 6 | 698 | 0 |
| 34 | alternate | v33 | decisive loss: Rebel victory: cities controlled | 7 | 1 | 21 | 11 | 6 (2) | 39% | 11 / 9 | 1907 | 5 |
| 35 | standard | v34 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 16 | 4 | 2 (0) | 28% | 13 / 7 | 1003 | 3 |
| 36 | alternate | v35 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 9 | 1 (0) | 12% | 12 / 9 | 816 | 0 |
| 37 | standard | v36 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 13 | 6 | 2 (1) | 34% | 13 / 6 | 379 | 1 |
| 38 | alternate | v37 | decisive loss: Rebel victory: cities controlled | 3 | 0 | 0 | 10 | 2 (1) | 26% | 14 / 11 | 918 | 1 |
| 39 | standard | v38 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 7 | 10 | 3 (0) | 30% | 13 / 5 | 586 | 5 |
| 40 | alternate | v39 | decisive loss: Rebel victory: cities controlled | 4 | 8 | 10 | 6 | 3 (0) | 24% | 11 / 10 | 354 | 3 |
| 41 | standard | v40 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 11 | 7 | 2 (0) | 31% | 13 / 5 | 236 | 2 |
| 42 | alternate | v41 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 9 | 7 | 3 (1) | 45% | 13 / 9 | 1340 | 0 |
| 43 | standard | v42 | decisive loss: Rebel victory: cities controlled | 10 | 2 | 0 | 7 | 2 (0) | 34% | 13 / 4 | 1006 | 5 |
| 44 | alternate | v43 | decisive loss: Rebel victory: cities controlled | 6 | 16 | 4 | 11 | 2 (0) | 8% | 14 / 10 | 358 | 4 |
| 45 | standard | v44 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 7 | 5 | 0 (0) | - | 13 / 6 | 788 | 0 |
| 46 | alternate | v45 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 3 | 12 | 3 (0) | 40% | 14 / 10 | 652 | 1 |
| 47 | standard | v46 | decisive loss: Rebel victory: cities controlled | 10 | 3 | 5 | 6 | 2 (1) | 47% | 13 / 6 | 424 | 4 |
| 48 | alternate | v47 | decisive loss: Rebel victory: cities controlled | 5 | 4 | 12 | 3 | 0 (0) | - | 11 / 9 | 866 | 0 |
| 49 | standard | v48 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 7 | 14 | 6 (1) | 44% | 13 / 6 | 645 | 6 |
| 50 | alternate | v49 | decisive loss: Rebel victory: cities controlled | 5 | 4 | 0 | 12 | 2 (0) | 10% | 13 / 9 | 991 | 1 |
| 51 | standard | v50 | decisive loss: Rebel victory: capital captured | 3 | 0 | 0 | 11 | 1 (0) | 8% | 14 / 12 | 354 | 0 |
| 52 | alternate | v51 | decisive loss: Rebel victory: cities controlled | 4 | 1 | 3 | 8 | 1 (0) | 3% | 13 / 9 | 928 | 1 |
| 53 | standard | v52 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 2 | 12 | 1 (0) | 27% | 13 / 6 | 247 | 3 |
| 54 | alternate | v53 | decisive loss: Rebel victory: cities controlled | 3 | 0 | 11 | 2 | 0 (0) | - | 11 / 9 | 356 | 3 |
| 55 | standard | v54 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 2 | 10 | 4 (1) | 55% | 13 / 6 | 1272 | 5 |
| 56 | alternate | v55 | decisive loss: Rebel victory: share of total income | 6 | 4 | 17 | 9 | 4 (2) | 46% | 13 / 11 | 1366 | 4 |
| 57 | standard | v56 | decisive loss: Rebel victory: cities controlled | 10 | 0 | 9 | 11 | 2 (1) | 32% | 12 / 7 | 471 | 9 |
| 58 | alternate | v57 | decisive loss: Rebel victory: cities controlled | 5 | 4 | 0 | 9 | 2 (0) | 47% | 11 / 10 | 920 | 0 |
| 59 | standard | v58 | decisive loss: Rebel victory: capital captured | 2 | 0 | 0 | 8 | 2 (0) | 35% | 13 / 13 | 533 | 0 |
| 60 | alternate | v59 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 6 | 3 (1) | 39% | 11 / 9 | 1107 | 0 |
| 61 | standard | v60 | decisive loss: Rebel victory: cities controlled | 12 | 0 | 13 | 7 | 1 (0) | 23% | 13 / 6 | 170 | 7 |
| 62 | alternate | v61 | decisive loss: Rebel victory: cities controlled | 5 | 2 | 0 | 9 | 2 (0) | 22% | 13 / 9 | 1039 | 0 |
| 63 | standard | v62 | decisive loss: Rebel victory: share of total income | 6 | 0 | 6 | 13 | 1 (0) | 40% | 15 / 10 | 809 | 1 |
| 64 | alternate | v63 | decisive loss: Rebel victory: cities controlled | 4 | 2 | 0 | 10 | 1 (0) | 42% | 13 / 10 | 350 | 1 |
| 65 | standard | v64 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 11 | 9 | 2 (0) | 38% | 14 / 3 | 173 | 1 |
| 66 | alternate | v65 | decisive loss: Rebel victory: cities controlled | 8 | 6 | 2 | 13 | 2 (0) | 18% | 13 / 10 | 461 | 2 |
| 67 | standard | v66 | decisive loss: Rebel victory: cities controlled | 9 | 3 | 20 | 8 | 3 (0) | 28% | 13 / 5 | 253 | 8 |
| 68 | alternate | v67 | decisive loss: Rebel victory: cities controlled | 7 | 8 | 18 | 14 | 2 (0) | 22% | 14 / 10 | 597 | 5 |
| 69 | standard | v68 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 11 | 8 | 3 (0) | 32% | 13 / 4 | 740 | 3 |
| 70 | alternate | v69 | decisive loss: Rebel victory: cities controlled | 8 | 8 | 0 | 13 | 6 (0) | 21% | 13 / 7 | 1226 | 4 |
| 71 | standard | v70 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 2 | 8 | 4 (1) | 35% | 13 / 5 | 657 | 4 |
| 72 | alternate | v71 | decisive loss: Rebel victory: cities controlled | 5 | 4 | 0 | 8 | 1 (1) | 42% | 13 / 9 | 1078 | 2 |
| 73 | standard | v72 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 5 | 14 | 3 (1) | 47% | 13 / 5 | 1062 | 2 |
| 74 | alternate | v73 | decisive loss: Rebel victory: cities controlled | 5 | 10 | 16 | 7 | 0 (0) | - | 13 / 8 | 445 | 3 |
| 75 | standard | v74 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 4 | 7 | 4 (1) | 26% | 13 / 5 | 860 | 2 |
| 76 | alternate | v75 | decisive loss: Rebel victory: capital captured | 4 | 4 | 2 | 10 | 1 (0) | 16% | 14 / 13 | 891 | 0 |
| 77 | standard | v76 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 5 | 7 | 1 (1) | 57% | 13 / 5 | 1001 | 3 |
| 78 | alternate | v77 | decisive loss: Rebel victory: cities controlled | 5 | 4 | 0 | 9 | 2 (0) | 26% | 13 / 8 | 1178 | 1 |
| 79 | standard | v78 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 11 | 3 (0) | 39% | 13 / 5 | 1213 | 2 |
| 80 | alternate | v79 | decisive loss: Rebel victory: cities controlled | 4 | 4 | 4 | 9 | 2 (0) | 6% | 14 / 10 | 778 | 1 |
| 81 | standard | v80 | decisive loss: Rebel victory: cities controlled | 10 | 7 | 16 | 6 | 1 (0) | 30% | 13 / 5 | 260 | 6 |
| 82 | alternate | v81 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 5 | 8 | 0 (0) | - | 14 / 9 | 1226 | 0 |
| 83 | standard | v82 | decisive loss: Rebel victory: cities controlled | 6 | 4 | 9 | 8 | 1 (0) | 23% | 13 / 6 | 193 | 9 |
| 84 | alternate | v83 | decisive loss: Rebel victory: cities controlled | 5 | 3 | 18 | 9 | 3 (2) | 56% | 13 / 10 | 699 | 3 |
| 85 | standard | v84 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 1 | 10 | 2 (0) | 26% | 13 / 6 | 679 | 1 |
| 86 | alternate | v85 | decisive loss: Rebel victory: share of total income | 5 | 0 | 0 | 9 | 2 (1) | 29% | 11 / 8 | 1057 | 2 |
| 87 | standard | v86 | decisive loss: Rebel victory: cities controlled | 12 | 4 | 8 | 7 | 1 (0) | 40% | 13 / 5 | 542 | 4 |
| 88 | alternate | v87 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 0 | 8 | 5 (2) | 55% | 11 / 9 | 1507 | 0 |
| 89 | standard | v88 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 4 | 6 | 3 (1) | 38% | 13 / 6 | 664 | 3 |
| 90 | alternate | v89 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 4 | 3 | 1 (0) | 44% | 10 / 7 | 947 | 1 |
| 91 | standard | v90 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 7 | 13 | 4 (2) | 43% | 13 / 6 | 792 | 6 |
| 92 | alternate | v91 | decisive loss: Rebel victory: cities controlled | 3 | 4 | 1 | 5 | 0 (0) | - | 13 / 9 | 462 | 0 |
| 93 | standard | v92 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 10 | 7 | 1 (0) | 27% | 13 / 4 | 473 | 5 |
| 94 | alternate | v93 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 3 | 5 | 1 (0) | 37% | 11 / 9 | 1167 | 3 |
| 95 | standard | v94 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 14 | 6 | 2 (0) | 24% | 13 / 5 | 302 | 4 |
| 96 | alternate | v95 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 9 | 5 | 3 (1) | 45% | 11 / 10 | 1109 | 1 |
| 97 | standard | v96 | decisive loss: Rebel victory: cities controlled | 8 | 1 | 7 | 10 | 5 (0) | 26% | 13 / 6 | 205 | 5 |
| 98 | alternate | v97 | decisive loss: Rebel victory: cities controlled | 4 | 6 | 4 | 4 | 2 (1) | 46% | 11 / 8 | 347 | 3 |
| 99 | standard | v98 | decisive loss: Rebel victory: cities controlled | 6 | 4 | 0 | 10 | 5 (3) | 48% | 13 / 7 | 424 | 4 |
| 100 | alternate | v99 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 5 | 3 | 2 (1) | 47% | 10 / 8 | 1184 | 1 |

## How the notebook changed

### Version 1, after game 1 (standard: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused too much on drilling and moving isolated armies without adequate strength or support, leading to disastrous defeats against Confederate strongpoints like Fort Donelson. We failed to recruit new troops or manage our supply lines, allowing the Rebel armies to outnumber us, capture our northern cities, and trigger a defeat condition on turn 5.

**Strategy for the next game.** Next game, we will prioritize recruiting new troops and reinforcing existing armies to match Rebel numbers, maintain steady supplies, and avoid launching low-odds attacks against fortified enemy cities.

**Changes:**

- added: When an army is adjacent to an enemy-held city with inferior strength, do not order move into it; instead, order recruit to reinforce your forces first. (We attacked Fort Donelson at 23% odds and lost because our army size was too small.)
- added: When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size. (We sat on excess cash while Rebel forces grew significantly larger than ours.)
- added: When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving. (Our armies ran out of supplies and suffered attrition and combat penalties.)
- added: When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength. (We relied too much on drilling and failed to hold key ground against advancing Confederate armies.)

**Notebook:**

1. When an army is adjacent to an enemy-held city with inferior strength, do not order move into it; instead, order recruit to reinforce your forces first.
2. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
3. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
4. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.

### Version 2, after game 2 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused excessively on drilling and idle management while the Confederacy aggressively captured territory and expanded their armies. By failing to launch offensive moves or reinforce our forces actively through recruitment, we allowed the enemy to dominate the map and outnumber us significantly.

**Strategy for the next game.** We will actively recruit new forces and use move orders to capture enemy cities and contest Confederate expansion, ending our over-reliance on drilling.

**Changes:**

- revised: When an army is adjacent to an enemy-held city with inferior strength, order move to capture it. (Previous instruction told us not to move and to recruit instead, which resulted in complete passivity and allowed the enemy to capture territory unchecked.)

**Notebook:**

1. When an army is adjacent to an enemy-held city with inferior strength, order move to capture it.
2. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
3. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
4. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.

### Version 3, after game 3 (standard: Rebel victory: capital captured, 6 turns)

**Diagnosis.** We focused too much on drilling and moving isolated armies while neglecting recruitment and maintaining supply lines. Without fresh troops to replace losses and expand our forces, our numbers dwindled from 98,000 to 80,300 while the Rebels grew stronger. Allowing Jackson to take Washington ended the game swiftly.

**Strategy for the next game.** Next game, we will aggressively recruit to outnumber the Confederacy, maintain full supply stocks for our advancing columns, and immediately defend our capital and key supply nodes against Confederate incursions.

**Changes:**

- added: When an army has 1 or less supply, order supply to prevent starvation and attrition losses. (In this game, McDowell ran out of supplies and suffered severe effectiveness penalties while blockaded in Philadelphia.)

**Notebook:**

1. When an army is adjacent to an enemy-held city with inferior strength, order move to capture it.
2. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
3. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
4. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
5. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.

### Version 4, after game 4 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused heavily on recruiting and expanding our armies, but we initiated attacks at poor odds without sufficient numerical superiority, allowing the Confederate forces to crush our isolated armies. The teacher's game utilized concentrated offensive movements paired with timely rail and fleet deployments to seize key locations while maintaining force concentration.

**Strategy for the next game.** We will focus on building up strong, concentrated armies using recruit and join, ensuring high odds before launching attacks on enemy-held cities, while utilizing rail movements to respond quickly to threats.

**Changes:**

- added: When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%. (We lost several battles this game by attacking into fortified or superior enemy forces at low odds.)

**Notebook:**

1. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
2. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
3. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
4. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
5. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
6. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.

### Version 5, after game 5 (standard: Rebel victory: capital captured, 5 turns)

**Diagnosis.** We focused entirely on drilling and building ships instead of recruiting troops or capturing cities, which left our forces too weak to stop the Confederate advance. The enemy quickly overwhelmed our capital and out-expanded us across the map.

**Strategy for the next game.** Next game we will actively recruit troops, capture neutral and enemy cities to expand our income and territory, and use our armies aggressively rather than wasting turns drilling while the enemy marches on our capital.

**Changes:**

- dropped: When you have spare cash and armies are not engaged in combat, order drill to increase their experience rating. (Continuous drilling resulted in zero city captures and let the enemy overrun our capital without effective resistance.)

**Notebook:**

1. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
2. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
3. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
4. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
5. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
6. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.

### Version 6, after game 6 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused heavily on recruiting and drilling but issued zero move orders to capture enemy cities or expand our territory. Consequently, the Confederacy easily claimed enough cities to secure a victory by turn 5 while we remained entirely passive.

**Strategy for the next game.** In the next game, we will balance recruiting and drilling with aggressive movement orders to capture adjacent enemy cities and prevent the Confederacy from dominating the map.

**Changes:**

- dropped: When you have idle armies and no immediate offensive targets, order drill to raise their experience up to the leader rating. (Excessive drilling caused us to completely neglect movement and city capture, leading to a swift defeat by city count.)

**Notebook:**

1. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
2. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
3. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
4. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
5. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
6. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.

### Version 7, after game 7 (standard: Rebel victory: cities controlled, 13 turns)

**Diagnosis.** We focused too heavily on drilling existing armies while neglecting to recruit replacements and capture enemy cities. Our armies repeatedly ran out of supplies because we failed to manage them proactively, and our forces in Philadelphia were isolated and slowly ground down by naval bombardment. The computer Union successfully maintained aggressive expansion, naval operations, and railroad movement.

**Strategy for the next game.** Next game we will maintain our current robust set of core rules, balancing recruitment, regular resupply of distant or active armies, and targeted offensive movements against enemy cities while avoiding excessive passive drilling that leaves us vulnerable.

**Notebook:**

1. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
2. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
3. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
4. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
5. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
6. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.

### Version 8, after game 8 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We relied excessively on drilling and building ships while failing to capture enemy territory or adequately defend our cities. The computer opponent actively moved and captured key locations early on, whereas our forces remained static and were eventually overwhelmed by concentrated Rebel counter-attacks.

**Strategy for the next game.** Next game, we will immediately prioritize aggressive movement and capturing neutral or enemy cities while maintaining a healthy recruitment schedule, avoiding excessive passive drilling that costs us territory.

**Changes:**

- dropped: When your armies have high experience and you have spare cash, order drill to maximize leader ratings. (We spent far too many turns drilling instead of taking the offensive or expanding our territory, leading to a city-control loss.)

**Notebook:**

1. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
2. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
3. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
4. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
5. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
6. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.

### Version 9, after game 9 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We lost because we failed to recruit and grow our armies, keeping our total troop strength stagnant while the Rebels grew past 100,000 men. We also initiated attacks with severe numerical disadvantages and poor odds, leading to high casualties and retreat. Finally, we neglected keeping our armies supplied and capturing key economic cities.

**Strategy for the next game.** Next game we will aggressively recruit to grow our troop numbers, only attack when odds exceed 60%, and ensure all armies are well-supplied before initiating movements.

**Notebook:**

1. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
2. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
3. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
4. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
5. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
6. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.

### Version 10, after game 10 (alternate: Rebel victory: cities controlled, 3 turns)

**Diagnosis.** We focused on gathering troops and waiting while the computer enemy aggressively seized neutral and enemy cities from turn one, ultimately capturing our capital and winning quickly. Our passive defense and lack of rapid expansion left us outnumbered in territory and income.

**Strategy for the next game.** Next game we will aggressively order early movement to seize cities from the very first turn while continuing to recruit and build our forces to match the computer's expansion speed.

**Changes:**

- added: When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately. (The teacher's game immediately captured multiple cities on turn one, setting a strong pace, whereas we delayed and lost the initiative.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.

### Version 11, after game 11 (standard: Rebel victory: cities controlled, 17 turns)

**Diagnosis.** We lasted 17 turns compared to 8 for no orders, but our strategy suffered from chronic starvation and lack of concentration. We recruited early on but then neglected reinforcement while letting armies run out of supply repeatedly, leading to attrition and defeats. We also failed to fortify Washington, which ultimately fell in November 1863 and cost us the game.

**Strategy for the next game.** Next game, we will maintain rigorous supply management to prevent our armies from starving, continuously reinforce key positions, and fortify Washington immediately to protect our capital and extend our resistance.

**Changes:**

- revised: When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size. (Recruitment needs to be sustained to replace losses, as seen in our fluctuating army size.)
- revised: When an army has 1 or less supply, order supply to prevent starvation and attrition losses. (We frequently hit 0 supply on major armies like McClellan and McDowell, destroying their combat effectiveness.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.

### Version 12, after game 12 (alternate: Rebel victory: share of total income, 7 turns)

**Diagnosis.** We failed to recruit any new troops throughout the entire game, keeping our army size stagnant around 39,000 men while the computer grew its forces to over 140,000. Although we initially captured several neutral cities, we lacked the troop strength and reinforcements to hold our gains or win against concentrated Confederate resistance.

**Strategy for the next game.** Next game, we will maintain our early aggressive capture of neutral cities while strictly adhering to regular recruitment using our growing treasury. We must build a massive army to match the enemy's strength and avoid attacking heavily defended positions at poor odds.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.

### Version 13, after game 13 (standard: Rebel victory: capital captured, 2 turns)

**Diagnosis.** The Union lost quickly in two turns because Washington was left completely undefended, allowing the Confederate army under Jackson to march in and capture the capital immediately while our forces were scattered on distant movements.

**Strategy for the next game.** Next game I will ensure the capital remains strongly defended and fortified against direct enemy advances, while carefully building up our troops and maintaining solid supply lines before initiating major offensives.

**Changes:**

- added: When the enemy army is within striking distance of Washington, do not move the garrison away; order fortify on Washington instead. (Added because the capital was captured on turn 2 due to lack of defense and fortresses protecting Washington.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.
8. When the enemy army is within striking distance of Washington, do not move the garrison away; order fortify on Washington instead.

### Version 14, after game 14 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We captured early territory and Richmond, but our armies were too small to hold or break strong enemy forces. We failed to recruit new men despite a growing treasury, and we spent too many turns drilling instead of reinforcing or attacking properly, letting Confederate counterattacks break our lines and seize Washington.

**Strategy for the next game.** We will aggressively expand our territory early, maintain a healthy cash reserve, and continually recruit new forces at major cities to keep our army sizes competitive against the Confederacy, while avoiding excessive drilling when strength is low.

**Changes:**

- dropped: When the enemy army is within striking distance of Washington, do not move the garrison away; order fortify on Washington instead. (It proved too restrictive and contributed to our defeat by halting active defense in previous trials.)
- added: When your armies are under 8,000 men and funds exceed $400, order recruit at your cities rather than drill to build combat power. (Our game failed because our armies shrank through attrition and combat while we wasted turns drilling instead of reinforcing our numbers.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.
8. When your armies are under 8,000 men and funds exceed $400, order recruit at your cities rather than drill to build combat power.

### Version 15, after game 15 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused heavily on drilling armies instead of recruiting and expanding our forces. With cash reserves remaining high and total troop numbers stagnant or shrinking, the Confederacy outproduced and overwhelmed us. We must consistently recruit at major cities when funds are available.

**Strategy for the next game.** Next game, we will immediately initiate recruitment alongside our initial expansion moves. We will maintain treasury flow while aggressively building our army size to outmatch Confederate forces, avoiding excessive drilling while our forces remain weak in numbers.

**Changes:**

- revised: When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size. (We accumulated cash instead of turning it into troops, causing us to be severely outnumbered.)
- revised: When your armies are under 8,000 men and funds exceed $400, order recruit at your cities rather than drill to build combat power. (We wasted too many turns drilling small, vulnerable armies instead of expanding our manpower.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $500 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.
8. When your armies are under 8,000 men and funds exceed $400, order recruit at your cities rather than drill to build combat power.

### Version 16, after game 16 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We failed to recruit enough troops early on and relied too heavily on drilling instead of building combat power and expanding our territory. While we accumulated cash, our army sizes remained stagnant and unable to break heavily defended enemy positions or outnumber the Confederates effectively, leading to a loss of city control.

**Strategy for the next game.** We will focus heavily on early recruitment to expand our total manpower, use our cash reserves to reinforce armies rather than excessive drilling, and press attacks only when we hold overwhelming numerical superiority.

**Changes:**

- revised: When your armies are under 8,000 men and funds exceed $400, order recruit at your cities rather than drill to build combat power. (We raised the threshold to 15,000 men and $300 to ensure we aggressively build up larger combat-effective armies early instead of wasting turns drilling small forces.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.
8. When your army size is under 15,000 men and funds exceed $300, order recruit at your cities rather than drill to build combat power.

### Version 17, after game 17 (standard: Rebel victory: capital captured, 2 turns)

**Diagnosis.** We focused entirely on immediate captures and naval building while ignoring recruitment and defense of the capital, allowing Jackson to march on Washington unopposed and capture it in May 1861.

**Strategy for the next game.** Recruit troops aggressively at major cities to build a massive numerical advantage while keeping our capital defended against enemy breakthroughs.

**Changes:**

- revised: When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately. (Kept as baseline opening move command.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.
8. When your army size is under 15,000 men and funds exceed $300, order recruit at your cities rather than drill to build combat power.

### Version 18, after game 18 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused too much on drilling and failed to concentrate our forces for effective attacks, while our treasury sat idle with over $1000 instead of being used to recruit heavily. The computer expanded its armies and captured cities systematically while we squandered our turns.

**Strategy for the next game.** Next game we will aggressively recruit at major cities whenever funds allow, maintain high supply levels, and launch concentrated attacks only at favorable odds while avoiding excessive drilling.

**Changes:**

- revised: When your army size is under 30,000 men and funds exceed $300, order recruit at your cities rather than drill to build combat power. (We raised armies too slowly in past games, so we need a higher threshold to ensure our forces are large enough to contest the enemy.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.
8. When your army size is under 30,000 men and funds exceed $300, order recruit at your cities rather than drill to build combat power.

### Version 19, after game 19 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused heavily on drilling rather than expanding our army through recruitment and maintaining supply lines, leading to starving armies and poor combat outcomes. Meanwhile, the Rebel forces steadily captured our cities and overwhelmed us.

**Strategy for the next game.** Next game, we will prioritize continuous recruitment at major cities, keep supply lines fully maintained, and strictly avoid attacking at unfavorable odds while expanding our territory aggressively.

**Changes:**

- dropped: When your army size is under 30,000 men and funds exceed $300, order recruit at your cities rather than drill to build combat power. (This overlapping lesson caused us to over-focus on recruiting limits instead of maintaining balance and supply.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.

### Version 20, after game 20 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We failed to recruit any new troops throughout the entire game, allowing our initial 39,000 men to whittle down through combat attrition while the Rebels grew to over 54,000. Although we successfully captured cities early on and eliminated their fleet, our static army sizes could not hold territory against larger Rebel counterattacks.

**Strategy for the next game.** We will aggressively capture neutral and enemy cities in the opening months while actively using our growing treasury to recruit and reinforce our armies, avoiding unfavorable low-odds attacks and keeping our forces large enough to withstand Rebel counter-offensives.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.

### Version 21, after game 21 (standard: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We attacked enemy forces in fortified cities with inferior odds, leading to heavy losses and defeat in five turns. We also neglected recruitment, keeping our armies small while the enemy expanded.

**Strategy for the next game.** We will focus on recruiting to strengthen our forces, avoid low-odds attacks, and maintain supply lines while capturing neutral territories.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When you have an idle army with superior numbers next to an enemy city, order move to attack only when odds exceed 60%.

### Version 22, after game 22 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We expanded our territory early but attacked heavily fortified or superior enemy forces without sufficient numbers, notably suffering a disastrous 12% odds attack at Nashville. While we recruited well, we neglected supply lines and allowed Confederate armies to concentrate, counterattack, and overrun our positions.

**Strategy for the next game.** We will secure neutral border cities in the opening turn, aggressively recruit men at major cities while keeping our treasury healthy, maintain full supply lines, and strictly limit attacks to favorable odds above 60% against unfortified targets to wear down the Confederacy without wasting our strength.

**Changes:**

- revised: When you have an idle army next to an enemy city, order move to attack only when combat odds exceed 60% and the defender is not in a fortified city. (We launched an attack at 12% odds into Nashville against a strong defender and got severely punished; we must avoid attacking entrenched or superior forces.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When you have an idle army next to an enemy city, order move to attack only when combat odds exceed 60% and the defender is not in a fortified city.

### Version 23, after game 23 (standard: Rebel victory: capital captured, 2 turns)

**Diagnosis.** We pushed our armies forward aggressively at the start, leaving Washington completely undefended. The Confederate AI immediately exploited this gap by marching Jackson straight into our capital on Turn 2, ending the game instantly. We must always protect Washington and avoid leaving our core territory empty while advancing.

**Strategy for the next game.** Next game, we will secure our strategic position by keeping a strong garrison or army near Washington while sending other forces to capture neutral and enemy cities. We will balance aggressive expansion with careful home defense to prevent quick capital losses.

**Changes:**

- dropped: When you have an idle army next to an enemy city, order move to attack only when combat odds exceed 60% and the defender is not in a fortified city. (This overly restrictive rule contributed to poor performance and was not supported by effective gameplay results.)
- added: When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives. (We lost the game in two turns because the capital was completely undefended and the Rebel AI walked right in.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 24, after game 24 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused excessively on drilling instead of aggressively expanding our city control and matching the enemy's recruitment and territorial gains. While we built up some forces, we failed to secure enough cities to prevent the Confederacy from reaching the 28-city victory threshold, whereas the computer player actively captured cities and engaged in steady recruitment and movement.

**Strategy for the next game.** Next game, we will aggressively recruit forces and continuously capture neutral and enemy cities to deny the Confederacy the 28 cities required for their victory, limiting passive drilling and focusing on territorial expansion.

**Changes:**

- dropped: When armies have high experience potential and no immediate threats, order drill to maximize combat ratings. (Excessive drilling consumed our turns while the computer rapidly captured the necessary cities for an alternate map victory.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 25, after game 25 (standard: Rebel victory: capital captured, 5 turns)

**Diagnosis.** We attacked enemy-held cities with insufficient force strength and odds, losing critical battles while failing to recruit or reinforce our armies. Meanwhile, the Rebel forces outpaced us and captured Washington due to our inadequate garrisoning and offensive overextension.

**Strategy for the next game.** We will focus on building up our army sizes through steady recruitment, maintaining full supply lines, and establishing strong defensive garrisons around Washington and key cities before attempting major offensives.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 26, after game 26 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused too much on scattered attacks and drilling while ignoring recruitment. Our army sizes remained static around 35,000 men while the computer systematically recruited and expanded to over 100,000 men, overwhelming us economically and geographically.

**Strategy for the next game.** Next game we will aggressively recruit new troops using our growing treasury, maintain strong concentrated forces, and match the computer's army expansion rather than relying on drilling and small-force maneuvering.

**Changes:**

- dropped: When your armies have high experience and cash is above $500, order drill to maximize combat effectiveness. (Drilling did not help us win battles or deter the computer's massive troop growth; recruitment is vastly superior.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 27, after game 27 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We suffered a rapid defeat because we initiated poorly supported attacks without reinforcing our armies or keeping them supplied. Our army strength dwindled while the Rebels grew, and we failed to contest their advances or protect our core cities.

**Strategy for the next game.** Next game we will aggressively recruit to match Rebel numbers, keep our forces well-supplied before attacking, and maintain a solid defense around Washington while systematically capturing border cities.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 28, after game 28 (alternate: Rebel victory: cities controlled, 13 turns)

**Diagnosis.** We focused too much on drilling and accumulated cash instead of aggressively recruiting troops and expanding our army size. While we kept our treasury full, the Confederacy outproduced and outnumbered us heavily by 1863, leading to our defeat.

**Strategy for the next game.** Next game, we will prioritize recruiting new troops aggressively across all available cities to match the Confederate force growth, while maintaining steady pressure on enemy territory.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 29, after game 29 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We failed to recruit any new troops or properly manage our supply lines, leading to starving armies and low combat odds. While we captured some border cities early, the Rebel forces steadily overwhelmed us as our numbers dwindled and our armies became cut off and blockaded.

**Strategy for the next game.** We will focus on aggressive early expansion while aggressively recruiting to maintain superior force numbers. We will strictly monitor supply levels to prevent starvation and utilize railroads and fortification to secure critical hubs against Rebel counterattacks.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 30, after game 30 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** The Union army suffered a rapid defeat because it relied heavily on drilling instead of reinforcing numbers or launching coordinated offensives. Without recruitment, total troop strength shrank from 39,100 to 32,100, allowing the Confederate forces to outmaneuver and overwhelm our smaller armies in key battles.

**Strategy for the next game.** In the next game, we will immediately initiate capture moves on border cities while aggressively utilizing our cash to recruit new troops and reinforce existing armies, avoiding excessive drills that leave our force numbers stagnant.

**Changes:**

- revised: When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size. (We failed to recruit in this game, leading to a severe manpower deficit against Confederate numbers. We must actively build up strength.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 31, after game 31 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused too much on drilling and failed to recruit or build our economy, resulting in stagnant troop numbers and declining city counts while the Confederates grew stronger.

**Strategy for the next game.** We will aggressively recruit new armies in major cities when funds are available, maintain supply lines, and push forward to capture strategic cities while keeping our capital defended.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 32, after game 32 (alternate: Rebel victory: cities controlled, 3 turns)

**Diagnosis.** We pushed forward with weak armies without sufficient numbers or supply, attacking prepared enemies at bad odds while neglecting to recruit and reinforce early. The Confederates concentrated superior forces and crushed our isolated detachments.

**Strategy for the next game.** We will focus heavily on early recruitment and reinforcement at major hubs while consolidating our forces, avoiding premature low-odds attacks until our armies outnumber and out-supply the enemy.

**Changes:**

- revised: When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately. (Maintained to secure initial territory without change.)
- revised: When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size. (Ensures we build up strength instead of marching small forces to defeat.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 33, after game 33 (standard: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We attacked enemy forces without sufficient numerical superiority or supply, resulting in costly defeats and a steady loss of cities and income. Meanwhile, we neglected to recruit new forces to replace our losses while the Rebels grew stronger.

**Strategy for the next game.** We will focus on recruiting heavily in the opening turns to build our army size, avoid low-odds attacks, maintain army supply, and secure our core cities while steadily advancing on adjacent enemy positions.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 34, after game 34 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We relied excessively on drilling and isolated attacks with small forces instead of building up large armies through recruitment and consolidating our units. The Confederacy outgrew us in numbers and ultimately captured our capital and cities.

**Strategy for the next game.** Next game we will aggressively recruit forces in major cities to build large armies, maintain adequate supply, and defend Washington while systematically capturing enemy territory.

**Changes:**

- revised: When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size. (We failed to recruit enough and were vastly outnumbered by the end of the game.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 35, after game 35 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** This game resulted in a quick defeat because we neglected recruiting and army expansion while excessively drilling and building ships. We failed to use our funds to grow our forces, leading to attrition, starvation, and a lack of combat power to hold territory against growing Confederate armies.

**Strategy for the next game.** Next game we will aggressively recruit to build up a large army, maintain our supply lines, and capture strategic enemy cities while avoiding excessive drilling at the expense of troop strength.

**Changes:**

- dropped: When your treasury is above $500 and no armies need supply, order drill to build up general experience. (Excessive drilling contributed to our failure to recruit and expand army size, leading to defeat.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 36, after game 36 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We failed to build up our forces through recruitment and failed to supply our armies adequately, allowing the Confederate computer to outnumber us massively (87,100 to 31,500 men) and capture cities to trigger a Rebel victory.

**Strategy for the next game.** Next game we will aggressively use our treasury to recruit troops at major cities every turn while maintaining adequate supply lines and securing border territories to counter the Confederate buildup.

**Changes:**

- revised: When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size. (We accumulated cash up to $816 by the end but failed to recruit, leaving our army size dangerously small compared to the growing Rebel forces.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 37, after game 37 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused heavily on drilling and naval construction while neglecting recruitment and maintaining army supply lines. This led to a gradual decline in our manpower and widespread supply shortages, allowing the Rebels to gradually capture our cities and achieve victory.

**Strategy for the next game.** Next game we will maintain our focus on aggressive initial expansion while strictly prioritizing recruitment and supply management over excessive drilling and non-essential naval builds to ensure our armies stay strong and well-supplied.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 38, after game 38 (alternate: Rebel victory: cities controlled, 3 turns)

**Diagnosis.** We pushed our small starting armies into offensive moves without recruiting or building up strength, leading to disastrous defeats against concentrated Confederate forces. Meanwhile, the computer player patiently built up its forces through recruitment and maintained defensive positions before striking.

**Strategy for the next game.** We will focus heavily on recruiting fresh troops at major cities to build up our army size before launching major offensives, while using fortify and supply to hold our gains and outlast the Confederacy.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 39, after game 39 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We failed to recruit any new troops throughout the entire game, allowing the Rebel army to outnumber us significantly in strength and quality over time. Excessive drilling and poor-odds attacks wasted valuable turns while our cities fell.

**Strategy for the next game.** Next game we will aggressively recruit forces every turn when funds permit, avoid low-odds attacks, maintain army supply, and systematically capture enemy and neutral territory to secure our income and outnumber the Confederacy.

**Changes:**

- added: When your cities offer recruits and treasury is above $200, order recruit to replace losses and expand our forces. (We completely neglected recruitment in this game, leading to a fatal deficit in manpower compared to the Rebels.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When your cities offer recruits and treasury is above $200, order recruit to replace losses and expand our forces.

### Version 40, after game 40 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused heavily on recruiting and drilling large stacks, but neglected securing our borders and advancing on weakly held enemy territory. Meanwhile, the computer aggressively captured cities and neutralized our threats.

**Strategy for the next game.** We will aggressively capture neutral and enemy-adjacent cities from turn one, balance our recruitment with steady territorial expansion, and ensure no enemy forces go unchecked near our capital.

**Changes:**

- dropped: When your cities offer recruits and treasury is above $200, order recruit to replace losses and expand our forces. (It was redundant with existing recruitment rules and performed poorly.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 41, after game 41 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused too much on drilling and building wooden ships while failing to recruit new troops or adequately supply our armies. This led to low troop numbers, out-of-supply units, and defeats in battle against Confederate forces that outmatched us.

**Strategy for the next game.** Next game we will prioritize recruiting new troops to maintain our strength, keep our armies fully supplied, and avoid unnecessary drills and ship construction until our land forces and front lines are secure.

**Changes:**

- revised: When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size. (We failed to recruit in this game, leading to declining troop strength while the enemy grew.)
- revised: When an army has 1 or less supply, order supply to prevent starvation and attrition losses. (Armies ran out of supplies because we neglected the supply command and marched too much.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 42, after game 42 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We captured initial cities but failed to recruit or reinforce our armies, leaving our forces small and vulnerable. While we spent turns drilling, the Rebels built up massive armies (over 80,000 men) and systematically overwhelmed our positions and captured our cities, leading to a quick defeat.

**Strategy for the next game.** Next game, we will aggressively capture initial cities while immediately pivoting to regular recruitment using our growing treasury to match the enemy's troop strength, avoiding excessive drilling until our army sizes are sufficient to hold territory.

**Changes:**

- dropped: When your armies have high experience and you need defensive readiness, order drill to maximize combat effectiveness. (Excessive drilling caused us to neglect recruiting new men, leaving our total troop count severely outnumbered while the enemy massed large armies.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 43, after game 43 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We suffered a decisive defeat by failing to recruit enough to match Confederate strength growth and allowing our armies to engage in unfavorable, low-odds attacks. Furthermore, our armies repeatedly ran out of supply without timely replenishment or proper defensive positioning.

**Strategy for the next game.** We will focus on maintaining strong recruitment at major cities to grow our forces, keeping our armies fully supplied before undertaking any moves, and aggressively defending Washington while striking vulnerable Confederate outposts.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 44, after game 44 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We successfully recruited large armies and expanded our troop numbers, but our attacks into Nashville and against fortified enemy positions resulted in heavy losses and low odds victories or defeats. Meanwhile, the computer focused on seizing empty cities and building up naval strength to protect supply lines and economy.

**Strategy for the next game.** Next game, we will aggressively capture empty and neutral cities early on like the computer did, build up our naval fleet to prevent blockades, and avoid low-odds attacks on well-defended enemy strongpoints until our armies are fully drilled and reinforced.

**Changes:**

- revised: When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it. (We attacked Nashville with insufficient odds and suffered heavy losses; we need to ensure overwhelming superiority before assaulting fortified cities.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 45, after game 45 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We failed to recruit any new troops throughout the entire game, allowing the Confederate forces to outnumber and overwhelm us in cities and strength. While we drilled and fortified, we neglected economic growth and army expansion.

**Strategy for the next game.** Next game, we will vigorously recruit new troops whenever funds permit while continuing to aggressively capture neutral and enemy cities to maintain income and territory.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 46, after game 46 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We pushed our small initial armies into offensive attacks without building up their strength or supply first, resulting in heavy defeats against larger Confederate forces. Meanwhile, we neglected recruiting and supplying our armies, leading to attrition and a shrinking military while the Rebels expanded.

**Strategy for the next game.** Next game, we will prioritize recruiting heavily at major cities using our available cash, maintain full supply stocks for all active armies, and avoid attacking superior enemy forces until our numbers outmatch them.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 47, after game 47 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We focused too much on naval building and drilling while neglecting proper recruitment and supply management. Our armies ran out of supply, losing combat strength and troops to attrition, while the Rebels massed huge armies in the interior and seized our cities.

**Strategy for the next game.** Next game we will aggressively recruit to match Confederate force numbers, keep our main armies fully supplied before moving, and balance expansion with maintaining secure supply lines to prevent devastating attrition.

**Changes:**

- revised: When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size. (We failed to keep pace with Rebel troop numbers because we spent cash on ships instead of recruits.)
- dropped: When naval units are needed, order build wooden to maintain maritime superiority. (Building excessive wooden ships drained our attention and funds from maintaining field armies and supply lines.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 48, after game 48 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused heavily on drilling armies instead of aggressively capturing cities or expanding our territory. While our forces gained experience, the Confederacy systematically captured territory and won via city count dominance. We also failed to use rail or naval attacks effectively.

**Strategy for the next game.** We will aggressively capture neutral and enemy cities in the early game, increase recruitment to match Confederate numbers, and avoid excessive drilling while maintaining a steady offensive pressure to prevent the enemy from controlling the map.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 49, after game 49 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We failed to recruit any new troops, letting our total strength dwindle while the Confederacy grew to 140,000+ men. We also neglected to defend Washington, allowing Stonewall Jackson to capture our capital in July 1862 and trigger a Rebel victory.

**Strategy for the next game.** Next game we will aggressively recruit to maintain our manpower superiority, keep our armies supplied and concentrated, and ensure Washington remains heavily defended against Confederate raids.

**Changes:**

- revised: When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives. (We lost Washington and the game in 1862 because no army was left behind or moved back to protect our capital from Jackson's advance.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 50, after game 50 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** In this alternate map game, we advanced quickly and recruited at major cities, but we repeatedly attacked enemy-held cities with inferior odds or insufficient army sizes against strong entrenched forces. We also neglected to supply our advancing armies or properly consolidate forces, leading to decisive defeats in battle and a rapid loss of city control.

**Strategy for the next game.** Next game, we will maintain our focus on early expansion and troop recruitment while strictly avoiding attacks on enemy armies unless we hold a clear numerical and supply advantage. We will ensure our advancing forces are well-supplied and properly consolidated before attempting to storm enemy strongholds.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 51, after game 51 (standard: Rebel victory: capital captured, 3 turns)

**Diagnosis.** We pushed too aggressively on multiple fronts with weak armies, leaving Washington defended by a minuscule force that Jackson easily overran in July 1861. Meanwhile, we failed to recruit or reinforce our units, resulting in a rapid loss of our capital and defeat.

**Strategy for the next game.** Next game, we will maintain a strong defensive presence around Washington to prevent enemy counter-attacks on our capital, utilize recruitment to keep our armies at full strength, and avoid overextending our forces into high-risk battles before we are properly supplied and reinforced.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 52, after game 52 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We attacked heavily fortified enemy positions with small, unsupported armies, resulting in catastrophic defeats (such as Buell's assault on Nashville at 3% odds). Meanwhile, the Confederate computer expanded its forces, rail-transported commanders effectively, and overwhelmed our isolated garrisons.

**Strategy for the next game.** Next game, we will focus on building up our army sizes through consistent recruitment, keeping our forces supplied and concentrated, and avoiding low-odds attacks against fortified Confederate strongpoints while steadily capturing neutral territories.

**Changes:**

- revised: When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives. (We must prioritize capital defense and avoid launching unsupported attacks on strong enemy garrisons.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 53, after game 53 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We lost quickly because we failed to recruit new armies and constantly attacked into superior enemy defenses or stacked forces at terrible odds, while our income dwindled and enemy armies expanded unchecked.

**Strategy for the next game.** Next game we will aggressively recruit forces with our starting cash, maintain army supply lines before marching, and avoid attacking enemy stacks in fortified positions unless we have overwhelming numerical superiority.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 54, after game 54 (alternate: Rebel victory: cities controlled, 3 turns)

**Diagnosis.** We focused heavily on drilling rather than expanding our territory or reinforcing our forces, allowing the Confederates to capture key western cities and secure a quick victory. We must aggressively capture neutral or enemy cities and reinforce our armies instead of passive drilling.

**Strategy for the next game.** Next game we will aggressively move to capture neutral and enemy cities from turn one, utilize recruits to grow our forces, and avoid excessive drilling while the enemy advances unchecked.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 55, after game 55 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We accumulated a large cash reserve but failed to recruit new armies or maintain proper supply lines, leading to starving armies and repeated defeats in the West while Confederate forces outflanked and overwhelmed us.

**Strategy for the next game.** We will aggressively recruit new armies with our cash reserves, maintain steady supply lines to avoid attrition, and press the offensive in the West to secure key cities while protecting Washington.

**Changes:**

- revised: When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size. (We failed to recruit in this game despite holding high cash, allowing the Rebels to outnumber our field strength.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 56, after game 56 (alternate: Rebel victory: share of total income, 6 turns)

**Diagnosis.** We captured initial cities and recruited well in October, but we neglected to defend Washington. Jackson marched from the Shenandoah and captured our capital in January 1862, ending the game immediately. We spent too many turns drilling instead of maintaining a defensive cover for Washington and counter-attacking enemy columns.

**Strategy for the next game.** Next game, we will execute our initial captures and recruit early, but we will keep a strong army stationed in or adjacent to Washington at all times to prevent Jackson or other Confederate columns from seizing our capital. We will balance recruiting with maintaining defensive positions near the core cities.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 57, after game 57 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** This game was lost because we failed to recruit new armies and build up our strength, letting our numbers dwindle while the Rebels grew massively. We also neglected army supply and allowed McDowell in Washington to run out of supply, which left the capital vulnerable and eventually led to its capture and a decisive defeat.

**Strategy for the next game.** Next game, we will aggressively recruit forces to keep our numbers competitive with the Confederacy, maintain strict attention to army supply lines especially in the capital, and combine our armies for concentrated offensives rather than spreading out and drilling excessively.

**Changes:**

- revised: When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size. (We failed to recruit in this game, leading to a severe manpower disadvantage. We must actively use recruit to maintain force parity.)
- revised: When an army has 1 or less supply, order supply to prevent starvation and attrition losses. (McDowell's army in Washington went out of supply for multiple turns, ruining its combat effectiveness and leading to the fall of the capital.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 58, after game 58 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** In this alternate map game, we aggressively pushed forces forward without sufficient concentration or supplies, resulting in costly failed attacks against entrenched Rebel positions and fortified cities. While we correctly recruited early, our poorly coordinated offensive moves led to high attrition and loss of city control, allowing the Confederacy to seize cities and secure victory.

**Strategy for the next game.** Next game, we will prioritize economic and manpower buildup while keeping our armies well-supplied and concentrated before launching coordinated attacks. We will use defensive fortifications around key positions and avoid piecemeal assaults that drain our strength.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 59, after game 59 (standard: Rebel victory: capital captured, 2 turns)

**Diagnosis.** We focused entirely on immediate offensive moves without building up our forces or defending our capital. Jackson bypassed our weak advance and captured Washington directly in May 1861, ending the game immediately.

**Strategy for the next game.** We will secure Washington immediately, build up our armies through regular recruitment, and maintain defensive forces near the capital while expanding our territory carefully.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 60, after game 60 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We attacked enemy-held cities with insufficient strength and poor odds, while neglecting to recruit new forces or reinforce existing armies. The computer player successfully expanded its economy and captured key cities while we faltered in western skirmishes.

**Strategy for the next game.** Next game we will aggressively recruit forces to build up our manpower while executing coordinated advances to capture neutral and enemy cities, ensuring we outnumber defenders before attacking.

**Changes:**

- revised: When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size. (Our army size stagnated because we issued zero recruit orders throughout the entire game, losing our strength advantage.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 61, after game 61 (standard: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** We failed to recruit any new troops throughout the entire game, allowing the Rebel army to outnumber us significantly (160,900 to 69,100 by the end). While we successfully held Washington and defended some attacks, our passivity and failure to expand our forces or aggressively capture cities led to a slow strangulation and a Rebel victory by city count.

**Strategy for the next game.** In the next game, we will aggressively recruit new troops in major cities whenever funds permit, maintain our defensive lines around Washington and our western holdings, and use our armies to steadily capture enemy cities to prevent a Rebel territorial victory.

**Changes:**

- added: When cities offer recruits and treasury is above $300, order recruit to continuously reinforce and expand our forces. (We failed to recruit any troops in Training Game 61, leading to a catastrophic troop deficit against the Rebels. We must actively recruit to keep pace with enemy numbers.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $400 and cities offer recruits, order recruit at your major cities to build up army size.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When cities offer recruits and treasury is above $300, order recruit to continuously reinforce and expand our forces.

### Version 62, after game 62 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We pushed forward with small, unreinforced starting armies against fortified and concentrated Confederate forces, resulting in disastrous defeats like Buell's annihilation at Nashville. Meanwhile, we accumulated over $1,000 in the treasury instead of using it to recruit and build massive forces like the computer did.

**Strategy for the next game.** Next game, we will aggressively recruit using our cash reserves to build overwhelming force superiority, match the computer's troop generation, and avoid suicidal attacks with small armies while keeping supply lines secure.

**Changes:**

- dropped: When cities offer recruits and treasury is above $300, order recruit to continuously reinforce and expand our forces. (This was a duplicate rule with slightly different thresholds; merged into the core recruitment rule.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 63, after game 63 (standard: Rebel victory: share of total income, 6 turns)

**Diagnosis.** We captured several border cities early on, but neglected recruiting new troops and replacing losses. Meanwhile, we left Washington poorly defended, allowing Jackson to seize it in January 1862 and end the game in a Rebel victory.

**Strategy for the next game.** Next game, we will aggressively capture border cities while maintaining a robust recruitment program to keep army sizes high, and we will keep a strong force stationed near Washington to prevent any surprise Confederate capital raids.

**Changes:**

- revised: When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses. (We failed to recruit in this game and our troop numbers dwindled, causing us to lose the initiative.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 64, after game 64 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** In this alternate map game, we failed to secure enough cities and allowed the Confederate forces to expand and outnumber us. We launched attacks with inferior odds (such as Grant attacking Beauregard at 42% odds) instead of building up our forces, managing supply, and utilizing the fleet and rail network to strike where the enemy was weak, as the teacher's game demonstrated.

**Strategy for the next game.** Next game we will aggressively recruit and build our forces while capturing neutral cities early, avoiding low-odds attacks, maintaining supply, and utilizing rail and naval assets effectively to outpace the Confederate economy and secure a Union victory.

**Changes:**

- revised: When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately. (Maintained to secure early territory.)
- revised: When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses. (Kept to ensure we match Confederate force growth.)
- revised: When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it. (Kept to prevent low-odds suicidal attacks.)
- revised: When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving. (Maintained to prevent supply penalties.)
- revised: When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength. (Kept for defense of key positions.)
- revised: When an army has 1 or less supply, order supply to prevent starvation and attrition losses. (Maintained for force preservation.)
- revised: When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives. (Kept to protect our capital from falling.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 65, after game 65 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We failed to recruit any new troops during the entire game, allowing the Confederate army to outnumber and crush us. We spent excessive turns drilling and making poorly supported attacks while neglecting to reinforce our armies or expand our forces.

**Strategy for the next game.** Next game we will aggressively recruit new troops using our starting treasury, maintain supply lines for all advancing armies, and avoid excessive drilling in favor of force generation and decisive offensive operations.

**Changes:**

- revised: When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses. (We completely ignored recruiting in this game, leading to a fatal deficit in manpower compared to the Rebels.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.

### Version 66, after game 66 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** The Confederacy achieved a rapid victory by concentrating superior forces and capturing key cities while our armies repeatedly launched low-odds attacks against fortified positions without sufficient concentration. We failed to use the join command to pool our manpower and relied on scattered forces.

**Strategy for the next game.** Next game, we will focus on concentrating our forces via the join command before attacking, maintain proper supply lines, and steadily recruit to counter the growing Confederate army size.

**Changes:**

- added: When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives. (We lost battles due to small fragmented armies attacking larger Rebel forces; joining forces is necessary to achieve numerical superiority.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.

### Version 67, after game 67 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused heavily on drilling and buying ships while neglecting recruitment and supply management. Our armies repeatedly launched attacks at poor odds without sufficient support, and we failed to merge scattered forces. As a result, our manpower dwindled, our front lines collapsed, and the Confederates seized key cities to achieve victory.

**Strategy for the next game.** Next game we will prioritize aggressive recruitment and proper supply management, avoiding reckless attacks at low odds while merging our forces to secure vital cities and defend our core territory.

**Changes:**

- revised: When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses. (We failed to recruit adequately in this game, letting our manpower decline while the enemy grew stronger.)
- revised: When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it. (We initiated several poor-odds attacks because we did not wait for overwhelming local superiority.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.

### Version 68, after game 68 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused heavily on drilling commanders and recruiting locally while failing to supply our armies and allowing the Rebel forces to concentrate and outmaneuver us. Our attacks failed due to poor odds and lack of supply, and our economy declined as we lost vital cities.

**Strategy for the next game.** We will open by capturing adjacent neutral and enemy cities quickly, maintain sufficient recruits and supplies at all times, and avoid low-odds attacks while grouping our armies for concentrated offensives.

**Changes:**

- revised: When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses. (We had enough cash but failed to recruit efficiently early on, falling behind the Rebel army growth.)
- revised: When an army has 1 or less supply, order supply to prevent starvation and attrition losses. (Our units ran out of supplies and suffered defeats in enemy territory due to neglect.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.

### Version 69, after game 69 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We suffered a decisive loss because we failed to recruit new troops or manage our army supplies properly, leading to starving armies and low numbers while the Rebels aggressively expanded. We also initiated unprofitable attacks at terrible odds instead of building up defensive and offensive strength.

**Strategy for the next game.** Next game, we will prioritize recruiting new troops to maintain superior numbers, carefully manage our supply lines to prevent attrition, and only attack when odds are heavily in our favor while keeping our core cities fortified.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.

### Version 70, after game 70 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We repeatedly ordered attacks against heavily defended enemy forces in Louisville at terrible odds (averaging 21%), causing massive casualties and wearing down our armies while the Confederates concentrated and crushed us. Meanwhile, our fleet in Philadelphia was blockaded and neglected, causing constant supply starvation and attrition losses.

**Strategy for the next game.** We will focus on capturing neutral territory early, maintaining supply lines to avoid starvation, avoiding suicidal low-odds attacks against fortified Confederate positions, and using our naval fleet actively to break enemy blockades.

**Changes:**

- added: When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison. (Our seaport in Philadelphia was blockaded for multiple turns, causing constant supply starvation and casualties while our fleet remained idle.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
9. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.

### Version 71, after game 71 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We suffered another rapid defeat because we failed to recruit fresh forces to replace casualties and grow our strength while the enemy steadily expanded their armies. Furthermore, our offensive attacks were launched without adequate numerical superiority, leading to repeated failed assaults and starving out-of-supply units.

**Strategy for the next game.** We will focus heavily on recruiting fresh troops every turn cash permits, avoiding under-strength attacks, and keeping our main armies fully supplied to prevent attrition while systematically countering Confederate expansions.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
9. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.

### Version 72, after game 72 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We expanded our army sizes through recruitment and won some early battles, but we failed to build up a strong naval presence or secure our captured territories effectively. The Confederate forces swept through our northern flank, outmaneuvered us, and seized key cities, leading to a rapid defeat on the alternate map.

**Strategy for the next game.** Next game, we will focus on aggressive capture of neutral border cities early on, maintaining robust recruitment at major financial hubs, and ensuring our main field armies are concentrated and well-supplied before striking enemy strongholds.

**Changes:**

- dropped: When you have spare cash at the start of a turn, order build wooden to construct warships and protect your seaports from enemy raids. (This lesson had a poor track record and did not prevent naval pressures effectively compared to direct offensive movements.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
9. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.

### Version 73, after game 73 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused too much on expensive unsupported attacks and failed to recruit or reinforce our armies, leaving us outnumbered in key sectors. While we won naval skirmishes, our land forces withered away and could not hold territory against concentrated Confederate advances.

**Strategy for the next game.** We will maintain a disciplined balance of defensive fortification, essential recruitment to keep our armies strong, careful supply management, and concentrated attacks only when we hold a clear numerical and tactical advantage.

**Changes:**

- revised: When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses. (We accumulated over $1,000 cash while our army strength steadily dropped from 98,000 to 82,000 men. We must convert idle cash into reinforcements.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
9. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.

### Version 74, after game 74 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused too heavily on drilling and static defense while the Confederate forces rapidly captured surrounding cities and accumulated superior numbers and territory. Although we accumulated cash and built up our forces late in the game, we failed to maintain aggressive expansion or adequately contest enemy movements, allowing them to secure the required 28 cities for victory.

**Strategy for the next game.** Next game we will aggressively pursue territorial capture from turn one, utilizing our capital and major cities for steady recruitment while keeping our field armies mobile rather than passive drill targets, ensuring we contest every Confederate city advance.

**Changes:**

- revised: When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately. (Maintained to ensure immediate early territorial gains matching successful computer openings.)
- revised: When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses. (Kept to guarantee sufficient force generation to counter growing Rebel army strengths.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
9. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.

### Version 75, after game 75 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We lost because we engaged in premature and uncoordinated offensives against entrenched or superior Rebel forces without maintaining proper supply lines or reinforcing our armies. While we accumulated treasury cash, our troop strength dwindled and we allowed the Confederacy to seize key Western and Eastern cities unchecked.

**Strategy for the next game.** Next game we will aggressively recruit to maintain manpower dominance, keep our armies fully supplied before moving, avoid attacking superior positions without adequate numbers, and secure our core cities while steadily pressing the Confederate territory.

**Changes:**

- added: When a city offers recruits and funds exceed $300, order recruit at that city to expand our manpower before launching major campaigns. (We failed to recruit in this game, leading to a steady decline in our total men while the Rebels grew stronger.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
9. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
10. When a city offers recruits and funds exceed $300, order recruit at that city to expand our manpower before launching major campaigns.

### Version 76, after game 76 (alternate: Rebel victory: capital captured, 4 turns)

**Diagnosis.** We focused on distant offensives without securing our rear and capital. J.E.B. Stuart slipped through to capture Washington on Turn 4 while our main forces were scattered, and Grant made poor attacks against strong forces without sufficient support.

**Strategy for the next game.** Next game we will protect our capital and core cities first, maintain stronger defensive reserves near Washington, avoid low-odds attacks, and methodically recruit and build forces before launching major campaigns.

**Changes:**

- revised: When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives. (We lost the game in Turn 4 because J.E.B. Stuart captured an undefended Washington while our forces were attacking elsewhere.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
9. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
10. When a city offers recruits and funds exceed $300, order recruit at that city to expand our manpower before launching major campaigns.

### Version 77, after game 77 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused too heavily on limited drills and failed to recruit or build fleets, leaving our forces small and vulnerable while the Rebels out-expanded and eventually swamped us in cities and numbers.

**Strategy for the next game.** We will aggressively recruit new forces early, build up a protective naval fleet to challenge Confederate shipping, merge major armies under top leaders, and push continuously on enemy border cities to maintain territorial parity.

**Changes:**

- dropped: When a city offers recruits and funds exceed $300, order recruit at that city to expand our manpower before launching major campaigns. (Redundant with lesson 2 while having a poor track record.)
- added: When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding. (We lost control of the seas completely in this game, allowing the enemy to blockade and bombard unchecked.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
9. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
10. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 78, after game 78 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** The Confederacy rapidly expanded their forces and launched coordinated counter-offensives while our armies remained isolated and under-supplied. We attacked fortified positions like Fort Donelson prematurely without sufficient strength or preparation, leading to heavy losses and allowing the enemy to capture vital territory and income centers.

**Strategy for the next game.** Next game, we will prioritize aggressive recruitment in major cities while maintaining fully supplied, concentrated armies under capable leaders. We will avoid attacking fortified enemy positions without overwhelming numerical superiority, use rail and movement to reinforce threatened points promptly, and continuously expand our naval presence to control the seas and protect our income.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
9. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
10. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 79, after game 79 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We attacked enemy forces prematurely without building up our army sizes via recruitment or consolidating our units. Our small armies repeatedly lost battles and suffered attrition. We failed to maintain army supply, leading to out-of-supply states, whereas the computer player built up recruits, used rails effectively, and managed its forces carefully.

**Strategy for the next game.** Next game, we will prioritize recruiting heavily from major cities while keeping our armies well-supplied and consolidated under strong leaders. We will avoid low-odds attacks and focus on building a powerful, concentrated force before launching major offensives.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
9. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
10. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 80, after game 80 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We launched attacks into strongly held Confederate positions at terrible odds (such as attacking Nashville with an inferior force), causing our armies to be crushed and losing control of the map quickly while the computer steadily expanded its city count.

**Strategy for the next game.** We will focus entirely on capturing neutral territory, building up our forces through recruitment, and avoiding attacks on fortified enemy cities unless we hold overwhelming numerical superiority.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
9. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
10. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 81, after game 81 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** The game was lost because we repeatedly initiated unfavorable attacks against fortified or superior enemy forces (such as attacking Columbus and Harper's Ferry at low odds), suffered high attrition and supply failure due to failing to supply armies on time, neglected defensive fortifications on threatened cities, and allowed the enemy to capture crucial cities while our forces were tied down in losing battles.

**Strategy for the next game.** We will focus on building up our forces in major cities, keeping our armies well-supplied and consolidated under strong leaders, and avoiding rash attacks on enemy strongholds until we achieve overwhelming numerical and positional advantage.

**Changes:**

- revised: When an army is adjacent to an enemy-held city and outnumbers the enemy significantly with superior combat odds, order move to capture it. (We launched attacks at 30% odds and lost repeatedly; we must only attack when we have clear superiority to avoid devastating attrition.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly with superior combat odds, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
9. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
10. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 82, after game 82 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We captured several neutral cities early on, but then halted our offensives and spent crucial turns drilling instead of recruiting troops or attacking enemy positions. The Confederate computer aggressively built up strength, concentrated its forces, and systematically crushed our isolated armies.

**Strategy for the next game.** Next game we will aggressively recruit forces from major cities to maintain numerical parity with the Confederacy, continuously push our armies forward to capture and hold territory, and avoid wasting turns on drilling while the enemy expands unchecked.

**Changes:**

- dropped: When armies have successfully captured initial territory and face enemy counter-attacks, order drill to build combat experience. (Drilling caused us to waste critical turns while the enemy massed forces and overwhelmed our smaller armies; we need recruitment and aggressive movement instead.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly with superior combat odds, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
9. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
10. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 83, after game 83 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We attacked fortified or superior enemy forces without adequate preparation or supply, resulting in severe losses and lost cities. Excessive drilling left our armies idle while Confederate forces advanced unchecked and captured our territory.

**Strategy for the next game.** We will focus on recruiting strong armies, maintaining supply lines, and capturing strategic neutral cities early while avoiding uncoordinated attacks against superior forces.

**Changes:**

- revised: When an army is adjacent to an enemy-held city and outnumbers the enemy significantly with superior combat odds, order move to capture it. (We attacked at poor odds (23%) without enough strength, leading to disastrous defeats.)
- dropped: When armies are not in active combat, order drill to improve experience ratings. (Excessive drilling caused us to neglect capturing territory and defending our cities, leading to a rapid loss.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When an army is adjacent to an enemy-held city and outnumbers the enemy significantly with superior combat odds, order move to capture it.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
8. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
9. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
10. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 84, after game 84 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** The game was lost because the Union capital, Washington, was left undefended and was easily captured by Confederate general Pemberton in December 1861. While our armies focused on drilling and capturing distant cities like Louisville and Fort Donelson, we neglected local defense and allowed enemy forces to march unopposed into our capital.

**Strategy for the next game.** In the next game, we will immediately secure Washington with a defensive force while aggressively capturing adjacent neutral territories, ensuring we never leave our capital vulnerable to enemy capture while expanding our territorial control.

**Changes:**

- dropped: When an army is adjacent to an enemy-held city and outnumbers the enemy significantly with superior combat odds, order move to capture it. (This lesson had a poor record and did not help prevent our defeat or improve tactical outcomes.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 85, after game 85 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We attacked enemy forces without adequate preparation, leading to devastating defeats at terrible odds. We completely neglected recruiting new troops and supplying our armies, causing McDowell to run out of supplies and our forces to crumble under Confederate counter-attacks.

**Strategy for the next game.** Next game we will maintain our forces by regularly recruiting and supplying our armies while avoiding low-odds attacks, ensuring our strength grows to match the computer.

**Changes:**

- revised: When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses. (We failed to recruit any troops this game, leaving us outnumbered and weak.)
- revised: When an army has 1 or less supply, order supply to prevent starvation and attrition losses. (McDowell ran out of supplies and was easily beaten because we ignored supply lines.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 86, after game 86 (alternate: Rebel victory: share of total income, 5 turns)

**Diagnosis.** The Confederate forces outmatched and overwhelmed us due to our failure to recruit and build up our army size while our treasury grew. We sat on over $1000 without raising troops, letting the enemy forces grow to nearly 90,000 men while our numbers actually dwindled. Furthermore, we neglected to properly defend the capital and coordinate our movements, leading to Washington falling in December 1861.

**Strategy for the next game.** Next game, we will aggressively use our ample treasury to recruit and reinforce our armies at every turn while aggressively pursuing strategic territory and keeping Washington heavily defended against Confederate incursions.

**Changes:**

- revised: When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses. (We accumulated over $1,000 in cash during the game and completely failed to recruit, allowing the Rebels to massively outnumber us.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 87, after game 87 (standard: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** In this game, our forces spread too thin attempting to attack without sufficient concentration or forts, leading to high attrition and constant supply shortages during winter and spring months. The Rebel armies steadily reinforced and eventually captured Washington when our rear was unprotected.

**Strategy for the next game.** Next game, we will maintain tighter defensive clusters around Washington and key supply hubs, ensuring all offensive columns are fully supplied and reinforced before moving on enemy strongpoints.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 88, after game 88 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused too much on distant, unsupported movements and neglected recruitment and reinforcement, allowing the Confederacy to outmaneuver us and seize critical territory while our armies slowly bled down in strength.

**Strategy for the next game.** Next game, we will aggressively secure neutral territories early, maintain a steady stream of recruits to keep our field strength high, and combine local offensive maneuvers with robust naval operations to deny the Confederacy city control.

**Changes:**

- revised: When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses. (We failed to recruit in this game, leading to severe manpower attrition; we must consistently reinforce our ranks.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 89, after game 89 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused heavily on building ships and drilling while neglecting recruiting and reinforcing our armies. As a result, our total troop strength dwindled from 98,000 down to 76,000, allowing the Confederates to outnumber us, capture our cities, and trigger a city-control victory.

**Strategy for the next game.** Next game, we will aggressively recruit to keep our troop numbers well above the enemy while capturing key neutral cities early, maintaining army supplies, and using our fleets and rail network effectively to counter Confederate advances.

**Changes:**

- dropped: When troops are low and funds exceed $300, order recruit at major cities to maintain forces. (Replaced by the more precise standard lesson 2 which has a longer and better track record.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 90, after game 90 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused too much on drilling and commerce raiding while the Rebels aggressively captured cities and outmaneuvered us. Failing to recruit new forces and consolidate our numbers left us too weak to hold key territory, leading to a rapid Confederate victory.

**Strategy for the next game.** Next game, we will aggressively capture nearby neutral cities on turn one, immediately begin recruiting to expand our army strength, and actively counter Confederate incursions rather than idling in place to drill.

**Changes:**

- revised: When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately. (Maintained to ensure rapid territorial expansion early in the game.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 91, after game 91 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** The Confederacy won by capturing enough cities and eventually the capital. We initiated attacks at very poor odds (averaging 43%) and failed to recruit or reinforce our armies to replace losses, leading to a steady attrition of our forces.

**Strategy for the next game.** Next game, we will focus on maintaining positive supply lines, avoiding low-odds attacks, actively recruiting to replace losses, and keeping our forces concentrated and well-supplied.

**Changes:**

- added: When attacking enemy cities, only order move into cities where your army outnumbers the defender significantly to ensure successful battles instead of costly defeats. (We lost multiple battles and suffered heavy casualties attacking at low odds during this game.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.
10. When attacking enemy cities, only order move into cities where your army outnumbers the defender significantly to ensure successful battles instead of costly defeats.

### Version 92, after game 92 (alternate: Rebel victory: cities controlled, 3 turns)

**Diagnosis.** We captured initial neutral cities promptly but failed to aggressively recruit and reinforce key positions, allowing Confederate commanders like A.S. Johnston and J.E. Johnston to overrun our central and western cities and overwhelm our fragmented forces.

**Strategy for the next game.** We will aggressively expand our territory in the opening turns, maintain strong recruitment in major cities to build overwhelming army sizes, and ensure our forces are properly merged and supplied before launching coordinated advances against Confederate strongpoints.

**Changes:**

- dropped: When attacking enemy cities, only order move into cities where your army outnumbers the defender significantly to ensure successful battles instead of costly defeats. (This lesson had a very poor record and was not supported by the overall strategy needed for map control.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 93, after game 93 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We lost because we relied too heavily on drilling and did not recruit new troops or reinforce our existing armies to keep pace with Confederate growth. While the computer Union player actively recruited, used the rail network, and expanded its forces to hold territory, our standing forces dwindled, ran out of supply, and were eventually overwhelmed by superior numbers.

**Strategy for the next game.** Next game, we will aggressively recruit and reinforce our armies in addition to capturing neutral cities early, maintaining strong troop numbers to match the Confederate forces instead of wasting turns drilling under-strength units.

**Changes:**

- dropped: When an army is not engaged in active frontline combat, order drill to increase its experience rating. (Excessive drilling consumed turns and funds while our army sizes shrank and we lost battles due to numerical inferiority.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 94, after game 94 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We failed to recruit any new troops throughout the entire game, keeping our army size stagnant at around 39,000 men while the computer grew its forces to over 75,000 men. We also wasted valuable turns on drilling and raiding instead of aggressively capturing cities and recruiting to meet the victory conditions.

**Strategy for the next game.** Next game we will aggressively use recruit every turn possible when funds allow to outnumber the enemy, while actively moving to capture cities and expand our territory instead of wasting time drilling and raiding.

**Changes:**

- revised: When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses. (We completely ignored recruiting in this game, leading to a stagnant army size of 39,000 while the computer built up to 75,000 men and overwhelmed us.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 95, after game 95 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused heavily on drilling static armies rather than recruiting new forces or maintaining our supply lines, leading to dwindling troop numbers and lost territory. Meanwhile, the enemy aggressively advanced, cut off our supplies, and overwhelmed our unsupported garrisons.

**Strategy for the next game.** Next game we will aggressively recruit to maintain army size, keep our supply lines fully stocked, and push forward to capture and hold key cities while defending our capital.

**Changes:**

- revised: When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses. (We failed to recruit in this game while our forces dwindled and the enemy grew vastly superior in numbers.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 96, after game 96 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused heavily on drilling and made too few recruits and aggressive captures while the computer steadily expanded its city count and army size, eventually overwhelming us on the map.

**Strategy for the next game.** We will prioritize aggressive recruitment and city capture from turn one while maintaining steady expansion to outpace the Confederate territorial gain.

**Changes:**

- revised: When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately. (Kept from notebook v95 as a foundational opening rule.)
- revised: When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses. (Kept from notebook v95 to ensure we build up army sizes comparable to the computer.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 97, after game 97 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We attacked enemy cities prematurely with weak, uncoordinated forces while neglecting recruitment and supply management. This caused high attrition and allowed the Rebels to systematically capture our territory and outnumber us.

**Strategy for the next game.** Next game, we will prioritize building up our forces through recruitment, keeping our armies well-supplied and consolidated before making any offensive moves, and maintaining a defensive posture around key strategic cities.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 98, after game 98 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused too much on scattered drills and isolated advances instead of aggressively building concentrated force pools and capturing core enemy cities as the computer did. Our armies were whittled down in piecemeal attacks against enemy concentrations.

**Strategy for the next game.** We will prioritize massive recruitments in major cities, combine forces aggressively under top leaders, and maintain constant pressure on enemy population and supply centers while securing our own capital.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 99, after game 99 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We captured initial neutral cities rapidly, but overextended our armies against stronger Confederate positions in poor-odds attacks, leading to heavy casualties and loss of key cities. Furthermore, we failed to properly manage supply lines and cash reserves, letting armies run out of supplies and losing control of the city count.

**Strategy for the next game.** Next game, we will focus on consolidating our forces before launching attacks, maintaining positive supply lines to every army, and avoiding low-odds engagements while steadily outproducing the Confederacy through careful recruitment and naval control.

**Changes:**

- revised: When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses. (We accumulated cash while losing troops in failed attacks; recruiting more reliably maintains our force strength.)
- dropped: When an army has 1 or less supply, order drill to build experience while waiting. (Drilling stalled our operational readiness and left armies unprepared to respond to enemy movements.)
- added: When planning an attack, check that attacking odds exceed 50% to prevent costly defeats and loss of territory. (Too many poor-odds attacks (averaging 48%) drained our manpower and caused decisive retreats.)

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

### Version 100, after game 100 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused too much on drilling and isolated maneuvers while neglecting regular recruitment. The computer player consistently recruited heavily each turn to expand its forces above 100k men, whereas our army size stagnated around 38k, leaving us too weak to hold territory against Confederate advances.

**Strategy for the next game.** We will aggressively recruit troops every turn using our growing treasury to outnumber the enemy, while maintaining steady offensives and railway deployments to capture key cities and counter Confederate advances.

**Notebook:**

1. When the game starts in April 1861, order move on adjacent neutral or enemy cities to capture them immediately.
2. When your treasury is above $300 and cities offer recruits, order recruit at your major cities to build up army size and replace losses.
3. When Washington is empty or adjacent to enemy forces, order move to bring an army back to defend the capital before initiating distant offensives.
4. When your armies are idle and not facing immediate enemy attack, order supply to keep them fully stocked before moving.
5. When the enemy captures cities and threatens your capital, order fortify on threatened cities to multiply your defensive strength.
6. When an army has 1 or less supply, order supply to prevent starvation and attrition losses.
7. When multiple idle armies occupy the same city, order join to merge them under the best leader for stronger offensives.
8. When an enemy fleet blockades your seaport, order fleet sail to clear the blockade and relieve your besieged garrison.
9. When a seaport has no fleet and funds exceed $200, order build wooden or build ironclad to establish naval presence and counter enemy raiding.

