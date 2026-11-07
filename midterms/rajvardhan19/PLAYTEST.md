# Playtest guide: 15 minutes with VGA Civil War Strategy

You command the Union against the game's original 1998 computer player. Thank you for
playing. This page is all you need. Nothing here makes paid model calls or needs a key.

## Setup (2 minutes)

From a clone of the course repository, with Python 3.11 or later and no installs:

```sh
cd midterms/rajvardhan19
python3 play-ui/server.py
```

Open the printed address, `http://127.0.0.1:8765`, in a desktop browser. Use
`127.0.0.1`, not `localhost`. If the port is busy, add `--port 8766`.

To play in a terminal instead, run `python3 -m cws.play` and type `help`.

## What to do

1. **Minutes 0-2.** Read the date bar and open *Campaign objectives*. Before you click
   anything, decide what you think you have to do to win.
2. **Minutes 2-10.** Play the standard war. Select a city to inspect it, and select an
   army to see its orders. *Find recruits* is free. Every order explains itself before
   you confirm it. Press *End turn* when you are done. Try at least one recruit, one
   march into another city and one attack.
3. **Minutes 10-13.** Under *New campaign*, start a random war on the alternate map
   and play two or three turns.
4. **Minutes 13-15.** Watch the 1998 AI play the Union by itself, in a terminal:

   ```sh
   python3 -m cws.play --watch original-ai --scenario alternate --seed 1002
   ```

   It takes about ten seconds. This is the strongest baseline the language-model
   players are measured against.

## What I would like to know

Please answer briefly and anonymously; nothing about you is needed.

1. What did you think the goal was after minute 2, and was it right?
2. One thing you had to guess, and the one question that would have removed the guess.
3. Which order or screen confused you, and what did you expect instead?
4. Did any turn's result surprise you? What happened, and what had you expected?
5. Anything broken: an error, a stuck screen, or an order the game refused without a
   clear reason.
6. Would you play another turn? Why or why not?

Send the answers through CourseWorks or as agreed by Friday, November 6. I will quote
them anonymously in `PEER-NOTES.md` with what I changed because of them.
