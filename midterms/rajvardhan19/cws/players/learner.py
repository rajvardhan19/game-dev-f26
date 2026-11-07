"""A Union player that learns across games: a lessons notebook it rewrites after each one.

During a game it is the model player with memory of its last 3 turns, plus its
notebook at the top of every prompt. After a training game, one more model
call reviews the game and rewrites the notebook: at most 12 lessons, with what
changed and why, and the strategy it means to follow next.

What the review sees is what the player saw: its own orders, refusals and
notes, each turn's visible report, the opening numbers of each turn as shown
on screen, and the end-of-game result. Never the seed, the dice, the engine,
hidden enemy fields or the opponent's code.

The notebook learns only on training seeds (SUITE.md). It is frozen before any
validation or evaluation game, and a frozen notebook refuses every update.
"""

import hashlib
import json
import os
import tempfile
from pathlib import Path

from .model_player import SYSTEM, ModelPlayer

MAX_LESSONS, MAX_CHARS = 12, 200

RULES = SYSTEM.split("Reply with JSON only")[0].strip()

REVIEW_SYSTEM = f"""You are the Union commander in VGA Civil War Strategy. You have just finished a \
training game against the game's computer, and you will play more games after this one. Before each \
game, your lessons notebook is placed at the top of every prompt you see.

Rewrite the notebook from what this game showed you:
- at most {MAX_LESSONS} lessons, each one concrete instruction under {MAX_CHARS} characters;
- keep lessons this game supported, revise those it contradicted, drop those that did not help, \
and add what you learned;
- lessons must hold for any game on these maps: no dice, no one-off luck;
- judge by results across your games (the scoreboard), not by one turn.

Also give a short diagnosis of why this game went as it did, list what you changed and why, \
and state the overall strategy you will follow next game.

The rules you play under:
{RULES}

Reply with JSON only."""

# Optional changes to how the review learns (never what): gemini-c, declared 2026-10-26.
METHOD_NOTES = {
    "mirror": "WHAT YOU ACTUALLY DID is measured from your own orders in this game. Compare it with what your "
              "notebook told you to do. Where they differ, decide whether the lesson was wrong or you did not "
              "follow it, and write the lesson so that you will.",
    "track_record": "Each lesson shows its track record: the games it was in your notebook for, and how many turns "
                    "longer (+) or shorter (-) you lasted than a player who gives no orders at all, in the very same "
                    "games. Keep lessons with a good record unless this game clearly contradicts them; rewrite or "
                    "drop lessons with a poor one. A reworded lesson starts a new record.",
    "priority": "Order your lessons by priority, most important first: when two lessons conflict during play you "
                "will follow the earlier one, so put the rule that must never be broken first.",
    "openings": "Also write your opening plan for each map: the orders you will give on turn 1, from how your "
                "openings went so far. Keep the plan for a map you did not play this time unless you have reason "
                "to change it.",
    "select": "Your notebook is tested in rounds of games. A new version replaces your current one only if it does "
              "at least about as well; otherwise you go back to your current one. Improve your current notebook "
              "from what these games showed.",
    "teacher": "TEACHER'S GAME shows how the game's own computer played the Union on this same game, from the same "
               "start (its dice differ once its play differs from yours). Compare it with your game: what did it do "
               "that you did not, and how did that turn out? Draw your own lessons in your own words, using only "
               "commands you have.",
    "contrast": "CONTRAST measures your play against the game's own computer playing the Union on this same game, "
                "rate by rate, and shows which of your own rates went with lasting longer across all your games so far. "
                "Decide from these measurements which few behaviours make the difference, and write your lessons about "
                "those.",
    "actionable": "Write every lesson as a rule you can act on: \"When <something you can see on screen>, "
                  "<the orders to give, using the command names>.\"",
}


def review_system(method: dict | None = None) -> str:
    """The review prompt; each switched-on method adds one instruction. With none it is unchanged."""
    extra = [METHOD_NOTES[k] for k in METHOD_NOTES if (method or {}).get(k)]
    if not extra:
        return REVIEW_SYSTEM
    return REVIEW_SYSTEM.replace("\n\nThe rules you play under:",
                                 "\n" + "".join(f"\n- {x}" for x in extra) + "\n\nThe rules you play under:")


REVIEW_SCHEMA = {
    "type": "object",
    "properties": {
        "diagnosis": {"type": "string"},
        "lessons": {"type": "array", "items": {"type": "string"}, "maxItems": MAX_LESSONS},
        "changes": {"type": "array", "items": {
            "type": "object",
            "properties": {"kind": {"type": "string", "enum": ["added", "revised", "dropped"]},
                           "lesson": {"type": "string"}, "why": {"type": "string"}},
            "required": ["kind", "lesson", "why"]}},
        "strategy": {"type": "string"},
    },
    "required": ["diagnosis", "lessons", "changes", "strategy"],
}


def review_schema(method: dict | None = None) -> dict:
    """With openings switched on, the review also returns an opening plan per map."""
    if not (method or {}).get("openings"):
        return REVIEW_SCHEMA
    schema = json.loads(json.dumps(REVIEW_SCHEMA))
    schema["properties"]["openings"] = {"type": "object", "properties": {
        "standard": {"type": "string"}, "alternate": {"type": "string"}}}
    schema["required"].append("openings")
    return schema


def _clip(text, n: int) -> str:
    return " ".join(str(text).split())[:n]


def clean_review(data) -> dict:
    """Validate a review reply; raises ValueError if it cannot be used."""
    if not isinstance(data, dict):
        raise ValueError("review is not an object")
    lessons = data.get("lessons")
    if not isinstance(lessons, list) or not all(isinstance(x, str) for x in lessons):
        raise ValueError("lessons must be a list of strings")
    kept: list[str] = []
    for lesson in lessons:
        lesson = _clip(lesson, MAX_CHARS)
        if lesson and lesson.lower() not in (k.lower() for k in kept):
            kept.append(lesson)
    if not kept:
        raise ValueError("the review left the notebook empty")
    changes = []
    for c in data.get("changes", []) if isinstance(data.get("changes"), list) else []:
        if isinstance(c, dict) and c.get("kind") in ("added", "revised", "dropped"):
            changes.append({"kind": c["kind"], "lesson": _clip(c.get("lesson", ""), MAX_CHARS),
                            "why": _clip(c.get("why", ""), 300)})
    out = {"diagnosis": _clip(data.get("diagnosis", ""), 600), "lessons": kept[:MAX_LESSONS],
           "changes": changes, "strategy": _clip(data.get("strategy", ""), 500)}
    if isinstance(data.get("openings"), dict):
        out["openings"] = {m: _clip(data["openings"].get(m, ""), 400) for m in ("standard", "alternate")
                           if isinstance(data["openings"].get(m), str) and data["openings"][m].strip()}
    return out


class LessonBook:
    """The notebook on disk, with every version kept."""

    def __init__(self, path: Path, model: str = "") -> None:
        self.path = Path(path)
        if self.path.exists():
            self.data = json.loads(self.path.read_text())
        else:
            self.data = {"format": 1, "name": self.path.stem, "model": model, "frozen": False, "version": 0,
                         "lessons": [], "strategy": "",
                         "versions": [{"version": 0, "lessons": [], "strategy": "", "note": "empty notebook"}]}

    @property
    def lessons(self) -> list[str]:
        return list(self.data["lessons"])

    @property
    def version(self) -> int:
        return self.data["version"]

    @property
    def frozen(self) -> bool:
        return self.data["frozen"]

    def sha(self) -> str:
        return hashlib.sha256(json.dumps(self.data["lessons"]).encode()).hexdigest()[:16]

    def update(self, review: dict, game: dict) -> None:
        if self.frozen:
            raise PermissionError(f"{self.path} is frozen; it can no longer learn")
        self.data["version"] += 1
        self.data["lessons"], self.data["strategy"] = review["lessons"], review["strategy"]
        if review.get("openings"):                       # a map left out keeps its plan
            self.data["openings"] = {**self.data.get("openings", {}), **review["openings"]}
        self.data["versions"].append({"version": self.version, "after_game": game, **review})
        self.save()

    def freeze(self) -> None:
        self.data["frozen"], self.data["frozen_sha"] = True, self.sha()
        self.save()

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=self.path.parent, suffix=".tmp")
        with os.fdopen(fd, "w") as f:
            json.dump(self.data, f, indent=1)
        os.replace(tmp, self.path)


class LearningPlayer(ModelPlayer):
    """The model player with memory and a notebook; it also keeps what it saw for the review."""

    def __init__(self, client, lessons: list[str], name: str = "model-lessons", history_turns: int = 3,
                 priority: bool = False, opening: str | None = None, fronts: bool = False, plan: bool = False) -> None:
        super().__init__(client, "history", history_turns, lessons=lessons, name=name, priority=priority,
                         opening=opening, fronts=fronts, plan=plan)
        self.seen: dict[int, dict] = {}                  # turn -> the opening numbers on screen
        self.conditions: list[str] = []
        self.memory_turns: list[dict] = []
        self.final: dict | None = None

    def decide(self, obs, legal, memory):
        if obs["turn"] not in self.seen:
            self.seen[obs["turn"]] = _screen_numbers(obs)
            self.conditions = obs["victory_conditions"]
        return super().decide(obs, legal, memory)

    def end(self, memory: dict, final_obs: dict) -> None:
        """run_episode's on_end hook: the turns as the player lived them, and the final screen."""
        self.memory_turns = [dict(t, note=self._notes.get(t["turn"], "")) for t in memory["turns"]]
        self.final = _screen_numbers(final_obs)


def _screen_numbers(obs: dict) -> dict:
    t = obs["treasury"]
    return {"date": obs["date"], "cash": t["Union"]["cash"], "income": t["Union"]["income"],
            "cities": t["Union"]["cities"], "rebel_cities": t["Rebel"]["cities"],
            "men": sum(a["men"] for a in obs["your_armies"]), "armies": len(obs["your_armies"]),
            "enemy_men": sum(a["men"] for a in obs["enemy_armies"])}


def review_text(game_no: int, scenario: str, reason: str, turns: int, player: LearningPlayer,
                book_version: int, scoreboard: list[str], records: dict | None = None,
                mirror: str | None = None, passive_turns: int | None = None, teacher: str | None = None,
                contrast: str | None = None) -> str:
    """`records`, `mirror` and `passive_turns` are only given when those methods are switched on."""
    result = f"RESULT: {reason}, after {turns} turns."
    if passive_turns is not None:
        result += f" A player giving no orders at all lasted {passive_turns} turns in this same game."
    lines = [f"TRAINING GAME {game_no}, map: {scenario}.",
             "VICTORY CONDITIONS: " + "; ".join(player.conditions), result, ""]
    if player.lessons:
        lines += [f"YOUR NOTEBOOK DURING THIS GAME (version {book_version}):"]
        for i, x in enumerate(player.lessons, 1):
            if records is None:
                lines.append(f"{i}. {x}")
            else:
                n, mean = records.get(x, (0, None))
                lines.append(f"{i}. {x} [record: {n} games, {mean:+.1f} turns against no orders]" if n
                             else f"{i}. {x} [record: no games yet]")
    else:
        lines += ["YOUR NOTEBOOK DURING THIS GAME: empty (this was your first game)."]
    if mirror:
        lines += ["", "WHAT YOU ACTUALLY DID (measured from your own orders):", mirror]
    if teacher:
        lines += ["", "TEACHER'S GAME (the game's own computer as the Union, on this same game):", teacher]
    if contrast:
        lines += ["", "CONTRAST (measured):", contrast]
    if scoreboard:
        lines += ["", "SCOREBOARD OF YOUR EARLIER TRAINING GAMES (most recent last):"] + scoreboard
    lines += ["", "THIS GAME, TURN BY TURN (as you saw it):"] + turn_lines(player)
    if player.final:
        f = player.final
        lines += ["", f"FINAL POSITION ({f['date']}): {f['cities']} cities, {f['armies']} armies, {f['men']:,} men, "
                      f"${f['cash']}; the Rebels held {f['rebel_cities']} cities and showed {f['enemy_men']:,} men."]
    return "\n".join(lines)


def turn_lines(player: LearningPlayer, max_events: int = 30) -> list[str]:
    """One game as the player lived it: numbers on screen, plan, orders, refusals, the visible report."""
    lines = []
    for t in player.memory_turns:
        s = player.seen.get(t["turn"], {})
        if s:
            lines.append(f"{s['date']}: you had ${s['cash']} (income {s['income']}), {s['cities']} cities, "
                         f"{s['armies']} armies, {s['men']:,} men; the Rebels held {s['rebel_cities']} cities "
                         f"and showed {s['enemy_men']:,} men.")
        if t.get("note"):
            lines.append(f"  Your plan: {t['note']}")
        done = [a["action"] for a in t["actions"] if a["accepted"] and a["action"] != "end turn"]
        lines.append(f"  You ordered: {', '.join(done) or 'nothing'}")
        bad = [a["action"] for a in t["actions"] if not a["accepted"]]
        if bad:
            lines.append(f"  Refused (not legal at that moment): {', '.join(bad)}")
        events = [e["text"] for e in t["report"] if e.get("kind") not in ("plan", "turn")]
        lines += [f"    - {e}" for e in events[:max_events]]
        if len(events) > max_events:
            lines.append(f"    - ... and {len(events) - max_events} more")
    return lines


def review(client, text: str, system: str = REVIEW_SYSTEM, schema: dict = REVIEW_SCHEMA) -> tuple[dict | None, str, int, int]:
    """One review call. Returns (clean review or None, error, input tokens, output tokens)."""
    try:
        reply = client.generate(system, text, schema)
    except Exception as error:
        return None, f"{type(error).__name__}: {str(error)[:200]}", 0, 0
    if not reply["complete"]:
        return None, f"incomplete response ({reply['finish']})", reply["input_tokens"], reply["output_tokens"]
    try:
        return clean_review(json.loads(reply["text"])), "", reply["input_tokens"], reply["output_tokens"]
    except ValueError as error:                          # json.JSONDecodeError is a ValueError
        return None, f"unusable review: {error}", reply["input_tokens"], reply["output_tokens"]
