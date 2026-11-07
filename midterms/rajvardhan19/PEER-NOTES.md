# Peer playtest notes

Anonymous observations only. Private feedback goes through CourseWorks.
My partner played this build from [PLAYTEST.md](PLAYTEST.md), a 15-minute guide with six questions.

## Notes I gave (playtest of a classmate's build, week of November 2)

I playtested a classmate's build for 15 minutes and sent my notes to them directly by text.
The notes are private feedback, so they are not in this public repository; a copy is with my
CourseWorks submission.

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
