# Learning journal: `gemini-h`

Model `gemini-3.7-flash`. 50 training games; notebook version 48 (frozen, sha bdae8c3e0ff35eeb).

## What it did, game by game

| game | map | notebook | result | turns | recruits | drills | moves | attacks (won) | mean odds | cities peak / end | last-turn cash | refused |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | standard | v0 | decisive loss: Rebel victory: capital captured | 3 | 4 | 0 | 12 | 2 (0) | 37% | 15 / 15 | 361 | 0 |
| 2 | alternate | v1 | decisive loss: Rebel victory: cities controlled | 12 | 16 | 31 | 24 | 5 (2) | 54% | 19 / 11 | 371 | 1 |
| 3 | standard | v2 | decisive loss: Rebel victory: capital captured | 7 | 7 | 11 | 16 | 7 (1) | 38% | 13 / 8 | 291 | 1 |
| 4 | alternate | v3 | win: Union victory: share of total income | 17 | 27 | 20 | 33 | 13 (11) | 71% | 24 / 24 | 460 | 0 |
| 5 | standard | v4 | decisive loss: Rebel victory: cities controlled | 8 | 3 | 7 | 19 | 7 (0) | 31% | 13 / 6 | 246 | 2 |
| 6 | alternate | v5 | win: Union victory: share of total income | 5 | 9 | 0 | 21 | 9 (4) | 47% | 20 / 20 | 561 | 0 |
| 7 | standard | v6 | win: Union victory: cities controlled | 22 | 37 | 16 | 59 | 26 (16) | 53% | 33 / 33 | 457 | 0 |
| 8 | alternate | v7 | decisive loss: Rebel victory: share of total income | 6 | 14 | 1 | 19 | 2 (0) | 34% | 13 / 12 | 367 | 0 |
| 9 | standard | v8 | decisive loss: Rebel victory: cities controlled | 15 | 13 | 7 | 51 | 14 (5) | 38% | 13 / 6 | 159 | 5 |
| 10 | alternate | v9 | win: Union victory: share of total income | 6 | 16 | 3 | 15 | 5 (4) | 57% | 19 / 19 | 473 | 1 |
| 11 | standard | v10 | win: Union victory: capital captured | 17 | 25 | 4 | 63 | 17 (5) | 42% | 19 / 19 | 430 | 0 |
| 12 | alternate | v11 | win: Union victory: share of total income | 4 | 6 | 0 | 20 | 4 (1) | 41% | 19 / 19 | 509 | 1 |
| 13 | standard | v12 | win: Union victory: capital captured | 15 | 23 | 6 | 55 | 19 (6) | 41% | 22 / 22 | 371 | 2 |
| 14 | alternate | v13 | decisive loss: Rebel victory: cities controlled | 5 | 9 | 5 | 15 | 2 (0) | 28% | 13 / 11 | 642 | 2 |
| 15 | standard | v14 | decisive loss: Rebel victory: capital captured | 14 | 18 | 8 | 46 | 22 (6) | 41% | 14 / 10 | 287 | 2 |
| 16 | alternate | v15 | decisive loss: Rebel victory: share of total income | 7 | 13 | 6 | 16 | 1 (1) | 44% | 16 / 12 | 552 | 0 |
| 17 | standard | v16 | held out: Rebel victory: time expired | 24 | 23 | 11 | 59 | 21 (11) | 56% | 20 / 18 | 383 | 5 |
| 18 | alternate | v17 | win: Union victory: share of total income | 13 | 16 | 8 | 48 | 20 (8) | 47% | 24 / 24 | 645 | 0 |
| 19 | standard | v18 | decisive loss: Rebel victory: cities controlled | 5 | 4 | 6 | 14 | 4 (2) | 41% | 11 / 6 | 454 | 0 |
| 20 | alternate | v19 | win: Union victory: share of total income | 13 | 24 | 6 | 34 | 16 (6) | 47% | 22 / 22 | 504 | 0 |
| 21 | standard | v20 | decisive loss: Rebel victory: cities controlled | 14 | 12 | 10 | 40 | 11 (2) | 37% | 15 / 7 | 250 | 3 |
| 22 | alternate | v21 | win: Union victory: share of total income | 7 | 14 | 1 | 23 | 5 (4) | 67% | 22 / 22 | 506 | 0 |
| 23 | standard | v22 | decisive loss: Rebel victory: capital captured | 3 | 4 | 2 | 10 | 4 (0) | 16% | 14 / 14 | 339 | 0 |
| 24 | alternate | v23 | win: Union victory: share of total income | 13 | 22 | 12 | 40 | 11 (5) | 44% | 24 / 24 | 552 | 0 |
| 25 | standard | v24 | win: Union victory: capital captured | 3 | 6 | 0 | 10 | 3 (1) | 50% | 14 / 14 | 343 | 0 |
| 26 | alternate | v25 | win: Union victory: share of total income | 18 | 28 | 13 | 61 | 23 (13) | 52% | 23 / 23 | 479 | 0 |
| 27 | standard | v26 | decisive loss: Rebel victory: capital captured | 4 | 10 | 1 | 12 | 4 (2) | 42% | 14 / 13 | 313 | 0 |
| 28 | alternate | v27 | decisive loss: Rebel victory: cities controlled | 5 | 2 | 5 | 17 | 5 (1) | 29% | 16 / 11 | 676 | 0 |
| 29 | standard | v28 | decisive loss: Rebel victory: capital captured | 3 | 6 | 4 | 7 | 1 (0) | 33% | 14 / 12 | 472 | 0 |
| 30 | alternate | v29 | win: Union victory: share of total income | 6 | 18 | 0 | 20 | 5 (3) | 53% | 23 / 23 | 457 | 0 |
| 31 | standard | v30 | decisive loss: Rebel victory: capital captured | 19 | 19 | 14 | 65 | 15 (8) | 54% | 18 / 12 | 289 | 9 |
| 32 | alternate | v31 | win: Union victory: share of total income | 6 | 13 | 1 | 19 | 7 (6) | 53% | 23 / 23 | 641 | 0 |
| 33 | standard | v32 | decisive loss: Rebel victory: capital captured | 7 | 12 | 1 | 26 | 5 (1) | 40% | 19 / 19 | 315 | 1 |
| 34 | alternate | v33 | decisive loss: Rebel victory: cities controlled | 8 | 12 | 14 | 17 | 3 (1) | 34% | 17 / 12 | 732 | 0 |
| 35 | standard | v34 | held out: Rebel victory: time expired | 24 | 48 | 15 | 77 | 23 (9) | 41% | 26 / 24 | 430 | 2 |
| 36 | alternate | v35 | decisive loss: Rebel victory: capital captured | 7 | 20 | 1 | 20 | 6 (4) | 48% | 18 / 18 | 428 | 0 |
| 37 | standard | v36 | held out: Rebel victory: time expired | 24 | 37 | 23 | 75 | 23 (11) | 51% | 24 / 24 | 375 | 6 |
| 38 | alternate | v37 | win: Union victory: share of total income | 10 | 14 | 7 | 34 | 9 (5) | 53% | 22 / 22 | 460 | 0 |
| 39 | standard | v38 | held out: Rebel victory: time expired | 24 | 20 | 10 | 82 | 29 (11) | 44% | 20 / 10 | 289 | 1 |
| 40 | alternate | v39 | win: Union victory: share of total income | 11 | 27 | 8 | 33 | 11 (7) | 54% | 22 / 22 | 511 | 0 |
| 41 | standard | v40 | win: Union victory: capital captured | 23 | 36 | 25 | 51 | 18 (11) | 57% | 17 / 17 | 339 | 3 |
| 42 | alternate | v41 | decisive loss: Rebel victory: cities controlled | 10 | 10 | 9 | 27 | 10 (5) | 57% | 16 / 11 | 680 | 0 |
| 43 | standard | v42 | decisive loss: Rebel victory: capital captured | 2 | 4 | 0 | 7 | 1 (1) | 33% | 15 / 15 | 409 | 0 |
| 44 | alternate | v43 | win: Union victory: share of total income | 10 | 24 | 0 | 31 | 7 (1) | 42% | 22 / 22 | 399 | 0 |
| 45 | standard | v44 | decisive loss: Rebel victory: capital captured | 10 | 18 | 6 | 26 | 11 (3) | 43% | 13 / 12 | 374 | 1 |
| 46 | alternate | v44 | win: Union victory: share of total income | 10 | 23 | 7 | 28 | 3 (1) | 42% | 23 / 23 | 460 | 1 |
| 47 | standard | v45 | held out: Rebel victory: time expired | 24 | 35 | 14 | 89 | 37 (15) | 42% | 27 / 26 | 457 | 8 |
| 48 | alternate | v46 | win: Union victory: share of total income | 7 | 17 | 0 | 20 | 7 (3) | 53% | 23 / 23 | 466 | 0 |
| 49 | standard | v47 | decisive loss: Rebel victory: cities controlled | 19 | 22 | 3 | 63 | 12 (6) | 53% | 16 / 7 | 316 | 5 |
| 50 | alternate | v47 | win: Union victory: share of total income | 7 | 17 | 0 | 20 | 2 (1) | 50% | 22 / 22 | 438 | 0 |

## How the notebook changed

### Version 1, after game 1 (standard: Rebel victory: capital captured, 3 turns)

**Diagnosis.** Lost in July 1861 because Washington was left completely unguarded while Jackson was adjacent at Harper's Ferry. McDowell marched to Front Royal and Harper's Ferry rather than covering the capital, allowing Jackson's move into Washington to instantly trigger a Rebel sudden-death victory. In the West, A.S. Johnston bypassed borders to seize Indianapolis and Columbus due to dispersed Union forces.

**Strategy for the next game.** In the opening turns, secure and fortify Washington with a strong garrison to prevent sudden-death defeat. In the West, form a consolidated army under Grant or Buell to defeat Rebel field forces at Louisville before advancing southward. Maintain defensive lines across Ohio, Indiana, and Maryland before launching aggressive deep penetrations.

**Changes:**

- added: Never leave Washington empty while enemy forces are within striking distance; keep a garrison or blocking army in place. (Jackson walked straight into an undefended Washington on turn 3, ending the game immediately.)
- added: Do not advance past an active enemy army in Virginia if it leaves an open path to Washington. (McDowell advanced into Front Royal and Harper's Ferry without screening Washington from Jackson.)
- added: Defend northern border cities like Indianapolis and Cincinnati before pushing deep into Kentucky or Tennessee. (A.S. Johnston penetrated into Indiana and Ohio while McClellan and Pope pushed into Lexington/Nashville.)
- added: Concentrate forces with 'join' before attacking enemy commanders holding defensive terrain. (Attacking A.S. Johnston piecemeal at Louisville and Indianapolis led to consecutive bloody repulses.)
- added: Do not use fleet raiding early when ships are needed to defend seaports and prevent blockades. (Commerce raiding achieved negligible financial damage ($5-$34) while losing two ships to attrition.)

**Notebook:**

1. Never leave Washington empty while enemy forces are within striking distance; keep a garrison or blocking army in place.
2. Do not advance past an active enemy army in Virginia if it leaves an open path to Washington.
3. Defend northern border cities like Indianapolis and Cincinnati before pushing deep into Kentucky or Tennessee.
4. Concentrate forces with 'join' before attacking enemy commanders holding defensive terrain.
5. Do not use fleet raiding early when ships are needed to defend seaports and prevent blockades.

### Version 2, after game 2 (alternate: Rebel victory: cities controlled, 12 turns)

**Diagnosis.** The Union lost by city control in March 1863 because of passive early spending, allowing the treasury to hoard over $1000 in 1861 instead of max-recruiting every turn. This let the Confederacy mass 50k+ death stacks and sweep through Strasburg, Harpers Ferry, Baltimore, and Philadelphia while picking off small, unjoined Union garrisons.

**Strategy for the next game.** Maximize army recruitment every turn starting April 1861 in high-yield cities. Fortify Washington, Cincinnati, and Louisville, holding firm defense lines under Grant and Sherman while merging smaller units. Secure the Shenandoah/Baltimore approaches to prevent northern breakthroughs, and counter-attack only when outnumbering the enemy on favorable ground.

**Changes:**

- added: Spend treasury aggressively every turn on recruiting; never hoard excess gold when cities are vulnerable. (Hoarding cash in 1861 allowed the Rebels to field massive 50k stacks that overwhelmed Union positions.)
- added: Call 'troops' every turn and recruit in the highest-value core cities to maximize manpower growth. (Large cities yield significantly more recruits per $100 spent, accelerating troop buildup.)
- added: Block the Shenandoah and Baltimore corridors early to stop Confederate raids into Philadelphia and Harrisburg. (Jackson bypassed the frontier, captured Baltimore and Philadelphia, and triggered city-count defeat.)
- revised: Consolidate small detachments into main armies using 'join' rather than leaving small forces exposed. (Small outposts like Fremont at Manassas and Pope at Paducah were annihilated in isolation.)
- dropped: Do not use fleet raiding early when ships are needed to defend seaports and prevent blockades. (Commerce raiding was minor compared to the critical failure of ground recruitment and territorial defense.)

**Notebook:**

1. Spend treasury aggressively every turn on recruiting; never hoard excess gold when cities are vulnerable.
2. Call 'troops' every turn and recruit in the highest-value core cities to maximize manpower growth.
3. Fortify key frontier and border cities (Washington, Cincinnati, Louisville) early to gain defensive multipliers.
4. Consolidate small detachments into main armies using 'join' rather than leaving small forces exposed.
5. Block the Shenandoah and Baltimore corridors early to stop Confederate raids into Philadelphia and Harrisburg.
6. Never make low-odds attacks against entrenched defenders; hold fortified lines and let the enemy attack.
7. Rail top commanders (Grant, Sherman) directly to threatened fronts to command unified defense forces.
8. Keep Washington strongly garrisoned and fortified at level 2 at all times.
9. Maintain supply lines by avoiding overextended advances into enemy territory without secure friendly adjacencies.
10. Build ironclads once available in March 1862 to control coastal approaches and eliminate Rebel fleets.

### Version 3, after game 3 (standard: Rebel victory: capital captured, 7 turns)

**Diagnosis.** Lost on turn 7 due to an unforced capital loss: McDowell vacated Washington to seize Harper's Ferry, leaving the level 2 fort completely empty and allowing Bragg to capture Washington unopposed. Additionally, McClellan became cut off and supply-starved in Pittsburgh after multiple costly offensive marches against Jackson.

**Strategy for the next game.** Establish an unshakeable defensive baseline by fortifying Washington, Baltimore, and Cincinnati to level 2 with permanent garrisons that never vacate their cities. Use regular recruiting and drilling to expand field armies, maintaining secure, contiguous supply lines while letting Confederate forces exhaust themselves against Union fortifications before launching decisive counteroffensives.

**Changes:**

- added: NEVER vacate Washington: keep a dedicated garrison of at least 15,000 men inside Washington at all times to prevent sudden Rebel capture. (Ordering McDowell out of Washington left the capital completely undefended, resulting in instant defeat when Bragg walked in.)
- added: Do not waste naval assets on commerce raiding; fleet raid slowly loses ships for trivial economic damage. (Raiding destroyed all Union ships across several turns while yielding negligible Rebel economic damage.)
- revised: Maintain contiguous lines of friendly cities; armies cut off from friendly adjacencies quickly run out of supply and lose half combat power. (McClellan became isolated in Pittsburgh when Rebels took surrounding cities, causing crippling supply failure.)
- revised: Armies over 40,000 men move late in the turn sequence; keep field strike armies moderately sized (25k-35k) for better initiative. (McClellan's massive 46,000-man army consistently acted after Confederate armies moved into flanking positions.)

**Notebook:**

1. NEVER vacate Washington: keep a dedicated garrison of at least 15,000 men inside Washington at all times to prevent sudden Rebel capture.
2. Upgrade Washington and Baltimore forts to level 2 immediately; fortified garrisons defeat superior Rebel attacks consistently.
3. Call 'troops' every turn and spend treasury aggressively on recruiting in high-value, secure core cities.
4. Never initiate low-odds attacks against Rebel leaders; hold fortified positions and let Rebels break themselves attacking you.
5. Maintain contiguous lines of friendly cities; armies cut off from friendly adjacencies quickly run out of supply and lose half combat power.
6. Armies over 40,000 men move late in the turn sequence; keep field strike armies moderately sized (25k-35k) for better initiative.
7. Consolidate fragmented garrisons using 'join' rather than leaving small detachments to be destroyed in detail.
8. Do not waste naval assets on commerce raiding; fleet raid slowly loses ships for trivial economic damage.
9. Use rail movement to instantly reposition reserve armies or key generals to threatened frontier cities before marches resolve.
10. Drill idle garrisons to build experience up to leader rating limits when they are not actively required to move or reinforce.

### Version 4, after game 4 (alternate: Union victory: share of total income, 17 turns)

**Diagnosis.** Achieved a decisive economic victory by fortifying critical frontier hubs (Indianapolis, Baltimore, Washington) to level 2, where repeated Rebel assaults led by Lee were shattered at minimal friendly cost. Aggressive recruiting in high-income core cities, timely rail transfers of reinforcements, and methodical counter-offensives against depleted Rebel forces enabled steady expansion across the West and border states to surpass the 60% income victory threshold.

**Strategy for the next game.** Pursue an active defense-in-depth and economic expansion strategy: lock down Washington, Baltimore, and key western junction cities with level 2 forts and strong garrisons. Exhaust Confederate offensive stacks against these fortifications while recruiting in core cities, then use mobile field corps (25k-35k) and rail reserves to counter-punch, isolate, and capture border and Mississippi valley cities to trigger the 60% income victory condition.

**Changes:**

- revised: Upgrade key bastion forts (Washington, Baltimore, Indianapolis) to level 2 early; level 2 forts allow defenders to repel and destroy superior forces. (Fortifying Indianapolis to level 2 absorbed five consecutive assaults by Lee and Bragg, demonstrating that western chokepoints benefit from max fortifications just as much as eastern capitals.)
- added: Build ironclads from March 1862 onward to dominate naval combat and protect against Confederate blockade sorties. (Constructing ironclads secured total naval dominance in Philadelphia and enabled coastal operations without risking fleet elimination.)
- added: Use 'fleet invade' to seize isolated neutral ports like Jacksonville to safely expand city count and income share. (Amphibious landings captured undefended coastal ports without tying down major land field armies, accelerating economic victory.)
- added: Regularly inspect supply levels and manually resupply frontier armies before winter/spring attrition drops combat efficiency. (McDowell and McClellan suffered supply drops during campaigns; timely supply orders prevented severe combat debuffs.)
- dropped: Do not waste naval assets on commerce raiding; fleet raid slowly loses ships for trivial economic damage. (Replaced with active naval doctrine (ironclads and amphibious invasions) which proved far more strategically impactful.)

**Notebook:**

1. Never vacate Washington: maintain a dedicated garrison of at least 15,000 men inside the capital at all times to prevent sudden capture.
2. Upgrade key bastion forts (Washington, Baltimore, Indianapolis) to level 2 early; level 2 forts allow defenders to repel and destroy superior forces.
3. Call 'troops' every turn and spend treasury aggressively on recruiting in high-value, secure core cities.
4. Let Rebel field armies break themselves attacking fortified cities before launching counter-offensives against their depleted survivors.
5. Maintain contiguous lines of friendly cities; cut-off armies lose supply quickly and fight at half strength.
6. Keep field strike armies sized between 25k and 35k men; armies over 40k move late in the turn sequence and risk losing initiative.
7. Consolidate fragmented garrisons using 'join' to avoid leaving small detachments vulnerable to defeat in detail.
8. Use rail movement every turn possible to instantly reposition reserve armies or top generals to threatened frontier cities.
9. Drill idle garrisons to max leader ratings whenever they are not required to move, recruit, or fortify.
10. Build ironclads from March 1862 onward to dominate naval combat and protect against Confederate blockade sorties.
11. Use 'fleet invade' to seize isolated neutral ports like Jacksonville to safely expand city count and income share.
12. Regularly inspect supply levels and manually resupply frontier armies before winter/spring attrition drops combat efficiency.

### Version 5, after game 5 (standard: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** Passive containment and chasing enemy raiders allowed small Confederate forces (A.S. Johnston, Lee, Pemberton) to sweep through undefended Union interior cities (Indianapolis, Columbus, St. Louis, Springfield, Pittsburg, Philadelphia), achieving a 32-city victory condition by mid-1862. Additionally, McClellan and Buell repeatedly attacked top Confederate leaders defending in cities while under-supplied, taking repeated tactical defeats.

**Strategy for the next game.** Establish fortified defensive anchors in the East (Washington, Harper's Ferry, Baltimore) while actively recruiting garrisons to shield western/interior rail hubs (Cincinnati, Indianapolis, Louisville, St. Louis). Utilize strategic rail redeployment to cut off and trap encroaching Confederate raiding forces rather than pursuing them from behind. Avoid attacking high-rated Confederate generals on defense, forcing them to break themselves against fortified bastions before launching decisive counte

**Changes:**

- added: Never leave interior cities (Cincinnati, Indianapolis, St. Louis, Pittsburg) completely undefended when Rebel armies are nearby; uninhibited raiders capture territory rapidly. (Uncontested Rebel advances through empty western and middle states allowed the AI to win on city count by July 1862.)
- revised: Do not attack elite Confederate commanders (Lee, A.S. Johnston) entrenched in cities without overwhelming (2:1+) odds; let them attack fortified Union positions instead. (Repeated assaults by McClellan and Buell against Lee and Johnston resulted in consistent defeats and army exhaustion.)
- revised: Use rail movement every turn to immediately shift reinforcements directly ahead of advancing enemy raiders rather than chasing them on foot. (Chasing fast enemy leaders across the map on foot left Union forces one step behind and vulnerable to being cut off.)

**Notebook:**

1. Never leave interior cities (Cincinnati, Indianapolis, St. Louis, Pittsburg) completely undefended when Rebel armies are nearby; uninhibited raiders capture territory rapidly.
2. Do not attack elite Confederate commanders (Lee, A.S. Johnston) entrenched in cities without overwhelming (2:1+) odds; let them attack fortified Union positions instead.
3. Always maintain a dedicated garrison of at least 15,000 men inside Washington to prevent sudden decapitation strikes.
4. Fortify key frontier bastions (Harper's Ferry, Baltimore) to level 2 early; high fort levels routinely shatter Confederate assaults.
5. Use rail movement every turn to immediately shift reinforcements directly ahead of advancing enemy raiders rather than chasing them on foot.
6. Call 'troops' every turn and invest funds aggressively into raising new garrisons across threatened northern cities.
7. Ensure supply lines remain contiguous; cut-off armies drop to zero supply and fight at half combat effectiveness.
8. Keep mobile field strike forces between 25k and 35k men; armies exceeding 40k move late in the turn sequence.
9. Consolidate scattered garrison forces using 'join' under the highest-rated general to prevent piecemeal destruction.
10. Manually resupply field armies before combat or march orders when supply drops to 1 or below.
11. Construct ironclads starting March 1862 to command the coastline and suppress Confederate blockades.
12. Deploy fleet raids and amphibious landings to drain Confederate income and secure undefended coastal cities.

### Version 6, after game 6 (alternate: Union victory: share of total income, 5 turns)

**Diagnosis.** Fast 5-turn economic victory achieved by aggressively claiming neutral border cities on turn 1, maintaining high recruitment volume, using rail to plug defensive gaps in Cincinnati, sustaining naval commerce raids, and exploiting an under-garrisoned Richmond for a rapid economic and territorial collapse.

**Strategy for the next game.** Aggressively secure neutral border cities on turn 1, maximize turn-by-turn recruitment across northern industrial centers, rail reinforcements to hold defensive lines in the West, continuously raid enemy commerce, and push concentrated field forces into exposed Confederate hubs and Richmond to trigger an early economic or territorial victory.

**Changes:**

- added: Grab key neutral border cities (Baltimore, Louisville, Paducah, Manassas) on turn 1 to rapidly expand tax income and secure forward lines. (Immediate turn-1 expansion into neutral border hubs established an overwhelming income advantage that led to a 5-turn win.)
- added: Seize Richmond immediately if the enemy leaves it weakly guarded; capturing the capital heavily swings income and supply. (A rapid strike on an exposed Richmond in late 1861 decisively triggered the victory condition.)
- dropped: Construct ironclads starting March 1862 to command the coastline and suppress Confederate blockades. (Too late-game specific and unnecessary when games can be decided rapidly in 1861 via commerce raiding and land dominance.)

**Notebook:**

1. Grab key neutral border cities (Baltimore, Louisville, Paducah, Manassas) on turn 1 to rapidly expand tax income and secure forward lines.
2. Call 'troops' every turn and spend surplus revenue recruiting across available northern and border cities to outpace Rebel manpower.
3. Use rail transit every turn to reposition fresh armies directly into threatened border cities ahead of advancing Rebel raiders.
4. Maintain a garrison in Washington of at least 15,000 men and upgrade its fort level early to deter sudden Confederate decapitation thrusts.
5. Never leave interior frontier hubs (Cincinnati, Indianapolis, St. Louis) empty; hold them defensively where fort multipliers punish attackers.
6. Keep mobile field armies between 25k and 35k men so they move early in turn resolution; armies over 40k move late.
7. Execute naval commerce raids continuously with available fleets to steadily deplete Confederate treasury and hamper their recruitment.
8. Seize Richmond immediately if the enemy leaves it weakly guarded; capturing the capital heavily swings income and supply.
9. Do not attack entrenched elite generals in fortified cities without overwhelming local superiority; wear them down defensively first.
10. Maintain contiguous supply lines through friendly neighbors; cut-off armies lose supply and fight at half effectiveness.
11. Merge scattered garrisons using 'join' under high-rated leaders to build efficient, high-initiative strike forces.
12. Manually buy supply for key attacking or defending field armies whenever their supply level falls to 1 or below.

### Version 7, after game 7 (standard: Union victory: cities controlled, 22 turns)

**Diagnosis.** Game 7 succeeded by systematically expanding across the Western and Deep South theatres (Tennessee, Georgia, Alabama, Mississippi, Carolinas) while containing Rebel forces in Virginia. Continuous fleet raiding severely depleted Rebel finances, and reaching 32 cities proved far faster and safer than assaulting the massive Richmond fortress.

**Strategy for the next game.** Open with rapid border city capture (Baltimore, Louisville, Paducah, Manassas) and commence non-stop commerce raiding. Build western offensive columns under Grant and Buell to push down the Mississippi and through Tennessee into Georgia and the Carolinas, while holding Virginia defensively. Achieve strategic victory by reaching 32 controlled cities.

**Changes:**

- revised: Win via 32-city control by sweeping lightly defended southern cities rather than assaulting heavily fortified capitals like Richmond. (Assaulting 77k+ troops in fort-2 Richmond caused heavy casualties; taking open peripheral cities (Savannah, Charleston, Raleigh, Columbia) easily delivered the 32-city win.)
- revised: Do not attack entrenched elite generals in level-2 fortified cities without overwhelming local superiority; bypass or starve them. (Frontal attacks against Lee in New Orleans and Johnston in Richmond failed due to high defensive fort multipliers.)

**Notebook:**

1. Grab key neutral border cities (Baltimore, Louisville, Paducah, Manassas) on turn 1 to expand tax income and secure forward lines.
2. Call 'troops' every turn and spend surplus revenue recruiting across available northern and border cities to outpace Rebel manpower.
3. Use rail transit every turn to reposition fresh armies directly into threatened border hubs or forward assembly areas.
4. Execute naval commerce raids continuously with available fleets to steadily deplete Confederate treasury and hamper recruitment.
5. Win via 32-city control by sweeping lightly defended southern cities rather than assaulting heavily fortified capitals like Richmond.
6. Keep mobile field armies between 25k and 35k men so they move early in turn resolution; armies over 40k move late.
7. Maintain contiguous supply lines; cut-off armies fight at half effectiveness and rapidly lose strength.
8. Never leave interior frontier hubs (Cincinnati, Indianapolis, St. Louis) empty; small garrisons deter or delay enemy raiders.
9. Merge scattered garrisons using 'join' under high-rated leaders (Grant, Sherman, Buell) to build decisive strike forces.
10. Manually buy supply for key attacking or defending field armies whenever their supply level falls to 1 or below.
11. Do not attack entrenched elite generals in level-2 fortified cities without overwhelming local superiority; bypass or starve them.
12. Maintain a garrison in Washington of at least 15,000 men and upgrade its fort level early to deter sudden Confederate thrusts.

### Version 8, after game 8 (alternate: Rebel victory: share of total income, 6 turns)

**Diagnosis.** The Union suffered a sudden income-share defeat in early 1862 after Stuart and J.E. Johnston bypassed forward units and seized undefended core Northern cities (Philadelphia, Indianapolis, Columbus).

**Strategy for the next game.** Secure neutral border hubs on turn 1 while leaving screening detachments in key Northern economic hubs to prevent enemy cavalry and armies from penetrating the rear, then leverage combined armies under Grant and Sherman to roll up Confederate frontier cities.

**Changes:**

- revised: Win by seizing 28 cities or establishing income dominance by capturing vulnerable peripheral Confederate cities. (Corrected the 32-city threshold to the accurate 28-city requirement for alternate maps and emphasized guarding income share.)
- revised: Never leave Northern core and hub cities (Philly, Columbus, Indianapolis, Cincinnati) empty; raiders can cause income defeat. (Stuart and Johnston marched directly through empty Northern economic centers to trigger a Confederate income victory.)

**Notebook:**

1. Grab key neutral border cities (Baltimore, Louisville, Paducah, Manassas) on turn 1 to expand tax income and secure forward lines.
2. Call 'troops' every turn and recruit across available northern and border cities to maintain superior overall manpower.
3. Use rail transit every turn to reposition fresh armies directly into threatened border hubs or forward assembly areas.
4. Execute naval commerce raids continuously with available fleets to steadily deplete Confederate treasury and hamper recruitment.
5. Win by seizing 28 cities or establishing income dominance by capturing vulnerable peripheral Confederate cities.
6. Keep mobile field armies between 25k and 35k men so they move early in turn resolution; armies over 40k move late.
7. Maintain contiguous supply lines; cut-off armies fight at half effectiveness and rapidly lose strength.
8. Never leave Northern core and hub cities (Philly, Columbus, Indianapolis, Cincinnati) empty; raiders can cause income defeat.
9. Merge scattered garrisons using 'join' under high-rated leaders (Grant, Sherman, Thomas) to build decisive strike forces.
10. Manually buy supply for key attacking or defending field armies whenever their supply level falls to 1 or below.
11. Do not attack entrenched elite generals in level-2 fortified cities without overwhelming local superiority; bypass or starve them.
12. Maintain a garrison in Washington of at least 15,000 men and upgrade its fort level early to deter sudden Confederate thrusts.

### Version 9, after game 9 (standard: Rebel victory: cities controlled, 15 turns)

**Diagnosis.** We overextended into the deep South (capturing Richmond and Norfolk with McDowell) while neglecting northern territorial defense. Confederate raiders and mega-stacks (Jackson and A.S. Johnston) repeatedly took Washington, Philadelphia, Harrisburg, and Columbus, gutting our income and cutting supply lines. Our isolated armies fought repeatedly out of supply and were eliminated in detail.

**Strategy for the next game.** Next game, maintain a tight, cohesive defensive front protecting Washington, Baltimore, Philadelphia, and the Ohio River line with fortified garrisons. Concentrate offensive manpower into two 35k-40k strike groups led by Grant and McClellan. Defeat Confederate incursions into the North before pushing down the Mississippi or into Virginia along secure, resupplied corridors.

**Changes:**

- revised: Do not advance deep into enemy territory unless your home base and flanks are secure; contiguous friendly connections are required to prevent cut-off attrition. (McDowell advanced to Richmond and Norfolk while the Union core collapsed behind him, cutting him off from supply and failing to stop the loss of the game.)
- revised: Never order an attack with an army at 0 supply; check supply levels and use 'supply' command before moving into combat. (Multiple armies moved and fought while out of supplies, suffering severe combat penalties and attrition.)
- added: Eliminate enemy penetrations into the North immediately to maintain tax income and prevent Rebel victory by city count. (Letting Jackson and Johnston roam Pennsylvania and Ohio gave the Confederacy the 32+ cities needed to win.)
- dropped: Win by seizing 28 cities or establishing income dominance by capturing vulnerable peripheral Confederate cities. (Going for peripheral captures diverted strength from protecting core high-value northern cities.)

**Notebook:**

1. Prioritize securing and fortifying Washington and Baltimore on Turn 1; losing Washington forfeits the +100 income bonus and destroys the supply economy.
2. Call 'troops' and recruit every turn, concentrating new recruits into core armies rather than leaving scattered understrength detachments.
3. Do not advance deep into enemy territory unless your home base and flanks are secure; contiguous friendly connections are required to prevent cut-off attrition.
4. Never order an attack with an army at 0 supply; check supply levels and use 'supply' command before moving into combat.
5. Form 2-3 concentrated field armies of 30,000 to 40,000 men under top generals (Grant, Thomas, McClellan) rather than maintaining 5+ small, vulnerable forces.
6. Defend northern anchor cities (Philadelphia, Harrisburg, Columbus, Cincinnati) with fortified garrisons to block Confederate invasion corridors.
7. Use rail transit every turn to rapidly shift reinforcements or retreat threatened garrisons to fortified positions.
8. When facing enemy stacks over 30,000 men led by Lee or Jackson, defend behind forts rather than attacking them in the open.
9. Consolidate adjacent armies in the same city using 'join' before launching major counter-offensives.
10. Do not chase peripheral Confederate ports while the main Rebel army threatens your capital and core income cities.
11. Keep fleets raiding commerce to suppress Rebel income, but do not rely on it alone to stop enemy recruitment if Rebels hold 25+ cities.
12. Eliminate enemy penetrations into the North immediately to maintain tax income and prevent Rebel victory by city count.

### Version 10, after game 10 (alternate: Union victory: share of total income, 6 turns)

**Diagnosis.** Rapid 6-turn victory via economic dominance. Early border-city captures (Baltimore, Louisville, Manassas) and commerce raiding built an insurmountable income lead. Merging large armies and railing reserves to frontline battles enabled capturing Richmond and crushing Rebel counter-offensives.

**Strategy for the next game.** Open with rapid border city expansion and Turn 1 commerce raiding. Maximize recruitment into concentrated western and eastern field armies. Use railroads to reinforce threatened sectors and project overwhelming force against Richmond and the Tennessee corridor to trigger an early economic or capital-capture victory.

**Changes:**

- added: Secure neutral border cities (Baltimore, Manassas, Louisville, Strasburg) on Turn 1 to expand income base and establish defensive buffers. (Early aggressive expansion into neutral border territory established immediate income dominance and safe operating depth.)
- added: Rail a large army into newly captured Richmond immediately to secure it against Confederate counter-attacks. (Railing McDowell's 30k force into Richmond in Jan 1862 cemented the capture and blocked Rebel recapture attempts.)
- revised: Order 'fleet raid' from Turn 1 onward to bleed Rebel treasury and suppress their recruitment capacity. (Continuous commerce raiding drained $50-$80 every turn, crippling Rebel recruitment and accelerating economic victory.)
- dropped: Defend northern anchor cities (Philadelphia, Harrisburg, Columbus, Cincinnati) with fortified garrisons to block Confederate invasion corridors. (Fortifying deep northern cities is too passive; holding the forward border cities and St. Louis/Cincinnati with active field armies is far more effective.)

**Notebook:**

1. Secure neutral border cities (Baltimore, Manassas, Louisville, Strasburg) on Turn 1 to expand income base and establish defensive buffers.
2. Call 'troops' and recruit heavily every turn into frontline cities to build decisive numerical superiority.
3. Order 'fleet raid' from Turn 1 onward to bleed Rebel treasury and suppress their recruitment capacity.
4. Use 'rail' every turn to rush reinforcements into threatened cities before combat resolves.
5. Use 'join' to merge armies in key hubs (Cincinnati, Paducah, Washington) into 30,000+ man strike forces under top generals.
6. Defend key hubs (St. Louis, Cincinnati, Indianapolis) with substantial garrisons to repel aggressive Confederate probes.
7. Pounce on lightly defended Richmond or isolated Rebel armies whenever a concentrated force is adjacent.
8. Rail a large army into newly captured Richmond immediately to secure it against Confederate counter-attacks.
9. Check supply status in winter/spring and manually supply combat armies before attacking to avoid half-strength penalties.
10. Do not attack across rivers or into fortified cities without overwhelming numbers and full supply.
11. Never leave western anchor cities like St. Louis under-garrisoned on Turn 1 against western Confederate pushes.
12. Hold Washington continuously to protect the vital +100 income bonus and supply line integrity.

### Version 11, after game 11 (standard: Union victory: capital captured, 17 turns)

**Diagnosis.** Game 11 was won in November 1863 by capturing Richmond with a concentrated 94k+ army under Grant. Continuous fleet raiding deprived the Confederacy of income, while strategic use of rail and join allowed us to amass an overwhelming strike force at Fredericksburg. Fortifying Washington to Level 2 proved vital in repelling desperate late-game Confederate raids on our capital.

**Strategy for the next game.** Execute a dual-track strategy: in the East, fortify Washington to Level 2, use rail and join at Fredericksburg to create an 80,000+ man army under Grant, and capture Richmond in 1863; in the West, deploy mobile garrisons to contain raiders while advancing deep into undefended Confederate interior cities; maintain fleet raiding every turn to starve the Rebel war economy.

**Changes:**

- revised: Fortify Washington to Level 2 early to guarantee capital security and protect the critical +100 income bonus. (Fortifying Washington to level 2 easily repelled Stuart's surprise counter-attack without diverting frontline field armies.)
- revised: Use 'join' to build an 80,000+ man mega-army under Grant at Fredericksburg to crush Richmond's garrison. (A 30k army is insufficient against level 2 Richmond forts; assembling 80k-100k+ under Grant ensures breakthrough.)
- added: Attack fortified capitals with 2:1+ numerical advantage; follow up failed assaults immediately before defenders recover. (Grant failed the first assault against 44k defenders in level 2 forts, but broke through on the second turn once defenders took losses.)
- added: Advance aggressively in the West against undefended Confederate cities (Nashville, Chattanooga, Atlanta, Montgomery). (Buell's unchecked sweep through Tennessee and Georgia stretched Confederate armies and boosted Union income.)

**Notebook:**

1. Secure neutral border cities (Baltimore, Manassas, Louisville) on Turn 1 to expand income and establish defensive depth.
2. Order 'fleet raid' from Turn 1 onward to continually drain Rebel commerce and cripple their recruiting funds.
3. Call 'troops' and recruit heavily each turn in high-yield cities (Baltimore, Pittsburg, Columbus, Washington).
4. Fortify Washington to Level 2 early to guarantee capital security and protect the critical +100 income bonus.
5. Use 'rail' every turn to concentrate reinforcements into frontline staging hubs like Fredericksburg before marching.
6. Use 'join' to build an 80,000+ man mega-army under Grant at Fredericksburg to crush Richmond's garrison.
7. Attack fortified capitals with 2:1+ numerical advantage; follow up failed assaults immediately before defenders recover.
8. Manually purchase supply for combat armies at 1 or less supply before launching attacks to prevent half-strength penalties.
9. Maintain garrisons at key interior rail hubs (Cincinnati, Louisville, St. Louis) to contain mobile Rebel raiders.
10. Isolate and eliminate cut-off Rebel armies with converged multi-army attacks to force surrenders.
11. Advance aggressively in the West against undefended Confederate cities (Nashville, Chattanooga, Atlanta, Montgomery).
12. Keep open rail lines and friendly adjacent cities to all active field armies to prevent winter supply attrition.

### Version 12, after game 12 (alternate: Union victory: share of total income, 4 turns)

**Diagnosis.** A swift 4-turn victory by capturing key Confederate production centers. Seizing neutral border cities on Turn 1 boosted early income and allowed Turn 1 defense of St. Louis. Grant's rapid unopposed march down the Mississippi (Paducah-Memphis-Vicksburg-Jackson) combined with an early strike to capture weakly garrisoned Richmond pushed Union income over the 60% threshold by October 1861.

**Strategy for the next game.** Execute a high-tempo two-front blitz: expand across neutral border cities on Turn 1 while reinforcing St. Louis and launching naval raids. In the West, drive Grant aggressively down the Mississippi corridor to take Memphis, Vicksburg, and Jackson. In the East, push McClellan and Fremont through northern Virginia to assault Richmond as soon as an opening appears, using rail to reinforce threatened interior points.

**Changes:**

- revised: Advance rapidly down the Mississippi with Grant (Paducah to Memphis to Vicksburg) to grab high-value, lightly guarded Rebel cities. (Grant is positioned in the West at start; driving him down the Mississippi seizes huge chunks of Rebel income faster than staging him east.)
- added: Recruit at St. Louis on Turn 1 to easily repel A.S. Johnston's early Missouri incursions. (Reinforcing Pope in St. Louis immediately on Turn 1 reliably defeats A.S. Johnston's scripted opening attack.)
- added: Exploit lightly garrisoned enemy capitals; capture Richmond immediately if Stuart or Lee leaves it under-defended. (Richmond was defended by only 1,200 men in August 1861, enabling McClellan to seize it easily and trigger a rapid income win.)

**Notebook:**

1. Secure neutral border cities (Baltimore, Strasburg, Manassas, Louisville, Paducah) on Turn 1 to expand income and secure frontlines.
2. Order 'fleet raid' from Turn 1 onward to continually drain Rebel commerce and restrict their recruitment.
3. Recruit at St. Louis on Turn 1 to easily repel A.S. Johnston's early Missouri incursions.
4. Advance rapidly down the Mississippi with Grant (Paducah to Memphis to Vicksburg) to grab high-value, lightly guarded Rebel cities.
5. Exploit lightly garrisoned enemy capitals; capture Richmond immediately if Stuart or Lee leaves it under-defended.
6. Use 'rail' every turn to reposition reinforcements or counter Rebel raiders threatening interior hubs like Columbus or Cincinnati.
7. Fortify Washington and Richmond after capture to protect capital income bonuses and defend against counterattacks.
8. Use 'join' in frontline hubs to combine fragmented units under 4-5 star commanders before major battles.
9. Check city recruit yields with 'troops' and spend excess income reinforcing high-capacity northern industrial cities.
10. Buy supply manually whenever an active combat army drops to 1 supply to prevent fighting at half strength.
11. Pursue multi-pronged advances in the East and West simultaneously to divide Confederate defense forces.
12. Keep supply corridors and rail links connected behind advancing columns to prevent winter supply decay.

### Version 13, after game 13 (standard: Union victory: capital captured, 15 turns)

**Diagnosis.** The Union achieved a decisive capital-capture victory in July 1863 by massing a 123,000-man strike force under Grant at Manassas and overwhelming Jackson's level-2 fort at Richmond. Consistent commerce raiding starved the Confederacy of funds, while tactical use of rail allowed rapid shifting of reserves to contain Rebel deep raids across Ohio, Pennsylvania, and Missouri.

**Strategy for the next game.** Open by seizing border hubs (Baltimore, Manassas, Louisville, Paducah) and initiating non-stop fleet commerce raiding. Contain Confederate border incursions using rail mobility and local superiority, then concentrate Northern manpower into an unstoppable 100,000+ man strike corps under Grant to storm Richmond for a capital-capture victory.

**Changes:**

- revised: Assemble a 100k+ mega-army under Grant using 'join' at Manassas/Washington to decisively storm fortified Richmond for a swift capital win. (Massing over 120k men under Grant successfully broke through Richmond's level-2 forts despite Jackson defending, securing immediate victory.)
- revised: Avoid deep westward or southern solo advances without maintaining contiguous friendly cities to prevent chronic out-of-supply penalties. (McClellan's deep push down the Mississippi frequently ran out of supplies and suffered attrition without securing continuous lines.)
- added: Trap and cut off overextended Rebel raiders so defeated forces surrender entirely rather than retreating. (Surrounding Pemberton in Louisville and Ashby in Lexington forced full surrenders, eliminating thousands of Rebel troops permanently.)
- added: When rebuilding the fleet or adding ironclads, ensure syntax matches active fleet status (use 'build ironclad' once a fleet exists). (Eliminated illegal fleet order refusals by respecting naval command constraints.)

**Notebook:**

1. Secure neutral border cities (Baltimore, Manassas, Louisville, Paducah) on Turn 1 to establish defensive perimeters and expand income.
2. Keep Union fleet continuously on 'fleet raid' to systematically deplete Rebel treasury and curb their recruitment capacity.
3. Assemble a 100k+ mega-army under Grant using 'join' at Manassas/Washington to decisively storm fortified Richmond for a swift capital win.
4. Trap and cut off overextended Rebel raiders so defeated forces surrender entirely rather than retreating.
5. Use 'rail' every turn to transport recruits and high-rated generals directly into threatened sectors or staging hubs.
6. Avoid deep westward or southern solo advances without maintaining contiguous friendly cities to prevent chronic out-of-supply penalties.
7. Do not attack fortified enemy armies without overwhelming numerical superiority (odds 45%+); mass troops before attacking.
8. Use 'join' in frontline staging cities to combine fragmented brigades under 4-5 star commanders before launching major assaults.
9. Check recruit pools with 'troops' each turn and invest treasury into high-yield northern cities like Washington, Baltimore, and Cincinnati.
10. Buy supply manually whenever combat armies drop to 1 supply to prevent fighting at half strength or suffering winter attrition.
11. Keep garrisons in Washington and key border junctions to deflect counter-offensives from high-rated Rebel commanders.
12. When rebuilding the fleet or adding ironclads, ensure syntax matches active fleet status (use 'build ironclad' once a fleet exists).

### Version 14, after game 14 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** Over-focusing on building a massive army in Washington left the Midwest and Ohio Valley wide open. Unchecked Rebel generals captured St Louis, Springfield, Indianapolis, Louisville, Cincinnati, and Baltimore, triggering an early 28-city Confederate victory.

**Strategy for the next game.** Execute a dual-front strategy: quickly assemble a 70k+ strike force under Grant to assault Richmond within 3-4 turns, while actively recruiting and garrisoning in the Midwest (Cincinnati, Columbus, St Louis) to prevent rapid Rebel city-control victories.

**Changes:**

- added: Defend Ohio Valley and Midwest hubs (Cincinnati, Indianapolis, St Louis); never let Rebel raiders sweep empty cities toward a 28-city win. (Rebels won on Turn 5 by reaching 28 cities because the entire western and midwestern theater was left undefended.)
- revised: Assemble a 70k-100k army under Grant to strike Richmond quickly before Rebels can expand across the western map. (Waiting too many turns to build a 100k+ mega-army delays the capital strike and cedes map control.)
- dropped: When rebuilding the fleet or adding ironclads, ensure syntax matches active fleet status (use 'build ironclad' once a fleet exists). (Syntax nuances are secondary to vital operational defense against Confederate rapid territorial expansion.)

**Notebook:**

1. Secure neutral border cities (Baltimore, Manassas, Louisville, Paducah) on Turn 1 to establish defensive perimeters and expand income.
2. Defend Ohio Valley and Midwest hubs (Cincinnati, Indianapolis, St Louis); never let Rebel raiders sweep empty cities toward a 28-city win.
3. Keep Union fleet continuously on 'fleet raid' to systematically deplete Rebel treasury and curb their recruitment capacity.
4. Assemble a 70k-100k army under Grant to strike Richmond quickly before Rebels can expand across the western map.
5. Trap and cut off overextended Rebel raiders so defeated forces surrender entirely rather than retreating.
6. Use 'rail' every turn to transport recruits and high-rated generals directly into threatened sectors or staging hubs.
7. Avoid deep westward or southern solo advances without maintaining contiguous friendly cities to prevent chronic out-of-supply penalties.
8. Do not attack fortified enemy armies without overwhelming numerical superiority (odds 45%+); mass troops before attacking.
9. Use 'join' in frontline staging cities to combine fragmented brigades under 4-5 star commanders before launching major assaults.
10. Check recruit pools with 'troops' each turn and invest treasury into high-yield northern cities like Washington, Baltimore, and Cincinnati.
11. Buy supply manually whenever combat armies drop to 1 supply to prevent fighting at half strength or suffering winter attrition.
12. Keep active garrisons in Washington and key border junctions to deflect counter-offensives from high-rated Rebel commanders.

### Version 15, after game 15 (standard: Rebel victory: capital captured, 14 turns)

**Diagnosis.** Lost in May 1863 due to leaving Washington entirely undefended while Beauregard was adjacent in Harper's Ferry, allowing an immediate Rebel capital capture. Additionally, launching sequential uncombined attacks into Baltimore chewed up Union divisions, and Buell's isolated western moves ended in surrender.

**Strategy for the next game.** Lock down Washington and key border junctions with fortified garrisons while raiding Confederate trade by sea. Methodically consolidate northern recruits into a 60k-80k army under Grant, maintaining strict supply links and merging forces before launching high-odds assaults on Rebel strongpoints.

**Changes:**

- revised: Never leave Washington unoccupied if an enemy army occupies Harper's Ferry, Manassas, or Baltimore; maintain a dedicated garrison. (Game 15 was lost instantly when Washington was left empty and Beauregard walked in unopposed from Harper's Ferry.)
- revised: Merge forces using 'join' into a single massive stack before attacking a concentrated enemy; never send multiple separate armies sequentially. (Attacking Baltimore sequentially with three separate corps resulted in three low-odds defeats in July 1862 instead of one decisive victory.)
- revised: Avoid deep solo advances down the Mississippi without contiguous friendly supply lines to prevent army isolation and surrender. (Buell's isolated movements deep in the West left him cut off, out of supply, and eventually forced him to surrender.)

**Notebook:**

1. Never leave Washington unoccupied if an enemy army occupies Harper's Ferry, Manassas, or Baltimore; maintain a dedicated garrison.
2. Merge forces using 'join' into a single massive stack before attacking a concentrated enemy; never send multiple separate armies sequentially.
3. Secure neutral border cities (Baltimore, Manassas, Louisville, Paducah) on Turn 1 to expand income and establish defensive buffers.
4. Defend Ohio Valley hubs (Cincinnati, Indianapolis, Columbus); never allow Rebel raiders to sweep empty northern cities.
5. Keep Union fleet continuously on 'fleet raid' to deplete Rebel treasury and suppress enemy reinforcement rates.
6. Buy supply manually whenever an active army drops to 1 supply to avoid half-strength combat penalties and winter attrition.
7. Avoid deep solo advances down the Mississippi without contiguous friendly supply lines to prevent army isolation and surrender.
8. Do not attack fortified or concentrated defenders without overwhelming numbers and favorable odds (at least 50%+).
9. Use 'rail' every turn to rapidly reposition high-rated commanders and reinforcements directly to threatened sectors.
10. Check recruit options with 'troops' every turn and invest in high-yield cities like Washington, Baltimore, and Cincinnati.
11. Trap and cut off retreat routes of overextended Rebel raiders so defeated forces surrender completely.
12. Consolidate frontline commands under 4-5 star generals (Grant, McClellan) rather than operating fragmented weak corps.

### Version 16, after game 16 (alternate: Rebel victory: share of total income, 7 turns)

**Diagnosis.** Lost on Rebel income threshold (60% income/27 cities) in May 1862 despite having a 2:1 troop advantage. J.E. Johnston and Beauregard slipped behind Union lines into un-garrisoned northern and eastern cities (Harper's Ferry, Baltimore, Philadelphia, Cincinnati), capturing high-income territory unopposed while Union armies drilled and consolidated away from threats.

**Strategy for the next game.** In the next game, maintain tight territorial defense across Maryland, Pennsylvania, and the Ohio Valley. Rapidly intercept any Confederate units crossing the border before executing southern offensive operations, ensuring Union income dominance is protected.

**Changes:**

- added: Never leave rear northern cities (Philadelphia, Harrisburg, Baltimore, Columbus) ungarrisoned; Rebel raiders will capture them and trigger an early income loss. (J.E. Johnston took Harper's Ferry, Baltimore, and Philadelphia uncontested, giving the Confederacy the 60% income victory in early 1862.)
- added: Prioritize intercepting and destroying deep enemy raiders over offensive pushes into Confederate interior territory. (Pushing into Nashville and Fort Donelson while raiders rampaged through Maryland, Pennsylvania, and Ohio caused rapid territorial collapse.)
- added: Reinforce St. Louis with recruits or rail reinforcements immediately; fortifying a depleted garrison under 2,000 men cannot hold against 10,000+ attackers. (St. Louis held three attacks at level 2 forts but was annihilated when Jackson arrived with 14k against Pope's 500 men.)
- dropped: Avoid deep solo advances down the Mississippi without contiguous friendly supply lines to prevent army isolation and surrender. (Replaced with higher-priority defensive lessons preventing immediate economic defeat from Rebel raiders.)
- dropped: Trap and cut off retreat routes of overextended Rebel raiders so defeated forces surrender completely. (Replaced by direct raider interception and homeland security imperatives.)
- dropped: Consolidate frontline commands under 4-5 star generals (Grant, McClellan) rather than operating fragmented weak corps. (Redundant with existing consolidation and rail repositioning guidelines.)

**Notebook:**

1. Never leave rear northern cities (Philadelphia, Harrisburg, Baltimore, Columbus) ungarrisoned; Rebel raiders will capture them and trigger an early income loss.
2. Prioritize intercepting and destroying deep enemy raiders over offensive pushes into Confederate interior territory.
3. Reinforce St. Louis with recruits or rail reinforcements immediately; fortifying a depleted garrison under 2,000 men cannot hold against 10,000+ attackers.
4. Secure neutral border cities (Baltimore, Manassas, Louisville, Paducah) on Turn 1 to expand income and establish defensive buffers.
5. Defend Ohio Valley hubs (Cincinnati, Indianapolis, Columbus); never allow Rebel raiders to sweep empty northern cities.
6. Merge forces using 'join' into a single stack before attacking concentrated enemies; never attack with piecemeal detachments.
7. Keep Union fleet continuously on 'fleet raid' to deplete Rebel treasury and suppress enemy reinforcement rates.
8. Buy supply manually whenever an active army drops to 1 supply to avoid half-strength combat penalties and winter attrition.
9. Do not attack fortified or concentrated defenders without overwhelming numbers and favorable odds (at least 50%+).
10. Use 'rail' every turn to rapidly reposition high-rated commanders and reinforcements directly to threatened sectors.
11. Check recruit options with 'troops' every turn and invest in high-yield cities like Washington, Baltimore, and Cincinnati.
12. Never leave Washington unoccupied if an enemy army occupies Harper's Ferry, Manassas, or Baltimore; maintain a dedicated garrison.

### Version 17, after game 17 (standard: Rebel victory: time expired, 24 turns)

**Diagnosis.** In Game 17, the Union survived all 24 turns but lost on time because constant Rebel raiders ping-ponging across Pennsylvania and Ohio kept major Union field armies bogged down in defensive recovery. Isolated deep-south raids by small forces (McDowell) were eventually encircled and destroyed, while key attacks were launched with unsupplied armies fighting at half strength.

**Strategy for the next game.** Lock down the northern perimeter with dedicated garrisons and fortresses, use concentrated, fully-supplied field armies under top generals to rapidly trap and destroy Rebel incursions, and advance southward methodically along railroad corridors rather than sending isolated raiders.

**Changes:**

- added: Never attack with an army at 0 supply; unsupplied armies fight at half strength and suffer disastrous combat odds. (McClellan repeatedly attacked Pemberton while out of supply, drastically reducing combat effectiveness and failing to dislodge him.)
- added: Do not push small, isolated raiding detachments into the deep South without secure supply lines and retreat paths. (McDowell marched deep into Mississippi and Georgia with under 7,000 men and was cut off, out of supply, and destroyed at Atlanta.)
- revised: Maintain permanent garrisons in critical northern border hubs (Washington, Baltimore, Cincinnati, Columbus). (Pemberton and Jackson repeatedly captured unguarded northern hubs, forcing massive diversions of Union main armies.)

**Notebook:**

1. Never attack with an army at 0 supply; unsupplied armies fight at half strength and suffer disastrous combat odds.
2. Prioritize intercepting and trapping enemy raiders in the Northeast and Ohio before launching deep southern pushes.
3. Do not push small, isolated raiding detachments into the deep South without secure supply lines and retreat paths.
4. Maintain permanent garrisons in critical northern border hubs (Washington, Baltimore, Cincinnati, Columbus).
5. Consolidate field armies using 'join' before attacking fortified or concentrated enemy positions.
6. Secure neutral border cities (Baltimore, Louisville, Paducah) on Turn 1 for income and forward staging.
7. Keep Union fleet continuously on 'fleet raid' to sap Confederate treasury and throttle their reinforcement rate.
8. Buy supply manually whenever an active army drops to 1 supply to prevent combat penalties and winter attrition.
9. Do not attack defenders with low odds (under 50%); maneuver to cut off retreat or wait for concentrated strength.
10. Use 'rail' every turn to reposition high-rated commanders and reinforcements directly to threatened sectors.
11. Check recruit options with 'troops' every turn and invest in high-yield cities like Washington, Baltimore, and Cincinnati.
12. Never leave Washington unoccupied if an enemy army occupies Harper's Ferry, Manassas, or Fredericksburg.

### Version 18, after game 18 (alternate: Union victory: share of total income, 13 turns)

**Diagnosis.** Game 18 was won decisively in May 1863 by economic dominance (income share) and strategic encirclement. Continuous commerce raiding stripped Rebel funds while steady recruitment built overwhelming field stacks in Washington, the Midwest, and the Mississippi corridor. Aggressive Rebel raiding incursions into Pennsylvania and Ohio were trapped against borders and destroyed with complete surrenders, enabling a final multi-pronged drive that seized Richmond and Vicksburg.

**Strategy for the next game.** Open by seizing neutral border hubs and putting the navy on continuous raid. Funnel revenue into high-yield northern recruit cities and rail reinforcements to maintain solid defense lines across Washington, Ohio, and the Mississippi. Isolate and eliminate any Rebel incursions into northern territory by cutting off their retreat paths. Once the North is completely pacified and massive 40,000+ corps are consolidated under top commanders, launch coordinated simultaneous advances on Richmond, Tennes

**Changes:**

- revised: Prioritize intercepting and trapping enemy raiders in the Northeast and Midwest; cut off their retreat routes to force complete surrender. (Trapping deep Rebel incursions into Harrisburg and Cincinnati eliminated entire enemy field armies instantly through surrender without retreat paths.)
- revised: Consolidate field armies using 'join' into 30,000-50,000 man corps before attacking major enemy concentrations. (Concentrated 40k+ corps led by high-rated generals (McClellan, Hooker, Sherman) easily overpowered Confederate defenders at Richmond, Memphis, and Harrisburg.)

**Notebook:**

1. Never attack with an army at 0 supply; unsupplied armies fight at half strength and suffer severe combat penalties.
2. Prioritize intercepting and trapping enemy raiders in the Northeast and Midwest; cut off their retreat routes to force complete surrender.
3. Do not push small, isolated raiding detachments into the deep South without secure supply lines and retreat paths.
4. Maintain strong garrisons in critical northern border hubs (Washington, Baltimore, Cincinnati, Columbus).
5. Consolidate field armies using 'join' into 30,000-50,000 man corps before attacking major enemy concentrations.
6. Secure neutral border cities (Baltimore, Louisville, Paducah) on Turn 1 for income and forward staging.
7. Keep the Union fleet on 'fleet raid' every turn to drain Rebel revenue and severely restrict their recruitment.
8. Buy supply manually whenever an active army drops to 1 supply to prevent combat penalties and winter attrition.
9. Do not attack defenders with low odds (under 50%); maneuver to cut off retreat or wait for concentrated strength.
10. Use 'rail' every turn to reposition high-rated commanders and reinforcements directly to threatened sectors.
11. Check recruit options with 'troops' every turn and invest in high-yield cities like Washington, Baltimore, and Cincinnati.
12. Never leave Washington unoccupied if an enemy army occupies Harper's Ferry, Manassas, or Fredericksburg.

### Version 19, after game 19 (standard: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** The Confederacy achieved a swift 32-city victory in 5 turns by slipping raiders (A.S. Johnston, Jackson, J.E. Johnston) past the frontier into undefended Northern hubs (Indianapolis, Columbus, Pittsburgh, Philadelphia, Springfield). Failed low-odds attacks on Turn 1 and chasing peripheral targets like Harper's Ferry left our interior completely open to rapid capture.

**Strategy for the next game.** Establish an airtight defensive perimeter across the Potomac and Ohio rivers on Turn 1. Consolidate northern recruits into massive corps under top generals (Grant, McDowell) and aggressively use railroad movement to immediately block, corner, and eliminate any Confederate forces that attempt to raid north.

**Changes:**

- revised: Never leave interior Northern cities (Columbus, Pittsburgh, Philadelphia, Indianapolis) unguarded when enemy raiders breach the frontier. (Rebel raiders exploited gaps to capture Columbus, Pittsburgh, Philadelphia, and Springfield unopposed, triggering a 32-city sudden victory.)
- revised: Use 'rail' proactively every turn to reposition forces directly in the path of penetrating enemy armies. (Failing to rail reinforcements to block deep raiders allowed enemy commanders to sweep through the Ohio Valley and Pennsylvania.)

**Notebook:**

1. Never attack with an army at 0 supply; unsupplied armies fight at half strength and suffer severe combat penalties.
2. Prioritize intercepting and trapping enemy raiders in the Northeast and Midwest; cut off their retreat routes to force complete surrender.
3. Never leave interior Northern cities (Columbus, Pittsburgh, Philadelphia, Indianapolis) unguarded when enemy raiders breach the frontier.
4. Maintain strong garrisons in critical border hubs (Washington, Baltimore, Cincinnati, Columbus) to prevent breakthrough raids.
5. Consolidate field armies using 'join' into 30,000-50,000 man corps before attacking major enemy concentrations.
6. Secure neutral border cities (Baltimore, Louisville, Paducah) on Turn 1 for income and forward staging.
7. Keep the Union fleet on 'fleet raid' every turn to drain Rebel revenue and severely restrict their recruitment.
8. Buy supply manually whenever an active army drops to 1 supply to prevent combat penalties and winter attrition.
9. Do not attack defenders with low odds (under 50%); maneuver to cut off retreat or wait for concentrated strength.
10. Use 'rail' proactively every turn to reposition forces directly in the path of penetrating enemy armies.
11. Check recruit options with 'troops' every turn and invest in high-yield cities like Washington, Baltimore, and Cincinnati.
12. Never leave Washington unoccupied if an enemy army occupies Harper's Ferry, Manassas, or Fredericksburg.

### Version 20, after game 20 (alternate: Union victory: share of total income, 13 turns)

**Diagnosis.** A steady income-share victory achieved by keeping the fleet on continuous commerce raiding, defending Washington and Cincinnati stubbornly against repeated assaults, consolidating 30,000+ man field armies to crush isolated Rebel forces in Paducah and Vicksburg, and aggressively capturing high-value western cities like Memphis, Jackson, and Baton Rouge.

**Strategy for the next game.** Open by seizing neutral border hubs and putting the navy on permanent commerce raiding. Anchor the Eastern theater defensively at Washington and Fredericksburg with fortified garrisons while building 30k+ corps via rail and join to systematically roll up the Mississippi Valley, capturing western cities to win by economic strangulation.

**Changes:**

- revised: Exploit western openings (Memphis, Jackson, Vicksburg, Baton Rouge) to rapidly drive Confederate income below 40%. (Replaced the redundant Washington defense reminder (already covered by border hub garrisoning) with active exploitation of the western theater to trigger economic victory.)

**Notebook:**

1. Never attack with an army at 0 supply; unsupplied armies fight at half strength and suffer severe combat penalties.
2. Prioritize intercepting and trapping enemy raiders in the Northeast and Midwest; cut off their retreat routes to force complete surrender.
3. Never leave interior Northern cities (Columbus, Pittsburgh, Philadelphia, Indianapolis) unguarded when enemy raiders breach the frontier.
4. Maintain strong garrisons in critical border hubs (Washington, Baltimore, Cincinnati, Columbus) to prevent breakthrough raids.
5. Consolidate field armies using 'join' into 30,000-50,000 man corps before attacking major enemy concentrations.
6. Secure neutral border cities (Baltimore, Louisville, Paducah) on Turn 1 for income and forward staging.
7. Keep the Union fleet on 'fleet raid' every turn to drain Rebel revenue and severely restrict their recruitment.
8. Buy supply manually whenever an active army drops to 1 supply to prevent combat penalties and winter attrition.
9. Do not attack defenders with low odds (under 50%); maneuver to cut off retreat or wait for concentrated strength.
10. Use 'rail' proactively every turn to reposition forces directly in the path of penetrating enemy armies.
11. Check recruit options with 'troops' every turn and invest in high-yield cities like Washington, Baltimore, and Cincinnati.
12. Exploit western openings (Memphis, Jackson, Vicksburg, Baton Rouge) to rapidly drive Confederate income below 40%.

### Version 21, after game 21 (standard: Rebel victory: cities controlled, 14 turns)

**Diagnosis.** Piecemeal, sequential attacks by multiple separate armies against concentrated Rebel forces (like Johnston in Baltimore) caused repeated defeats. Simultaneously, overextending Grant deep south with small forces against Lee's 40k doomstack and leaving the Midwest completely open to Pemberton's raids collapsed both flanks.

**Strategy for the next game.** Open by securing neutral border cities and establishing strong defensive anchors at Washington, Baltimore, and Cincinnati. Merge field armies into 40k+ doomstacks with 'join' before engaging main Rebel concentrations, keeping the fleet raiding to throttle Confederate funds while maintaining a mobile reserve to crush raiders in the Midwest.

**Changes:**

- added: Never launch multiple separate attacks into the same city on one turn; always merge armies using 'join' first so they fight as one unified force. (Attacking Baltimore with three separate armies in one turn resulted in three consecutive lost battles rather than one overwhelming victory.)
- added: Do not overextend isolated detachments into deep Southern cities (Nashville, Chattanooga) against superior Confederate field armies. (Grant was repeatedly crushed and eventually destroyed because he held Nashville and Lexington with only 7k-12k men against Lee's 45k.)
- revised: Maintain an active field army in the Ohio Valley (Cincinnati, Columbus, Louisville) to intercept and destroy Midwest raiders. (Pemberton marched unopposed through Louisville, Cincinnati, Columbus, and Indianapolis because forces were concentrated entirely in the East.)
- dropped: Exploit western openings (Memphis, Jackson, Vicksburg, Baton Rouge) to rapidly drive Confederate income below 40%. (Premature western advances dilute Union force concentration and leave Northern home territory vulnerable to collapse.)

**Notebook:**

1. Never launch multiple separate attacks into the same city on one turn; always merge armies using 'join' first so they fight as one unified force.
2. Do not attack enemy defenders when combat odds are under 50%; maneuver to cut off retreat, defend fortified positions, or wait for reinforcements.
3. Never attack or move with an army at 0 supply; unsupplied armies fight at half strength and suffer severe attrition.
4. Maintain an active field army in the Ohio Valley (Cincinnati, Columbus, Louisville) to intercept and destroy Midwest raiders.
5. Do not overextend isolated detachments into deep Southern cities (Nashville, Chattanooga) against superior Confederate field armies.
6. Secure high-value neutral border cities (Baltimore, Louisville, Paducah) on Turn 1 to expand income and create defensive barriers.
7. Keep the Union fleet on 'fleet raid' every turn to steadily drain Confederate treasury and limit their recruitment.
8. Buy supply manually whenever an active army drops to 1 supply to prevent combat penalties and winter supply loss.
9. Use 'rail' immediately to reposition large armies directly in front of penetrating enemy spearheads before they capture interior hubs.
10. Check recruit options with 'troops' every turn and invest in high-yield cities like Washington, Baltimore, Columbus, and Cincinnati.
11. When an enemy raider is isolated deep in Northern territory, cut all adjacent friendly rail and march paths to force full surrender on defeat.
12. Fortify key chokepoint cities when facing superior enemy numbers; fort levels double or triple defensive combat power.

### Version 22, after game 22 (alternate: Union victory: share of total income, 7 turns)

**Diagnosis.** Achieved a rapid 7-turn income victory by securing critical border cities early, massing a large strike force under Buell in the West to crush Johnston, fortifying Fredericksburg to break Lee's 32k-man assault, and relentlessly raiding Rebel commerce.

**Strategy for the next game.** Lock down eastern approaches by garrisoning and fortifying Fredericksburg and Strasburg, keep the fleet on raid, and concentrate overwhelming mass in the West to sweep the Mississippi and Tennessee valleys for a rapid income or total conquest victory.

**Changes:**

- revised: Fortify frontline chokepoint cities (like Fredericksburg) when facing superior enemy death stacks; fort multipliers easily defeat massive attacks. (Fortifying Fredericksburg allowed 10k defenders to decisively defeat Lee's 32,700-man assault, exhausting his army and protecting Washington.)
- added: Push aggressively down the Mississippi and Tennessee rivers (Paducah, Memphis, Vicksburg, Decatur) to rapidly collapse Rebel income. (Rapid western advances combined with commerce raiding quickly pushed Union income above the 60% threshold for an early automatic victory.)
- dropped: Do not overextend isolated detachments into deep Southern cities (Nashville, Chattanooga) against superior Confederate field armies. (Subsumed by combat odds rules and offensive western momentum guidelines.)

**Notebook:**

1. Never launch multiple separate attacks into the same city on one turn; always merge armies using 'join' first so they fight as one unified force.
2. Do not attack enemy defenders when combat odds are under 50%; maneuver to cut off retreat, defend fortified positions, or wait for reinforcements.
3. Never attack or move with an army at 0 supply; unsupplied armies fight at half strength and suffer severe attrition.
4. Maintain an active field army in the Ohio Valley (Cincinnati, Columbus, Louisville) to intercept and destroy Midwest raiders.
5. Fortify frontline chokepoint cities (like Fredericksburg) when facing superior enemy death stacks; fort multipliers easily defeat massive attacks.
6. Secure high-value neutral border cities (Baltimore, Louisville, Paducah) on Turn 1 to expand income and create defensive barriers.
7. Keep the Union fleet on 'fleet raid' every turn to steadily drain Confederate treasury and limit their recruitment.
8. Buy supply manually whenever an active army drops to 1 supply to prevent combat penalties and winter supply loss.
9. Use 'rail' immediately to reposition large armies directly in front of penetrating enemy spearheads before they capture interior hubs.
10. Check recruit options with 'troops' every turn and invest in high-yield cities like Washington, Baltimore, Columbus, and Cincinnati.
11. When an enemy raider is isolated deep in Northern territory, cut all adjacent friendly rail and march paths to force full surrender on defeat.
12. Push aggressively down the Mississippi and Tennessee rivers (Paducah, Memphis, Vicksburg, Decatur) to rapidly collapse Rebel income.

### Version 23, after game 23 (standard: Rebel victory: capital captured, 3 turns)

**Diagnosis.** Catastrophic defeat in 3 turns caused by evacuating Washington (moving McDowell to Manassas), leaving the capital completely empty. Jackson walked in from Harpers Ferry before garrison moves resolved, triggering an immediate instant-loss capital capture.

**Strategy for the next game.** Never vacate Washington while Confederate forces threaten Harpers Ferry or Manassas. Open by securing Baltimore, Paducah, and Louisville, maintaining fleet raids, recruiting heavily in primary industrial hubs, and advancing steadily in the West while maintaining an unshakeable defense around the capital.

**Changes:**

- added: Never leave Washington undefended; always maintain a solid garrison or ensure adjacent enemy threats like Jackson at Harpers Ferry or Manassas are neutralized first. (Evacuating McDowell to Manassas left Washington completely empty, allowing Jackson to walk in on Turn 3 for an instant Rebel victory.)
- dropped: When an enemy raider is isolated deep in Northern territory, cut all adjacent friendly rail and march paths to force full surrender on defeat. (Dropped to make room for the critical capital defense rule; general positioning and field armies already contain raiders.)

**Notebook:**

1. Never leave Washington undefended; always maintain a solid garrison or ensure adjacent enemy threats like Jackson at Harpers Ferry or Manassas are neutralized first.
2. Never launch multiple separate attacks into the same city on one turn; always merge armies using 'join' first so they fight as one unified force.
3. Do not attack enemy defenders when combat odds are under 50%; maneuver to cut off retreat, defend fortified positions, or wait for reinforcements.
4. Never attack or move with an army at 0 supply; unsupplied armies fight at half strength and suffer severe attrition.
5. Maintain an active field army in the Ohio Valley (Cincinnati, Columbus, Louisville) to intercept and destroy Midwest raiders.
6. Fortify frontline chokepoint cities when facing superior enemy stacks; fort multipliers easily defeat massive attacks.
7. Secure high-value neutral border cities (Baltimore, Louisville, Paducah) on Turn 1 to expand income and create defensive barriers.
8. Keep the Union fleet on 'fleet raid' every turn to steadily drain Confederate treasury and limit their recruitment.
9. Buy supply manually whenever an active army drops to 1 supply to prevent combat penalties and winter supply loss.
10. Use 'rail' immediately to reposition large armies directly in front of penetrating enemy spearheads before they capture interior hubs.
11. Check recruit options with 'troops' every turn and invest in high-yield cities like Washington, Baltimore, Columbus, and Cincinnati.
12. Push aggressively down the Mississippi and Tennessee rivers (Paducah, Memphis, Vicksburg, Decatur) to rapidly collapse Rebel income.

### Version 24, after game 24 (alternate: Union victory: share of total income, 13 turns)

**Diagnosis.** A decisive 13-turn economic victory was achieved by securing border neutrals early, building a massive western doomstack under Grant, using rail to counter rebel incursions into the Ohio Valley, and maintaining constant naval commerce raiding to choke Rebel finances.

**Strategy for the next game.** Open by seizing vital border neutrals (Baltimore, Louisville, Lexington) and putting the fleet on commerce raid. Build a massive central field army under top generals (Grant/Rosecrans) via recruitment and 'join', use railroad transport to block and destroy enemy raiding thrusts in the Ohio Valley, and execute a steady drive down the Mississippi and Tennessee river corridors to starve the Confederacy of income and secure a swift victory.

**Changes:**

- revised: Never leave Washington undefended; always maintain a solid garrison or ensure adjacent enemy threats at Harpers Ferry, Manassas, or Fredericksburg are neutralized. (Added Fredericksburg to the threat list after seeing repeated AI attempts to threaten Washington from Virginia neutrals.)
- revised: Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington) on Turn 1 to maximize income and form defensive buffer zones. (Included Lexington explicitly as an essential Turn 1 neutral capture to secure Kentucky.)

**Notebook:**

1. Never leave Washington undefended; always maintain a solid garrison or ensure adjacent enemy threats at Harpers Ferry, Manassas, or Fredericksburg are neutralized.
2. Never launch multiple separate attacks into the same city on one turn; merge armies using 'join' first so they fight as a single unified force.
3. Do not attack enemy defenders when combat odds are below 50%; wait for reinforcements, fortify defensively, or cut off their lines of supply.
4. Never attack or move with an army at 0 supply; unsupplied armies suffer 50% combat penalties and severe winter attrition.
5. Maintain an active field army in the Ohio Valley (Cincinnati, Columbus, Louisville) to intercept and crush Confederate Midwest raiders.
6. Fortify frontline chokepoint cities when facing superior enemy stacks; fort multipliers easily defeat massive Confederate assaults.
7. Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington) on Turn 1 to maximize income and form defensive buffer zones.
8. Keep the Union fleet on 'fleet raid' every turn to continuously drain Confederate treasury and suppress their recruitment capacity.
9. Buy supply manually whenever an active army drops to 1 supply to prevent attrition and offensive combat debuffs.
10. Use 'rail' immediately to reposition large armies directly in front of penetrating enemy spearheads before they capture interior hubs.
11. Check recruit options with 'troops' every turn and invest in high-yield recruit centers like Washington, Baltimore, Columbus, and Cincinnati.
12. Push aggressively down the Mississippi and Tennessee rivers (Paducah, Memphis, Vicksburg, Decatur) to rapidly collapse Rebel income.

### Version 25, after game 25 (standard: Union victory: capital captured, 3 turns)

**Diagnosis.** Securing Manassas and fortifying Washington on Turn 1 created an impenetrable defense, while capitalizing on Confederate redeployment away from Richmond enabled McDowell to rush and capture the Rebel capital on Turn 3 for an instant victory.

**Strategy for the next game.** Fortify Washington and secure border states on Turn 1, advance to Manassas, and immediately seize Richmond if left vulnerable while containing Confederate raiders in the West.

**Changes:**

- revised: Never leave Washington undefended; fortify it to level 2 early so a moderate garrison can easily repel Confederate counterattacks. (Fortifying Washington to level 2 proved critical, allowing Fremont to effortlessly repel Jackson's 17k assault with 20% combat odds.)
- added: Strike Richmond immediately via Manassas if the Confederate AI vacates or leaves its capital lightly garrisoned. (Capitalizing on J.E. Johnston railing out of Richmond allowed McDowell to take Manassas and capture Richmond on Turn 3 for a quick decisive victory.)
- dropped: Push aggressively down the Mississippi and Tennessee rivers (Paducah, Memphis, Vicksburg, Decatur) to rapidly collapse Rebel income. (Dropped to make room for capital snipe rules, as an immediate eastern push on Richmond can win games much faster than slow western river campaigns.)

**Notebook:**

1. Never leave Washington undefended; fortify it to level 2 early so a moderate garrison can easily repel Confederate counterattacks.
2. Strike Richmond immediately via Manassas if the Confederate AI vacates or leaves its capital lightly garrisoned.
3. Never launch multiple separate attacks into the same city on one turn; merge armies using 'join' first so they fight as a single unified force.
4. Do not attack enemy defenders when combat odds are below 50%; wait for reinforcements, fortify defensively, or cut off their lines of supply.
5. Never attack or move with an army at 0 supply; unsupplied armies suffer 50% combat penalties and severe winter attrition.
6. Maintain an active field army in the Ohio Valley (Cincinnati, Columbus, Louisville) to intercept and crush Confederate Midwest raiders.
7. Fortify frontline chokepoint cities when facing superior enemy stacks; fort multipliers easily defeat massive Confederate assaults.
8. Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington) on Turn 1 to maximize income and form defensive buffer zones.
9. Keep the Union fleet on 'fleet raid' every turn to continuously drain Confederate treasury and suppress their recruitment capacity.
10. Buy supply manually whenever an active army drops to 1 supply to prevent attrition and offensive combat debuffs.
11. Use 'rail' immediately to reposition large armies directly in front of penetrating enemy spearheads before they capture interior hubs.
12. Check recruit options with 'troops' every turn and invest in high-yield recruit centers like Washington, Baltimore, Columbus, and Cincinnati.

### Version 26, after game 26 (alternate: Union victory: share of total income, 18 turns)

**Diagnosis.** Securing key neutral border cities on Turn 1 and taking Richmond early established a strong economic lead. Fortifying Richmond and Washington to level 2 allowed modest garrisons to shatter massive Confederate counterattacks by Stonewall Jackson and J.E. Johnston. Continuous naval raiding bled the Rebel economy while targeted rail movements and mass recruitment in northern hubs contained western incursions and secured an income threshold victory.

**Strategy for the next game.** Open by seizing border neutrals (Baltimore, Louisville, Paducah, Lexington) and capturing Richmond immediately if lightly held. Fortify key anchor cities (Washington, Richmond, Philadelphia) to level 2 to decimate Rebel offensives on defense. Drain Confederate finances with continuous fleet raids, use interior rail lines to intercept deep enemy raiders, and recruit heavily in high-value hubs to build decisive numerical superiority for an economic or territory victory.

**Changes:**

- revised: Fortify captured high-value forward cities like Richmond to level 2; fort multipliers easily smash massive Confederate counteroffensives. (Fortifying Richmond to level 2 allowed a 12k garrison to repeatedly crush 40,000+ Rebel stacks under Stonewall Jackson.)

**Notebook:**

1. Never leave Washington undefended; fortify it to level 2 early so a moderate garrison can easily repel Confederate counterattacks.
2. Strike Richmond immediately via Manassas if the Confederate AI vacates or leaves its capital lightly garrisoned.
3. Fortify captured high-value forward cities like Richmond to level 2; fort multipliers easily smash massive Confederate counteroffensives.
4. Never attack enemy defenders when combat odds are below 50%; wait for reinforcements, fortify defensively, or cut off their lines of supply.
5. Never attack or move with an army at 0 supply; unsupplied armies suffer 50% combat penalties and severe winter attrition.
6. Maintain an active field army in the Ohio Valley (Cincinnati, Columbus, Louisville) to intercept and crush Confederate Midwest raiders.
7. Never launch multiple separate attacks into the same city on one turn; merge armies using 'join' first so they fight as a single unified force.
8. Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington) on Turn 1 to maximize income and form defensive buffer zones.
9. Keep the Union fleet on 'fleet raid' every turn to continuously drain Confederate treasury and suppress their recruitment capacity.
10. Buy supply manually whenever an active army drops to 1 supply to prevent attrition and offensive combat debuffs.
11. Use 'rail' immediately to reposition large armies directly in front of penetrating enemy spearheads before they capture interior hubs.
12. Check recruit options with 'troops' every turn and invest in high-yield recruit centers like Washington, Baltimore, Columbus, and Cincinnati.

### Version 27, after game 27 (standard: Rebel victory: capital captured, 4 turns)

**Diagnosis.** In May 1861, McDowell marched out of Washington to take Harper's Ferry, leaving the capital completely vacated. Although Washington had level 2 forts, forts offer zero defense without a garrison. When R.E. Lee railed to Fredericksburg and marched into Washington, his high leader rating gave him earlier turn resolution than Fremont's inbound move from Baltimore, handing the Confederacy an immediate capital-capture victory.

**Strategy for the next game.** On Turn 1, fortify Washington and keep a permanent garrison in place while grabbing neutral border cities (Baltimore, Louisville, Paducah). Use the Western armies under McClellan and Grant to pressure Tennessee, keep the fleet on raid to starve Rebel finances, and never strip Washington of troops when Confederate armies occupy northern Virginia.

**Changes:**

- revised: Never leave Washington without an active garrison; empty forts provide zero defense, and top Rebel generals like Lee will move first and seize it. (McDowell vacated Washington to capture Harper's Ferry, allowing Lee to walk into an empty capital before incoming reinforcements could resolve movement.)
- added: Fortify Washington to level 2 early and keep at least 15,000 men stationed inside whenever Confederate forces hold Manassas or Fredericksburg. (Ensures Washington maintains a dedicated garrison at all times rather than relying on dynamic moves that resolve after Confederate marches.)
- dropped: Check recruit options with 'troops' every turn and invest in high-yield recruit centers like Washington, Baltimore, Columbus, and Cincinnati. (Dropped to make room for the mandatory Washington garrison rule; recruiting is already standard operational practice.)

**Notebook:**

1. Never leave Washington without an active garrison; empty forts provide zero defense, and top Rebel generals like Lee will move first and seize it.
2. Fortify Washington to level 2 early and keep at least 15,000 men stationed inside whenever Confederate forces hold Manassas or Fredericksburg.
3. Strike Richmond immediately via Manassas if the Confederate AI vacates or leaves its capital lightly garrisoned.
4. Fortify captured high-value forward cities like Richmond to level 2; fort multipliers easily smash massive Confederate counteroffensives.
5. Never attack enemy defenders when combat odds are below 50%; wait for reinforcements, fortify defensively, or cut off their lines of supply.
6. Never attack or move with an army at 0 supply; unsupplied armies suffer 50% combat penalties and severe winter attrition.
7. Maintain an active field army in the Ohio Valley (Cincinnati, Columbus, Louisville) to intercept and crush Confederate Midwest raiders.
8. Never launch multiple separate attacks into the same city on one turn; merge armies using 'join' first so they fight as a single unified force.
9. Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington) on Turn 1 to maximize income and form defensive buffer zones.
10. Keep the Union fleet on 'fleet raid' every turn to continuously drain Confederate treasury and suppress their recruitment capacity.
11. Buy supply manually whenever an active army drops to 1 supply to prevent attrition and offensive combat debuffs.
12. Use 'rail' immediately to reposition large armies directly in front of penetrating enemy spearheads before they capture interior hubs.

### Version 28, after game 28 (alternate: Rebel victory: cities controlled, 5 turns)

**Diagnosis.** A single Confederate army (A.S. Johnston) penetrated deep into the undefended Midwest, capturing St. Louis, Springfield, Indianapolis, Columbus, and Pittsburgh unopposed. Meanwhile, the Union hoarded treasury instead of recruiting blockers, launched low-odds piecemeal attacks against Richmond, and allowed the Confederacy to hit the 28-city instant victory threshold by December 1861.

**Strategy for the next game.** On Turn 1, secure neutral border cities and fortify Washington. Spend all available income on recruiting across available cities each turn. Position strong field armies to block and destroy western Confederate incursions in the Ohio Valley and Midwest before attempting concentrated multi-corps offensives in the East.

**Changes:**

- added: Spend treasury aggressively on recruits every turn; hoarding cash allows the Confederacy to outbuild and overrun the map. (Sitting on over $600-$700 in late 1861 without recruiting left northern cities completely bare.)
- added: Monitor total city counts constantly; preventing the Rebels from reaching 28 cities is critical to avoiding an instant defeat. (Lost the game in only 5 turns because the Confederacy reached the 28-city threshold.)
- revised: Never attack Richmond or heavily garrisoned capitals without overwhelming numbers, as the AI heavily reinforces threatened capitals. (Repeated attacks on Richmond were repulsed and crushed when the AI recruited 15,000+ men there in a single turn.)
- dropped: Buy supply manually whenever an active army drops to 1 supply to prevent attrition and offensive combat debuffs. (Replaced to make room for vital city threshold and recruitment spending rules.)

**Notebook:**

1. Never leave Washington without an active garrison; empty forts provide zero defense, and top Rebel generals like Lee will move first and seize it.
2. Spend treasury aggressively on recruits every turn; hoarding cash allows the Confederacy to outbuild and overrun the map.
3. Monitor total city counts constantly; preventing the Rebels from reaching 28 cities is critical to avoiding an instant defeat.
4. Rail or move field armies directly into the path of deep Confederate raiders to prevent them from capturing undefended interior hubs.
5. Never attack Richmond or heavily garrisoned capitals without overwhelming numbers, as the AI heavily reinforces threatened capitals.
6. Fortify key frontier and transit cities (Louisville, Manassas, Fredericksburg) to level 2 to stop enemy counteroffensives.
7. Never attack enemy defenders when combat odds are below 50%; wait for reinforcements, fortify defensively, or cut off their lines of supply.
8. Never attack or move with an army at 0 supply; unsupplied armies suffer 50% combat penalties and severe winter attrition.
9. Maintain an active field army in the Ohio Valley (Cincinnati, Columbus, Louisville) to intercept and crush Confederate Midwest raiders.
10. Never launch multiple separate attacks into the same city on one turn; merge armies using 'join' first so they fight as a single unified force.
11. Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington) on Turn 1 to maximize income and form defensive buffer zones.
12. Keep the Union fleet on 'fleet raid' every turn to continuously drain Confederate treasury and suppress their recruitment capacity.

### Version 29, after game 29 (standard: Rebel victory: capital captured, 3 turns)

**Diagnosis.** In Turn 3, Jackson attacked Washington from adjacent Harper's Ferry with 26,600 men against Grant's tiny garrison of 4,800 men, capturing the capital and causing an instant defeat. Moving McDowell out to Manassas without heavily garrisoning Washington left the capital fatally exposed to adjacent Rebel strike forces.

**Strategy for the next game.** Secure neutral border cities on Turn 1 while reinforcing and fortifying Washington with a robust multi-brigade garrison. Hold defensive chokepoints along the Ohio and Potomac rivers, use fleet raiding to constrict Confederate finances, and assemble decisive offensive stacks before counter-attacking into Virginia and the West.

**Changes:**

- revised: Washington must maintain a heavy garrison (15k+ men) whenever Rebel armies are at Harper's Ferry or Manassas; token garrisons will be overrun instantly. (A small token garrison of 4,800 men under Grant was easily overrun by Jackson's 26,600 men attacking from Harper's Ferry, losing the game instantly.)
- revised: Fortify key frontier and transit cities (Louisville, Manassas, Fredericksburg, Washington) to stop enemy counteroffensives. (Added Washington explicitly to key fortification priorities to ensure defensive multipliers against Confederate early thrusts.)

**Notebook:**

1. Washington must maintain a heavy garrison (15k+ men) whenever Rebel armies are at Harper's Ferry or Manassas; token garrisons will be overrun instantly.
2. Spend treasury aggressively on recruits every turn; hoarding cash allows the Confederacy to outbuild and overrun the map.
3. Monitor total city counts constantly; preventing the Rebels from reaching 28 cities is critical to avoiding an instant defeat.
4. Rail or move field armies directly into the path of deep Confederate raiders to prevent them from capturing undefended interior hubs.
5. Never attack Richmond or heavily garrisoned capitals without overwhelming numbers, as the AI heavily reinforces threatened capitals.
6. Fortify key frontier and transit cities (Louisville, Manassas, Fredericksburg, Washington) to stop enemy counteroffensives.
7. Never attack enemy defenders when combat odds are below 50%; wait for reinforcements, fortify defensively, or cut off their lines of supply.
8. Never attack or move with an army at 0 supply; unsupplied armies suffer 50% combat penalties and severe winter attrition.
9. Maintain an active field army in the Ohio Valley (Cincinnati, Columbus, Louisville) to intercept and crush Confederate Midwest raiders.
10. Never launch multiple separate attacks into the same city on one turn; merge armies using 'join' first so they fight as a single unified force.
11. Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington) on Turn 1 to maximize income and form defensive buffer zones.
12. Keep the Union fleet on 'fleet raid' every turn to continuously drain Confederate treasury and suppress their recruitment capacity.

### Version 30, after game 30 (alternate: Union victory: share of total income, 6 turns)

**Diagnosis.** Game 30 was a swift 6-turn economic victory. Turn 1 expansion secured high-income border cities, while maximum recruitment each turn rapidly built overwhelming manpower. Constant fleet raiding starved Confederate finances, Grant swept the Mississippi corridor uncontested, and railing a major force to Cincinnati decisively crushed the Confederate Ohio Valley counteroffensive.

**Strategy for the next game.** Open by seizing border neutrals to build an early income lead while putting the fleet on permanent raiding duty. Reinvest all income into recruitment across available cities every turn. Advance along the Western river corridors with concentrated forces while keeping the East fortified and railing reinforcements to intercept Midwest incursions.

**Changes:**

- revised: Never attack enemy defenders when combat odds are below 50%; wait for reinforcements, fortify defensively, or cut off their lines of supply. (Repeated failed attacks on Jefferson City at 28% odds showed that waiting for the enemy to run out of supply converts bad assaults into overwhelming 80% victories.)

**Notebook:**

1. Washington must maintain a heavy garrison (15k+ men) whenever Rebel armies are at Harper's Ferry or Manassas; token garrisons will be overrun instantly.
2. Spend treasury aggressively on recruits every turn; hoarding cash allows the Confederacy to outbuild and overrun the map.
3. Monitor total city counts constantly; preventing the Rebels from reaching 28 cities is critical to avoiding an instant defeat.
4. Rail or move field armies directly into the path of deep Confederate raiders to prevent them from capturing undefended interior hubs.
5. Never attack Richmond or heavily garrisoned capitals without overwhelming numbers, as the AI heavily reinforces threatened capitals.
6. Fortify key frontier and transit cities (Louisville, Manassas, Fredericksburg, Washington) to stop enemy counteroffensives.
7. Never attack enemy defenders when combat odds are below 50%; wait for reinforcements, fortify defensively, or cut off their lines of supply.
8. Never attack or move with an army at 0 supply; unsupplied armies suffer 50% combat penalties and severe winter attrition.
9. Maintain an active field army in the Ohio Valley (Cincinnati, Columbus, Louisville) to intercept and crush Confederate Midwest raiders.
10. Never launch multiple separate attacks into the same city on one turn; merge armies using 'join' first so they fight as a single unified force.
11. Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington) on Turn 1 to maximize income and form defensive buffer zones.
12. Keep the Union fleet on 'fleet raid' every turn to continuously drain Confederate treasury and suppress their recruitment capacity.

### Version 31, after game 31 (standard: Rebel victory: capital captured, 19 turns)

**Diagnosis.** Game 31 was lost on Turn 19 when Washington was left completely empty while J.E.B. Stuart was adjacent in Harper's Ferry, allowing an immediate Rebel capture of the capital. Additionally, McClellan overextended deep into the Gulf states with a massive army, isolating critical manpower while Rebel raiders systematically rolled up the Ohio Valley and Mid-Atlantic.

**Strategy for the next game.** On Turn 1, secure neutral border hubs (Baltimore, Louisville, Paducah, Lexington) and fortify Washington to Level 2. Maintain a strict permanent garrison in Washington whenever enemies are nearby. Keep primary field armies consolidated along the Ohio Valley and Virginia front to crush Rebel raiders before launching any coordinated offensive southward.

**Changes:**

- revised: Never leave Washington ungarrisoned or move its garrison away if enemy forces occupy Harper's Ferry, Manassas, or Fredericksburg; an empty capital causes instant defeat. (Grant moved out of Washington toward Baltimore and Philadelphia while Stuart was adjacent at Harper's Ferry, resulting in Washington being walked into and instant defeat.)
- dropped: Keep the Union fleet on 'fleet raid' every turn to continuously drain Confederate treasury and suppress their recruitment capacity. (Rebel fleets frequently contest raids and sink Union ships, making automatic blind raiding inefficient compared to territorial defense and securing theater armies.)
- added: Do not overextend main field armies deep into the Deep South (New Orleans, Mobile) until the Northern border and Mid-Atlantic corridors are fully secured. (McClellan's deep push down the Mississippi/Gulf isolated a massive 50k force, leaving the Midwest and Mid-Atlantic underdefended against multiple Rebel incursions.)

**Notebook:**

1. Never leave Washington ungarrisoned or move its garrison away if enemy forces occupy Harper's Ferry, Manassas, or Fredericksburg; an empty capital causes instant defeat.
2. Spend treasury aggressively on recruits every turn; hoarding cash allows the Confederacy to outbuild and overrun the map.
3. Monitor total city counts constantly; preventing the Rebels from reaching 28 cities is critical to avoiding an instant defeat.
4. Rail or move field armies directly into the path of deep Confederate raiders to prevent them from capturing undefended interior hubs.
5. Never attack Richmond or heavily garrisoned capitals without overwhelming numbers, as the AI heavily reinforces threatened capitals.
6. Fortify key frontier and transit cities (Louisville, Manassas, Fredericksburg, Washington) to stop enemy counteroffensives.
7. Never attack enemy defenders when combat odds are below 50%; wait for reinforcements, fortify defensively, or cut off their lines of supply.
8. Never attack or move with an army at 0 supply; unsupplied armies suffer 50% combat penalties and severe winter attrition.
9. Maintain an active field army in the Ohio Valley (Cincinnati, Columbus, Louisville) to intercept and crush Confederate Midwest raiders.
10. Never launch multiple separate attacks into the same city on one turn; merge armies using 'join' first so they fight as a single unified force.
11. Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington) on Turn 1 to maximize income and form defensive buffer zones.
12. Do not overextend main field armies deep into the Deep South (New Orleans, Mobile) until the Northern border and Mid-Atlantic corridors are fully secured.

### Version 32, after game 32 (alternate: Union victory: share of total income, 6 turns)

**Diagnosis.** Rapid Union expansion into key neutral buffer cities on Turn 1 established strong early income. Heavy continuous recruitment and decisive Western offensives under Grant and Burnside steadily dismantled Rebel positions in Missouri and along the Tennessee/Mississippi rivers, quickly pushing Union income past the 60% victory threshold by January 1862.

**Strategy for the next game.** Execute immediate Turn 1 moves into neutral border cities (Baltimore, Manassas, Lexington, Louisville, Paducah) to maximize income. Reinvest all income into maximum recruitment each turn, maintain secure garrisons at Washington and Ohio hubs, and push unified Western armies along the Mississippi and Cumberland axes to trigger an income or city threshold victory.

**Changes:**

- revised: Never attack with weak, unreinforced detachments (under 3,000 men); merge or reinforce them before attacking to prevent armies being wiped out. (Pope's 800-man remnant attacked Beauregard in Fort Donelson and was completely wiped out with 12% odds; weak detached attacks waste men and leaders.)
- revised: Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington, Manassas) on Turn 1 to maximize income and build buffer zones. (Taking Manassas alongside the other border cities secures the Virginia perimeter immediately while denying Confederate forward momentum.)

**Notebook:**

1. Never leave Washington ungarrisoned or move its garrison away if enemy forces occupy Harper's Ferry, Manassas, or Fredericksburg; an empty capital causes instant defeat.
2. Spend treasury aggressively on recruits every turn; hoarding cash allows the Confederacy to outbuild and overrun the map.
3. Monitor total city counts constantly; preventing the Rebels from reaching 28 cities is critical to avoiding an instant defeat.
4. Rail or move field armies directly into the path of deep Confederate raiders to prevent them from capturing undefended interior hubs.
5. Never attack Richmond or heavily garrisoned capitals without overwhelming numbers, as the AI heavily reinforces threatened capitals.
6. Fortify key frontier and transit cities (Louisville, Manassas, Fredericksburg, Washington) to stop enemy counteroffensives.
7. Never attack enemy defenders when combat odds are below 50%; wait for reinforcements, fortify defensively, or cut off their lines of supply.
8. Never attack or move with an army at 0 supply; unsupplied armies suffer 50% combat penalties and severe winter attrition.
9. Maintain an active field army in the Ohio Valley (Cincinnati, Columbus, Louisville) to intercept and crush Confederate Midwest raiders.
10. Never attack with weak, unreinforced detachments (under 3,000 men); merge or reinforce them before attacking to prevent armies being wiped out.
11. Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington, Manassas) on Turn 1 to maximize income and build buffer zones.
12. Do not overextend main field armies deep into the Deep South (New Orleans, Mobile) until the Northern border and Mid-Atlantic corridors are fully secured.

### Version 33, after game 33 (standard: Rebel victory: capital captured, 7 turns)

**Diagnosis.** Lost in March 1862 due to instant capital loss. While Union forces overextended deep into the South (capturing Atlanta and Montgomery), Stonewall Jackson swept through Baltimore and Philadelphia and stormed an understrength, unfortified Washington (12,100 defenders vs 35,400 attackers). Capital security and Eastern corridor containment were neglected.

**Strategy for the next game.** Lock down Washington immediately with fort level 2 and a robust garrison. Secure the border neutrals on Turn 1, eliminate Rebel incursions into MD, PA, and the Ohio Valley with superior concentrated forces, and only advance into the Deep South after the Northern and Mid-Atlantic theaters are completely secure.

**Changes:**

- revised: Heavily garrison and fortify Washington to level 2 whenever enemy armies occupy adjacent cities (Manassas, Harper's Ferry, Baltimore, Fredericksburg); capital loss causes instant defeat. (Washington fell because it was unfortified and undermanned when Jackson advanced from Baltimore.)
- revised: Prioritize securing the DC/PA/MD corridor before launching deep Southern offensives into Georgia or Alabama. (Advancing Grant and Pope into Atlanta and Montgomery while Jackson and Johnston raided Maryland and Pennsylvania left the home front critically vulnerable.)

**Notebook:**

1. Heavily garrison and fortify Washington to level 2 whenever enemy armies occupy adjacent cities (Manassas, Harper's Ferry, Baltimore, Fredericksburg); capital loss causes instant defeat.
2. Spend treasury aggressively on recruits every turn; hoarding cash allows the Confederacy to outbuild and overrun the map.
3. Monitor total city counts constantly; preventing the Rebels from reaching 28 cities is critical to avoiding an instant defeat.
4. Rail or move field armies directly into the path of deep Confederate raiders to prevent them from capturing undefended interior hubs.
5. Never attack Richmond or heavily garrisoned capitals without overwhelming numbers, as the AI heavily reinforces threatened capitals.
6. Fortify key frontier and transit cities (Washington, Louisville, Manassas, Fredericksburg) early to hold choke points against counterattacks.
7. Never attack enemy defenders when combat odds are below 50%; wait for reinforcements, fortify defensively, or cut off their lines of supply.
8. Never attack or move with an army at 0 supply; unsupplied armies suffer 50% combat penalties and severe winter attrition.
9. Maintain an active field army in the Ohio Valley (Cincinnati, Columbus, Louisville) to intercept and crush Confederate Midwest raiders.
10. Never attack with weak, unreinforced detachments (under 3,000 men); merge or reinforce them before attacking to prevent armies being wiped out.
11. Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington, Manassas) on Turn 1 to maximize income and build buffer zones.
12. Prioritize securing the DC/PA/MD corridor before launching deep Southern offensives into Georgia or Alabama.

### Version 34, after game 34 (alternate: Rebel victory: cities controlled, 8 turns)

**Diagnosis.** In Game 34, cash was hoarded during the first three turns rather than spent on mass recruitment, allowing the Confederacy to amass massive western field armies (Johnston and Bragg). The AI swept through St. Louis, Springfield, Louisville, Indianapolis, and Columbus, triggering a 28-city sudden-death victory by May 1862 while Union forces launched desperate low-odds counterattacks.

**Strategy for the next game.** Maximize recruit spending from the opening turn to match Confederate army generation, immediately secure neutral border cities, fortify crucial Western and Eastern transit hubs, and concentrate large field armies under top generals to block Rebel territorial expansion toward the 28-city victory limit.

**Changes:**

- revised: Recruit aggressively from Turn 1 with all available funds; never hoard cash above $300 while cities offer recruits. (Hoarding over $1000 in late 1861 allowed the Confederacy to vastly outproduce Union forces and overwhelm the western theatre.)
- revised: Hold the Western line (St. Louis, Springfield, Louisville, Cincinnati) with substantial garrisons to deny rapid Rebel expansion. (Neglecting western hub defense permitted Confederate armies to chain-capture western cities and hit the 28-city threshold.)
- added: Join and concentrate armies in key transit hubs under 8-star or best available generals before engaging major Rebel stacks. (Fragmented Union forces were defeated piecemeal by concentrated Rebel stacks under J.E. Johnston and Bragg.)

**Notebook:**

1. Recruit aggressively from Turn 1 with all available funds; never hoard cash above $300 while cities offer recruits.
2. Monitor total Confederate city count every turn; when Rebels reach 25+ cities, shift all priorities to reclaiming lost territory.
3. Hold the Western line (St. Louis, Springfield, Louisville, Cincinnati) with substantial garrisons to deny rapid Rebel expansion.
4. Never attack enemy positions when combat odds are below 50%; reinforce, merge, or cut supply lines instead.
5. Rail large, concentrated field armies directly to threatened front-line hubs rather than feeding small isolated detachments.
6. Heavily garrison and fortify Washington to level 2 whenever Confederate armies occupy adjacent cities.
7. Never attack Richmond or heavily garrisoned capitals without overwhelming numbers (at least 3:1 odds).
8. Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington, Manassas) on Turn 1 to maximize income.
9. Join and concentrate armies in key transit hubs under 8-star or best available generals before engaging major Rebel stacks.
10. Never attack or march with unsupplied armies (0 supply) due to severe 50% combat penalties and heavy winter attrition.
11. Maintain active naval commerce raiding only after ground recruiting needs and front-line garrisons are fully funded.
12. Fortify key frontier choke points (Louisville, Cincinnati, Washington) early to blunt Confederate offensive momentum.

### Version 35, after game 35 (standard: Rebel victory: time expired, 24 turns)

**Diagnosis.** The Union built a commanding numerical and territorial advantage (272k men, 24 cities), but suffered a timeout loss in March 1865 because operations devolved into an endless city-trading cycle in the deep South and Midwest. Failure to decisively hunt down and destroy major Rebel field armies (Bragg, Beauregard) allowed the AI to constantly retake border hubs (Louisville, Paducah, St. Louis), keeping the city count below the 32-city victory threshold.

**Strategy for the next game.** Execute a rapid Turn 1 expansion into border neutrals (Baltimore, Louisville, Paducah, Manassas), fortifying key frontier pivots. Mass two dominant Western and Eastern army groups under top-tier generals (Grant, Sherman) to systematically destroy mobile Confederate field armies and secure the Mississippi and Tennessee corridors. Once Confederate field forces are eliminated, drive decisively past the 32-city victory threshold or assault Richmond with 3:1 numerical superiority before 1865.

**Changes:**

- added: To avoid timeout defeats by 1865, actively eliminate enemy armies and push past 30 cities rather than passively swapping deep South territory. (Game 35 was lost on time expiration at 24 cities despite huge manpower supremacy because operations traded cities rather than forcing a decisive conclusion.)
- added: Always resupply frontline corps immediately when supply falls to 1, avoiding unsupplied status in winter attrition months. (McDowell and McClellan suffered multiple turns out of supply, drastically lowering combat effectiveness and suffering attrition.)
- revised: Hold Midwest border hubs (St. Louis, Louisville, Cincinnati) with fortified garrisons to prevent Rebel raiders from rolling up rear supply lines. (Bragg and Beauregard repeatedly captured unfortified Midwest hubs (St. Louis, Indianapolis, Cincinnati), forcing repeated retreats.)
- dropped: Monitor total Confederate city count every turn; when Rebels reach 25+ cities, shift all priorities to reclaiming lost territory. (Rebels rarely held 25+ cities once Union expanded; the primary danger is stagnating in the low 20s and running out the clock.)

**Notebook:**

1. Recruit aggressively from Turn 1 with all available funds; never hoard cash above $300 while cities offer recruits.
2. Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington, Manassas) on Turn 1 to maximize early revenue.
3. Hold Midwest border hubs (St. Louis, Louisville, Cincinnati) with fortified garrisons to prevent Rebel raiders from rolling up rear supply lines.
4. Never attack enemy positions when combat odds are below 50%; reinforce, merge, or cut supply lines instead.
5. Join and concentrate field armies under 8-star generals (Grant, Sherman) into 40k+ death stacks to hunt and crush Confederate field armies.
6. Rail large, concentrated field armies directly to threatened front-line hubs rather than feeding small isolated detachments.
7. Heavily garrison and fortify Washington to level 2 whenever Confederate armies occupy adjacent cities.
8. Never attack Richmond or heavily fortified capitals without overwhelming numbers (at least 3:1 odds).
9. Never attack or march with unsupplied armies (0 supply) due to severe 50% combat penalties and heavy winter attrition.
10. Maintain active naval commerce raiding only after ground recruiting needs and front-line garrisons are fully funded.
11. To avoid timeout defeats by 1865, actively eliminate enemy armies and push past 30 cities rather than passively swapping deep South territory.
12. Always resupply frontline corps immediately when supply falls to 1, avoiding unsupplied status in winter attrition months.

### Version 36, after game 36 (alternate: Rebel victory: capital captured, 7 turns)

**Diagnosis.** Despite holding Richmond, Norfolk, and Raleigh and outnumbering the Rebels 2:1, Washington was left completely undefended when Beauregard occupied adjacent Harper's Ferry, allowing an instant sudden-death capture.

**Strategy for the next game.** Expand rapidly into border cities on Turn 1, prioritize Washington's garrison and fortifications whenever Virginia/Maryland borders are contested, mass 40k+ stacks under Grant and Sherman to systematically crush Confederate field armies, and capture Confederate capitals only with secured lines.

**Changes:**

- revised: Never leave Washington unoccupied when Confederate armies hold or enter adjacent cities (Harper's Ferry, Manassas, Baltimore, Fredericksburg); garrison it immediately. (Washington was left empty while enemy armies occupied adjacent Harper's Ferry, resulting in an immediate capital loss defeat.)
- added: Fortify Washington to level 2 and maintain at least 15,000 defenders whenever enemy corps operate in Northern Virginia or Maryland. (Guarantees Washington cannot be taken in a sudden single-turn dash by flanking Rebel forces.)
- dropped: To avoid timeout defeats by 1865, actively eliminate enemy armies and push past 30 cities rather than passively swapping deep South territory. (Replaced by urgent capital preservation rules to prevent sudden defeat while winning on the scoreboard.)

**Notebook:**

1. Recruit aggressively from Turn 1 with all available funds; never hoard cash above $300 while cities offer recruits.
2. Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington, Manassas) on Turn 1 to maximize early revenue.
3. Never leave Washington unoccupied when Confederate armies hold or enter adjacent cities (Harper's Ferry, Manassas, Baltimore, Fredericksburg); garrison it immediately.
4. Fortify Washington to level 2 and maintain at least 15,000 defenders whenever enemy corps operate in Northern Virginia or Maryland.
5. Hold Midwest border hubs (St. Louis, Louisville, Cincinnati) with fortified garrisons to prevent Rebel raiders from rolling up rear supply lines.
6. Never attack enemy positions when combat odds are below 50%; reinforce, merge, or cut supply lines instead.
7. Join and concentrate field armies under 8-star generals (Grant, Sherman) into 40k+ death stacks to hunt and crush Confederate field armies.
8. Rail large, concentrated field armies directly to threatened front-line hubs rather than feeding small isolated detachments.
9. Never attack Richmond or heavily fortified capitals without overwhelming numbers (at least 3:1 odds).
10. Never attack or march with unsupplied armies (0 supply) due to severe 50% combat penalties and heavy winter attrition.
11. Maintain active naval commerce raiding only after ground recruiting needs and front-line garrisons are fully funded.
12. Always resupply frontline corps immediately when supply falls to 1, avoiding unsupplied status in winter attrition months.

### Version 37, after game 37 (standard: Rebel victory: time expired, 24 turns)

**Diagnosis.** In Game 37, we built a strong military and captured Deep South cities, but Lee and Beauregard repeatedly raided behind our lines into Pennsylvania and Ohio (taking Philadelphia, Harrisburg, Pittsburgh, and Columbus). Chasing these incursions scattered our forces and delayed territorial consolidation, resulting in a time-limit expiration loss at 24 cities instead of achieving the 32-city victory condition or striking Richmond.

**Strategy for the next game.** In the next game, secure the border neutrals on Turn 1 and establish fortified anchor points at Washington, Baltimore, Cincinnati, and Louisville. Rapidly form a massive 50k+ army under Grant to crush Rebel field armies, while systematically clearing and holding sectors to push past the 32-city threshold before the March 1865 time limit.

**Changes:**

- revised: Hold Midwest and Mid-Atlantic hubs (Cincinnati, Columbus, Harrisburg, Louisville) with adequate garrisons to block Rebel raiders. (Lee and Beauregard repeatedly captured Pennsylvania and Ohio cities from the rear because our northern hubs were left empty.)
- added: Prevent isolated small detachments from advancing deep into the South without mutual support or garrison coverage. (Buell and Sherman took southern cities that were repeatedly recaptured by Van Dorn and Stuart because garrisons were absent.)
- revised: Drive aggressively toward the 32-city victory threshold before 1865 rather than engaging in endless city-trading in the rear. (The game timed out in March 1865 with Union holding 24 cities despite huge troop superiority; we must actively close out the win condition.)
- dropped: Maintain active naval commerce raiding only after ground recruiting needs and front-line garrisons are fully funded. (Naval raiding provided marginal returns compared to maintaining solid ground garrisons and pushing for the 32-city victory condition.)

**Notebook:**

1. Recruit aggressively every turn with all available funds; never hoard cash above $200 while cities offer recruits.
2. Secure high-value neutral border cities (Baltimore, Louisville, Paducah, Lexington, Manassas) on Turn 1 to maximize early income.
3. Never leave Washington unoccupied when Confederate armies hold or enter adjacent cities; fortify Washington to level 2 early.
4. Hold Midwest and Mid-Atlantic hubs (Cincinnati, Columbus, Harrisburg, Louisville) with adequate garrisons to block Rebel raiders.
5. Never attack enemy positions when combat odds are below 50%; reinforce, merge, or cut supply lines instead.
6. Join and concentrate field armies under 8-star generals (Grant, Sherman) into 50k+ death stacks to hunt and crush Confederate field armies.
7. Rail large, concentrated strike armies directly to threatened front-line sectors to rapidly eliminate breakthrough forces like Lee.
8. Prevent isolated small detachments from advancing deep into the South without mutual support or garrison coverage.
9. Never attack Richmond or heavily fortified capitals without overwhelming numbers (at least 3:1 odds) and full supply.
10. Never attack or march with unsupplied armies (0 supply) due to severe 50% combat penalties and winter attrition.
11. Always resupply frontline corps immediately when supply falls to 1, especially before winter attrition months (Jan, Mar, May, Nov).
12. Drive aggressively toward the 32-city victory threshold before 1865 rather than engaging in endless city-trading in the rear.

### Version 38, after game 38 (alternate: Union victory: share of total income, 10 turns)

**Diagnosis.** Decisive victory via 60% income share in November 1862. Sherman swept the Mississippi Valley to capture Memphis, Vicksburg, and New Orleans, while ironclad commerce raiding throttled Confederate finances. Meanwhile, a fortified Washington repelled repeated assaults by Stuart, and defensive rail maneuvers blunted Jackson's deep Midwest raids.

**Strategy for the next game.** Maximize early economic expansion by securing border neutrals on Turn 1 while building a level 2 fort at Washington. Concentrate eastern forces to defend the capital and rail interceptors against Rebel incursions. Simultaneously push Sherman down the Mississippi to capture Memphis, Vicksburg, and New Orleans, supported by ironclad naval raids to achieve a swift 60% income victory.

**Changes:**

- revised: Drive a strong western army (Sherman/Grant) down the Mississippi corridor to take Memphis, Vicksburg, and New Orleans, gutting Rebel income. (Targeting the Mississippi Valley captures high-value ports, cuts Confederate connections, and reliably triggers an early income victory.)
- added: Build ironclads and maintain continuous commerce raiding; sinking $50-$100 Rebel cash per turn accelerates income victory. (Ironclad fleet raids drained Rebel treasury every turn without risking land attrition, accelerating the 60% income threshold.)
- revised: Avoid costly direct assaults on heavily fortified enemy capitals like Richmond; win via income share, encirclement, or collapse. (Replaced the old 32-city rule with income share and encirclement focus, which proved much faster and safer.)

**Notebook:**

1. Recruit aggressively every turn across all offered hubs; never hoard cash above $200 when recruitment is available.
2. Secure neutral border cities (Baltimore, Louisville, Paducah, Lexington) immediately on Turn 1 to build early income dominance.
3. Fortify Washington to level 2 early and maintain a 30k+ garrison; defender fort multipliers inflict devastating losses on Rebel attackers.
4. Drive a strong western army (Sherman/Grant) down the Mississippi corridor to take Memphis, Vicksburg, and New Orleans, gutting Rebel income.
5. Build ironclads and maintain continuous commerce raiding; sinking $50-$100 Rebel cash per turn accelerates income victory.
6. Rail reserve corps directly to intercept or pin breakthrough Rebel raiders threatening rear hubs like Harrisburg or Columbus.
7. Never initiate attacks with odds below 50%; merge forces, cut Rebel supply, or force them to attack fortified positions.
8. Join and concentrate field armies under 7-8 star generals (Grant, Sherman, McClellan) rather than scattering small corps.
9. Never advance or attack with 0-supply armies; resupply immediately when supply drops to 1, especially before winter attrition months.
10. Garrison or retake Midwest rail and recruitment centers (Cincinnati, Indianapolis, Columbus) to prevent enemy isolation plays.
11. Avoid costly direct assaults on heavily fortified enemy capitals like Richmond; win via income share, encirclement, or collapse.
12. Surround retreating enemy forces without friendly adjacent retreat paths to force complete surrenders.

### Version 39, after game 39 (standard: Rebel victory: time expired, 24 turns)

**Diagnosis.** The game was lost on time because deep, uncoordinated thrusts into Georgia and Florida overextended Union corps, leading to the destruction of Buell and Banks while Rebel raiders gutted our Midwest rear. In the late game, massive cash reserves were hoarded instead of being converted into recruits, and multiple futile assaults against level-2 fortified Richmond wasted critical armies and momentum.

**Strategy for the next game.** Open by fortifying Washington and securing neutral border cities on Turn 1. Build and maintain commerce raiding fleets to drain Confederate income. Form two primary doomstacks in the East and West under Grant and McClellan while keeping regional defensive corps to protect Midwest rail hubs from Rebel raiders. Advance along a contiguous territorial front rather than plunging isolated corps into the deep South, and win through economic and city dominance without suiciding armies against fortified 

**Changes:**

- revised: Never send isolated corps deep into the Deep South (Atlanta, Savannah, Jacksonville) without securing adjacent supply lines and rear hubs. (Buell and Banks were repeatedly isolated and crushed in Jacksonville and Montgomery after advancing without rear support.)
- revised: Never assault level-2 fortified enemy capitals (Richmond) head-on; win via income share, encirclement, or peripheral conquest. (Repeated assaults against Beauregard in fortified Richmond failed at 23-35% odds, burning men and turns at the end.)
- revised: Join field armies into 50k-80k doomstacks under 7-8 star generals (Grant, McClellan, Sherman) before launching major offensives. (Consolidated large armies commanded by Grant and McClellan consistently won field battles and forced surrenders.)

**Notebook:**

1. Recruit aggressively every turn across all offered hubs; never hoard cash above $200 when recruitment is available.
2. Secure neutral border cities (Baltimore, Louisville, Paducah, Lexington) immediately on Turn 1 to build early income dominance.
3. Fortify Washington to level 2 early and maintain a 30k+ garrison; defender fort multipliers inflict devastating losses on Rebel attackers.
4. Join field armies into 50k-80k doomstacks under 7-8 star generals (Grant, McClellan, Sherman) before launching major offensives.
5. Never send isolated corps deep into the Deep South (Atlanta, Savannah, Jacksonville) without securing adjacent supply lines and rear hubs.
6. Guard and retake Midwest rail and recruitment centers (Cincinnati, Indianapolis, Columbus, St. Louis) immediately to prevent rear collapse.
7. Never assault level-2 fortified enemy capitals (Richmond) head-on; win via income share, encirclement, or peripheral conquest.
8. Never initiate attacks with odds below 50%; merge forces, cut Rebel supply, or force them to attack fortified positions.
9. Resupply armies when supply drops to 1, especially before winter attrition months (Jan, Mar, May, Nov) to prevent strength loss.
10. Rail reserve corps directly to intercept or pin breakthrough Rebel raiders threatening rear hubs like Harrisburg or Columbus.
11. Build ironclads and maintain continuous commerce raiding; sinking $50-$100 Rebel cash per turn accelerates economic collapse.
12. Surround retreating enemy forces without friendly adjacent retreat paths to force complete surrenders.

### Version 40, after game 40 (alternate: Union victory: share of total income, 11 turns)

**Diagnosis.** Decisive Union victory in November 1862 via 60% income dominance after 11 turns. The Turn 1 neutral city grab immediately established an overwhelming income advantage ($410+). Washington was fortified to level 2 and reinforced via rail with Meade, easily shattering three massive assaults by Stuart's 30k doomstack with fort-multiplied defense. In the West, Grant, Banks, and Rosecrans methodically captured St. Louis, Springfield, Fort Donelson, Memphis, Decatur, and Vicksburg while commerce raiding continuously drained Rebel funds.

**Strategy for the next game.** On Turn 1, capture all accessible neutral border cities and initiate commerce raiding to establish an early cash and income lead. Fortify Washington to level 2 and maintain a dedicated garrison to absorb eastern Rebel attacks. Maximize recruitment each turn across all offered hubs, combine Western forces under Grant and Banks to systematically take Mississippi and Tennessee valley hubs, and win by reaching the 60% total income threshold.

**Changes:**

- revised: Secure neutral border cities (Baltimore, Louisville, Paducah, Lexington, Fredericksburg) on Turn 1 to build immediate income dominance. (Fredericksburg provides critical buffer and income on Turn 1 alongside the other border neutrals.)
- revised: Join field armies into 40k-80k doomstacks under top-tier generals (Grant, Sherman, Meade) before launching major offensives. (Meade proved to be an elite defensive and offensive general when reinforced into high-strength stacks.)
- revised: Rail reserve corps directly to reinforce threatened hubs or intercept breakthrough Rebel raiders before they capture key cities. (Railing Meade directly into Washington immediately before Stuart attacked saved the capital and inflicted massive casualties.)

**Notebook:**

1. Recruit aggressively every turn across all offered hubs; never hoard cash above $200 when recruitment is available.
2. Secure neutral border cities (Baltimore, Louisville, Paducah, Lexington, Fredericksburg) on Turn 1 to build immediate income dominance.
3. Fortify Washington to level 2 early and maintain a strong garrison; defender fort multipliers inflict devastating losses on Rebel attackers.
4. Join field armies into 40k-80k doomstacks under top-tier generals (Grant, Sherman, Meade) before launching major offensives.
5. Never send isolated corps deep into the Deep South without securing adjacent supply lines and neighboring rear hubs.
6. Guard and retake Midwest rail and recruitment centers (Cincinnati, Indianapolis, Columbus, St. Louis) immediately to prevent rear collapse.
7. Never assault level-2 fortified enemy capitals head-on; win via income share (60%), peripheral encirclement, or attrition.
8. Never initiate attacks with odds below 50%; merge forces, cut Rebel supply, or force enemy stacks to attack fortified positions.
9. Resupply armies when supply drops to 1, especially before winter attrition months (Jan, Mar, May, Nov), to prevent strength loss.
10. Rail reserve corps directly to reinforce threatened hubs or intercept breakthrough Rebel raiders before they capture key cities.
11. Maintain continuous fleet commerce raiding from Turn 1; sinking Rebel cash each turn accelerates Confederate economic collapse.
12. Cut off enemy retreat routes to adjacent friendly cities before attacking to force complete surrenders of trapped Rebel armies.

### Version 41, after game 41 (standard: Union victory: capital captured, 23 turns)

**Diagnosis.** Union achieved a capital capture victory in November 1864 after 23 turns. Harper's Ferry level 2 fortification blunted early Virginia offensives, while Midwest counter-offensives trapped and destroyed several isolated Rebel forces (Johnston, Stuart, Beauregard). Once the Midwest and West were stabilized, Buell massed a 118,000-man grand army at Fredericksburg and stormed Richmond to seal the victory.

**Strategy for the next game.** Maximize Turn 1 recruitment and secure neutral border hubs. Fortify Washington and Harper's Ferry to level 2 to absorb Confederate Eastern attacks. Use Grant, Sherman, and McDowell in the West and Midwest to isolate and eliminate deep Rebel incursions. Simultaneously maintain fleet commerce raiding to erode Rebel income, and assemble a 100k+ grand army in Virginia to decisively seize Richmond.

**Changes:**

- revised: Fortify Washington and critical border hubs (like Harper's Ferry) to level 2; fort defense multipliers decimate attacking Rebel stacks. (Harper's Ferry level-2 fort repeatedly repelled Jackson's 20,000-man army with minimal Union losses, neutralizing the Shenandoah threat entirely.)
- revised: Assault fortified capitals directly once you assemble a 100k+ super-stack, or win via peripheral encirclement and economic collapse. (Buell's 108k-118k doomstack successfully captured Richmond against Jackson's 58k garrison across two consecutive assaults.)
- revised: Join field armies into 50,000-120,000 man doomstacks under top generals before launching major offensives or capital assaults. (Forming 100k+ stacks under capable commanders provides the raw combat weight needed to overcome fortified capitals and large Rebel concentrations.)

**Notebook:**

1. Recruit aggressively every turn across all offered hubs; never hoard cash above $200 when recruitment is available.
2. Secure neutral border cities (Baltimore, Louisville, Paducah, Lexington, Fredericksburg) on Turn 1 to build immediate income dominance.
3. Fortify Washington and critical border hubs (like Harper's Ferry) to level 2; fort defense multipliers decimate attacking Rebel stacks.
4. Join field armies into 50,000-120,000 man doomstacks under top generals before launching major offensives or capital assaults.
5. Never send isolated corps deep into Rebel territory without securing adjacent supply lines and neighboring rear hubs.
6. Guard and retake Midwest rail and recruitment centers (Cincinnati, Indianapolis, Columbus, St. Louis) immediately to prevent rear collapse.
7. Assault fortified capitals directly once you assemble a 100k+ super-stack, or win via peripheral encirclement and economic collapse.
8. Cut off enemy retreat routes to adjacent friendly cities before attacking to force complete surrenders of trapped Rebel armies.
9. Resupply armies when supply drops to 1, especially before winter attrition months (Jan, Mar, May, Nov), to prevent strength loss.
10. Rail reserve corps directly to reinforce threatened hubs or intercept breakthrough Rebel raiders before they capture key cities.
11. Maintain continuous fleet commerce raiding from Turn 1; sinking Rebel cash each turn accelerates Confederate economic collapse.
12. Never initiate open field attacks with poor odds; let enemy raiders attack fortified hubs or surround them before striking.

### Version 42, after game 42 (alternate: Rebel victory: cities controlled, 10 turns)

**Diagnosis.** Lost on turn 10 to Rebel 28-city territorial conquest. We completely stopped recruiting after early turns despite having $400-$800 in treasury, allowing manpower to stagnate while the Rebels raised massive stacks. Furthermore, leaving the Northeast corridor unguarded allowed J.E. Johnston to blitz Harper's Ferry, Baltimore, and Philadelphia uncontested.

**Strategy for the next game.** Execute early Turn 1 expansion into border cities, fortify Washington and Louisville, and recruit continuously every single turn without skipping. Form two 50k+ doomstacks under Grant and McClellan to crush invading Rebel armies in the Midwest and East while using rail defense to safeguard Philadelphia, Baltimore, and Cincinnati from flanking maneuvers.

**Changes:**

- revised: Call troops and recruit every turn without exception when cash is available; never skip recruitment to hoard money or focus purely on drills. (We skipped recruitment across five turns despite having over $600 in the treasury, letting our troop count stagnate while the Rebels out-produced us.)
- added: Protect the Northeast corridor (Philadelphia, Baltimore, Washington, Harper's Ferry); never leave them completely empty for enemy raiders. (J.E. Johnston marched unopposed through Harper's Ferry to Baltimore and Philadelphia, pushing the Rebels over the 28-city victory limit.)
- added: Track the 28-city threshold constantly; recapture lost peripheral hubs promptly to prevent sudden Confederate territorial victory. (The game ended instantly in late 1862 because the Rebels quietly reached 29 cities while we focused narrowly on Richmond.)
- dropped: Never initiate open field attacks with poor odds; let enemy raiders attack fortified hubs or surround them before striking. (Replaced by more critical defensive and strategic recruitment imperatives.)

**Notebook:**

1. Call troops and recruit every turn without exception when cash is available; never skip recruitment to hoard money or focus purely on drills.
2. Secure neutral border cities (Baltimore, Louisville, Paducah, Lexington, Fredericksburg) on Turn 1 to build immediate income dominance.
3. Fortify Washington and Louisville to level 2; fort defense multipliers decimate attacking Rebel stacks even when heavily outnumbered.
4. Join field armies into 50,000-120,000 man doomstacks under top generals before launching major offensives or capital assaults.
5. Protect the Northeast corridor (Philadelphia, Baltimore, Washington, Harper's Ferry); never leave them completely empty for enemy raiders.
6. Guard and retake Midwest rail and recruitment centers (Cincinnati, Indianapolis, Columbus, St. Louis) immediately to prevent rear collapse.
7. Assault fortified capitals directly once you assemble a 100k+ super-stack, or win via peripheral encirclement and economic collapse.
8. Cut off enemy retreat routes to adjacent friendly cities before attacking to force complete surrenders of trapped Rebel armies.
9. Resupply armies when supply drops to 1, especially before winter attrition months (Jan, Mar, May, Nov), to prevent strength loss.
10. Rail reserve corps directly to intercept breakthrough Rebel raiders before they capture vital northern industrial hubs.
11. Maintain continuous fleet commerce raiding from Turn 1; sinking Rebel cash each turn accelerates Confederate economic collapse.
12. Track the 28-city threshold constantly; recapture lost peripheral hubs promptly to prevent sudden Confederate territorial victory.

### Version 43, after game 43 (standard: Rebel victory: capital captured, 2 turns)

**Diagnosis.** Catastrophic Turn 2 defeat caused by completely vacating Washington. McDowell moved to Fredericksburg on Turn 1 and Manassas on Turn 2 while Jackson took Harper's Ferry. With no garrison in Washington, Jackson walked in unopposed for an instant Rebel capital capture victory.

**Strategy for the next game.** Ensure Washington is permanently garrisoned and fortified from Turn 1. Secure neutral border cities (Louisville, Baltimore, Paducah) without vacating capital defense, rail reinforcements to hot sectors, build overwhelming doomstacks, and execute commerce raiding until Richmond can be safely besieged.

**Changes:**

- added: Never leave Washington empty under any circumstances; keep a dedicated garrison or fortify it immediately if enemy forces hold Harper's Ferry or Manassas. (Game 43 was instantly lost on Turn 2 because Washington was left completely empty while Jackson was adjacent in Harper's Ferry.)
- revised: Secure neutral border cities (Baltimore, Louisville, Paducah, Lexington) on Turn 1 to expand income while keeping capital defenses secure. (Removed Fredericksburg as an automatic Turn 1 target since marching McDowell out of Washington left the capital undefended.)
- dropped: Track the 28-city threshold constantly; recapture lost peripheral hubs promptly to prevent sudden Confederate territorial victory. (Dropped to make room for mandatory capital defense rule; city count monitoring is secondary to survival.)

**Notebook:**

1. Call troops and recruit every turn without exception when cash is available; never skip recruitment to hoard money or focus purely on drills.
2. Never leave Washington empty under any circumstances; keep a dedicated garrison or fortify it immediately if enemy forces hold Harper's Ferry or Manassas.
3. Secure neutral border cities (Baltimore, Louisville, Paducah, Lexington) on Turn 1 to expand income while keeping capital defenses secure.
4. Fortify Washington and Louisville to level 2; fort defense multipliers decimate attacking Rebel stacks even when heavily outnumbered.
5. Join field armies into 50,000-120,000 man doomstacks under top generals before launching major offensives or capital assaults.
6. Protect the Northeast corridor (Philadelphia, Baltimore, Washington, Harper's Ferry); never leave them open to adjacent enemy raiders.
7. Guard and retake Midwest rail and recruitment centers (Cincinnati, Indianapolis, Columbus, St. Louis) immediately to prevent rear collapse.
8. Assault fortified capitals directly once you assemble a 100k+ super-stack, or win via peripheral encirclement and economic collapse.
9. Cut off enemy retreat routes to adjacent friendly cities before attacking to force complete surrenders of trapped Rebel armies.
10. Resupply armies when supply drops to 1, especially before winter attrition months (Jan, Mar, May, Nov), to prevent strength loss.
11. Rail reserve corps directly to intercept breakthrough Rebel raiders before they capture vital northern industrial hubs.
12. Maintain continuous fleet commerce raiding from Turn 1; sinking Rebel cash each turn accelerates Confederate economic collapse.

### Version 44, after game 44 (alternate: Union victory: share of total income, 10 turns)

**Diagnosis.** Game 44 was a clean 10-turn economic victory on the alternate map. Early seizure of neutral border hubs and fortifying Louisville allowed us to repel repeated Confederate attacks in the West while massing McDowell in Virginia. Taking Richmond in January 1862 and rolling through North Carolina coastal ports, combined with relentless commerce raiding and disciplined recruitment, pushed Union income past the 60% threshold.

**Strategy for the next game.** Execute Turn 1 neutral city captures and fortify Louisville and Washington. Maintain continuous naval commerce raiding. Spend all available cash each turn recruiting in major depots. Mass eastern forces under McDowell to take Richmond and North Carolina ports, while using fortified western hubs to absorb Confederate thrusts, achieving a rapid economic or territorial victory.

**Changes:**

- revised: Exploit weakly defended capitals or push coastal peripheries (Norfolk, Raleigh, Wilmington) to rapidly secure the 60% income victory threshold. (Game 44 demonstrated that capturing Richmond early and mopping up Atlantic seaports guarantees an income-share win without requiring massive bloody attritional assaults in the deep interior.)

**Notebook:**

1. Call troops and recruit every turn without exception when cash is available; never skip recruitment to hoard money or focus purely on drills.
2. Never leave Washington empty under any circumstances; keep a dedicated garrison or fortify it immediately if enemy forces hold Harper's Ferry or Manassas.
3. Secure neutral border cities (Baltimore, Louisville, Paducah, Lexington) on Turn 1 to expand income while keeping capital defenses secure.
4. Fortify Washington and Louisville to level 2; fort defense multipliers decimate attacking Rebel stacks even when heavily outnumbered.
5. Join field armies into 50,000-120,000 man doomstacks under top generals before launching major offensives or capital assaults.
6. Protect the Northeast corridor (Philadelphia, Baltimore, Washington, Harper's Ferry); never leave them open to adjacent enemy raiders.
7. Guard and retake Midwest rail and recruitment centers (Cincinnati, Indianapolis, Columbus, St. Louis) immediately to prevent rear collapse.
8. Exploit weakly defended capitals or push coastal peripheries (Norfolk, Raleigh, Wilmington) to rapidly secure the 60% income victory threshold.
9. Cut off enemy retreat routes to adjacent friendly cities before attacking to force complete surrenders of trapped Rebel armies.
10. Resupply armies when supply drops to 1, especially before winter attrition months (Jan, Mar, May, Nov), to prevent strength loss.
11. Rail reserve corps directly to intercept breakthrough Rebel raiders before they capture vital northern industrial hubs.
12. Maintain continuous fleet commerce raiding from Turn 1; sinking Rebel cash each turn accelerates Confederate economic collapse.

### Version 45, after game 46 (alternate: Union victory: share of total income, 10 turns)

**Diagnosis.** The Union achieved an early 60% income victory in November 1862 by executing a disciplined dual-theater strategy. In the West, Louisville was held and fortified while Grant and Rosecrans systematically liberated Missouri and pushed down the Mississippi corridor to take Memphis, Vicksburg, and Jackson. In the East, fortifying Washington and railing reinforcements directly to the capital easily smashed Lee's massive counteroffensive, while Sherman seized an undefended Richmond. Continuous naval commerce raiding drained Rebel treasuries throughout the war.

**Strategy for the next game.** Open by seizing vital neutral border cities and initiating round-the-clock naval commerce raiding. Upgrade fortifications at Washington and Louisville to level 2 to create impassable defensive bastions. Maximize recruitment every turn across available hubs, merge western and eastern forces into decisive doomstacks under Grant, Sherman, and Rosecrans, and advance methodically down the Mississippi and toward Richmond to capture Confederate income hubs.

**Changes:**

- revised: Call troops and recruit strictly from the offered list every turn when cash allows; never skip recruitment to hoard money or drill idle units. (Clarified that recruitment commands must strictly match the offered cities list to avoid illegal orders.)
- revised: Rail reserve corps directly to threatened border bastions (Louisville, Washington) to intercept incoming Rebel thrusts. (Railing reserves to Louisville and Washington effectively turned the tide against repeated Johnston and Lee offensives.)

**Notebook:**

1. Call troops and recruit strictly from the offered list every turn when cash allows; never skip recruitment to hoard money or drill idle units.
2. Never leave Washington empty; maintain a dedicated garrison and fortify to level 2 early to crush any Confederate offensive.
3. Secure neutral border cities (Baltimore, Louisville, Lexington, Paducah) on Turn 1 to maximize early income and establish defensive anchors.
4. Fortify Louisville and Washington to level 2; fort defense multipliers shatter superior Rebel doomstacks repeatedly.
5. Join field armies into 50,000-120,000 man doomstacks under top commanders (Grant, Sherman, Rosecrans) before striking deep into Confederate territory.
6. Protect the Northeast corridor (Philadelphia, Baltimore, Washington, Harper's Ferry); eliminate adjacent raiders immediately.
7. Guard and immediately recapture Midwest rail hubs (St. Louis, Indianapolis, Cincinnati, Columbus) to maintain vital reinforcement networks.
8. Exploit weakly garrisoned Confederate hubs and capitals (Richmond, Memphis, Vicksburg) to rapidly push over the 60% income victory threshold.
9. Cut off Rebel retreat paths into adjacent friendly cities before attacking to force complete surrenders of trapped enemy forces.
10. Resupply armies whenever supply drops to 1, particularly prior to seasonal attrition turns (Jan, Mar, May, Nov).
11. Rail reserve corps directly to threatened border bastions (Louisville, Washington) to intercept incoming Rebel thrusts.
12. Maintain continuous fleet commerce raiding from Turn 1; steadily sinking Rebel cash starves their recruitment and supply.

### Version 46, after game 47 (standard: Rebel victory: time expired, 24 turns)

**Diagnosis.** The game was lost on time (March 1865) despite holding 27 cities and overwhelming economic superiority because massive armies were repeatedly thrown into a meat grinder against J.E. Johnston in level-2 fortified Richmond (defend 20 cap) rather than seizing the remaining 5 vulnerable peripheral cities (Wilmington, Norfolk, Charleston SC, Mobile) needed for the 32-city / 80% income victory condition.

**Strategy for the next game.** Open by fortifying Washington, securing border neutrals (Baltimore, Louisville, Paducah), and raiding with the fleet. Consolidate Western armies under Grant to sweep the Mississippi Valley and Deep South (Nashville, Atlanta, New Orleans, Jackson, Mobile). In the East, hold Washington and Pennsylvania with fortified chokepoints while sweeping exterior coastal cities (Norfolk, Wilmington, Charleston) to trigger a decisive 32-city victory without throwing stacks into Richmond's forts.

**Changes:**

- revised: Never attack heavily garrisoned level-2 fortified capitals (Richmond); bypass them to capture exterior cities and win via 32 cities or 80% income. (Repeated failed assaults on Richmond's level-2 forts with 60k+ stacks cost massive casualties and wasted turns that could have secured an easy 32-city victory.)
- revised: Resupply armies whenever supply drops to 1, particularly prior to seasonal attrition turns (Jan, Mar, May, Nov); never march with 0 supply. (McClellan attacked repeatedly while out of supply, halving his combat power and causing disastrous retreats.)
- revised: Maintain continuous fleet commerce raiding from Turn 1, and rebuild sunk ships to ensure ongoing economic attrition against Rebel cash. (Raiding fleet lost all ships by 1864 and was not replaced, allowing Rebel income to rebound late-game.)

**Notebook:**

1. Call troops and recruit strictly from the offered list every turn when cash allows; never skip recruitment to hoard money or drill idle units.
2. Never leave Washington empty; maintain a dedicated garrison and fortify to level 2 early to crush any Confederate offensive.
3. Secure neutral border cities (Baltimore, Louisville, Lexington, Paducah) on Turn 1 to maximize early income and establish defensive anchors.
4. Fortify Louisville and Washington to level 2; fort defense multipliers shatter superior Rebel doomstacks repeatedly.
5. Join field armies into 50,000-120,000 man doomstacks under top commanders (Grant, Sherman, Rosecrans) before striking deep into Confederate territory.
6. Never attack heavily garrisoned level-2 fortified capitals (Richmond); bypass them to capture exterior cities and win via 32 cities or 80% income.
7. Protect the Northeast corridor (Philadelphia, Baltimore, Washington, Harper's Ferry); eliminate adjacent raiders immediately.
8. Guard and immediately recapture Midwest rail hubs (St. Louis, Indianapolis, Cincinnati, Columbus) to maintain vital reinforcement networks.
9. Cut off Rebel retreat paths into adjacent friendly cities before attacking to force complete surrenders of trapped enemy forces.
10. Resupply armies whenever supply drops to 1, particularly prior to seasonal attrition turns (Jan, Mar, May, Nov); never march with 0 supply.
11. Rail reserve corps directly to threatened border bastions (Louisville, Washington) to intercept incoming Rebel thrusts.
12. Maintain continuous fleet commerce raiding from Turn 1, and rebuild sunk ships to ensure ongoing economic attrition against Rebel cash.

### Version 47, after game 48 (alternate: Union victory: share of total income, 7 turns)

**Diagnosis.** Fast 7-turn victory achieved through early expansion into neutral border cities, relentless recruitment, fortifying Washington and Louisville, continuous naval commerce raiding, and bypassing Richmond to rapidly secure peripheral cities for an overwhelming 60% income majority.

**Strategy for the next game.** Open by claiming neutral border cities and commencing continuous naval raiding. Maximize per-turn recruitments, fortify key bastions (Washington, Louisville) to level 2, rail reserves to intercept Rebel thrusts, and expand swiftly across peripheral objectives (Missouri, Tennessee, Virginia periphery) to win by income or city count without risking costly assaults on Richmond.

**Changes:**

- revised: Never attack heavily garrisoned level-2 fortified capitals (Richmond); bypass them to capture exterior cities and win via 28 cities or 60% income. (Corrected the victory condition thresholds from 32 cities / 80% income to the exact game rules of 28 cities / 60% income, aligning strategic targets with victory triggers.)

**Notebook:**

1. Call troops and recruit strictly from the offered list every turn when cash allows; never skip recruitment to hoard money or drill idle units.
2. Never leave Washington empty; maintain a dedicated garrison and fortify to level 2 early to crush any Confederate offensive.
3. Secure neutral border cities (Baltimore, Louisville, Lexington, Paducah) on Turn 1 to maximize early income and establish defensive anchors.
4. Fortify Louisville and Washington to level 2; fort defense multipliers shatter superior Rebel doomstacks repeatedly.
5. Join field armies into 50,000-120,000 man doomstacks under top commanders (Grant, Sherman, Rosecrans) before striking deep into Confederate territory.
6. Never attack heavily garrisoned level-2 fortified capitals (Richmond); bypass them to capture exterior cities and win via 28 cities or 60% income.
7. Protect the Northeast corridor (Philadelphia, Baltimore, Washington, Harper's Ferry); eliminate adjacent raiders immediately.
8. Guard and immediately recapture Midwest rail hubs (St. Louis, Indianapolis, Cincinnati, Columbus) to maintain vital reinforcement networks.
9. Cut off Rebel retreat paths into adjacent friendly cities before attacking to force complete surrenders of trapped enemy forces.
10. Resupply armies whenever supply drops to 1, particularly prior to seasonal attrition turns (Jan, Mar, May, Nov); never march with 0 supply.
11. Rail reserve corps directly to threatened border bastions (Louisville, Washington) to intercept incoming Rebel thrusts.
12. Maintain continuous fleet commerce raiding from Turn 1, and rebuild sunk ships to ensure ongoing economic attrition against Rebel cash.

### Version 48, after game 50 (alternate: Union victory: share of total income, 7 turns)

**Diagnosis.** Game 50 on the alternate map was a swift, decisive 7-turn victory via 60% income share. Securing neutral border hubs on Turn 1 and fortifying Louisville and Washington blunted early Rebel drives. When A.S. Johnston launched a deep raid across the Midwest into Pennsylvania, Grant systematically liberated lost cities from behind while local recruitment in Harrisburg trapped and annihilated Johnston upon his suicidal assault. In the West, Pope swept down the Mississippi capturing Fort Donelson, Memphis, Vicksburg, and Jackson uncontested, while fleet commerce raiding continuously squeezed Rebel c

**Strategy for the next game.** Open by fortifying Washington and Louisville while seizing Baltimore, Lexington, Louisville, and Paducah on Turn 1. Maximize recruitment every single turn using all available cash from the troops list. Maintain fleet commerce raiding continuously to drain Confederate finances. Advance in the West along the Mississippi corridor with Grant and Pope taking lightly defended hubs, bypass Richmond's heavy fortifications, and secure an early economic or 28-city victory.

**Changes:**

- revised: Guard and immediately recapture Midwest rail hubs (St. Louis, Indianapolis, Cincinnati, Columbus) to maintain vital reinforcement networks. (Rebel raiders frequently bypass border fortresses into the Midwest; trailing them with a main army while recruiting ahead in Keystone cities traps and destroys them without derailing the overall campaign.)

**Notebook:**

1. Call troops and recruit strictly from the offered list every turn when cash allows; never skip recruitment to hoard money or drill idle units.
2. Never leave Washington empty; maintain a dedicated garrison and fortify to level 2 early to crush any Confederate offensive.
3. Secure neutral border cities (Baltimore, Louisville, Lexington, Paducah) on Turn 1 to maximize early income and establish defensive anchors.
4. Fortify Louisville and Washington to level 2; fort defense multipliers shatter superior Rebel doomstacks repeatedly.
5. Join field armies into 50,000-120,000 man doomstacks under top commanders (Grant, Sherman, Rosecrans) before striking deep into Confederate territory.
6. Never attack heavily garrisoned level-2 fortified capitals (Richmond); bypass them to capture exterior cities and win via 28 cities or 60% income.
7. Protect the Northeast corridor (Philadelphia, Baltimore, Washington, Harper's Ferry); eliminate adjacent raiders immediately.
8. Guard and immediately recapture Midwest rail hubs (St. Louis, Indianapolis, Cincinnati, Columbus) to maintain vital reinforcement networks.
9. Cut off Rebel retreat paths into adjacent friendly cities before attacking to force complete surrenders of trapped enemy forces.
10. Resupply armies whenever supply drops to 1, particularly prior to seasonal attrition turns (Jan, Mar, May, Nov); never march with 0 supply.
11. Rail reserve corps directly to threatened border bastions (Louisville, Washington) to intercept incoming Rebel thrusts.
12. Maintain continuous fleet commerce raiding from Turn 1, and rebuild sunk ships to ensure ongoing economic attrition against Rebel cash.

