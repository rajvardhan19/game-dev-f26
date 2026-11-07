"""Local UI adapter. Run: python3 play-ui/server.py (standard library only; --live for model players)."""
import argparse
import hashlib
import json
import os
import random
import signal
import sys
import tempfile
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from types import SimpleNamespace
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
STATIC = Path(__file__).resolve().parent / "static"
PRACTICE = (101, 102, 103, 104)      # the development seeds; evaluation and training seeds are never offered
RANDOM_SEEDS = (1000, 999_999)       # no declared split uses these (SUITE.md)
# Agents the browser can watch. Model players use the evaluation's own settings (SUITE.md, EVALUATION.md).
WATCHABLE = {
    "original-ai": dict(label="The 1998 AI, commanding the Union", live=False),
    "gemini-h": dict(label="gemini-h: Gemini 3.7 Flash with the notebook it wrote in training", live=True,
                     player="model-lessons", model="gemini-3.7-flash", timeout=90.0, tokens=8192,
                     lessons="lessons/gemini-h.json"),
    "flash-lite": dict(label="Gemini 3.5 Flash-Lite with memory of its last 3 turns", live=True,
                       player="model-history", model="gemini-3.5-flash-lite", timeout=30.0, tokens=2048),
}


def snapshot(destination):
    """Read a consistent source snapshot without writing to the working engine."""
    paths = sorted((ROOT / "cws").rglob("*.py")) + sorted(p for p in (ROOT / "data").rglob("*") if p.is_file())
    contents = {p: p.read_bytes() for p in paths}
    if any(p.read_bytes() != content for p, content in contents.items()):
        raise RuntimeError("Engine changed during snapshot; restart the UI server.")
    digest = hashlib.sha256()
    for path, content in contents.items():
        relative = path.relative_to(ROOT)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        digest.update(str(relative).encode() + content)
    return digest.hexdigest()[:12]


FIXED_COSTS = {"recruit": 100, "fortify": 200}       # engine lines 421 and 442 (recruit), 474 (fortify)
SHIP_COSTS = {"wooden": 100, "ironclad": 200}        # SUB navy lines 1514-1578; the human pays double for an ironclad


def own_neighbours(obs, city_id):
    """SUB cutoff, line 1121: how many of the city's neighbours the Union holds."""
    by = {c["id"]: c for c in obs["cities"]}
    return sum(1 for n in by[city_id]["neighbors"] if by.get(n, {}).get("owner") == "Union")


def spend_preview(obs, legal, spent):
    """What each legal order costs now, and the supply upkeep due at turn end, from the player's own screen.

    Uses the engine's QBasic arithmetic (cws.qb). Upkeep is SUB iterate, lines 1413-1435, for the armies where they
    stand now; marches, battles and captures resolve first, so it is an estimate. Nothing here rolls dice.
    """
    from cws.qb import cint, f32
    cash, realism = obs["treasury"]["Union"]["cash"], obs["settings"]["realism"]
    armies = {a["id"]: a for a in obs["your_armies"]}
    costs = {}
    for action in legal:
        verb, *rest = action.split()
        cost = 0
        if verb in FIXED_COSTS:
            cost = FIXED_COSTS[verb]
        elif verb == "build" and rest and rest[0] in SHIP_COSTS:
            cost = SHIP_COSTS[rest[0]]
        elif verb == "supply" and rest and rest[0].isdigit() and int(rest[0]) in armies:
            army = armies[int(rest[0])]                   # SUB resupply, lines 3602-3615
            size = army["men"] // 100
            x = 0
            if size > 0 and not (realism and own_neighbours(obs, army["city"]) < 1):
                x = cint(f32(cash / size * 10))
                if x + army["supply"] > 5:
                    x = 5 - army["supply"]
            if x >= 1:
                cost = cash - max(cint(f32(cash - .1 * x * size)), 0)
        costs[action] = cost
    left = cash
    for i in sorted(armies):
        size = armies[i]["men"] // 100
        if left >= f32(.2 * size) and (not realism or own_neighbours(obs, armies[i]["city"]) > 0):
            left = cint(f32(left - .2 * size))
    return {"costs": costs, "cash": cash, "spent": spent, "upkeep": cash - left,
            "income": obs["treasury"]["Union"]["income"]}


def war_seed(war):
    """'random' -> a fresh seed outside every declared split; a practice seed -> itself; anything else refused."""
    if war == "random":
        return random.SystemRandom().randint(*RANDOM_SEEDS), "a new random war"
    if isinstance(war, int) and not isinstance(war, bool) and war in PRACTICE:
        return war, f"practice war {war}"
    raise ValueError("Choose a random war or practice war 101-104.")


class Session:
    def __init__(self, engine):
        self.engine = engine
        self.lock = threading.Lock()
        self.revision = 0
        self.scenario, self.war = "standard", "practice war 101"
        self.turn_seen, self.turn_cash = None, 0
        engine.reset(self.scenario, 101, 600)

    def state(self, message="", accepted=None):
        obs, legal = self.engine.port().observe(), self.engine.port().legal_actions()
        cash = obs["treasury"]["Union"]["cash"]
        if obs["turn"] != self.turn_seen:
            self.turn_seen, self.turn_cash = obs["turn"], cash
        return dict(observation=obs, legal=legal, outcome=self.engine.outcome(), revision=self.revision,
                    scenario=self.scenario, war=self.war, message=message, accepted=accepted,
                    preview=spend_preview(obs, legal, max(self.turn_cash - cash, 0)))

    def mutate(self, request, body):
        if body.get("revision") != self.revision:
            return 409, self.state("The board changed in another tab. Review the updated orders.")
        if request == "/api/new":
            scenario = body.get("scenario")
            if scenario not in ("standard", "alternate"):
                raise ValueError("Choose standard or alternate.")
            seed, war = war_seed(body.get("war", 101))
            self.engine.reset(scenario, seed, 600)
            self.scenario, self.war, self.turn_seen = scenario, war, None
            self.revision += 1
            return 200, self.state("A new campaign is ready.")
        action = body.get("action")
        if not isinstance(action, str) or len(action) > 150:
            raise ValueError("Choose an order from the board.")
        result = self.engine.port().step(action)
        self.revision += 1
        return 200, self.state(result["text"], result["accepted"])


class Stopped(Exception):
    pass


def feed_entry(entry):
    """A runner trace entry as the browser shows it: only what the trace itself records."""
    if "turn_start" in entry:
        return {"kind": "turn", "turn": entry["turn_start"]}
    if "game_end" in entry:
        return {"kind": "end"}
    if "call" in entry:
        return {"kind": "call", "call": entry["call"], "ok": entry["ok"], "error": entry["error"],
                "latency": entry["latency"], "tokens": entry["input_tokens"] + entry["output_tokens"],
                "note": entry.get("note") or ""}
    return {"kind": "action", "action": entry["action"], "source": entry["source"], "why": entry.get("why", ""),
            "accepted": entry["accepted"], "text": entry["text"]}


class Watch:
    """One agent game at a time, played by the project's runner (its limits, fallbacks and labels)."""

    def __init__(self, live=False):
        self.live = live
        self.lock = threading.Lock()
        self.events, self.observation, self.summary = [], None, None
        self.status, self.label, self.scenario, self.stop = "idle", "", "standard", False

    def options(self):
        return [{"id": k, "label": v["label"], "available": self.live or not v["live"]} for k, v in WATCHABLE.items()]

    def start(self, body):
        spec = WATCHABLE.get(body.get("who"))
        if spec is None:
            raise ValueError("Choose an agent to watch.")
        if spec["live"] and not self.live:
            raise ValueError("Model players make paid calls: start the server with --live.")
        scenario = body.get("scenario")
        if scenario not in ("standard", "alternate"):
            raise ValueError("Choose standard or alternate.")
        seed, war = war_seed(body.get("war", 101))
        pace = body.get("pace", 0.4)
        if not isinstance(pace, (int, float)) or isinstance(pace, bool) or not 0 <= pace <= 2:
            raise ValueError("Pace is 0 to 2 seconds an order.")
        with self.lock:
            if self.status == "running":
                raise ValueError("An agent is already playing; stop it first.")
            self.events, self.observation, self.summary, self.stop = [], None, None, False
            self.status, self.label, self.scenario = "running", f"{spec['label']} · {war}", scenario
        threading.Thread(target=self._run, args=(body["who"], spec, scenario, seed, pace), daemon=True).start()

    def _player(self, who, spec, seed, scenario):
        from cws.evaluate import make_player
        if not spec["live"]:
            return make_player(who, seed, SimpleNamespace(), scenario)
        os.environ["COURSE_MODEL"] = spec["model"]
        lessons = str(ROOT / spec["lessons"]) if spec.get("lessons") else None
        args = SimpleNamespace(live=True, timeout=spec["timeout"], max_output_tokens=spec["tokens"], aids="",
                               lessons=lessons)
        return make_player(spec["player"], seed, args, scenario)

    def _run(self, who, spec, scenario, seed, pace):
        from cws.evaluate import cost, tier
        from cws.runner import Limits, run_episode

        def on_step(entry):
            if self.stop:
                raise Stopped()
            with self.lock:
                self.events.append(feed_entry(entry))
            if "action" in entry:
                time.sleep(pace)

        def on_observation(obs):
            with self.lock:
                self.observation = obs
        try:
            timeout = spec.get("timeout", 30.0)
            limits = Limits(engine_timeout=timeout + 30, decision_timeout=max(45.0, timeout + 15))
            r = run_episode(self._player(who, spec, seed, scenario), scenario, seed, limits,
                            on_step=on_step, on_observation=on_observation)
            summary = dict(reason=r.reason, tier=tier({"reason": r.reason}), turns=r.turns, date=r.date,
                           invalid_actions=r.invalid_actions, fallbacks=r.fallback_actions,
                           model_calls=r.model_calls, failed_calls=r.failed_calls,
                           tokens=r.input_tokens + r.output_tokens, cost_usd=cost(r))
            with self.lock:
                self.summary, self.status = summary, "done"
        except Stopped:
            with self.lock:
                self.status = "stopped"
        except Exception as error:          # shown to the viewer; the human game is unaffected
            with self.lock:
                self.summary, self.status = {"error": str(error)}, "error"

    def state(self, since=0):
        with self.lock:
            return dict(status=self.status, label=self.label, scenario=self.scenario,
                        events=self.events[since:], next=len(self.events),
                        observation=self.observation, summary=self.summary)


def handler(session, watch=None):
    watch = watch or Watch()

    class Handler(BaseHTTPRequestHandler):
        def reply(self, status, payload):
            data = json.dumps(payload).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def valid_host(self):
            return self.headers.get("Host") == f"127.0.0.1:{self.server.server_port}"

        def do_GET(self):
            if not self.valid_host():
                return self.reply(403, {"error": "Use the printed local URL."})
            url = urlparse(self.path)
            if url.path == "/api/state":
                try:
                    with session.lock:
                        return self.reply(200, session.state())
                except Exception as error:
                    return self.reply(503, {"error": str(error)})
            if url.path == "/favicon.ico":
                self.send_response(204)
                self.end_headers()
                return
            if url.path == "/api/watch/options":
                return self.reply(200, {"agents": watch.options(), "live": watch.live})
            if url.path == "/api/watch":
                since = parse_qs(url.query).get("since", ["0"])[0]
                return self.reply(200, watch.state(int(since) if since.isdigit() else 0))
            files = {"/": ("index.html", "text/html"), "/app.js": ("app.js", "text/javascript"),
                     "/style.css": ("style.css", "text/css")}
            if self.path not in files:
                return self.reply(404, {"error": "Not found"})
            name, mime = files[self.path]
            data = (STATIC / name).read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", mime + "; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Security-Policy", "default-src 'self'; style-src 'self'; script-src 'self'; object-src 'none'; frame-ancestors 'none'")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_POST(self):
            origin = self.headers.get("Origin")
            if not self.valid_host() or (origin and origin != f"http://127.0.0.1:{self.server.server_port}"):
                return self.reply(403, {"error": "Local same-origin requests only."})
            if self.path not in ("/api/step", "/api/new", "/api/watch/start", "/api/watch/stop"):
                return self.reply(404, {"error": "Not found"})
            try:
                length = int(self.headers.get("Content-Length", 0))
                if not 0 < length <= 2048 or self.headers.get("Content-Type") != "application/json":
                    raise ValueError("Expected a small JSON request.")
                body = json.loads(self.rfile.read(length))
                if not isinstance(body, dict):
                    raise ValueError("Expected an object.")
                if self.path == "/api/watch/start":
                    watch.start(body)
                    return self.reply(200, watch.state())
                if self.path == "/api/watch/stop":
                    watch.stop = True
                    return self.reply(200, watch.state())
                with session.lock:
                    status, payload = session.mutate(self.path, body)
                self.reply(status, payload)
            except (ValueError, TypeError) as error:
                self.reply(400, {"error": str(error)})
            except Exception as error:
                self.reply(503, {"error": str(error)})

        def log_message(self, *_):
            pass
    return Handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--live", action="store_true",
                        help="offer model players in 'Watch an AI' (paid calls; needs the Vertex settings)")
    args = parser.parse_args()

    def stop(*_):
        raise KeyboardInterrupt            # closing the terminal or a kill also removes the snapshot
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGHUP, stop)
    with tempfile.TemporaryDirectory(prefix="cws-play-ui-") as directory:
        destination = Path(directory)
        fingerprint = snapshot(destination)
        sys.path.insert(0, str(destination))
        from cws.client import EngineProcess
        with EngineProcess() as engine:
            session = Session(engine)
            with ThreadingHTTPServer(("127.0.0.1", args.port), handler(session, Watch(args.live))) as server:
                print(f"Local: http://127.0.0.1:{server.server_port}", flush=True)
                print(f"Independent game; engine snapshot {fingerprint}. Model players "
                      f"{'ON (paid calls)' if args.live else 'off (start with --live)'}. Ctrl-C to stop.", flush=True)
                try:
                    server.serve_forever()
                except KeyboardInterrupt:
                    pass


if __name__ == "__main__":
    main()
