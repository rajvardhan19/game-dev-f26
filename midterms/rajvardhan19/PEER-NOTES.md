# Peer playtest notes

Anonymous observations only. Private feedback goes through CourseWorks.
My partner played this build from [PLAYTEST.md](PLAYTEST.md), a 15-minute guide with six questions.

## Notes I gave (playtest of a classmate's build, week of November 2)

It was pretty simple to set up and start, and nothing needed installing. The game’s text and responses felt like the original. When I tried a word it didn’t recognise, such as all, it gave a clear unknown-word response instead of an error.

I wasn’t always sure where the points came from. I found the house, took the lamp, moved the rug and went down the trap door with 35 out of 45 points, without finding the egg in the forest. The game said the episode would end in the cellar, but I didn’t realise that entering it early would leave points behind. Is there any indication before going down that there are still points available elsewhere?

I didn’t find any bugs or unexpected dead ends. The dark attic was unforgiving, but that seemed intentional: my second move, north, got me eaten by a grue, while turn on lamp followed by down was safe. That made me pay closer attention to the text.

I made the same mistake as the model player by heading straight for the cellar once the trap door appeared. In that run, knowing when to stop exploring seemed to be the main challenge.

The change I would make is a short message whenever the score changes, such as “+10 points.” That would make it easier to learn which actions earn points without constantly checking the status line.

## Notes I received

Received 2026-11-06, verbatim:

> It was pretty simple to set up and boot. The game worked as intended. I played the game
> myself and also watched the agent play it, and it was spot on when it came to the game's
> mechanics.
>
> I had to guess or refer to the documentation constantly because the game didn't show how
> much each move or action would cost. I could only see the cost once the turn ended, which
> sometimes caught me off guard. A spend preview would help here, since it would let me
> check whether I could afford a move before making it.
>
> I didn't spot any bugs or dead ends. Everything was well tuned and calibrated, and a bad
> move just lowered my chances of winning. The agent could only see what it was supposed to,
> like a player's point of view. And yes, the video showed the agent choosing its own moves.
>
> The one change I would make is adding the spend preview feature.

## What I changed because of them

- **The spend preview, 2026-11-06.** I added the feature my partner asked for.
  - Every order in the browser UI now shows its price, and its confirmation shows my treasury after it.
  - A line under the treasury shows what I have spent this turn and the supply upkeep charged when the turn
    resolves. That upkeep is the cost that caught my partner off guard.
  - It uses only what the player sees and rolls no dice, so it gives no hidden information.
  - Tests check every price and the upkeep against what the engine actually charges
    (`play-ui/test_bridge.py`).
- **Their other observations confirmed what the tests check:**
  - the agent saw only a player's view;
  - a bad move only lowered the chances of winning;
  - there were no bugs or dead ends;
  - the video showed the agent choosing its own moves.
