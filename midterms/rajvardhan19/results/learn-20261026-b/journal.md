# Learning journal: `gemini-b`

Model `gemini-3.5-flash-lite`. 100 training games; notebook version 100 (frozen, sha 2aca9bd2a15690a9).

## What it did, game by game

| game | map | notebook | result | turns | recruits | drills | moves | attacks (won) | mean odds | cities peak / end | last-turn cash | refused |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | standard | v0 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 7 | 8 | 3 (0) | 32% | 13 / 6 | 686 | 1 |
| 2 | alternate | v1 | decisive loss: Rebel victory: cities controlled | 5 | 3 | 10 | 3 | 2 (0) | 31% | 10 / 7 | 1030 | 2 |
| 3 | standard | v2 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 5 | 3 | 0 (0) | - | 11 / 5 | 372 | 2 |
| 4 | alternate | v3 | decisive loss: Rebel victory: cities controlled | 4 | 3 | 0 | 4 | 0 (0) | - | 12 / 7 | 719 | 2 |
| 5 | standard | v4 | decisive loss: Rebel victory: capital captured | 7 | 0 | 0 | 11 | 2 (0) | 32% | 14 / 11 | 270 | 1 |
| 6 | alternate | v5 | decisive loss: Rebel victory: capital captured | 6 | 9 | 10 | 5 | 2 (1) | 50% | 11 / 11 | 573 | 3 |
| 7 | standard | v6 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 8 | 11 | 1 (0) | 40% | 13 / 6 | 347 | 5 |
| 8 | alternate | v7 | decisive loss: Rebel victory: share of total income | 3 | 5 | 0 | 8 | 1 (0) | 30% | 12 / 11 | 547 | 1 |
| 9 | standard | v8 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 0 | 10 | 2 (0) | 35% | 13 / 5 | 200 | 3 |
| 10 | alternate | v9 | decisive loss: Rebel victory: share of total income | 6 | 0 | 3 | 10 | 2 (0) | 22% | 13 / 9 | 1595 | 2 |
| 11 | standard | v10 | decisive loss: Rebel victory: cities controlled | 12 | 2 | 18 | 6 | 3 (2) | 58% | 13 / 4 | 360 | 8 |
| 12 | alternate | v11 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 4 | 6 | 1 (0) | 12% | 11 / 7 | 1078 | 1 |
| 13 | standard | v12 | decisive loss: Rebel victory: cities controlled | 10 | 0 | 16 | 9 | 2 (0) | 38% | 13 / 6 | 787 | 9 |
| 14 | alternate | v13 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 9 | 2 | 1 (0) | 37% | 10 / 8 | 650 | 2 |
| 15 | standard | v14 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 11 | 5 | 0 (0) | - | 13 / 7 | 224 | 3 |
| 16 | alternate | v15 | decisive loss: Rebel victory: cities controlled | 5 | 10 | 24 | 6 | 0 (0) | - | 13 / 9 | 443 | 6 |
| 17 | standard | v16 | decisive loss: Rebel victory: capital captured | 4 | 0 | 10 | 7 | 2 (0) | 34% | 13 / 10 | 738 | 1 |
| 18 | alternate | v17 | decisive loss: Rebel victory: cities controlled | 3 | 3 | 1 | 6 | 0 (0) | - | 11 / 8 | 635 | 3 |
| 19 | standard | v18 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 7 | 9 | 0 (0) | - | 13 / 6 | 380 | 1 |
| 20 | alternate | v19 | decisive loss: Rebel victory: cities controlled | 4 | 3 | 0 | 7 | 0 (0) | - | 11 / 9 | 550 | 2 |
| 21 | standard | v20 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 4 | 10 | 4 (1) | 37% | 13 / 5 | 371 | 2 |
| 22 | alternate | v21 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 9 | 1 (0) | 18% | 13 / 9 | 809 | 0 |
| 23 | standard | v22 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 8 | 6 | 1 (1) | 40% | 12 / 5 | 181 | 4 |
| 24 | alternate | v23 | decisive loss: Rebel victory: cities controlled | 6 | 3 | 5 | 8 | 2 (1) | 35% | 12 / 7 | 818 | 5 |
| 25 | standard | v24 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 16 | 7 | 1 (0) | 33% | 13 / 6 | 792 | 9 |
| 26 | alternate | v25 | decisive loss: Rebel victory: cities controlled | 4 | 3 | 4 | 7 | 0 (0) | - | 12 / 7 | 815 | 0 |
| 27 | standard | v26 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 4 | 11 | 4 (0) | 38% | 13 / 5 | 262 | 3 |
| 28 | alternate | v27 | decisive loss: Rebel victory: share of total income | 3 | 0 | 2 | 7 | 0 (0) | - | 11 / 10 | 872 | 2 |
| 29 | standard | v28 | decisive loss: Rebel victory: capital captured | 5 | 0 | 5 | 5 | 2 (0) | 28% | 13 / 9 | 550 | 1 |
| 30 | alternate | v29 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 3 | 10 | 3 (0) | 24% | 13 / 8 | 1008 | 2 |
| 31 | standard | v30 | decisive loss: Rebel victory: cities controlled | 9 | 0 | 10 | 5 | 2 (0) | 32% | 13 / 5 | 421 | 5 |
| 32 | alternate | v31 | decisive loss: Rebel victory: cities controlled | 7 | 20 | 23 | 0 | 0 (0) | - | 10 / 9 | 351 | 7 |
| 33 | standard | v32 | decisive loss: Rebel victory: capital captured | 7 | 1 | 17 | 8 | 0 (0) | - | 13 / 10 | 279 | 4 |
| 34 | alternate | v33 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 12 | 10 | 0 (0) | - | 13 / 9 | 1250 | 1 |
| 35 | standard | v34 | decisive loss: Rebel victory: cities controlled | 7 | 10 | 10 | 6 | 1 (0) | 44% | 13 / 6 | 243 | 2 |
| 36 | alternate | v35 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 8 | 5 | 0 (0) | - | 12 / 9 | 633 | 0 |
| 37 | standard | v36 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 8 | 8 | 0 (0) | - | 13 / 5 | 280 | 2 |
| 38 | alternate | v37 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 7 | 8 | 2 (0) | 29% | 12 / 8 | 635 | 1 |
| 39 | standard | v38 | decisive loss: Rebel victory: cities controlled | 8 | 2 | 11 | 9 | 3 (0) | 36% | 13 / 5 | 377 | 7 |
| 40 | alternate | v39 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 14 | 5 | 1 (0) | 37% | 12 / 8 | 936 | 3 |
| 41 | standard | v40 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 4 | 7 | 3 (0) | 32% | 13 / 5 | 288 | 1 |
| 42 | alternate | v41 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 2 | 9 | 0 (0) | - | 12 / 6 | 1024 | 5 |
| 43 | standard | v42 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 7 | 9 | 0 (0) | - | 13 / 5 | 187 | 3 |
| 44 | alternate | v43 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 13 | 13 | 1 (0) | 40% | 13 / 9 | 1259 | 4 |
| 45 | standard | v44 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 18 | 2 | 0 (0) | - | 12 / 4 | 1334 | 1 |
| 46 | alternate | v45 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 5 | 0 (0) | - | 11 / 7 | 1266 | 0 |
| 47 | standard | v46 | decisive loss: Rebel victory: capital captured | 5 | 10 | 23 | 5 | 1 (0) | 23% | 13 / 10 | 292 | 8 |
| 48 | alternate | v47 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 14 | 6 | 0 (0) | - | 12 / 7 | 877 | 2 |
| 49 | standard | v48 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 3 | 10 | 3 (0) | 37% | 13 / 5 | 1133 | 6 |
| 50 | alternate | v49 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 12 | 6 | 1 (0) | 37% | 10 / 8 | 1325 | 4 |
| 51 | standard | v50 | decisive loss: Rebel victory: cities controlled | 7 | 9 | 18 | 10 | 5 (1) | 39% | 13 / 6 | 263 | 14 |
| 52 | alternate | v51 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 0 | 7 | 1 (0) | 44% | 12 / 10 | 715 | 1 |
| 53 | standard | v52 | decisive loss: Rebel victory: cities controlled | 8 | 9 | 0 | 14 | 4 (2) | 38% | 14 / 8 | 307 | 7 |
| 54 | alternate | v53 | decisive loss: Rebel victory: share of total income | 6 | 18 | 0 | 12 | 0 (0) | - | 15 / 12 | 380 | 3 |
| 55 | standard | v54 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 1 | 9 | 2 (0) | 35% | 14 / 4 | 400 | 4 |
| 56 | alternate | v55 | decisive loss: Rebel victory: cities controlled | 7 | 8 | 7 | 9 | 2 (0) | 23% | 13 / 9 | 675 | 2 |
| 57 | standard | v56 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 11 | 3 | 1 (0) | 23% | 13 / 6 | 1178 | 4 |
| 58 | alternate | v57 | decisive loss: Rebel victory: cities controlled | 10 | 21 | 26 | 0 | 0 (0) | - | 10 / 8 | 340 | 7 |
| 59 | standard | v58 | decisive loss: Rebel victory: cities controlled | 10 | 10 | 11 | 4 | 2 (0) | 32% | 13 / 7 | 291 | 14 |
| 60 | alternate | v59 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 9 | 7 | 1 (0) | 42% | 12 / 8 | 1358 | 4 |
| 61 | standard | v60 | decisive loss: Rebel victory: share of total income | 11 | 6 | 21 | 8 | 5 (1) | 49% | 12 / 7 | 273 | 9 |
| 62 | alternate | v61 | decisive loss: Rebel victory: cities controlled | 6 | 13 | 16 | 8 | 3 (1) | 48% | 11 / 9 | 371 | 6 |
| 63 | standard | v62 | decisive loss: Rebel victory: capital captured | 10 | 13 | 23 | 7 | 3 (1) | 41% | 14 / 11 | 291 | 5 |
| 64 | alternate | v63 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 21 | 7 | 0 (0) | - | 13 / 9 | 1043 | 1 |
| 65 | standard | v64 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 4 | 8 | 2 (0) | 45% | 13 / 6 | 374 | 1 |
| 66 | alternate | v65 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 9 | 7 | 1 (0) | 37% | 12 / 9 | 334 | 8 |
| 67 | standard | v66 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 10 | 8 | 4 (0) | 35% | 13 / 5 | 238 | 3 |
| 68 | alternate | v67 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 3 | 10 | 2 (0) | 32% | 13 / 9 | 853 | 2 |
| 69 | standard | v68 | decisive loss: Rebel victory: capital captured | 6 | 0 | 7 | 9 | 3 (0) | 28% | 13 / 11 | 280 | 7 |
| 70 | alternate | v69 | decisive loss: Rebel victory: cities controlled | 5 | 9 | 0 | 7 | 2 (0) | 22% | 11 / 8 | 342 | 4 |
| 71 | standard | v70 | decisive loss: Rebel victory: cities controlled | 8 | 2 | 21 | 3 | 1 (0) | 40% | 13 / 6 | 547 | 3 |
| 72 | alternate | v71 | decisive loss: Rebel victory: cities controlled | 6 | 9 | 6 | 6 | 1 (0) | 33% | 11 / 8 | 1039 | 5 |
| 73 | standard | v72 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 4 | 5 | 1 (0) | 27% | 13 / 6 | 260 | 3 |
| 74 | alternate | v73 | decisive loss: Rebel victory: cities controlled | 6 | 6 | 0 | 13 | 5 (4) | 57% | 11 / 11 | 718 | 5 |
| 75 | standard | v74 | decisive loss: Rebel victory: cities controlled | 7 | 2 | 12 | 8 | 3 (1) | 31% | 13 / 5 | 210 | 4 |
| 76 | alternate | v75 | decisive loss: Rebel victory: cities controlled | 6 | 2 | 0 | 9 | 3 (2) | 58% | 10 / 9 | 1229 | 0 |
| 77 | standard | v76 | decisive loss: Rebel victory: cities controlled | 12 | 4 | 7 | 11 | 3 (1) | 31% | 13 / 6 | 738 | 9 |
| 78 | alternate | v77 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 10 | 0 (0) | - | 13 / 8 | 983 | 0 |
| 79 | standard | v78 | decisive loss: Rebel victory: cities controlled | 7 | 7 | 14 | 4 | 1 (0) | 57% | 13 / 7 | 693 | 10 |
| 80 | alternate | v79 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 12 | 7 | 0 (0) | - | 13 / 10 | 1227 | 5 |
| 81 | standard | v80 | decisive loss: Rebel victory: cities controlled | 6 | 4 | 12 | 6 | 1 (0) | 33% | 13 / 6 | 496 | 6 |
| 82 | alternate | v81 | decisive loss: Rebel victory: cities controlled | 4 | 3 | 8 | 4 | 0 (0) | - | 12 / 9 | 687 | 0 |
| 83 | standard | v82 | decisive loss: Rebel victory: cities controlled | 6 | 2 | 0 | 8 | 5 (0) | 42% | 13 / 6 | 711 | 0 |
| 84 | alternate | v83 | decisive loss: Rebel victory: share of total income | 5 | 0 | 5 | 12 | 2 (0) | 32% | 14 / 11 | 1463 | 1 |
| 85 | standard | v84 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 5 | 8 | 1 (0) | 37% | 13 / 5 | 288 | 8 |
| 86 | alternate | v85 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 1 | 9 | 2 (0) | 20% | 13 / 9 | 839 | 0 |
| 87 | standard | v86 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 13 | 5 | 1 (0) | 8% | 13 / 6 | 295 | 9 |
| 88 | alternate | v87 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 10 | 6 | 2 (0) | 31% | 11 / 8 | 622 | 3 |
| 89 | standard | v88 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 19 | 3 | 1 (0) | 45% | 13 / 6 | 823 | 8 |
| 90 | alternate | v89 | decisive loss: Rebel victory: cities controlled | 4 | 10 | 14 | 1 | 0 (0) | - | 10 / 9 | 342 | 7 |
| 91 | standard | v90 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 13 | 5 | 1 (0) | 23% | 12 / 5 | 852 | 1 |
| 92 | alternate | v91 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 5 | 8 | 1 (0) | 33% | 12 / 8 | 601 | 1 |
| 93 | standard | v92 | decisive loss: Rebel victory: cities controlled | 9 | 15 | 25 | 5 | 1 (0) | 4% | 14 / 6 | 239 | 8 |
| 94 | alternate | v93 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 14 | 6 | 0 (0) | - | 12 / 8 | 624 | 5 |
| 95 | standard | v94 | decisive loss: Rebel victory: cities controlled | 6 | 0 | 4 | 10 | 2 (0) | 35% | 13 / 4 | 893 | 1 |
| 96 | alternate | v95 | decisive loss: Rebel victory: share of total income | 5 | 0 | 1 | 6 | 2 (0) | 38% | 13 / 9 | 943 | 1 |
| 97 | standard | v96 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 14 | 5 | 0 (0) | - | 13 / 6 | 897 | 2 |
| 98 | alternate | v97 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 2 | 2 | 1 (0) | 37% | 10 / 8 | 754 | 0 |
| 99 | standard | v98 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 14 | 6 | 2 (0) | 34% | 13 / 5 | 1024 | 6 |
| 100 | alternate | v99 | decisive loss: Rebel victory: cities controlled | 8 | 0 | 8 | 10 | 3 (1) | 47% | 11 / 9 | 1159 | 3 |

## How the notebook changed

### Version 1, after game 1 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** The Union failed because it launched uncoordinated attacks into fortified enemy positions without enough force, allowing Confederate commanders like Jackson and Johnston to outmaneuver and isolate our armies. Our forces suffered severe attrition attacking Fort Donelson and Louisville while neglecting supply lines and failing to consolidate numbers, leading to loss of control over key cities and economic collapse.

**Strategy for the next game.** In the next game, we will focus on defensive consolidation, maintaining cash reserves for regular recruitment and timely supply purchases, and building up concentrated forces before launching methodical, overwhelming advances against vulnerable Confederate positions.

**Changes:**

- added: Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings. (Attacking Fort Donelson and Louisville with equal or inferior forces resulted in repeated bloody repulses and lost initiative.)
- added: Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions. (McDowell and other armies ran out of supplies, crippling our defensive capabilities and accelerating our defeat.)
- added: Prioritize recruiting and reinforcing armies rather than premature drilling when facing a mobile and aggressive enemy. (Spending valuable turns drilling while the Rebels actively captured our territory and built up massive forces cost us the game.)
- added: Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives. (Rebel forces freely marched through our territory and captured key cities because our armies were scattered or badly positioned.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies rather than premature drilling when facing a mobile and aggressive enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.

### Version 2, after game 2 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We expanded our forces early but failed to secure key border cities before the enemy struck. When we finally attacked, our armies were beaten by entrenched or superior rebel forces, and our subsequent focus on drilling allowed the Confederates to seize territory and achieve victory by turn 5.

**Strategy for the next game.** We will focus intensely on securing key border junctions and building up our primary armies without reckless attacks, maintaining strict defensive cohesion while denying enemy expansion.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies rather than premature drilling when facing a mobile and aggressive enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.

### Version 3, after game 3 (standard: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** The Confederate forces aggressively bypassed and outmaneuvered our scattered positions while we spent too many turns drilling instead of consolidating, reinforcing, and maintaining supply lines. Armies fell out of supply, and we lost vital northern cities without establishing a strong defensive core.

**Strategy for the next game.** Next game we will focus on keeping our forces concentrated, heavily reinforcing key cities, ensuring all active armies maintain unbroken supply lines, and avoiding excessive drilling while enemy forces threaten our heartland.

**Changes:**

- added: Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies. (Multiple armies fell out of supply during the game due to poor positioning and lack of accessible friendly neighboring cities.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies rather than premature drilling when facing a mobile and aggressive enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.

### Version 4, after game 4 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused too much on static positioning and slow consolidations while the AI moved rapidly across the map, seizing critical cities and encircling our forces. Our armies lacked offensive momentum, and failing to aggressively recruit and expand our footprint early allowed the Confederacy to overwhelm us in city count by turn 4.

**Strategy for the next game.** Next game, we will aggressively recruit forces from available cities on turn one, push out rapidly to secure bordering territory, and maintain constant offensive pressure on enemy-held cities rather than getting bogged down in passive defensive postures and slow concentration.

**Changes:**

- added: Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count and winning via territorial control. (We lost this game purely due to the AI rapidly taking control of cities, leading to a swift defeat on turn 4 before our slow positional strategy could mature.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies rather than premature drilling when facing a mobile and aggressive enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count and winning via territorial control.

### Version 5, after game 5 (standard: Rebel victory: capital captured, 7 turns)

**Diagnosis.** The Confederacy quickly outflanked our northern positions and concentrated overwhelming force against Washington, capturing our capital in early 1862. We repeatedly engaged in costly and inconclusive offensive maneuvers without sufficient force concentration, allowing Rebel armies like Jackson's to wear down our regional defenders and bypass our lines while our funds and supply management lagged.

**Strategy for the next game.** In the next game, we will prioritize defensive security around Washington and key rail hubs while aggressively recruiting and reinforcing our starting armies. We will avoid reckless deep thrusts into enemy territory, use rail links to rapidly counter Rebel incursions, and maintain tight supply lines to preserve our combat strength.

**Changes:**

- added: Never leave Washington or core capital approaches thinly defended against mobile enemy corps like Jackson's. (Jackson bypassed our field armies and captured Washington directly while our forces were tangled in peripheral offensives.)
- added: Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit. (The Rebels effectively used rail transfers to concentrate force and outmaneuver us while our armies marched slowly.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies rather than premature drilling when facing a mobile and aggressive enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count and winning via territorial control.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps like Jackson's.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.

### Version 6, after game 6 (alternate: Rebel victory: capital captured, 6 turns)

**Diagnosis.** We focused too heavily on drilling early in the game rather than expanding and consolidating our army strength. This allowed Confederate mobile forces like Jackson to bypass our lines, capture peripheral cities, and eventually sneak around to capture Washington undefended while our main forces were occupied elsewhere.

**Strategy for the next game.** Next game we will maintain a dedicated garrison army at Washington at all times, avoid excessive drilling in the first year, and use our superior industrial capacity to systematically recruit and expand our front-line forces while steadily pushing back Confederate incursions.

**Changes:**

- revised: Never leave Washington or core capital approaches thinly defended against mobile enemy corps like Jackson's. (Jackson bypassed our field armies and slipped into Washington while we were focused on distant offensives, ending the game immediately.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies rather than premature drilling when facing a mobile and aggressive enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count and winning via territorial control.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps like Jackson's.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.

### Version 7, after game 7 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We lost control of the map because Jackson's mobile Confederate corps rapidly bypassed our forward moves to seize Philadelphia and Pittsburg, cutting our supply lines and isolating core areas while we engaged in uncoordinated movements and excessive drilling instead of securing territory.

**Strategy for the next game.** In the next game, we will prioritize tight defensive cordons around core eastern cities, maintain strong field armies without over-drilling, and use proactive rail deployment to counter Rebel incursions before they capture key northern hubs.

**Changes:**

- revised: Never leave Washington or core capital approaches thinly defended against mobile enemy corps like Jackson's. (Jackson exploited our weak eastern defense to sweep through Philadelphia and Pittsburg, costing us the game on city count.)
- revised: Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit. (The AI rapidly utilized rail and mobility to concentrate forces, whereas our regional forces arrived piecemeal or too late.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies rather than premature drilling when facing a mobile and aggressive enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count and winning via territorial control.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps like Jackson's.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.

### Version 8, after game 8 (alternate: Rebel victory: share of total income, 3 turns)

**Diagnosis.** We expanded our army sizes and captured initial objectives, but we failed to adequately defend Washington, allowing J.E.B. Stuart to capture our capital on turn 3. Simultaneously, our offensive strike against Louisville lacked sufficient numerical and leader superiority, leading to a costly defeat that handed the initiative back to the Confederacy.

**Strategy for the next game.** In the next game, we will prioritize securing Washington immediately with a strong garrison to prevent early capital snipes, while methodically building up our economic base and troop strength through consistent recruitment before launching any major offensive operations.

**Changes:**

- revised: Never leave Washington or core capital approaches thinly defended against mobile enemy corps like Jackson's or Stuart's. (Updated from just Jackson to include Stuart, as J.E.B. Stuart successfully snuck in and captured our capital from Manassas in August 1861.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies rather than premature drilling when facing a mobile and aggressive enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count and winning via territorial control.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps like Jackson's or Stuart's.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.

### Version 9, after game 9 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We failed to protect our core border cities and supply lines, leading to an erosion of our income and territorial control. Jackson and A.S. Johnston exploited our uncoordinated movements and attacks against well-positioned enemy forces, while supply issues crippled our armies in the winter months.

**Strategy for the next game.** Next game, we will focus intensely on defensive consolidation, keeping our main armies supplied and concentrated near rail hubs, and avoiding reckless unsupported attacks against enemy-held cities until our force strength and supply networks are secure.

**Changes:**

- added: Keep primary armies supplied proactively during late autumn to prevent winter attrition and collapse. (In this game, our armies ran out of supplies during the critical winter phase, causing catastrophic combat penalties and inability to hold key positions like Louisville.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies rather than premature drilling when facing a mobile and aggressive enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count and winning via territorial control.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps like Jackson's or Stuart's.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Keep primary armies supplied proactively during late autumn to prevent winter attrition and collapse.

### Version 10, after game 10 (alternate: Rebel victory: share of total income, 6 turns)

**Diagnosis.** We failed to aggressively recruit and replace losses, allowing our total troop strength to dwindle while the Confederacy maintained pressure and out-maneuvered us. Our uncoordinated attacks on fortified positions like Nashville resulted in heavy losses, and we neglected naval defense, letting the enemy fleet neutralize Philadelphia and drain our income.

**Strategy for the next game.** Next game, we will aggressively use the recruit and reinforcement commands to build a massive numerical advantage, maintain a defensive naval fleet to protect our ports, and avoid reckless attacks on enemy strongpoints until our forces are fully concentrated and supported.

**Changes:**

- revised: Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy. (Our previous focus on avoiding premature drilling was good, but we completely stopped recruiting, leading to a steady decline in total troops from 39k down to 28k.)
- added: Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income. (The enemy fleet freely sailed to Philadelphia, blockaded us, and turned the city neutral, ruining our income and contributing to the defeat.)
- dropped: Keep primary armies supplied proactively during late autumn to prevent winter attrition and collapse. (Covered adequately by the broader general supply rule (lesson 2).)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.

### Version 11, after game 11 (standard: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** We focused excessively on drilling and maintaining static defense while neglecting aggressive expansion, city capture, and prompt troop reinforcement. The Confederates easily out-expanded us in city counts, out-maneuvered us with rail transport, and ultimately overwhelmed our isolated positions.

**Strategy for the next game.** Next game, we will aggressively recruit in major cities from turn one, actively push to capture neutral and enemy border cities, use rail transit to respond swiftly to enemy threats, and avoid getting bogged down in endless drilling while the enemy captures the map.

**Changes:**

- revised: Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count. (We lost this game primarily because we let the Confederacy capture over 30 cities while we remained passive.)
- revised: Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy. (Our army size dwindled over time while Rebel forces snowballed through continuous recruitment and combination.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.

### Version 12, after game 12 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused too much on drilling and passive defense while failing to recruit new armies or aggressively contest the enemy's city expansion. Our small, stagnant forces were systematically outflanked and crushed by Confederate mobile columns.

**Strategy for the next game.** We will actively recruit new troops in major cities, expand our territorial footprint by capturing neutral and enemy border towns, and use our rail network to concentrate forces against vulnerable Confederate positions while maintaining capital defense.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.

### Version 13, after game 13 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We once again fell into the trap of letting our main armies run out of supplies while over-drilling and failing to recruit fresh troops. Although we won early naval skirmishes, our armies in the west and center became isolated, suffered catastrophic supply losses, and were slowly picked apart by concentrated Confederate forces.

**Strategy for the next game.** Next game, we will strictly manage army supply lines, purchase supplies proactively when levels dip, and actively recruit new forces to replace losses rather than endlessly drilling under-strength armies.

**Changes:**

- added: Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes. (In this game, multiple armies (McDowell, McClellan) went out of supplies during critical periods and suffered severe combat penalties and attrition because we relied solely on waiting instead of buying supplies.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.

### Version 14, after game 14 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** This game was lost because we failed to aggressively capture neutral and enemy cities, focusing too much on drilling while the Confederacy rapidly expanded its city count and reached the 28-city threshold to trigger a technical victory on turn 4.

**Strategy for the next game.** In the next game, we will immediately pivot from passive drilling to actively moving our armies to capture neutral and enemy cities every turn, ensuring the Confederacy cannot reach the 28-city threshold while maintaining a defensive posture around our core cities.

**Changes:**

- added: Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold. (We lost this game quickly because the Confederacy quietly captured enough cities to trigger the alternate map victory condition while we spent turns drilling.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 15, after game 15 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We lost control of the map and eventually the game because we expanded our forces too thinly into the west without reinforcing or properly supplying them, leading to attrition and defeat in detail by concentrated Rebel armies. Furthermore, we neglected to recruit new forces to replace losses, causing our total manpower and city count to steadily decline.

**Strategy for the next game.** In the next game, we will focus on keeping our core armies concentrated near major supply and rail hubs, aggressively reinforce our ranks with new recruits, and avoid overextending into isolated western pockets without adequate logistical backing.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 16, after game 16 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused heavily on drilling and recruiting in the rear while the Confederate computer aggressively captured our key border and northern cities (St. Louis, Indianapolis, Louisville, Paducah). Our passive stance and lack of offensive pushes allowed the enemy to easily surpass the 28-city threshold for victory by turn 5.

**Strategy for the next game.** Next game, we will immediately pivot from passive drilling to aggressive territorial expansion and defense of border cities. We will capture neutral cities on turn 1, use our armies to actively block and counterattack Confederate advances into our territory, and contest every city to prevent an early enemy city-control victory.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 17, after game 17 (standard: Rebel victory: capital captured, 4 turns)

**Diagnosis.** We focused too much on drill and unsupported offensive marches into fortified or superior enemy positions while neglecting regular recruiting and capital defense. Jackson bypassed our forces to seize Washington directly in September 1861, ending the game.

**Strategy for the next game.** We will maintain a dedicated garrison at Washington, avoid premature attacks against defended cities, and use our resources to steadily recruit and reinforce our forces while securing neutral territory.

**Changes:**

- revised: Never leave Washington or core capital approaches thinly defended against mobile enemy corps. (Jackson marched straight into Washington in September 1861 because we lacked a defensive garrison there.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 18, after game 18 (alternate: Rebel victory: cities controlled, 3 turns)

**Diagnosis.** The game was lost early because enemy mobile corps easily bypassed our border forces and captured Washington, D.C. in August 1861 while our main forces were too passive or far away. We failed to defend our core capital and neglected active territorial expansion.

**Strategy for the next game.** Next game, we will immediately protect Washington with a strong garrison, maintain aggressive expansion into neutral and enemy cities, and use rail links to rapidly counter any Confederate incursions toward our capital.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 19, after game 19 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** The Confederate forces outmatched our scattered armies and systematically conquered key cities while our forces failed to concentrate or adequately recruit. We lost control of the map due to superior Rebel corps concentrations, leading to a swift defeat by March 1862.

**Strategy for the next game.** Next game, we will focus on concentrating our starting forces into robust armies, actively recruiting to match Confederate strength, and defending our core territory while systematically contesting key border cities to prevent the enemy from securing a quick city-control victory.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 20, after game 20 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** The Confederate forces aggressively pushed into the western and central border territories, isolating and defeating our frontier armies in detail. Meanwhile, our offensive attempts lacked sufficient concentration and allowed the enemy to counterattack, seize high-income cities, and trigger a swift city-control victory.

**Strategy for the next game.** Next game we will maintain tighter concentration of our forces along the western and central borders, avoiding premature advances into enemy strongpoints, while steadily reinforcing our armies and contesting every nearby neutral or enemy-held city to prevent a rapid Confederate land-grab.

**Changes:**

- revised: Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives. (Border security failed in the west as Confederate forces easily outmaneuvered and destroyed our isolated detachments.)
- revised: Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count. (The enemy rapidly accumulated cities to achieve a quick city-control victory threshold within four turns.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 21, after game 21 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We lost control of the map and suffered severe supply failures because our active armies moved away from friendly lines and supply hubs without adequate support or supply lines. Furthermore, we neglected regular recruitment and reinforcement, allowing the enemy to outnumber and overwhelm our standing forces while we stalled in prolonged, inconclusive combat.

**Strategy for the next game.** We will focus heavily on maintaining secure supply lines for all moving forces, keeping our armies close to rail connections, and actively reinforcing our strength while systematically expanding our city control to block Confederate victory thresholds.

**Changes:**

- revised: Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies. (Our armies repeatedly ran out of supplies due to advancing too far from friendly cities without proper supply chains.)
- revised: Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count. (We lost too many cities to Confederate expansion while our forces were bogged down or out of supply.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive againstelsch the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 22, after game 22 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** The Confederate forces exploited our weak western deployments early on, driving through Springfield and Indianapolis while our armies remained fragmented and insufficiently reinforced. Although our tactical defense at Fort Donelson and Louisville held against enemy assaults, the Rebels outpaced us in city acquisition and strategic positioning, triggering a rapid city-control victory.

**Strategy for the next game.** We will focus heavily on bolstering our western frontier early, reinforcing our key armies to prevent Confederate breakthroughs, and aggressively contesting neutral and high-income cities to deny the enemy the city-control threshold.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 23, after game 23 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We failed to aggressively recruit and replace our losses, allowing the Confederate armies to outnumber and crush our small forces one by one while capturing all key cities. Our lack of active expansion and failure to protect our supply lines led to severe attrition and defeat.

**Strategy for the next game.** Next game, we will aggressively recruit new forces each turn to maintain numerical parity, protect our supply lines vigilantly, and use our rail network to rapidly counter Rebel advances while contesting every city.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 24, after game 24 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** The game was lost because we repeatedly launched unsupported attacks against superior rebel forces without sufficient concentration, allowing Johnston and Pemberton to defeat our armies in detail while we neglected basic recruitment and supply lines.

**Strategy for the next game.** Next game, we will focus heavily on economic consolidation, maintaining robust recruitment in key industrial cities, keeping our armies concentrated and supplied, and avoiding reckless offensives until we achieve a decisive numerical advantage.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against the enemy.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 25, after game 25 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We focused too heavily on continuous drilling while our armies ran out of supply and lost key cities. Failing to maintain open supply lines to active field armies resulted in severe combat penalties and supply decay, while Rebel forces aggressively captured neutral and Union cities to reach the victory threshold.

**Strategy for the next game.** We will maintain strict vigilance over army supply lines, ensuring that every active field army is supplied before winter attrition and combat penalties occur. We will aggressively contest and capture neutral and enemy cities to prevent the Confederacy from securing the city control victory condition, while balancing our recruitment and defensive positioning around core territories.

**Changes:**

- revised: Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes. (We failed to keep our armies supplied because we neglected the supply command or mistimed it when units ran dry.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against income and enemy growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 26, after game 26 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** The Confederate forces outmaneuvered us on the alternate map by aggressively pushing through the western and northern sectors while we wasted turns drilling and failing to secure key cities. We lost control of the city count threshold rapidly as enemy columns encircled and overran our isolated outposts.

**Strategy for the next game.** We will immediately focus on rapid territorial expansion and aggressive capture of neutral and enemy border cities on the alternate map, halting excessive drilling to ensure we maintain numerical and city-count parity against the Confederate computer from turn one.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against income and enemy growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 27, after game 27 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We failed to protect our border cities and lost too many key locations early to Rebel incursions. Our armies repeatedly failed to break Confederate defenses in Cincinnati because we attacked without sufficient numerical superiority, and we neglected to recruit new forces to replace losses while the enemy expanded unchecked.

**Strategy for the next game.** Next game, we will focus on securing key border junctions immediately, protecting our income base, and avoiding costly attrition attacks against entrenched enemy forces. We will maintain strong defensive positions around core cities while building up sufficient force concentrations before launching deliberate, overwhelming offensives.

**Changes:**

- revised: Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives. (We failed to stop early Rebel advances into Kentucky and Ohio, allowing them to dictate the operational tempo.)
- revised: Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings. (Repeated failed attacks on A.S. Johnston in Cincinnati bled our armies dry without dislodging the enemy.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against income and enemy growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 28, after game 28 (alternate: Rebel victory: share of total income, 3 turns)

**Diagnosis.** We failed to protect Washington and our core territory while attempting uncoordinated advances. A.S. Johnston rampaged through the west crushing isolated forces, and J.E.B. Stuart easily seized our capital, ending the game in defeat on turn 3.

**Strategy for the next game.** We will maintain a strong defensive garrison around Washington to prevent rapid capital raids, keep our field armies concentrated to deter enemy spearheads, and systematically secure border cities before undertaking major operations.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against income and enemy growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 29, after game 29 (standard: Rebel victory: capital captured, 5 turns)

**Diagnosis.** We lost this game because our main armies remained idle or engaged in ill-advised attacks against enemy forces while Jackson flanked us through Harper's Ferry and captured Washington. We also failed to recruit any new troops to replace losses, and let the Confederates overrun our Midwestern and border cities unchecked.

**Strategy for the next game.** Next game we will maintain a strong defending force near Washington at all times to prevent early decapitation strikes, aggressively recruit to build up our numbers, and use our superior initial funds to secure our borders while avoiding costly premature attacks on enemy concentrations.

**Changes:**

- revised: Never leave Washington or core capital approaches thinly defended against mobile enemy corps. (J.E. Johnston and Jackson bypassed our forward forces and captured Washington directly because we failed to leave a defensive garrison in the capital.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against income and enemy growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 30, after game 30 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused too much on isolated offensive maneuvers and failed to recruit new armies while the AI massively outgrew us in manpower and city control. Our attacks on fortified or superior enemy forces failed, leading to attrition and a swift defeat.

**Strategy for the next game.** We will focus heavily on recruiting new armies to match Confederate manpower growth, secure our border cities compactly, avoid reckless attacks on enemy strongpoints, and systematically expand our economic base.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Prioritize recruiting and reinforcing armies regularly to keep our total manpower competitive against income and enemy growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income.
10. Actively purchase supply using the supply command for any army at supply level 1 or lower before winter attrition strikes.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 31, after game 31 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We lost control of the map and eventually the game because we never recruited any new troops to replace losses or expand our forces, resulting in our manpower dropping while the Rebel army grew massively. We also failed to maintain active supply lines for McDowell and McClellan, causing chronic out-of-supply conditions. Furthermore, spending so much cash and turns on building and losing wooden ships in Philadelphia early on drained resources better spent on ground forces.

**Strategy for the next game.** In the next game, we will completely stop wasting turns and money on early wooden fleets and instead focus on aggressive recruitment and reinforcement to match the Rebel force pool. We will maintain supply connectivity for all active corps, avoid over-drilling while our army count dwindles, and contest every critical border city to prevent the AI from achieving the city-control victory threshold.

**Changes:**

- revised: Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth. (Previous games showed zero recruitment leading to attrition defeat; we must actively raise new armies and reinforce existing ones.)
- dropped: Maintain at least a small active naval presence or build ironclads to contest enemy fleet bombardments and protect coastal income. (Early wooden ship investments were repeatedly destroyed and wasted cash that was desperately needed for army recruitment.)
- added: Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets. (Building wooden fleets in early turns resulted in immediate naval disaster and economic drain; funds must go to the land war.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with available forces to prevent the enemy from winning via the city control threshold.

### Version 32, after game 32 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused heavily on recruiting and drilling large armies while remaining completely passive on the strategic map. This allowed the computer to capture neutral and high-income cities unhindered, steadily accumulating the 28 cities required for a threshold victory despite our numerical superiority.

**Strategy for the next game.** We will transition from a purely passive drill-and-defend posture to active, aggressive campaigning. While continuing robust recruitment and supply management, we will immediately march our growing forces to seize neutral and border cities to deny the Confederacy the 28-city threshold, while using concentrated armies to counter-attack enemy spearheads.

**Changes:**

- revised: Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold. (We lost via city threshold while sitting entirely on defense and drilling, failing to claim available neutral cities.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.

### Version 33, after game 33 (standard: Rebel victory: capital captured, 7 turns)

**Diagnosis.** We focused too much on drilling and holding static positions while Rebel forces bypassed us, captured neutral and vital border cities, and eventually slipped through to capture Washington via unguarded flanks. We failed to actively expand our army footprint or contest key enemy movements.

**Strategy for the next game.** Next game we will aggressively recruit to build up our active field armies, maintain a strong protective garrison at Washington at all times, and use our marching forces to capture neutral and enemy border cities rather than idling and drilling while the Rebels maneuver around us.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.

### Version 34, after game 34 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused heavily on drilling and static positioning while the Confederate forces actively maneuvered, captured high-income cities, and crushed our isolated armies one by one. Our lack of aggressive expansion and failure to protect core territories allowed the enemy to surpass the city control threshold for a swift victory.

**Strategy for the next game.** Next game, we will aggressively recruit in major cities, immediately contest and capture neutral and enemy border territories, and avoid wasting turns on excessive drilling while the enemy captures the map.

**Changes:**

- revised: Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count. (We lost this game purely because we passively drilled while the enemy steadily captured cities until reaching the victory threshold.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.

### Version 35, after game 35 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused heavily on recruitment and drilling but lost control of key border cities because our armies were too passive or failed to maintain supply lines. Meanwhile, the Rebel fleet blockaded Philadelphia unhindered, draining our forces while Confederate armies steadily captured cities and achieved the control threshold.

**Strategy for the next game.** We will aggressively contest central border cities early, maintain robust supply lines for all active advancing corps, build ironclads to counter Confederate naval dominance, and keep recruitment steady in major cities to prevent the enemy from winning via the city control threshold.

**Changes:**

- revised: Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets. (Wooden fleets kept getting sunk or blockaded by enemy naval actions without achieving meaningful strategic impact.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.

### Version 36, after game 36 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** The game was lost quickly because we failed to contest the Rebel advance in the West, allowing A.S. Johnston to capture St. Louis, Springfield, and Indianapolis unopposed or with weak defensive forces, while we spent crucial turns drilling instead of expanding our military footprint and contesting territory.

**Strategy for the next game.** We will aggressively recruit and concentrate our forces to counter Confederate incursions in the Western theater early, preventing them from seizing key cities while aggressively capturing neutral territory to maintain income and city thresholds.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.

### Version 37, after game 37 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We failed to protect our core border cities and lost too many territories early, allowing the Confederacy to overrun our interior, sever our supply lines, and claim victory via city control thresholds. Excessive drilling while losing territory cost us critical map control.

**Strategy for the next game.** Next game, we will immediately prioritize aggressive securing and defending of border cities, utilize the recruit command actively to offset Rebel manpower growth, and avoid getting bogged down in endless drilling while losing our territorial base.

**Changes:**

- revised: Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count. (We focused too much on drilling and passive defense while the Rebels swallowed up cities and won on territory control.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.

### Version 38, after game 38 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We failed because we repeatedly engaged in uncoordinated piecemeal attacks against stronger Rebel forces, suffered tactical defeats in St. Louis and Columbus, and allowed the enemy to dominate the map and city count while we spent precious turns drilling instead of actively contesting territory or recruiting.

**Strategy for the next game.** Next game we will aggressively recruit to build up our army sizes, avoid passive drilling when territory is being lost, keep our forces concentrated, and systematically capture neutral and enemy cities to deny the Confederacy their victory threshold while securing our borders.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.

### Version 39, after game 39 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We lost control of critical cities and suffered severe supply and naval attrition. Our armies repeatedly attacked into unfavorable odds or became isolated without supply lines, while the Rebels captured city after city to reach the threshold.

**Strategy for the next game.** We will focus on maintaining solid supply lines for all active armies, reinforcing our core regions, and systematically expanding our city control while avoiding reckless attacks on enemy strongpoints.

**Changes:**

- revised: Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings. (Uncoordinated attacks against strong enemy positions repeatedly drained our forces and cost us key battles.)
- revised: Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions. (Armies running out of supplies became completely ineffective and vulnerable to destruction.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.

### Version 40, after game 40 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** The Confederacy quickly outmaneuvered us on the alternate map, seizing critical cities and threatening our core while our armies remained passive and spent turns drilling. Despite positive cash flow and winning minor naval skirmishes, our lack of aggressive city capture and reinforcement allowed the Rebels to reach the city control threshold for victory.

**Strategy for the next game.** Next game, we will immediately pivot from excessive drilling to aggressively recruiting, reinforcing, and capturing empty or neutral border cities to contest the Rebel city count and protect our core territories from being overrun.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.

### Version 41, after game 41 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** Our armies repeatedly attacked fortified positions or high-rating Rebel commanders without adequate strength, leading to massive attrition. Meanwhile, we neglected to recruit and replace losses, allowing the Confederates to outnumber us and capture cities freely while our armies ran out of supplies.

**Strategy for the next game.** We will focus heavily on maintaining strong defensive lines, keeping our armies fully supplied, and regularly using the recruit command to build up our manpower superiority before attempting any coordinated counter-offensives.

**Changes:**

- revised: Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth. (We failed to recruit in this game, causing our troop count to dwindle while Rebels reinforced unchecked.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.

### Version 42, after game 42 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** The Rebel forces quickly concentrated superior mobile armies, exploiting our scattered advances and crushing isolated forces at St. Louis, Louisville, and Cincinnati. Our armies lacked the mass and leader ratings to contest them, leading to a collapse of our border cities and an inevitable defeat by city control.

**Strategy for the next game.** We will concentrate our initial forces to secure key border cities, aggressively recruit to build up our manpower and match Rebel strength, avoid overextended movements, and keep our armies supplied and concentrated for coordinated defense and counter-attacks.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.

### Version 43, after game 43 (standard: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We failed to protect our rear and core cities from mobile Rebel thrusts, and lost key midwestern hubs like Indianapolis and Columbus while our forces were bottlenecked or reacting too slowly. Jackson and A.S. Johnston systematically outmanoeuvred us and cut our supply routes.

**Strategy for the next game.** We will maintain our comprehensive strategic framework, focusing on solidifying core supply networks, defending Washington and key industrial hubs, and aggressively responding to Rebel flanking movements with well-timed rail and field deployments.

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Focus our production economy entirely on ground recruitment, reinforcements, and vital ironclads rather than early fragile wooden fleets.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.

### Version 44, after game 44 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused too heavily on drilling and static defense while failing to actively recruit new troops or build ironclads to break the enemy naval blockade on Philadelphia. Consequently, our manpower stagnated, our blocked army starved, and the Rebels steadily captured cities to win on the city control threshold.

**Strategy for the next game.** We will actively recruit troops to grow our army size, build ironclads early to secure our seaports and lift blockades, and aggressively contest neutral and enemy cities to prevent a Rebel city-control victory.

**Changes:**

- revised: Build ironclads promptly when available to counter enemy fleets, break blockades, and protect our seaports. (Our wooden fleet was easily crushed by Rebel naval concentration, leaving Philadelphia blockaded and causing attrition.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect our seaports.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.

### Version 45, after game 45 (standard: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused almost exclusively on drilling our standing armies while neglecting recruitment and aggressive expansion, allowing the Confederacy to seize cities, grow unchecked, and outmaneuver us. Without active reinforcement and strategic counter-offensives, our territory steadily shrank until we lost on city control.

**Strategy for the next game.** We will shift from passive drilling to active recruitment, aggressive city capture, and timely counter-attacks to deny the Rebels territorial dominance while protecting our core supply lines.

**Changes:**

- added: Actively recruit and merge forces in key hubs every few turns to maintain offensive strength rather than relying solely on endless drilling. (Continuous drilling across all turns did nothing to stop the loss of cities and territory; we must build and maintain army sizes to project power.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect our seaports.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.
12. Actively recruit and merge forces in key hubs every few turns to maintain offensive strength rather than relying solely on endless drilling.

### Version 46, after game 46 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** The Confederacy achieved a rapid victory via city control thresholds while our forces remained passive in the East and failed to expand our economic base or contest key neutral cities. Although our tactical defenses held in the West, we neglected recruitment and aggressive expansion, allowing the enemy to capture nearly all surrounding territories.

**Strategy for the next game.** Next game we will aggressively recruit new armies on turn one, push out rapidly to claim neutral and high-income cities to block Confederate expansion, and maintain active patrols to prevent the AI from winning on city control.

**Changes:**

- revised: Actively recruit and deploy new armies in available cities during early turns to secure vital territory before the enemy engulfs the map. (We lost this game solely because we failed to build up our forces and contest empty cities, letting the enemy overwhelm our city count.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect our seaports.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.
12. Actively recruit and deploy new armies in available cities during early turns to secure vital territory before the enemy engulfs the map.

### Version 47, after game 47 (standard: Rebel victory: capital captured, 5 turns)

**Diagnosis.** We focused too much on drilling and standing still while the Confederate forces actively maneuvered, reinforced, and attacked our poorly defended rear. Specifically, leaving Washington with minimal defense allowed a Rebel army to march in and capture our capital on turn 5, ending the game immediately.

**Strategy for the next game.** We will keep a substantial defensive force stationed directly in Washington to block any Rebel incursions, while using our remaining armies to contest key border cities and maintain active offensive and recruiting pressure rather than endlessly drilling in place.

**Changes:**

- added: Maintain a strong defensive garrison inside Washington at all times to deter enemy raiding forces and prevent instant defeat via capital loss. (We lost the game in November 1861 because a Rebel army walked into an undefended Washington and captured our capital.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect our seaports.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.
12. Maintain a strong defensive garrison inside Washington at all times to deter enemy raiding forces and prevent instant defeat via capital loss.

### Version 48, after game 48 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused too heavily on drilling our small starting armies while the Rebel computer aggressively captured neutral and border cities, rapidly accumulating the city count and income needed for a technical victory. Our lack of active expansion and troop recruitment left us bottled up and overwhelmed by enemy maneuvers.

**Strategy for the next game.** Next game we will aggressively recruit new forces using our treasury reserves and immediately march to claim neutral and border cities rather than wasting turns drilling. We will keep our main armies moving to contest Rebel expansion while maintaining a solid defense around our capital.

**Changes:**

- added: Avoid excessive idle drilling when the enemy is rapidly seizing territory; aggressive expansion and city capture take absolute priority. (In past games, excessive drilling left us with small armies while the enemy easily won the city count race.)

**Notebook:**

1. Never attack fortified enemy cities or armies without overwhelming numerical superiority and high leader ratings.
2. Always maintain supply lines to every active army to avoid devastating combat penalties and troop desertions.
3. Regularly use the recruit command in friendly cities to expand our total manpower and keep pace with Rebel growth.
4. Secure our immediate strategic borders and neutralize advancing enemy spearheads before attempting deep offensives.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent them from becoming isolated and running out of supplies.
6. Actively capture and contest high-income and strategic cities every turn to prevent the enemy from dominating the city count.
7. Never leave Washington or core capital approaches thinly defended against mobile enemy corps.
8. Use rail transport proactively to reposition large forces to threatened border cities before enemy attacks hit.
9. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect our seaports.
10. Monitor army supply levels carefully and avoid movements that cut armies off from friendly neighboring supply cities.
11. Prioritize capturing empty or neutral cities immediately with active marching forces to prevent the enemy from winning via the city control threshold.
12. Avoid excessive idle drilling when the enemy is rapidly seizing territory; aggressive expansion and city capture take absolute priority.

### Version 49, after game 49 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We lost due to severe supply starvation in core armies (McDowell and McClellan), repeated failed frontal attacks into fortified/unfavorable terrain against A.S. Johnston in Cincinnati, and failure to recruit or expand our manpower base while the Confederacy steadily captured cities and built up massive forces.

**Strategy for the next game.** Next game, we will actively recruit troops to expand our forces, maintain strict vigilance over army supply lines to prevent starvation, avoid costly uncoordinated attacks on fortified enemy positions, and aggressively contest neutral and enemy cities to halt the Confederate city-control victory.

**Changes:**

- revised: Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority. (Repeated attacks into Cincinnati failed due to unfavorable combat odds against A.S. Johnston.)
- revised: Never leave armies idle without supply or reinforcement when strategic cities are falling to the enemy. (Armies like McDowell ran out of supply and sat idle while the Confederacy took city after city.)
- added: Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth. (We failed to recruit any new troops throughout the entire game while the Rebels grew massively in strength.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Protect Washington and core capital approaches against mobile enemy corps and cavalry spearheads.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Avoid excessive idle drilling when enemy forces are rapidly seizing territory and threatening cities.
12. Never leave armies idle without supply or reinforcement when strategic cities are falling to the enemy.

### Version 50, after game 50 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** Game 50 ended in a rapid Rebel victory by March 1862 because the Confederate forces aggressively captured empty cities and secured territory while our armies spent excessive turns drilling instead of actively moving, capturing, or defending key locations. Despite having ample funds, we failed to sufficiently recruit or contest enemy territorial expansion.

**Strategy for the next game.** In the next game, I will drastically reduce the frequency of drilling, immediately utilize our cash reserves to recruit troops, and actively march our armies to claim neutral and empty border cities before the Confederate forces can dominate the map.

**Changes:**

- revised: Avoid excessive drilling and prioritize capturing territory or intercepting enemy columns over static exercises. (Game 50 showed that spending multiple turns on drilling allowed the Rebels to quietly sweep up neutral and empty cities unchecked, leading to a swift defeat via city control.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Protect Washington and core capital approaches against mobile enemy corps and cavalry spearheads.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Avoid excessive drilling and prioritize capturing territory or intercepting enemy columns over static exercises.
12. Never leave armies idle without supply or reinforcement when strategic cities are falling to the enemy.

### Version 51, after game 51 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We lost control of key cities and suffered a rapid collapse due to poor supply management and repeated uncoordinated local attacks against entrenched enemy forces. While Grant eventually crushed A.S. Johnston in Cincinnati, our western and northern flanks crumbled as Rebel forces captured vital cities like St. Louis, Indianapolis, and Philadelphia while our armies ran out of supplies and remained idle or unsupported.

**Strategy for the next game.** Next game, we will focus heavily on economic expansion and securing neutral border cities early while maintaining strict supply lines for all field armies. We will avoid uncoordinated attacks, keep our main forces concentrated around strategic rail hubs, and aggressively contest enemy city-grabbing moves before the Confederacy achieves a threshold victory.

**Changes:**

- revised: Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority. (Repeated premature assaults on Jackson and Johnston cost us thousands of men and led to repeated retreats.)
- added: Never leave armies idle without supply or reinforcement when strategic cities are falling to the enemy. (Allowing McDowell to go out of supplies while Jackson and Stuart rampaged through the north doomed our defensive network.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Protect Washington and core capital approaches against mobile enemy corps and cavalry spearheads.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Avoid excessive drilling and prioritize capturing territory or intercepting enemy columns over static exercises.
12. Never leave armies idle without supply or reinforcement when strategic cities are falling to the enemy.

### Version 52, after game 52 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We captured initial border cities and fortified key positions, but our offensive push into Paducah failed against Jackson due to inferior combat odds, and enemy columns outmaneuvered us to seize northern cities, giving the Confederacy rapid city dominance.

**Strategy for the next game.** We will continue focusing on securing neutral border cities early, keeping our main armies supplied and concentrated, and avoiding unprofitable attacks on fortified enemy forces while maintaining defensive integrity around core territory.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Protect Washington and core capital approaches against mobile enemy corps and cavalry spearheads.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Avoid excessive drilling and prioritize capturing territory or intercepting enemy columns over static exercises.
12. Never leave armies idle without supply or reinforcement when strategic cities are falling to the enemy.

### Version 53, after game 53 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** The Confederacy quickly seized the initiative in the West, outmaneuvered our forces, and captured critical cities while we struggled with logistics and uncoordinated movements. Although McClellan successfully pushed to Nashville, our lack of secure supply lines, failure to properly consolidate or fortify key gains, and continuous losses in secondary sectors allowed the Rebels to reclaim territory and cross the city-control threshold for victory.

**Strategy for the next game.** Next game, we will focus aggressively on maintaining solid supply chains for all advancing columns, securing our economic base by capturing and holding neutral border cities early, and using rail lines efficiently to reinforce threatened sectors before enemy breakthroughs occur. We will keep our main armies concentrated to defeat Confederate forces in detail.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Protect Washington and core capital approaches against mobile enemy corps and cavalry spearheads.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Avoid excessive drilling and prioritize capturing territory or intercepting enemy columns over static exercises.
12. Never leave armies idle without supply or reinforcement when strategic cities are falling to the enemy.

### Version 54, after game 54 (alternate: Rebel victory: share of total income, 6 turns)

**Diagnosis.** The Rebel army under Bragg slipped past our lines and captured Washington in January 1862 because we left the capital under-defended while concentrating our main offensive forces in the West. We failed to maintain a permanent garrison in Washington.

**Strategy for the next game.** Next game, we will continue aggressive recruitment and neutral city expansion while strictly maintaining a strong permanent garrison army in Washington to block Confederate capital strikes, ensuring we do not lose by sudden coup while advancing in the West.

**Changes:**

- revised: Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids. (We lost the game instantly in January 1862 because Bragg marched unopposed into Washington while our forces were deployed elsewhere.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Avoid excessive drilling and prioritize capturing territory or intercepting enemy columns over static exercises.
12. Never leave armies idle without supply or reinforcement when strategic cities are falling to the enemy.

### Version 55, after game 55 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We repeatedly attacked fortified enemy positions at Cincinnati without sufficient force superiority, leading to heavy casualties and army exhaustion. Meanwhile, our lack of regular recruitment allowed the Rebels to outnumber and overwhelm us across the map.

**Strategy for the next game.** We will aggressively recruit new troops in our major cities every turn to maintain force parity with the Confederacy, secure vital neutral cities early, and avoid costly unsupported attacks on fortified enemy-held points.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Avoid excessive drilling and prioritize capturing territory or intercepting enemy columns over static exercises.
12. Never leave armies idle without supply or reinforcement when strategic cities are falling to the enemy.

### Version 56, after game 56 (alternate: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We successfully eliminated the enemy fleet early on, but concentrated Rebel forces, notably J.E. Johnston and A.S. Johnston, outfought our armies in key border cities like Louisville and Cincinnati. Our counterattacks lacked sufficient local concentration and suffered heavy losses against superior Rebel strength, leading to the loss of critical cities and a rapid Confederate victory.

**Strategy for the next game.** Next game, we will focus on rapidly recruiting large, consolidated armies in our heartland while securing neutral border cities. We will avoid piecemeal attacks against concentrated Confederate forces, build up our rail and naval assets, and maintain strong garrisons in key hubs to block enemy expansion.

**Changes:**

- added: Avoid attacking large enemy field concentrations with isolated forces; consolidate into armies over 30,000 men before engaging main Rebel columns. (Game 56 showed our attacks on Louisville and Cincinnati with smaller forces were easily crushed by concentrated Rebel armies.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Avoid attacking large enemy field concentrations with isolated forces; consolidate into armies over 30,000 men before engaging main Rebel columns.
12. Never leave armies idle without supply or reinforcement when strategic cities are falling to the enemy.

### Version 57, after game 57 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused excessively on drilling small armies while the Rebels aggressively captured key cities and pushed deep into our territory. Our offensive push on Fort Donelson failed because we attacked with an undersized force against fortified defenders, and we neglected recruit commands entirely, allowing the Confederacy to outnumber us significantly in field strength and city control.

**Strategy for the next game.** We will immediately prioritize recruiting and reinforcing our main armies while capturing neutral cities to build up our economic base. We will stop wasting turns on endless drilling, maintain solid defensive garrisons, and mass our forces into large armies before attempting any offensive operations against Rebel positions.

**Changes:**

- revised: Actively recruit and reinforce field armies every turn instead of spending turns exclusively on drilling. (Previous games proved that excessive drilling while ignoring recruitment leads to severe manpower deficits and loss of cities.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Avoid attacking large enemy field concentrations with isolated forces; consolidate into armies over 30,000 men before engaging main Rebel columns.
12. Actively recruit and reinforce field armies every turn instead of spending turns exclusively on drilling.

### Version 58, after game 58 (alternate: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We focused heavily on internal drilling and passive defense while failing to actively capture neutral or enemy cities. Meanwhile, the Confederacy aggressively expanded its territory, seized critical border points, and eventually achieved victory through total city control.

**Strategy for the next game.** Next game we will aggressively push out from our starting position to seize neutral cities early, maintain a steady stream of recruitment, and proactively attack vulnerable enemy-held cities to prevent the Confederacy from securing a territorial victory.

**Changes:**

- revised: Actively advance and capture surrounding neutral and enemy cities instead of hiding behind endless drilling turns. (We lost via city control because we sat passively drilling while the Rebels captured 28 cities.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Avoid attacking large enemy field concentrations with isolated forces; consolidate into armies over 30,000 men before engaging main Rebel columns.
12. Actively advance and capture surrounding neutral and enemy cities instead of hiding behind endless drilling turns.

### Version 59, after game 59 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We failed because our armies continually ran out of supply and were caught in passive drilling cycles instead of capturing and holding cities. The Rebels steadily took our economic base, leading to a loss of city control by turn 10.

**Strategy for the next game.** Next game, we will aggressively expand our city footprint early, keep our advancing columns strictly connected to supply networks to avoid attrition, and avoid wasteful passive drilling turns that let the Confederacy out-expand us.

**Changes:**

- revised: Actively advance and capture surrounding neutral and enemy cities instead of hiding behind endless drilling turns. (Game 58 showed we lost due to city count while our armies sat and drilled without expanding our territory.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Avoid attacking large enemy field concentrations with isolated forces; consolidate into armies over 30,000 men before engaging main Rebel columns.
12. Actively advance and capture surrounding neutral and enemy cities instead of hiding behind endless drilling turns.

### Version 60, after game 60 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused too much on drilling and standing still while the Confederacy aggressively captured cities and built massive armies. Our isolated forces were overwhelmed, and we failed to secure enough territory to contest their city count victory condition.

**Strategy for the next game.** We will aggressively use the recruit command every single turn to rapidly expand our armies, concentrate our forces into powerful columns, and push forward to capture neutral and enemy cities to prevent a Confederate city-count victory.

**Changes:**

- revised: Consolidate forces into large armies over 30,000 men and actively advance to contest every city instead of hiding behind endless drilling. (Previous games proved that excessive drilling leads to decisive defeat by city count while the enemy expands unchecked.)
- added: Recruit heavily every turn in available cities to ensure we outnumber the enemy and hold sufficient territory. (We lost this game because our army size stagnated while Confederate forces swelled to over 80,000 men.)
- dropped: Avoid attacking large enemy field concentrations with isolated forces; consolidate into armies over 30,000 men before engaging main Rebel columns. (Replaced by a broader lesson emphasizing aggressive territorial expansion alongside concentration.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Consolidate forces into large armies over 30,000 men and actively advance to contest every city instead of hiding behind endless drilling.
12. Recruit heavily every turn in available cities to ensure we outnumber the enemy and hold sufficient territory.

### Version 61, after game 61 (standard: Rebel victory: share of total income, 11 turns)

**Diagnosis.** We focused too much on passive drilling and failed to aggressively recruit new forces across our territory. As a result, our armies were slowly worn down through attrition and enemy pressure, leading to the loss of key cities and ultimately our capital.

**Strategy for the next game.** We will aggressively use the recruit command every turn in all available cities, maintain strong garrisons in key locations like Washington to prevent capital loss, and steadily advance our concentrated armies to capture and hold territory.

**Changes:**

- revised: Recruit heavily every turn in available cities to ensure we outnumber the enemy and hold sufficient territory. (We fell behind in manpower during the game because we neglected recruitment in favor of other tasks.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Consolidate forces into large armies over 30,000 men and actively advance to contest every city instead of hiding behind endless drilling.
12. Recruit heavily every turn in available cities to ensure we outnumber the enemy and hold sufficient territory.

### Version 62, after game 62 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused too much on drilling and localized counterattacks rather than aggressive territorial expansion and capturing key enemy cities. While our manpower grew, scattered movements allowed Rebel forces like J.E. Johnston to counter-attack, defeat our isolated armies, and secure the city threshold for victory.

**Strategy for the next game.** We will maintain our disciplined recruitment and concentrated force posture, but we will strictly avoid idle drilling when enemy cities are vulnerable, pushing decisive large-army offensives directly toward enemy-held territory to seize the initiative and prevent Rebel city-control victories.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Consolidate forces into large armies over 30,000 men and actively advance to contest every city instead of hiding behind endless drilling.
12. Recruit heavily every turn in available cities to ensure we outnumber the enemy and hold sufficient territory.

### Version 63, after game 63 (standard: Rebel victory: capital captured, 10 turns)

**Diagnosis.** We focused heavily on drilling rather than offensive operations or securing key territory, leading to stagnant growth while the Rebels built up forces. Crucially, we neglected Washington's defense, allowing Ashby to capture our capital and end the game in defeat.

**Strategy for the next game.** Next game, we will prioritize securing neutral cities early, maintain active offensives with concentrated armies, manage supply lines vigilantly, and permanently station a strong defensive army in Washington to ensure the capital remains secure against enemy raids.

**Changes:**

- added: Never leave Washington undefended; always maintain a substantial garrison army in the capital to deter raids. (We lost the game in September 1862 when Ashby marched unopposed into Washington and captured our capital.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Consolidate forces into large armies over 30,000 men and actively advance to contest every city instead of hiding behind endless drilling.
12. Never leave Washington undefended; always maintain a substantial garrison army in the capital to deter raids.

### Version 64, after game 64 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused too heavily on continuous drilling while neglecting recruitment and aggressive expansion. While our armies gained experience, our troop numbers dwindled and the Rebels systematically captured neutral and our own cities, achieving a city-control victory.

**Strategy for the next game.** In the next game, we will shift away from passive drilling and prioritize regular recruitment in major cities combined with aggressive capture of neutral and enemy border cities to secure economic superiority and prevent a Rebel city-control victory.

**Changes:**

- revised: Actively advance to capture and contest cities instead of stalling our forces with endless drilling. (Continuous drilling across multiple turns failed to translate into battlefield dominance and allowed the enemy to win via superior city control.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Actively advance to capture and contest cities instead of stalling our forces with endless drilling.
12. Never leave Washington undefended; always maintain a substantial garrison army in the capital to deter raids.

### Version 65, after game 65 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We lost control of the map because our armies suffered from continuous supply attrition and failed to adequately reinforce or expand our forces through recruitment, while the Rebel forces steadily captured critical northern cities.

**Strategy for the next game.** We will focus heavily on securing key economic and border cities early, utilizing the recruit command to replenish our manpower, and maintaining active supply lines to prevent our armies from starving or losing combat effectiveness.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Actively advance to capture and contest cities instead of stalling our forces with endless drilling.
12. Never leave Washington undefended; always maintain a substantial garrison army in the capital to deter raids.

### Version 66, after game 66 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused heavily on drilling and static defense while failing to recruit new armies or aggressively contest neutral and enemy cities. The Confederacy rapidly concentrated overwhelming forces, out-expanded our city control, and crushed our isolated garrisons, leading to a swift defeat.

**Strategy for the next game.** We will aggressively recruit new armies every turn in available cities to build a massive numerical advantage, secure neutral cities early for income, and advance coordinated forces to contest Rebel city control while maintaining a strong capital garrison.

**Changes:**

- revised: Actively recruit and mass new combat forces rather than stalling our strategy with endless drilling. (Previous games showed heavy reliance on drilling resulted in stagnant forces and inevitable defeat by city count, while zero recruits left us too weak to hold territory.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Actively recruit and mass new combat forces rather than stalling our strategy with endless drilling.
12. Never leave Washington undefended; always maintain a substantial garrison army in the capital to deter raids.

### Version 67, after game 67 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We lost control of key cities and suffered attrition because our armies lacked sufficient numbers and failed to mount effective coordinated offensives, while the Rebels concentrated superior forces, captured our industrial hubs, and cut our supply lines.

**Strategy for the next game.** We will focus heavily on recruiting fresh troops in available cities, maintaining stable supply lines, securing neutral territory early, and building up our economic and military strength to contest Confederate city control.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Actively recruit and mass new combat forces rather than stalling our strategy with endless drilling.
12. Never leave Washington undefended; always maintain a substantial garrison army in the capital to deter raids.

### Version 68, after game 68 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We failed to recruit any new troops during the entire game, allowing the Rebel forces to steadily outnumber and crush our field armies. Furthermore, our offensive movements lacked adequate concentration, resulting in disjointed attacks that were easily repulsed by Jackson in Louisville.

**Strategy for the next game.** In the next game, we will immediately initiate a regular recruitment program to build up our army sizes, avoid piecemeal attacks, and maintain a solid defensive posture while securing key border cities.

**Changes:**

- revised: Actively recruit and mass new combat forces rather than stalling our strategy with endless drilling. (We failed to recruit any troops (0 recruits) in game 68, which directly led to our military inferiority and defeat after only 5 turns.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Actively recruit and mass new combat forces rather than stalling our strategy with endless drilling.
12. Never leave Washington undefended; always maintain a substantial garrison army in the capital to deter raids.

### Version 69, after game 69 (standard: Rebel victory: capital captured, 6 turns)

**Diagnosis.** We lost quickly because Washington was left with an inadequate garrison, allowing Jackson to attack and capture our capital. Additionally, our armies suffered from continuous supply shortages and failed attacks against fortified Rebel positions like Fort Donelson, while excessive drilling drained our effectiveness.

**Strategy for the next game.** We will maintain a powerful, stationary garrison army permanently stationed in Washington to secure our capital against all raids, while our other field armies methodically capture neutral border cities, maintain strict supply lines without over-drilling, and gradually build up overwhelming force for targeted offensives.

**Changes:**

- revised: Never move the Washington garrison away or leave the capital undefended under any circumstances. (Game 69 showed that moving Fremont out of Washington left the capital completely vulnerable to Jackson's sudden advance, leading to an immediate defeat.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Actively recruit and mass new combat forces rather than stalling our strategy with endless drilling.
12. Never move the Washington garrison away or leave the capital undefended under any circumstances.

### Version 70, after game 70 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We expanded our manpower and built naval forces, but failed to concentrate our armies for decisive operations in the West. While we delayed in Springfield and allowed A.S. Johnston to run rampant, Rebel forces captured critical northern cities, leading to a rapid defeat via city control.

**Strategy for the next game.** We will aggressively recruit in large northern cities, keep Washington fully secured, and quickly concentrate our western forces to defeat A.S. Johnston before he can seize our heartland cities.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Actively recruit and mass new combat forces rather than stalling our strategy with endless drilling.
12. Never move the Washington garrison away or leave the capital undefended under any circumstances.

### Version 71, after game 71 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We lost because our active armies ran out of supply during winter and remained unsupplied for multiple turns, rendering them vulnerable and immobile while Confederate forces steadily captured our cities and achieved the control victory condition.

**Strategy for the next game.** We will maintain our core defensive and supply protocols while aggressively securing neutral cities and ensuring our active field armies never starve of supply, avoiding the crippling supply deficits that cost us the game.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Actively recruit and mass new combat forces rather than stalling our strategy with endless drilling.
12. Never move the Washington garrison away or leave the capital undefended under any circumstances.

### Version 72, after game 72 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused too much on drilling and uncoordinated offensive thrusts into western cities while the Rebels secured the economic core and rapidly out-expanded us in city control. Our isolated armies in the west were picked apart by A.S. Johnston, and we failed to maintain adequate defensive depth or aggressive city-capturing in the center, leading to a quick loss by city majority.

**Strategy for the next game.** We will prioritize aggressive capture of empty and neutral cities to keep pace with the Rebel city count, maintain strong defensive postures around Washington and key hubs, and use our economic advantage to recruit heavily rather than wasting turns drilling.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Build ironclads promptly when available to counter enemy fleets, break blockades, and protect ports.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Actively recruit and mass new combat forces rather than stalling our strategy with endless drilling.
12. Never move the Washington garrison away or leave the capital undefended under any circumstances.

### Version 73, after game 73 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We failed to maintain adequate economic and territorial expansion while squandering funds on excessive naval building instead of ground recruits. The Rebel armies steadily outflanked and crushed our isolated forces, and our failure to secure supply lines left key armies like McDowell and McClellan stranded and vulnerable.

**Strategy for the next game.** We will shift focus heavily towards ground recruitment and maintaining solid supply lines to our advancing forces, avoiding excessive naval spending while securing critical border cities to build a robust economic and military advantage.

**Changes:**

- revised: Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered. (Building ships repeatedly drained our treasury while ground armies were overwhelmed and outnumbered by Rebel forces.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Actively recruit and mass new combat forces rather than stalling our strategy with endless drilling.
12. Never move the Washington garrison away or leave the capital undefended under any circumstances.

### Version 74, after game 74 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We made early aggressive pushes and captured a few western cities, but our inability to continuously recruit fresh manpower and properly secure our rear lines left us outnumbered and overrun by concentrated Confederate offensives in the winter of 1861-1862.

**Strategy for the next game.** We will aggressively recruit new forces every turn possible to out-produce the Confederate armies, maintain a heavily guarded capital, secure high-value neutral cities early, and systematically advance on enemy strongpoints only when we have overwhelming numbers.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Actively recruit and mass new combat forces rather than stalling our strategy with endless drilling.
12. Never move the Washington garrison away or leave the capital undefended under any circumstances.

### Version 75, after game 75 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We focused too much on drilling and peripheral offensive movements instead of aggressive city capture and defense. Our armies ran out of supply in winter, and the Rebels steadily outgrew us in city control and territory, leading to a decisive Rebel victory.

**Strategy for the next game.** We will aggressively expand and capture empty and neutral cities across the map from turn one, prioritize recruitment to keep pace with Rebel manpower, maintain strict supply lines, and keep Washington heavily garrisoned at all times.

**Changes:**

- revised: Actively capture available empty cities and territory every turn rather than wasting time drilling. (Drilling proved to be a waste of valuable turns when we were losing the city control race against the Confederacy.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Actively capture available empty cities and territory every turn rather than wasting time drilling.
12. Never move the Washington garrison away or leave the capital undefended under any circumstances.

### Version 76, after game 76 (alternate: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We pushed west early with Grant and secured some victories, but our naval force was overwhelmed by concentrated Rebel fleets, leading to Philadelphia being blockaded and starved out. Meanwhile, the Confederates captured enough cities on alternate map to win by city threshold while our eastern forces remained static and vulnerable.

**Strategy for the next game.** Focus heavily on ground recruitment and capturing neutral or empty cities to prevent the Confederate city-count victory condition on the alternate map, while avoiding costly naval investments and keeping our western and eastern armies well-supplied and concentrated.

**Changes:**

- revised: Avoid building vulnerable isolated navies that draw blockades and drain resources better spent on ground forces. (Our fleet was crushed and blockaded Philadelphia, causing severe supply and casualty penalties that contributed to our defeat.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Actively capture available empty cities and territory every turn rather than wasting time drilling.
12. Avoid building vulnerable isolated navies that draw blockades and drain resources better spent on ground forces.

### Version 77, after game 77 (standard: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** The Confederacy achieved a technical victory by capturing 32 cities after 12 turns, exploiting our catastrophic supply failures in Washington and the West. Army #1 (McDowell) in Washington remained perpetually out of supply from November 1861 onward, losing combat effectiveness and eventually trapping our forces while Confederate armies relentlessly advanced and captured our vital economic centers.

**Strategy for the next game.** We will aggressively secure neutral border cities early, maintain strict oversight of supply lines to prevent armies from going unsupplied during winter phases, and reinforce our field strength through consistent recruitment while keeping Washington securely garrisoned and supplied.

**Changes:**

- dropped: Avoid building vulnerable isolated navies that draw blockades and drain resources better spent on ground forces. (This lesson was redundant and covered by the broader rule prioritizing ground strength over naval construction.)
- added: Never let any active army run out of supply; buy supply immediately or retreat to a friendly seaport/supply hub before November and January turns. (We repeatedly suffered crippling supply failures in Washington and field armies during winter phases, rendering forces like McDowell completely helpless.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Actively capture available empty cities and territory every turn rather than wasting time drilling.
12. Never let any active army run out of supply; buy supply immediately or retreat to a friendly seaport/supply hub before November and January turns.

### Version 78, after game 78 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** The Confederate forces outmaneuvered and overwhelmed our fragmented armies on the alternate map, concentrating superior forces to crush our units in key border cities like Louisville and Columbus while we failed to sufficiently reinforce or consolidate our positions.

**Strategy for the next game.** For the next game, we will focus on concentrating our forces into powerful regional armies rather than spreading thin across border cities, utilizing the rail network to rapidly respond to threats, and aggressively recruiting to match Confederate strength.

**Changes:**

- revised: Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail. (Game 78 showed that smaller isolated garrisons in forward cities were easily picked off by concentrated enemy armies.)
- dropped: Actively capture available empty cities and territory every turn rather than wasting time drilling. (This instruction caused reckless territorial expansion without adequate force concentration, leading to defeat.)
- added: Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail. (We must keep our forces massed to resist the steamrolling Confederate advances seen on the alternate map.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Never let any active army run out of supply; buy supply immediately or retreat to a friendly seaport/supply hub before November and January turns.

### Version 79, after game 79 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** The Confederacy aggressively captured midwestern cities like Louisville, Cincinnati, and St. Louis while our armies suffered from severe supply exhaustion and could not counterattack effectively. We failed to maintain active supply lines and let armies run out of supply before critical winter turns, leading to attrition and defeat.

**Strategy for the next game.** We will focus heavily on securing our supply lines, keeping our field armies supplied and concentrated near rail hubs, and blocking Rebel expansion into key midwestern cities while steadily building our economic and military strength.

**Changes:**

- revised: Never let any active army run out of supply; buy supply immediately or retreat to a friendly seaport or supply hub before November and January turns. (We lost control of multiple armies to zero supply in winter due to inadequate monitoring and poor positioning away from supply lines.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Never let any active army run out of supply; buy supply immediately or retreat to a friendly seaport or supply hub before November and January turns.

### Version 80, after game 80 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We expanded our territory early and won some naval skirmishes, but the Rebels concentrated superior forces against Louisville and defeated our garrison. We failed to recognize the concentration of enemy strength and did not recruit enough to match their forces, leading to city loss and a Rebel victory by October 1861.

**Strategy for the next game.** We will focus heavily on recruiting fresh armies in major cities to build up our aggregate strength, reinforce our defensive lines at key border hubs like Louisville and Cincinnati, and prevent the Rebels from outnumbering us or capturing 28 cities.

**Changes:**

- revised: Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth. (We failed to recruit sufficient troops to hold key cities against concentrated Confederate attacks.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Never let any active army run out of supply; buy supply immediately or retreat to a friendly seaport or supply hub before November and January turns.

### Version 81, after game 81 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We lost control of key cities and allowed Confederate forces to maneuver freely and capture territory unchecked. Our armies lacked coordination, suffered supply issues, and failed to adequately recruit and defend critical urban centers, leading to a rapid Confederate victory by city control.

**Strategy for the next game.** Next game, we will focus aggressively on capturing and holding neutral and enemy cities to prevent the Confederacy from reaching the city threshold for victory. We will maintain robust recruitment to grow our armies, keep our forces well-supplied and concentrated near rail hubs, and avoid risky winter campaigns while countering Rebel movements decisively.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Never let any active army run out of supply; buy supply immediately or retreat to a friendly seaport or supply hub before November and January turns.

### Version 82, after game 82 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** The game was lost in 4 turns because we spent crucial turns repeatedly drilling armies instead of actively capturing neutral cities, reinforcing our lines, and countering Confederate territorial expansion. The Rebels smoothly seized cities and built an overwhelming lead.

**Strategy for the next game.** Next game we will aggressively prioritize capturing neutral and empty cities on turn one and two, recruit actively to secure manpower parity, and minimize idle drilling turns to prevent quick Confederate city-control victories.

**Changes:**

- revised: Never waste turns idling or excessive drilling while empty or neutral cities remain unclaimed and the enemy is expanding. (In game 81, excessive drilling caused us to lose the city control race in only 4 turns.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Never waste turns idling or excessive drilling while empty or neutral cities remain unclaimed and the enemy is expanding.

### Version 83, after game 83 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We lost this game because our attacks into Cincinnati were repeatedly repulsed by the entrenched Rebel force, while the enemy aggressively captured our northern cities and choked our supply lines. Failing to properly concentrate superior forces and maintain supply led to attrition and loss of city control.

**Strategy for the next game.** Next game, we will focus on rapid early acquisition of neutral border cities, avoid piecemeal attacks against fortified enemy stacks in cities like Cincinnati, and rigorously manage our army supply lines and rail movements to keep our forces concentrated and well-supplied.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Never waste turns idling or excessive drilling while empty or neutral cities remain unclaimed and the enemy is expanding.

### Version 84, after game 84 (alternate: Rebel victory: share of total income, 5 turns)

**Diagnosis.** We made disastrous attacks against well-defended Rebel positions and strong armies without numerical superiority (attacking J.E. Johnston in Nashville and Beauregard in Decatur), resulting in crushed armies. We also neglected recruitment while our ground forces dwindled.

**Strategy for the next game.** We will focus entirely on capturing neutral and empty border cities for income while using the recruit command heavily to build up our army sizes. We will avoid attacking fortified enemy positions unless we hold a massive numerical and leader advantage.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Never waste turns idling or excessive drilling while empty or neutral cities remain unclaimed and the enemy is expanding.

### Version 85, after game 85 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We lost control of the map because our forces were spread thin, units ran out of supply, and we failed to recruit fresh manpower while the Rebels concentrated superior forces to capture our key cities and blockade Philadelphia.

**Strategy for the next game.** We will maintain our core defensive and logistical disciplines, focusing on keeping armies supplied, defending Washington, and aggressively expanding our economic footprint through unclaimed cities while reinforcing our frontline forces.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Never waste turns idling or excessive drilling while empty or neutral cities remain unclaimed and the enemy is expanding.

### Version 86, after game 86 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We pushed forward into border cities without sufficient combat strength or leadership, leading to costly defeats against concentrated Rebel armies. Our attacks into cities without numerical superiority wasted men we could not replace, while we failed to use the recruit command to build up our forces.

**Strategy for the next game.** In the next game, we will focus heavily on defensive consolidation and regular recruitment to build a powerful army before attempting any offensives. We will secure our immediate hinterlands, avoid costly uncoordinated attacks on enemy strongholds, and maintain strong garrisons while growing our economic and military base.

**Changes:**

- revised: Never attack defended cities with piecemeal forces; consolidate forces and recruit aggressively before launching offensives. (Game 86 showed that attacking with small, scattered armies into cities held by strong Rebel leaders results in devastating counterattacks and heavy losses.)
- dropped: Never waste turns idling or excessive drilling while empty or neutral cities remain unclaimed and the enemy is expanding. (This instruction encouraged premature and reckless advances into enemy territory without building up sufficient force strength first.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Never attack defended cities with piecemeal forces; consolidate forces and recruit aggressively before launching offensives.

### Version 87, after game 87 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We focused too much on drilling and failed to reinforce our armies or recapture lost economic centers. Small dispersed forces were systematically worn down and overwhelmed by concentrated Confederate armies, leading to a steady loss of cities and eventual defeat.

**Strategy for the next game.** We will focus on proactive recruitment to build up our field strength, maintain solid supply lines, and keep our forces concentrated to defend key cities while denying the enemy economic expansion.

**Changes:**

- revised: Reinforce and grow existing armies aggressively with the recruit command rather than relying solely on endless drilling. (Endless drilling did not prevent our defeat; we needed more manpower and reinforcements on the ground to hold our cities against larger Rebel forces.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Reinforce and grow existing armies aggressively with the recruit command rather than relying solely on endless drilling.

### Version 88, after game 88 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** The game was lost very quickly on the alternate map due to a failure to recruit and expand our forces while dispersing small armies that were subsequently crushed by concentrated Rebel attacks. We focused too much on drilling small, static forces instead of building and reinforcing powerful field armies, allowing the Confederates to seize key cities and achieve rapid victory.

**Strategy for the next game.** In the next game on the alternate map, we will immediately pivot to heavy recruitment in major cities to build up powerful armies rather than wasting turns drilling tiny forces. We will keep our main forces concentrated to deter Rebel incursions, aggressively secure neutral and empty cities to maintain economic parity, and avoid piecemeal movements that lead to catastrophic defeats.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Reinforce and grow existing armies aggressively with the recruit command rather than relying solely on endless drilling.

### Version 89, after game 89 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We focused too heavily on continuous drilling while our armies ran out of supply and fell behind in city control. The Confederate forces aggressively captured our economic hubs, cut our supply lines, and eventually overwhelmed us while we failed to expand our territory or properly manage supply purchases.

**Strategy for the next game.** We will immediately halt excessive drilling and prioritize expanding our territorial control, maintaining active supply lines, and reinforcing our primary armies using the recruit command to counter Confederate expansion.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Reinforce and grow existing armies aggressively with the recruit command rather than relying solely on endless drilling.

### Version 90, after game 90 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We focused heavily on drilling our armies rather than expanding our city control or aggressively taking empty or neutral cities. Meanwhile, the Confederate forces moved rapidly to capture key locations, outflank us, and achieve the city-count victory condition within 4 turns. Our passive posture allowed the enemy to dictate the pace and seize strategic dominance.

**Strategy for the next game.** We will immediately shift away from passive drilling and focus our efforts on aggressively securing empty and neutral cities, expanding our economic base, and using our superior numbers to capture key Confederate positions before they can secure victory through city dominance.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Reinforce and grow existing armies aggressively with the recruit command rather than relying solely on endless drilling.

### Version 91, after game 91 (standard: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We focused excessively on drilling while the Rebel armies aggressively maneuvered, attacked, and captured our key cities. Our uncoordinated attacks into fortified or superior positions failed, and small isolated forces were overwhelmed.

**Strategy for the next game.** Next game, we will immediately use the recruit command to strengthen our starting forces instead of wasting turns drilling. We will keep our armies concentrated to repel Confederate offensives and methodically capture empty or neutral cities to secure victory by city control.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Reinforce and grow existing armies aggressively with the recruit command rather than relying solely on endless drilling.

### Version 92, after game 92 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We pushed forward into border cities early without enough concentration, allowing A.S. Johnston's mobile forces to crush our separated western detachments in detail. Meanwhile, we spent valuable turns drilling and building ships instead of recruiting new strength or aggressively contesting key cities, letting the Confederacy rapidly accumulate city control for a quick victory.

**Strategy for the next game.** Next game, we will immediately prioritize recruiting large forces in core cities and keeping them concentrated rather than scattering isolated detachments. We will suppress unnecessary naval builds and drilling in favor of establishing a solid defensive line in the West, protecting our economic base, and matching Rebel expansion city for city.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Reinforce and grow existing armies aggressively with the recruit command rather than relying solely on endless drilling.

### Version 93, after game 93 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We lost control of too many cities, falling to 6 while the Rebels reached 32, triggering their victory condition. We continually suffered from armies running out of supply because we neglected maintaining supply connections and failed to use the supply command when funds were available, leaving active armies crippled at half strength and unable to hold territory.

**Strategy for the next game.** Next game, we will aggressively secure and hold our cities to prevent the Rebels from reaching the 32-city victory threshold, actively maintain supply lines and purchase supplies before critical turns, and concentrate our forces to defend key economic and political hubs while steadily out-recruiting the enemy.

**Changes:**

- revised: Always maintain supply lines to active armies and purchase supply immediately when levels drop. (Multiple armies went out of supply and stayed unsupplied, causing disastrous combat performance and loss of territory.)
- revised: Monitor army supply levels carefully and avoid movements that cut armies off from supply cities. (Unconnected movements during campaign maneuvers frequently left our large forces isolated from friendly adjacent cities, starving them of supply.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Reinforce and grow existing armies aggressively with the recruit command rather than relying solely on endless drilling.

### Version 94, after game 94 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We lost control of too many cities within 4 turns on the alternate map because the AI aggressively seized neutral and border locations while our forces remained passive, drilling instead of expanding and capturing cities.

**Strategy for the next game.** On the alternate map, we must aggressively advance to claim neutral and empty cities in the opening turns, using our funds for active expansion and recruiting rather than excessive drilling, while securing key rail junctions to block Rebel advances.

**Changes:**

- revised: Aggressively capture neutral and empty cities every turn rather than idling forces with prolonged drill commands. (Drilling too often caused us to lose the city count race and resulted in a fast defeat on the alternate map.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Aggressively capture neutral and empty cities every turn rather than idling forces with prolonged drill commands.

### Version 95, after game 95 (standard: Rebel victory: cities controlled, 6 turns)

**Diagnosis.** We repeatedly threw small or uncoordinated forces against Rebel armies in cities and suffered tactical defeats. Meanwhile, the Confederates successfully captured our core cities and isolated Philadelphia, leading to a swift defeat via city control.

**Strategy for the next game.** Next game, we will focus on concentrating our forces, aggressively recruiting to match Rebel numbers, and avoiding piecemeal attacks on fortified enemy armies while securing surrounding cities.

**Changes:**

- revised: Merge forces using the join command to create powerful armies capable of standing up to concentrated Confederate threats. (We lost battles because our armies were too small individually compared to concentrated Rebel forces.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Merge forces using the join command to create powerful armies capable of standing up to concentrated Confederate threats.

### Version 96, after game 96 (alternate: Rebel victory: share of total income, 5 turns)

**Diagnosis.** In this alternate map game, our early naval sortie was crushed, leaving Philadelphia blockaded and pounded into neutrality. On land, while our initial captures of Manassas, Fredericksburg, and Paducah were successful, our subsequent attacks on fortified Rebel positions like Fort Donelson failed due to poor odds and enemy defensive multipliers. Meanwhile, the Confederacy rapidly expanded and concentrated massive forces, overwhelming our western flank and winning via economic dominance within 5 turns.

**Strategy for the next game.** Next game, we will focus on internal economic consolidation, avoiding speculative naval gambits and costly assaults on fortified enemy positions. We will heavily utilize the recruit command to build up our active field armies, maintain strong defensive postures in key rail hubs, and slowly grind down the Confederate advantage through disciplined concentration of force.

**Changes:**

- revised: Avoid offensive attacks against fortified cities unless our strength significantly exceeds the defender's fortified multiplier. (Grant's repeated attacks on Fort Donelson failed because enemy fortifications multiplied defender strength, leading to heavy Union casualties and repulses.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Avoid offensive attacks against fortified cities unless our strength significantly exceeds the defender's fortified multiplier.

### Version 97, after game 97 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We once again fell into the trap of passive drilling while our armies ran out of supply and were slowly whittled down by the Rebels. We failed to expand our manpower pool through regular recruiting, and our isolated armies in the west and north ran out of supply during the winter months, leading to catastrophic losses and loss of city control.

**Strategy for the next game.** We must break the cycle of endless drilling that leads nowhere. For the next game, we will actively recruit new troops to boost our numbers, maintain strict supply lines with timely purchases, and use our armies to aggressively secure and hold cities rather than sitting idle while the Confederacy out-maneuvers us.

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Avoid offensive attacks against fortified cities unless our strength significantly exceeds the defender's fortified multiplier.

### Version 98, after game 98 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** On the alternate map, the Confederacy aggressively captured neutral and Union-held cities while our forces remained passive, drilled, or launched isolated attacks. We accumulated cash but failed to contest city control or expand our economic base, resulting in a rapid Confederate city-count victory by October 1861.

**Strategy for the next game.** On the alternate map, we must aggressively move to capture neutral and empty cities from the very first turn rather than idling or over-drilling. We will use available funds for timely recruitment and keep our armies moving to secure territory, preventing the Confederacy from quietly accumulating the 28 cities needed for a quick victory.

**Changes:**

- added: Aggressively seize neutral cities from turn one on the alternate map to deny the AI the 28-city threshold. (The alternate map allows the AI to rapidly win via city control if we spend turns drilling instead of capturing empty/neutral cities.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Aggressively seize neutral cities from turn one on the alternate map to deny the AI the 28-city threshold.

### Version 99, after game 99 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We failed to manage army supply lines properly, leading to McDowell running out of supply and losing combat effectiveness. Excessive drilling instead of recruiting and aggressive capturing allowed the AI to outgrow us in cities and troop strength, culminating in a Rebel victory.

**Strategy for the next game.** We will focus on aggressive early capture of neutral cities on the standard map, maintain strict vigilance over supply lines to prevent armies from going out of supply, and regularly recruit new troops to match Confederate growth while keeping Washington strongly defended.

**Changes:**

- revised: Aggressively seize neutral cities from turn one on the standard map to deny the AI the 32-city threshold. (Standard map victory condition requires denying the AI 32 cities, so our focus must be on early standard map expansion.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Aggressively seize neutral cities from turn one on the standard map to deny the AI the 32-city threshold.

### Version 100, after game 100 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** We suffered another defeat on the alternate map because we failed to use the recruit command to replenish our shrinking forces while the AI rapidly expanded its armies to over 78,000 men. Although our defensive battles held off individual attacks, our lack of offensive momentum and failure to capture and hold cities led to a slow war of attrition where the Confederacy eventually achieved city dominance.

**Strategy for the next game.** Next game on the alternate map, we will immediately initiate a robust recruitment campaign using our starting funds to build up our standing armies instead of relying solely on initial forces. We will combine these new troops into formidable corps, maintain solid supply lines, and push methodically to capture neutral and enemy cities to prevent the AI from achieving economic and territorial supremacy.

**Changes:**

- dropped: Aggressively seize neutral cities from turn one on the standard map to deny the AI the 32-city threshold. (This lesson was specific to the standard map layout and caused confusion on the alternate map where city counts and positions differ.)
- added: Aggressively use recruit and join commands early to build at least two massive field armies capable of taking and holding territory. (We consistently lose the manpower race and fail to project power because we hoard cash instead of raising troops and merging them into strong offensive forces.)

**Notebook:**

1. Never attack enemy armies in difficult terrain or cities without overwhelming numerical superiority.
2. Always maintain supply lines to active armies and purchase supply immediately when levels drop.
3. Regularly use the recruit command in friendly cities to expand manpower and counter Rebel growth.
4. Secure neutral border cities proactively to expand our economic base and prevent enemy city dominance.
5. Keep armies concentrated and close to friendly rail networks or supply hubs to prevent isolation.
6. Always keep a strong defensive army garrisoning Washington to prevent sudden enemy capital raids.
7. Use rail transport proactively to reposition large forces to threatened border cities before attacks hit.
8. Prioritize recruiting and field strength over unnecessary naval construction when ground forces are outnumbered.
9. Monitor army supply levels carefully and avoid movements that cut armies off from supply cities.
10. Prioritize capturing empty or neutral cities immediately to prevent enemy victory via city control.
11. Never disperse small armies into border cities where concentrated Rebel forces can isolate and destroy them in detail.
12. Aggressively use recruit and join commands early to build at least two massive field armies capable of taking and holding territory.

