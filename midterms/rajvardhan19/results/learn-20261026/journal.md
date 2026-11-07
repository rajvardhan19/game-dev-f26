# Learning journal: `gemini-a`

Model `gemini-3.5-flash-lite`. 16 training games; notebook version 16 (frozen, sha e7862f80e966d088).

## What it did, game by game

| game | map | notebook | result | turns | recruits | drills | moves | attacks (won) | mean odds | cities peak / end | last-turn cash | refused |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | standard | v0 | decisive loss: Rebel victory: share of total income | 6 | 0 | 9 | 7 | 1 (0) | 23% | 14 / 7 | 243 | 2 |
| 2 | alternate | v1 | decisive loss: Rebel victory: cities controlled | 5 | 0 | 8 | 6 | 2 (1) | 47% | 10 / 8 | 1294 | 3 |
| 3 | standard | v2 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 7 | 6 | 1 (1) | 30% | 13 / 5 | 398 | 3 |
| 4 | alternate | v3 | decisive loss: Rebel victory: cities controlled | 3 | 0 | 0 | 6 | 0 (0) | - | 10 / 8 | 958 | 3 |
| 5 | standard | v4 | decisive loss: Rebel victory: cities controlled | 10 | 3 | 0 | 7 | 2 (0) | 42% | 12 / 5 | 252 | 7 |
| 6 | alternate | v5 | decisive loss: Rebel victory: cities controlled | 5 | 10 | 0 | 0 | 0 (0) | - | 10 / 8 | 357 | 1 |
| 7 | standard | v6 | decisive loss: Rebel victory: capital captured | 3 | 3 | 0 | 7 | 1 (1) | 40% | 14 / 14 | 311 | 1 |
| 8 | alternate | v7 | decisive loss: Rebel victory: cities controlled | 4 | 6 | 0 | 6 | 2 (0) | 40% | 11 / 10 | 585 | 1 |
| 9 | standard | v8 | decisive loss: Rebel victory: cities controlled | 7 | 0 | 0 | 11 | 2 (0) | 35% | 13 / 5 | 856 | 4 |
| 10 | alternate | v9 | decisive loss: Rebel victory: cities controlled | 3 | 0 | 0 | 8 | 3 (0) | 29% | 12 / 9 | 797 | 0 |
| 11 | standard | v10 | decisive loss: Rebel victory: cities controlled | 9 | 9 | 13 | 12 | 3 (1) | 43% | 13 / 5 | 232 | 13 |
| 12 | alternate | v11 | decisive loss: Rebel victory: cities controlled | 4 | 0 | 0 | 5 | 1 (0) | 44% | 10 / 6 | 917 | 1 |
| 13 | standard | v12 | decisive loss: Rebel victory: cities controlled | 10 | 0 | 3 | 5 | 0 (0) | - | 13 / 5 | 673 | 8 |
| 14 | alternate | v13 | decisive loss: Rebel victory: cities controlled | 5 | 10 | 0 | 3 | 1 (0) | 37% | 10 / 7 | 372 | 3 |
| 15 | standard | v14 | decisive loss: Rebel victory: capital captured | 5 | 4 | 0 | 7 | 2 (0) | 36% | 12 / 11 | 385 | 0 |
| 16 | alternate | v15 | decisive loss: Rebel victory: cities controlled | 4 | 4 | 0 | 3 | 1 (0) | 37% | 10 / 9 | 473 | 2 |

## How the notebook changed

### Version 1, after game 1 (standard: Rebel victory: share of total income, 6 turns)

**Diagnosis.** We spread our forces too thin, attacked enemy positions prematurely without sufficient strength or supply lines, and allowed Jackson to crush Fremont and capture Washington. We failed to consolidate our armies, leading to piecemeal defeats while the Rebels concentrated their strength.

**Strategy for the next game.** In the next game, we will consolidate our scattered forces into two strong field armies, avoid reckless assaults on enemy territory, prioritize the defense of Washington and the East, maintain strict attention to supply lines, and steadily build up our economic and military capacity before advancing.

**Changes:**

- added: Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines. (We repeatedly threw small armies against prepared defenders like Jackson and Pemberton, resulting in heavy losses and retreats.)
- added: Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities. (Scattered forces allowed Confederate commanders like A.S. Johnston and Beauregard to defeat us in detail one by one.)
- added: Prioritize the defense of Washington and key regional hubs to prevent the loss of the capital and immediate defeat. (Fremont's small force was easily crushed by Jackson, leading directly to the loss of Washington and game over.)
- added: Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn. (Armies frequently went out of supplies, halving their combat strength and leaving them vulnerable to counterattacks.)
- added: Drill armies only when they are safely out of immediate enemy reach and well-supplied. (Drilling left units resting when they needed to retreat or reinforce active frontlines.)
- added: Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur. (The AI effectively used rail to redeploy Pemberton and Lee, whereas our responses were too slow.)
- added: Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops. (Our cash reserves dwindled by winter, preventing adequate supply purchases and leaving armies starving.)

**Notebook:**

1. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
2. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
3. Prioritize the defense of Washington and key regional hubs to prevent the loss of the capital and immediate defeat.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.

### Version 2, after game 2 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We concentrated armies in Baltimore and Springfield but failed to recruit or expand our territorial control. While we focused on drilling and minor engagements, the Rebels aggressively captured cities and outpaced us economically and territorially, leading to a defeat via city control.

**Strategy for the next game.** We will actively recruit troops to expand our forces, aggressively capture enemy and neutral cities to secure income and prevent a Rebel territorial victory, while maintaining solid defensive hubs around Washington and key positions.

**Changes:**

- added: Actively recruit new troops and capture neutral or enemy cities each turn to prevent the Confederacy from winning through territorial dominance. (We lost the game entirely because the Rebels secured 28 cities while we neglected expansion and recruitment, holding only 8 cities.)

**Notebook:**

1. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
2. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
3. Prioritize the defense of Washington and key regional hubs to prevent the loss of the capital and immediate defeat.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively recruit new troops and capture neutral or enemy cities each turn to prevent the Confederacy from winning through territorial dominance.

### Version 3, after game 3 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We failed because we repeatedly drilled or scattered our forces while the Rebels rapidly mobilized, used trains to concentrate overwhelmingly large armies, and captured our border cities. Our armies ran out of supply and were easily crushed one by one.

**Strategy for the next game.** Next game, we will immediately halt all non-essential drilling, keep our main forces concentrated and supplied, push aggressively to secure key cities, and counter Rebel rail movements with our own focused concentrations.

**Changes:**

- added: Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement. (We lost valuable turns and suffered supply issues while drilling instead of consolidating against the advancing Confederate armies.)

**Notebook:**

1. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
2. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
3. Prioritize the defense of Washington and key regional hubs to prevent the loss of the capital and immediate defeat.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively recruit new troops and capture neutral or enemy cities each turn to prevent the Confederacy from winning through territorial dominance.
9. Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement.

### Version 4, after game 4 (alternate: Rebel victory: cities controlled, 3 turns)

**Diagnosis.** The game was lost early due to failing to protect the capital of Washington and neglecting aggressive territorial expansion and recruitment. J.E.B. Stuart marched unopposed into Washington on Turn 3 while our armies were concentrated elsewhere or moving inefficiently, resulting in a sudden Rebel victory. We must balance front-line concentration with the strict defense of Washington and active city captures.

**Strategy for the next game.** In the next game, we will keep a garrison force permanently in or immediately adjacent to Washington to deter enemy captures, while simultaneously using our other armies to aggressively capture neutral territory and recruit troops to contest Confederate economic dominance.

**Changes:**

- added: Never leave Washington or critical core cities under-defended against rapid enemy cavalry or infantry advances. (J.E.B. Stuart captured an undefended Washington on turn 3, ending the game instantly.)

**Notebook:**

1. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
2. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
3. Prioritize the defense of Washington and key regional hubs to prevent the loss of the capital and immediate defeat.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively recruit new troops and capture neutral or enemy cities each turn to prevent the Confederacy from winning through territorial dominance.
9. Never leave Washington or critical core cities under-defended against rapid enemy cavalry or infantry advances.
10. Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement.

### Version 5, after game 5 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We lost because our armies became cut off from supply lines, particularly in Washington and western sectors, leading to severe troop attrition and inability to fight effectively. We also neglected recruitment, allowing the Confederacy to outnumber and out-territory us.

**Strategy for the next game.** Next game we will maintain active recruitment to build our numbers, strictly monitor supply lines and buy supplies before winter/starvation hits, and consolidate our forces to defend key cities while steadily pushing back Confederate territorial gains.

**Changes:**

- added: Check army supply states every turn and use the supply command immediately before armies run out of food and starve. (McDowell's army starved in Washington because we missed the exact turn supply could be replenished.)
- added: Recruit actively from available cities each spring and autumn to replace casualties and keep army sizes competitive. (We failed to recruit new armies throughout the game, causing our total force to dwindle while the Rebels expanded.)

**Notebook:**

1. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
2. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
3. Prioritize the defense of Washington and key regional hubs to prevent the loss of the capital and immediate defeat.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively recruit new troops and capture neutral or enemy cities each turn to prevent the Confederacy from winning through territorial dominance.
9. Never leave Washington or critical core cities under-defended against rapid enemy cavalry or infantry advances.
10. Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement.
11. Check army supply states every turn and use the supply command immediately before armies run out of food and starve.
12. Recruit actively from available cities each spring and autumn to replace casualties and keep army sizes competitive.

### Version 6, after game 6 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We successfully recruited heavily to grow our army size, but the Confederacy continuously outmaneuvered us in territorial control and neutral city capture. We failed to actively expand our own city count, allowing them to secure 28 cities and trigger a territorial victory by December 1861.

**Strategy for the next game.** We will aggressively recruit in the spring, concentrate our large armies, and actively march to capture neutral and enemy cities every turn to deny the Confederacy the 28-city threshold while maintaining a solid defense around Washington.

**Changes:**

- revised: Actively capture neutral and enemy cities every single turn with available mobile forces to block Confederate territorial victory conditions. (Previous lessons focused vaguely on recruiting and capturing, but we lost strictly due to passive city control; we must actively march and capture cities.)

**Notebook:**

1. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
2. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
3. Prioritize the defense of Washington and key regional hubs to prevent the loss of the capital and immediate defeat.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively capture neutral and enemy cities every single turn with available mobile forces to block Confederate territorial victory conditions.
9. Never leave Washington or critical core cities under-defended against rapid enemy cavalry or infantry advances.
10. Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement.
11. Check army supply states every turn and use the supply command immediately before armies run out of food and starve.
12. Recruit actively from available cities each spring and autumn to replace casualties and keep army sizes competitive.

### Version 7, after game 7 (standard: Rebel victory: capital captured, 3 turns)

**Diagnosis.** The Confederate army under Jackson swept completely past our poorly defended eastern positions and captured Washington in July 1861, ending the game in a rapid defeat. We failed to leave an adequate garrison or army in the capital while launching peripheral offensives.

**Strategy for the next game.** We will secure Washington immediately with a strong standing force to prevent early decapitation strikes, while consolidating our remaining armies for a disciplined, secure advance that maintains unbroken supply and unassailable rear areas.

**Changes:**

- dropped: Prioritize the defense of Washington and key regional hubs to prevent the loss of the capital and immediate defeat. (It was redundant with the stricter, absolute rule against leaving Washington under-defended.)

**Notebook:**

1. Never leave Washington or critical core cities under-defended against rapid enemy cavalry or infantry advances.
2. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
3. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively capture neutral and enemy cities every single turn with available mobile forces to block Confederate territorial victory conditions.
9. Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement.
10. Check army supply states every turn and use the supply command immediately before armies run out of food and starve.
11. Recruit actively from available cities each spring and autumn to replace casualties and keep army sizes competitive.

### Version 8, after game 8 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We successfully built up troop numbers through active recruitment and captured a few key cities, but our offensives failed because we repeatedly attacked defended positions without sufficient numerical superiority or leaders, leading to costly bounces at StLouis. Meanwhile, the Rebels swept through the west and captured enough cities to trigger a territorial victory.

**Strategy for the next game.** Next game, we will prioritize massing our recruited forces into overwhelming single-front armies rather than piecemeal attacks on fortified cities like StLouis. We will aggressively contest neutral cities early to deny the Rebels their territorial victory threshold while maintaining a stout defense around our core.

**Notebook:**

1. Never leave Washington or critical core cities under-defended against rapid enemy cavalry or infantry advances.
2. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
3. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively capture neutral and enemy cities every single turn with available mobile forces to block Confederate territorial victory conditions.
9. Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement.
10. Check army supply states every turn and use the supply command immediately before armies run out of food and starve.
11. Recruit actively from available cities each spring and autumn to replace casualties and keep army sizes competitive.

### Version 9, after game 9 (standard: Rebel victory: cities controlled, 7 turns)

**Diagnosis.** We repeatedly threw uncoordinated, unsupplied attacks into fortified or superior enemy forces (like A.S. Johnston in Cincinnati), leading to heavy losses and shattered armies. Meanwhile, the Rebels methodically out-expanded us, capturing our core cities and winning via territorial dominance.

**Strategy for the next game.** We will focus heavily on army concentration and maintaining secure supply lines, avoiding reckless attacks on enemy strongpoints. We will methodically secure border cities while keeping a strong defensive posture around Washington and our economic core.

**Changes:**

- revised: Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines. (This game's repeated failed attacks against A.S. Johnston at Cincinnati proved that attacking without superior numbers and high readiness results in catastrophic defeats.)

**Notebook:**

1. Never leave Washington or critical core cities under-defended against rapid enemy cavalry or infantry advances.
2. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
3. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively capture neutral and enemy cities every single turn with available mobile forces to block Confederate territorial victory conditions.
9. Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement.
10. Check army supply states every turn and use the supply command immediately before armies run out of food and starve.
11. Recruit actively from available cities each spring and autumn to replace casualties and keep army sizes competitive.

### Version 10, after game 10 (alternate: Rebel victory: cities controlled, 3 turns)

**Diagnosis.** We scattered our small starting forces into isolated attacks against stronger enemy concentrations in the west, leading to piecemeal defeats by A.S. Johnston and Beauregard. Meanwhile, we neglected recruiting new troops to expand our tiny armies, allowing the Confederates to easily overwhelm us in city count and force a rapid defeat.

**Strategy for the next game.** Next game, we will immediately focus on merging our starting forces into large, cohesive armies rather than sending small detachments on unsupported attacks. We will use our treasury to recruit heavily from available cities to build up numerical parity, maintain solid supply lines, and defend our core territory while steadily pushing back enemy forces.

**Changes:**

- revised: Actively recruit new armies from available cities every turn to build up our forces so we can match Confederate strength. (We failed to recruit in previous games and lost due to sheer lack of numbers against larger Confederate forces.)

**Notebook:**

1. Never leave Washington or critical core cities under-defended against rapid enemy cavalry or infantry advances.
2. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
3. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively recruit new armies from available cities every turn to build up our forces so we can match Confederate strength.
9. Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement.
10. Check army supply states every turn and use the supply command immediately before armies run out of food and starve.
11. Recruit actively from available cities each spring and autumn to replace casualties and keep army sizes competitive.

### Version 11, after game 11 (standard: Rebel victory: cities controlled, 9 turns)

**Diagnosis.** We lost control of key border cities and allowed Confederate armies under Lee and Jackson to capture crucial northern territory while our forces became bottlenecked and starved of supplies. We failed to sufficiently concentrate our forces and protect our supply lines, leading to stagnation and eventual defeat.

**Strategy for the next game.** Next game, we will immediately focus on consolidating our starting forces into robust offensive groups, securing our economic and supply lines early, and aggressively countering Rebel incursions while keeping our armies well-supplied and reinforced.

**Notebook:**

1. Never leave Washington or critical core cities under-defended against rapid enemy cavalry or infantry advances.
2. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
3. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively recruit new armies from available cities every turn to build up our forces so we can match Confederate strength.
9. Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement.
10. Check army supply states every turn and use the supply command immediately before armies run out of food and starve.
11. Recruit actively from available cities each spring and autumn to replace casualties and keep army sizes competitive.

### Version 12, after game 12 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** We concentrated forces in the East around Washington and secured initial successes in the West, but we failed to recruit new armies aggressively. This left our forces too small to hold extended fronts against Confederate counterattacks, leading to a loss of key cities and eventual defeat.

**Strategy for the next game.** Next game, we will heavily increase our recruitment rate from turn one, channeling funds into raising new armies across all available cities to ensure numerical parity with the Confederacy, while keeping our main forces concentrated and supplied.

**Notebook:**

1. Never leave Washington or critical core cities under-defended against rapid enemy cavalry or infantry advances.
2. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
3. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively recruit new armies from available cities every turn to build up our forces so we can match Confederate strength.
9. Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement.
10. Check army supply states every turn and use the supply command immediately before armies run out of food and starve.
11. Recruit actively from available cities each spring and autumn to replace casualties and keep army sizes competitive.

### Version 13, after game 13 (standard: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** We once again failed to recruit new armies or reinforce existing ones, leading to a steady attrition of our forces while the Confederacy grew massively in strength. Furthermore, we let armies like McDowell's run out of supplies repeatedly during winter, and our attempts to capture territory without sufficient force concentrations ended in defeat and loss of cities.

**Strategy for the next game.** Next game we must aggressively use the recruit and reinforce commands to build our army sizes and match Confederate manpower, while strictly monitoring army supply and avoiding uncoordinated attacks.

**Changes:**

- revised: Actively recruit and reinforce armies from available cities every turn to build up our forces and match Confederate strength. (We failed to recruit any new troops throughout the game while Confederate strength doubled, leading to defeat.)

**Notebook:**

1. Never leave Washington or critical core cities under-defended against rapid enemy cavalry or infantry advances.
2. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
3. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively recruit and reinforce armies from available cities every turn to build up our forces and match Confederate strength.
9. Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement.
10. Check army supply states every turn and use the supply command immediately before armies run out of food and starve.
11. Recruit actively from available cities each spring and autumn to replace casualties and keep army sizes competitive.

### Version 14, after game 14 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** We successfully increased recruitment compared to past games, but we failed to mount coordinated offensive campaigns or defend key positions effectively. The Confederates steadily captured cities while our forces remained scattered and reactive, eventually achieving a city-control victory.

**Strategy for the next game.** Next game we will maintain aggressive recruitment and force concentration while actively pushing outward to capture and hold strategic cities, preventing the enemy from out-expanding our territorial control.

**Notebook:**

1. Never leave Washington or critical core cities under-defended against rapid enemy cavalry or infantry advances.
2. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
3. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively recruit and reinforce armies from available cities every turn to build up our forces and match Confederate strength.
9. Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement.
10. Check army supply states every turn and use the supply command immediately before armies run out of food and starve.
11. Recruit actively from available cities each spring and autumn to replace casualties and keep army sizes competitive.

### Version 15, after game 15 (standard: Rebel victory: capital captured, 5 turns)

**Diagnosis.** We lost this game because we failed to secure our capital and allowed Jackson to repeatedly attack and capture Harper's Ferry and eventually Washington. While we tried to counter-attack in the West, our forces lacked sufficient concentration and leadership ratings to defeat enemy armies holding key cities, and we neglected defensive fortifications at Washington.

**Strategy for the next game.** Next game, we will prioritize the immediate defense and fortification of Washington while grouping our eastern forces under strong leadership to deter Stonewall Jackson. Simultaneously, we will methodically build up western armies through steady recruitment and maintain strict supply lines before attempting any offensive thrusts into Confederate territory.

**Changes:**

- added: Fortify threatened key cities immediately with local forces when an active enemy army is in an adjacent region. (Washington was left vulnerable to Jackson's repeated advances, leading directly to the loss of the capital and the game.)

**Notebook:**

1. Never leave Washington or critical core cities under-defended against rapid enemy infantry or cavalry advances.
2. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
3. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively recruit and reinforce armies from available cities every turn to build up our forces and match Confederate strength.
9. Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement.
10. Check army supply states every turn and use the supply command immediately before armies run out of food and starve.
11. Fortify threatened key cities immediately with local forces when an active enemy army is in an adjacent region.

### Version 16, after game 16 (alternate: Rebel victory: cities controlled, 4 turns)

**Diagnosis.** The Confederacy quickly seized key Western and Border cities and rapidly expanded its city count to 28, triggering a technical victory in late 1861. Although Union recruitment improved, our forces remained fragmented and reactive, failing to contest the rebel land grab and capital expansion.

**Strategy for the next game.** We will aggressively recruit and concentrate our starting forces while pushing outward from Washington and Springfield to contest enemy-held cities, preventing the Confederacy from achieving an early city-count victory.

**Changes:**

- added: Aggressively contest enemy city captures in the early game to prevent the Confederacy from reaching the 28-city threshold. (Game 16 ended quickly due to the rapid rebel acquisition of 28 cities; we must project force outward rather than purely turtling.)

**Notebook:**

1. Never leave Washington or critical core cities under-defended against rapid enemy infantry or cavalry advances.
2. Never attack fortified enemy positions or superior forces without a substantial numerical advantage and reliable supply lines.
3. Concentrate your starting armies into larger, powerful forces rather than scattering them across isolated cities.
4. Maintain a clear chain of supply by ensuring friendly neighbouring cities connect to all active armies every turn.
5. Drill armies only when they are safely out of immediate enemy reach and well-supplied.
6. Use rail transport strategically to shift reinforcements to threatened sectors before enemy breakthroughs occur.
7. Keep treasury reserves high enough to sustain recruitment and supply purchases through winter supply drops.
8. Actively recruit and reinforce armies from available cities every turn to build up our forces and match Confederate strength.
9. Never waste turns drilling when enemy armies are active nearby; focus entirely on concentration, supply, and movement.
10. Check army supply states every turn and use the supply command immediately before armies run out of food and starve.
11. Fortify threatened key cities immediately with local forces when an active enemy army is in an adjacent region.
12. Aggressively contest enemy city captures in the early game to prevent the Confederacy from reaching the 28-city threshold.

