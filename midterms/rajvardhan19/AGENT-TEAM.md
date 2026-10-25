# Agent team log

> **TODO (student): rewrite this page in your own voice before submitting.**
> The rubric treats an agent-voiced log as missing authorship. The tables
> below record verifiable facts (who had what access, what each produced,
> where the evidence is). The "What I decided" column and the reflections
> are yours to write.

I am Executive Producer and Creative Director. Agents proposed; I decided.

## The team

| Agent | Could see and do | What it recommended or produced | What I decided | Evidence |
|---|---|---|---|---|
| **Implementation agent**: Claude Code in VS Code, model `claude-opus-5-5`, one session on 2026-10-23 | Read and write in my workspace; run local commands (Python, QB64-PE build, tests); fetch public web pages (QB64-PE source, pricing listings). No credentials, no push, no PR, no paid model calls. | Ported the scoped rules from CWSTRAT.BAS. Built the five-operation interface, the separate engine process, runner, baselines, model player, tests, terminal play and the QB64 differential harness. Proposed the scope exclusions, the outcome tiers, Random Events OFF, batched model replies and the limits. Found and fixed three porting bugs through the harness. | TODO | `AGENTS.md`, `CLAUDE.md`; session transcript: TODO link or export |
| **Reusable skill**: `port-mechanic` | Runs inside the implementation agent with its permissions | One procedure per mechanic: read one SUB, hand-trace with scripted dice, test first, port with QB64 numeric rules, compare with the original under QB64, record ambiguities, summarise for review. It encodes my Week 3 method. First invoked by name on 2026-10-23 to verify SUB victor and the main-module paths after the review. | TODO | `.claude/skills/port-mechanic/SKILL.md`; invocations: 2026-10-23 (victor verification); TODO: a second session (e.g. a peer-playtest fix) |
| **Independent reviewer**: `rules-reviewer` | A fresh subagent (2026-10-23) with none of the building session's context; read-only tools; no instruction to approve | 1 blocking, 8 should-fix and 15 notes, all in `review.md`. The blocking one: a model batch could run past a mis-capitalised "End turn" into the next turn. It also found that SUB victor had never been compared with QB64. | TODO: which findings I accepted, which I rejected and why (the implementation agent's responses are at the end of `review.md`) | `.claude/agents/rules-reviewer.md`; `review.md` |
| **Playing agent** (not a builder): Gemini on Vertex AI | `observe()`, `legal_actions()`, its own last 3 turns; no tools, files, Game, map, opponent code or dice | Union orders, one batch per call | - | `cws/players/model_player.py`; `traces/<date>-live/` |

## Decisions

Facts first; the reasons and the rejected alternatives are mine to write.

| Decision | Made by | Alternative | Why (TODO: student) |
|---|---|---|---|
| Game: VGA Civil War Strategy v2.11, the Union against the original computer | me, Week 3 (2026-09-27) | | |
| Method: one mechanic at a time, hand-traced with seeded dice; ambiguities in QUESTIONS.md; separate engine process; two-seed leak test | me, Week 3 | | |
| Live provider: Vertex AI (course credit) | me, 2026-10-23 | Anthropic or OpenAI key | |
| Build in `Designing-AI-Agents/midterm/`, submit as `midterms/rajvardhan19/` | me, 2026-10-23 | | |
| Exclude navies, railroads, relieve, capital moves; Random Events OFF | proposed by the implementation agent; accepted / rejected: TODO | the full game | |
| Verify against the original compiled with QB64, not only hand traces | proposed by the implementation agent; TODO | hand traces only (my Week 3 plan) | |
| Outcome tiers (win / held out / decisive loss) instead of VP share | proposed after a test showed VP share rewards losing early; TODO | VP share | |
| Strong baseline = the original's own Union AI on the Union's observation | proposed by the implementation agent; TODO | a hand-written heuristic | |
| Model replies batched (up to 8 actions per call) | proposed by the implementation agent; TODO | one action per call (about 300 calls per game) | |
| Memory ablation: last 3 turns vs observation only | proposed by the implementation agent; TODO | no ablation | |

## What the agents got wrong, and how it was caught

Facts for me to reflect on:

1. **City names kept a leading blank** from `CITIES.GRD`. The baseline
   recruited nothing and lost every game. Caught by its invalid-action count.
2. **`evaluate` line 3019 ported with the wrong side.** Caught by the QB64
   differential run (seed 1, command 38) and located with the `--debug`
   harness.
3. **Arithmetic rounded too often.** VP 697 instead of 696 (seed 2,
   command 200). Caught by the same run and settled by reading the C++ that
   QB64 generates.
4. **A first claim that the opponent reads the player's orders** came from
   the same misread of line 3019. It was corrected in the rule map.
5. **Two gaps the implementation agent missed and the independent review
   found.**
   - A model batch ran past a mis-capitalised "End turn" into the next turn
     (blocking).
   - "Verified against the original" claims covered no victory condition,
     because the harness never called SUB victor.
   Both were fixed, and the harness was rebuilt from verbatim line
   extracts (`review.md`, Response).

TODO: what this taught me about directing agents, and what I would set up
differently.

## Game-project roles

TODO: design, production, technical, art and quality. Which an agent
covered, which I kept, and what is still uncovered (for example, art is
the terminal map only).
