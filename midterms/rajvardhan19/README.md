# VGA Civil War Strategy v2.11: a reconstruction and an agent that plays it

**rajvardhan19**: COMS E6998 section 014, midterm, Fall 2026.

A rules-exact reconstruction of W. R. Hutsell's *VGA Civil War Strategy*
(1998; QB64 port and v2.11 by Dave Mackey, MIT licence). You command the
Union against the game's own computer player. A Gemini model plays the same
side through a five-operation interface, and is compared with the original
game's own AI playing the Union.

- **Recording:** TODO: link (3-5 minutes; an agent playing with no manual move selection)
- **Evaluation:** [EVALUATION.md](EVALUATION.md) · **Suite:** [SUITE.md](SUITE.md)
- **Agent team log:** [AGENT-TEAM.md](AGENT-TEAM.md) · **Peer notes:** [PEER-NOTES.md](PEER-NOTES.md)
- **Rules and evidence:** [docs/rule-source-map.md](docs/rule-source-map.md) · **Open questions:** [QUESTIONS.md](QUESTIONS.md)

## Scope statement

The Week 3 commitment (scope record of origin, posted 2026-09-27):
reconstruct the rules of VGA Civil War Strategy v2.11 so a separate agent can
play against the original computer opponent. A rule is correct only if it
matches what CWSTRAT.BAS computes from the same state and dice rolls.

**Included.** Everything below plays as in v2.11:

- the full 40-city map and the shipped setups (standard and alternate);
- the leaders, the treasury and the shipped options;
- Union recruiting, movement, fortification, supply, joining, drilling and cancelling;
- the whole monthly resolution: the original computer opponent (`smarts`), initiative, battles, retreats, surrender, capture, supply, attrition and victory points;
- all six victory conditions.

An episode is one war, from the start date to a victory condition. The
original's own deadline (March 1865) is one of them, so every game ends.

**Excluded.** Navies, railroads, random events (an option the original
lets you turn off), relieving commanders, moving the capital, two-player
mode, saving and graphics. The [rule map](docs/rule-source-map.md#scope)
says what each exclusion changes.

**Evidence.** The original game code was compiled with QB64-PE and run
against this engine on the same seeds and commands. That covers every SUB,
including the computer opponent and SUB victor, plus the main-module rule
paths copied by line number.

- **Result:** 36 games and 3,392 commands produced identical game states
  after every command.
- **Coverage:** every command type and eight of the game's end conditions.
- **Where:** `tools/qb64-harness/`, re-checked in CI from recorded hashes.
  The rule map says exactly what the harness changes.

## Run it

Requirements: Python 3.11 or later. The game, the baselines and every test
use only the standard library. The live model needs `uv` (or pip) for one
package.

Every command below runs from the project folder:

```sh
cd midterms/rajvardhan19
```

Use `python3` wherever this page says `python` if that is the name your
installation provides.

**Play** (you are the Union; type an action's number or its text, or
`map`, `cities`, `armies`, `report`, `help`, `quit`):

```sh
python -m cws.play                          # standard 1861 campaign, seed 1
python -m cws.play --scenario alternate --seed 7
```

The quickest way to see an ending is to type `end turn` repeatedly: the
Confederacy wins in about 8 turns.

**Watch an agent play** (no input from you):

```sh
python -m cws.play --watch original-ai --scenario alternate --seed 9   # baseline, about 10 s
python -m cws.play --watch random --seed 3
```

**Test** (the same checks as CI):

```sh
python -m unittest discover -s tests -v
```

**Evaluate the baselines** (free, about 15 s):

```sh
python -m cws.evaluate --players original-ai random passive --extra-baseline-seeds --run my-baselines
```

Results go to `results/<run>/` and traces to `traces/<run>/`.

### Live model (Gemini on Vertex AI)

Use your own course Google Cloud project and an approved location:

```sh
gcloud auth application-default login          # once, with your course account
export GOOGLE_CLOUD_PROJECT='your-course-project'
export GOOGLE_CLOUD_LOCATION='your-approved-location'
export COURSE_MODEL='gemini-3.5-flash-lite'
uv sync --extra live                            # or: pip install "google-genai>=1.0,<3"
uv run --extra live python -m cws.play --watch model-history --live            # one game on dev seed 101
uv run --extra live python -m cws.evaluate --players model-history --split dev --live --run dev-1   # prompt work
uv run --extra live python -m cws.evaluate --players model-history model-obs-only --split eval --live --run <date>-live
```

`--live` is required for anything that makes paid calls. Model runs also
need an explicit `--split`. `dev` (seeds 101-102) is for prompt work;
`eval` is the declared comparison, whose seeds are held out from tuning.

Each call has a 30-second timeout, one attempt and a 2,048-token output
cap, and an episode allows at most 150 calls. A full evaluation is 12
episodes, of up to 24 turns (standard, reckless) or 27 (alternate).

## How it fits together

```
 runner (cws/runner.py) ── holds ──> EngineProcess ══ JSON lines ══> engine process (cws/server.py)
   │  limits, fallbacks, trace                                          CivilWarEpisode (cws/interface.py)
   │                                                                     Game (cws/engine.py) + smarts.py
   └─ gives the player only a PlayerPort: observe() · legal_actions() · step()
        player = ModelPlayer (Gemini, no tools) | OriginalAI | RandomPlayer | PassivePlayer
```

| Operation | Who calls it | What it does |
|---|---|---|
| `reset(seed)` | runner | New game; `RANDOMIZE seed` replaces the original's `RANDOMIZE TIMER` |
| `observe("union")` | player | What the original shows a human Union player: cities, both treasuries and VP, own armies in full, enemy armies' name, size, city and an out-of-supply flag, last turn's messages |
| `legal_actions("union")` | player | Menu choices that would change the game now; rolls no dice |
| `step("union", action)` | player | Validates and applies one action; a refused action changes nothing and is counted |
| `outcome()` | runner | Ongoing or terminal, with the victory condition, date, VP and counts |

## Rule and source map (summary)

The full map labels every rule `code` (with a CWSTRAT.BAS line), `observed`
(a QB64 run), `assumed` or `design` (with its reason):
[docs/rule-source-map.md](docs/rule-source-map.md). The `design` choices are:

- the action vocabulary, and listing only actions that change state;
- `troops` as the action that rolls recruits;
- ESC for the human retreat menu, No for "Raze?", Yes for "End Game";
- the episode seed in place of `TIMER`;
- the separate engine process;
- batched model replies;
- the runner's limits.

Quirks of the original are kept as written and listed in
[QUESTIONS.md](QUESTIONS.md).

## Sources and reuse terms

| Source | Use | Terms |
|---|---|---|
| *VGA Civil War Strategy* by W. R. Hutsell (1998); QB64 port v2.11 by Dave Mackey, via [historicalsource/Civil-War-Strategy-Game](https://github.com/historicalsource/Civil-War-Strategy-Game) and the fork [rajvardhan19/Mod-Civil-War-Strategy-Game](https://github.com/rajvardhan19/Mod-Civil-War-Strategy-Game) | Rules ported to Python; `source/CWSTRAT.BAS`, `source/VariablesGuide.md` and `data/original/*` included unmodified | MIT licence, (c) 2018 Dave Mackey: [source/LICENSE](source/LICENSE). The repository's third-party components (QB64 runtime libraries in `vendor-licenses/`) are not included here. |
| [QB64-PE](https://github.com/QB64-Phoenix-Edition/QB64pe) 4.7.0 | Compiled the original SUBs for the differential check; `libqb.cpp` and `rounding.h` cited for RND and rounding | MIT licence (QB64-PE); not redistributed here, only cited |
| Hutsell Games, [hutsellgames.com](https://hutsellgames.com/) | The original publisher; the free release and documentation | Credited; not used as a rules source (see the rule map's labels) |
| Course starter `game-dev-f26` | The five-operation pattern, the provider adapter's request controls, the skill and reviewer formats | Course materials |

No game art, music or prose from the original is included. The terminal map
is drawn from the city coordinates in `CITIES.GRD`.

## Files

| Path | What it is |
|---|---|
| `cws/engine.py`, `cws/smarts.py`, `cws/qb.py` | The rules, the original computer opponent, and QBasic numeric semantics |
| `cws/interface.py`, `cws/server.py`, `cws/client.py` | Five operations, the engine process, the runner's handle and the player's port |
| `cws/runner.py`, `cws/evaluate.py` | Episode limits, fallbacks and traces; the declared suite |
| `cws/players/` | `model_player.py` (Gemini), `baselines.py` (original AI, random, passive), `view.py` (masked board for the baseline) |
| `cws/play.py` | Terminal play and watch |
| `tests/` | Deterministic checks (see [EVALUATION.md](EVALUATION.md#ci)) |
| `tools/qb64-harness/` | The differential harness, its debugging aid and 36 recorded games |
| `source/`, `data/original/` | The original source and data, unmodified, with the MIT licence |
| `AGENTS.md`, `CLAUDE.md`, `.claude/`, `agent-config.json` | The building agent team's configuration |
| `ci/midterm-rajvardhan19.yml` | Copy of `.github/workflows/midterm-rajvardhan19.yml` |
