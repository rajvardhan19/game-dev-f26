# Implementation agent: VGA Civil War Strategy midterm

Standing instructions for any coding agent working in `midterms/rajvardhan19/`.
The student is Executive Producer and Creative Director; an agent proposes,
the student decides, merges and submits.

## What this project is

A bounded reconstruction of W. R. Hutsell's VGA Civil War Strategy v2.11
(QB64 port by Dave Mackey, MIT licence), played by a separate agent through
five operations, compared with the original game's own AI. Scope, exclusions
and evidence live in `docs/rule-source-map.md`; open questions in
`QUESTIONS.md`.

## The rule of evidence

A rule is correct only if it matches what CWSTRAT.BAS computes from the same
state and dice rolls. Never write a rule from memory of the game or from what
seems sensible.

- Translate one mechanic at a time with `.claude/skills/port-mechanic/SKILL.md`.
- Read only the SUB you are porting, plus
  `source/VariablesGuide.md` for the
  globals. Cite every port with `line N`.
- QBasic arithmetic is not Python arithmetic. Use `cws/qb.py`: decimal
  literals are doubles, arithmetic runs in double, an assignment rounds once
  to SINGLE and then half to even, comparisons cast both sides to SINGLE,
  and `AND`/`OR` never short-circuit, so every `RND` in a condition is
  consumed.
- Keep the source's quirks (unreachable `CASE`s, line 947's slots 1 and 2,
  line 2327's comparison with army size). Record each in `QUESTIONS.md`;
  do not "fix" the original.
- Record every ambiguity in `QUESTIONS.md` instead of guessing.

## Boundaries

- The engine (`cws/engine.py`, `cws/smarts.py`) owns state. The player sees
  only `observe`, `legal_actions` and `step`, in another process
  (`cws/server.py`, `cws/client.py`).
- Never put the dice, the seed, the opponent's routines or hidden enemy
  fields (leader, experience, supply, orders) into an observation, a legal
  action or a prompt.
- Never use a fixture or a baseline in place of a live model result, and never
  label a fallback move as a model move.
- No credentials in code, prompts, traces or reports. No paid calls during
  review or CI.

## Commands (working directory `midterms/rajvardhan19/`)

```sh
python -m unittest discover -s tests -v          # deterministic checks, no network
python -m cws.evaluate --players original-ai random passive --quiet
python3 tools/qb64-harness/compare.py --qb64 PATH/qb64pe --bas PATH/CWSTRAT.BAS --seeds 1 2 3
```

## Hand-off

Finish every rule change with the skill's summary and hand it to the
independent reviewer (`.claude/agents/rules-reviewer.md`) in a fresh
session. Never review or approve your own change.
