# Union Command — isolated playable UI

From the project root:

```sh
python3 play-ui/server.py
```

Open http://127.0.0.1:8765. Use `--port 8766` if that port is occupied.
Python 3.11+ and a browser are sufficient; no packages, API keys or paid calls
(except when watching a Gemini player, below).

Select map cities to inspect their visible garrisons. Select an army to filter
its legal orders. Every order explains its effect before confirmation. Use
End turn to resolve the war. Standard and alternate campaigns are available.
It is built for a desktop browser window.

## Spend preview

Added after a playtest (PEER-NOTES.md):
- Every order with a cash cost shows its price. Its confirmation shows the treasury after it: recruit $100, fortify $200,
  a wooden ship $100, an ironclad $200, and supply, whose price depends on your cash and the army's size.
- A line under the treasury shows what you have spent this turn, and the supply upkeep due when the turn resolves.
  Upkeep is 0.2 × each army's size in hundreds of men, paid if affordable and the army is not cut off.
- End turn repeats that warning.

All of it is computed from your own screen with the engine's arithmetic (SUB resupply, SUB iterate) and rolls no dice.
The upkeep is an estimate, because marches and battles resolve first. Tests check the prices and the upkeep against
what the engine actually charges.

## Watch an AI play

*Watch an AI* hands the war to an agent: the browser shows every order it submits,
accepted (✓) or refused (✗), with its source label, each model call's latency, tokens
and one-line note, and the map as the agent leaves it. The agent plays through the
project's own runner (`cws.runner.run_episode`), with the evaluation's limits; a
fallback turn is labelled `fallback`. Your own orders are locked while it plays.

- **The 1998 AI** is always available, free.
- **Gemini players** (`gemini-h` on 3.7 Flash with its own notebook; Flash-Lite with
  memory of 3 turns) make paid calls, so they are offered only when the server starts
  with `--live` and the Vertex settings, from the project root:

  ```sh
  set -a; . ./.env; set +a
  uv run --extra live python play-ui/server.py --live
  ```

  A Flash-Lite war costs about $0.02, a `gemini-h` war about $0.20-0.40.

Watched wars use practice war 101-104 or a random war, never an evaluation or training seed.

## Isolation from ongoing development

All UI files live here. This does not modify `cws/`, `viewer/`, training,
notebooks, results, traces, or the project's dependencies. At server startup,
the current Python engine and game data are copied to a temporary directory.
An independent `cws.server` process runs from that snapshot through the existing
`EngineProcess` interface. Later source edits do not change an active UI game;
restart the UI server to pick them up. The snapshot is removed when the server
exits normally. No rules are implemented or modified in this UI.

The browser receives observations and legal actions, plus runner-level outcome
information for the end screen. It cannot request raw traces or engine state.
The first game is practice war 101. *New campaign* offers a random war, whose seed
(1,000-999,999) no declared split uses, or practice war 101-104; evaluation and
training seeds are refused. Games have a 600-step limit. The browser never receives
the seed. Model players play only in *Watch an AI*, never in your game.

## Limits

One independent game per server, shared by tabs connected to that server. A
revision check rejects stale orders from another tab. Refreshing the page keeps
the active game; stopping the server loses it. New campaign replaces only this
UI's game. Existing terminal games cannot be imported. Underlying engine bugs
or rule changes belong to the engine owner and are not patched here.

Run the isolated bridge checks with `python3 -m unittest discover -s play-ui -p 'test_*.py' -v`.
CI runs them on every pull request. Stopping the server with Ctrl-C, closing its
terminal or a kill all remove the engine snapshot.
