# Agent team log

I am Executive Producer and Creative Director. Agents proposed; I decided. I wanted to see
how well AI agents can play games designed for humans.

## The team

| Agent | Could see and do | What it recommended or produced | What I decided | Evidence |
|---|---|---|---|---|
| **Implementation agent**: Claude Code in VS Code, `claude-opus-5-5`, one long session (2026-10-23 to 2026-11-06) | Read and write in my workspace; run local commands (Python, QB64-PE, tests, live runs I approved); fetch public pages. No push, no PR, no credentials in code. | The port, the five-operation interface, engine process, runner, baselines, model and learning players, tests and the QB64 harness. Later: every learning experiment, the held-out evaluation, the research report, the browser UI's integration and watch mode, and the recording. | Its proposals I accepted or changed are under Decisions. | `AGENTS.md`, `CLAUDE.md`, `SUITE.md`; the session: [docs/agent-session.md](docs/agent-session.md) |
| **Reusable skill**: `port-mechanic` | Runs inside the implementation agent, with its permissions | One SUB at a time: hand trace with scripted dice, test first, port with QB64 numeric rules, compare under QB64, record ambiguities. It encodes my Week 3 method. | Used for both porting sessions. | `.claude/skills/port-mechanic/SKILL.md`; invoked 2026-10-23 (SUB victor) and 2026-10-25 (navies and railroads) |
| **Independent reviewer**: `rules-reviewer` | A fresh subagent with no building context, read-only tools, and no instruction to approve | 2026-10-23: 1 blocking, 8 should-fix and 15 notes. 2026-10-25, on navies and railroads: no rule mismatch, 7 should-fix. | I had the blocking and should-fix items fixed; the minor notes were fixed or documented as known limitations. | `.claude/agents/rules-reviewer.md`; `review.md` |
| **UI builder**: a ChatGPT Plus agent | Its own folder, `play-ui/`, isolated from `cws/` and the training runs | The browser UI: a local server over the existing engine process, with its own tests | I wanted it to show the agent playing and to make the game easier for playtesters. I kept it isolated, and had it reviewed: Claude checked the integration on 2026-11-03 and added watch mode. | `play-ui/` |
| **Playing agents** (not builders): Gemini 3.5 Flash-Lite, 3.5 Flash and 3.7 Flash on Vertex AI | `observe()`, `legal_actions()`, its last 3 turns and, for learners, its own notebook; no tools, files, map, opponent code or dice | Union orders, in batches | - | `cws/players/`, `lessons/`, `traces/` |

## Decisions

| Decision | Made by | Alternative | Why |
|---|---|---|---|
| Game: VGA Civil War Strategy v2.11, the Union against the original computer | me, Week 3 (2026-09-27) | an original game | I wanted to see how well AI agents can play games designed for humans. |
| Live provider: Gemini on Vertex AI | me, 2026-10-23 | an Anthropic or OpenAI key | We got GCP credits from Columbia. |
| Exclude relieving commanders and capital moves; Random Events off | the implementation agent; I accepted | the full game | The game might have become too complicated to learn with a small training batch. |
| Bring navies and railroads into scope | me, 2026-10-25 | the land war only | To have a greater degree of strategy and complexity. |
| Verify against the original compiled with QB64, not only hand traces | the implementation agent; I accepted | hand traces only (my Week 3 plan) | Hand traces can miss things: running the original on the same seeds and commands catches mismatches I could miss by hand. |
| Outcome tiers (win / held out / decisive loss) instead of VP share | the implementation agent, after a test showed VP share rewards losing early; I accepted | VP share | Granular analysis of results. |
| Baseline: the original's own AI, playing the Union on the Union's screen | the implementation agent; I accepted | a hand-written heuristic | It is the opponent the game was designed around, so "as good as the 1998 AI" means something. |
| Model replies batched, up to 8 orders a call | the implementation agent; I accepted | one order a call | One order a call would need about 300 calls a game: too slow and too costly for the course budget. A human gives a turn's orders together; batching lets the model plan the same way. |
| Memory comparison: last 3 turns against the screen only | the implementation agent; I accepted | no comparison | I thought it would improve performance and help plan moves. |
| A learning player: a notebook the agent rewrites after each war, frozen before checks | me, 2026-10-26 | hand-tuning the prompt; fine-tuning | People get better at a game by playing it again and again, and I wanted an agent that does the same. Hand-tuning the prompt would be me playing through it; a notebook the agent writes itself keeps the learning the agent's. |
| A teacher: the review also sees the 1998 AI's replay (`gemini-e`) | the implementation agent; I approved | more wars with the same method | I thought seeing an expert play would make the agent learn quicker than on its own. |
| A frontier model on the plain method, for 100 wars (`gemini-h`) | me, 2026-10-27 | 30 wars | I wanted to test on a larger set of games, for better generalization. |
| Stop `gemini-h` at 50 wars | me, 2026-10-27 | finish 100 | The cost was too much. |
| Held-out evaluation: the declared pair, plus `gemini-f`, and 3.7 Flash with and without `gemini-h` | the implementation agent; I approved, 2026-11-03 | the declared pair only | |
| A spend preview in the browser UI: order prices, and the upkeep due at turn end | me, 2026-11-06, after my partner's playtest | no change before the deadline | It was my partner's one request: costs that only appeared once the turn ended had caught them off guard. |

## What the agents got wrong, and how it was caught

- **Porting bugs**, all caught by the QB64 comparison and fixed:
  - city names with a leading blank;
  - `evaluate` line 3019 ported with the wrong side;
  - arithmetic that rounded too often.
- **The independent review caught what the builder missed:**
  - a model batch could run past a mis-capitalised "End turn" into the next turn;
  - SUB victor had never been compared with QB64;
  - tests that could not fail on the slips they named;
  - a baseline condition dropped from line 2251. Fixing it changed the baseline's results.
- **The prompt grouped legal actions**, and the model answered "move 4 Paducah,
  Lexington". The first live trace caught it; each action is now listed whole.
- **Live runs:**
  - a network outage turned 84 training wars into fallback games; a guard now stops any
    war where half the calls fail;
  - the first 3.5 Flash run was invalid at a 2,048-token cap set for a model that reasons
    first.
- **Reporting:** several miscounts, all corrected after recomputing from the result files:
  - "120 tests";
  - "Washington fell in 15" (it was 11);
  - "22 wins, 4 hold-outs" after 49 wars (it was 21 and 5).

  The research report's generator scripts were lost when temporary files were cleaned;
  the report itself is unaffected.

Next time I would recompute every number from the data before it goes in a report, because
the agent made several miscounts I caught later. I would plan for failures: budget for
reasoning tokens and network drops, and guard against fallback games from the first run.
And I would decide the evaluation line-up earlier, before reusing the same 8 practice wars
for so many checks. The result that surprised me most: in my experiment, the best model came
close to the 1998 AI but didn't beat it.

## Game-project roles

I kept design (scope, the question, every experiment's go or stop) and the final quality
calls. Claude did the technical and production work, and the ChatGPT agent built the UI. The
independent reviewer and the QB64 harness covered quality.
