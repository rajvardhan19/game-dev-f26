"""The engine process: one episode, JSON lines on stdin and stdout.

Started by cws/client.py. The runner's process never holds the Game, so no
player code in that process can reach it, whatever Python allows.

Requests: {"op": "reset" | "observe" | "legal_actions" | "step" | "outcome", ...}
"""

import json
import sys

from .interface import CivilWarEpisode, PLAYER_ID


def main() -> None:
    episode = None
    for line in sys.stdin:
        try:
            req = json.loads(line)
            op = req["op"]
            if op == "reset":
                episode = CivilWarEpisode(req.get("scenario", "standard"), req.get("max_steps", 600))
                result = episode.reset(req.get("seed"))
            elif episode is None:
                raise RuntimeError("reset first")
            elif op == "observe":
                result = episode.observe(req.get("player_id", PLAYER_ID))
            elif op == "legal_actions":
                result = episode.legal_actions(req.get("player_id", PLAYER_ID))
            elif op == "step":
                result = episode.step(req.get("player_id", PLAYER_ID), req.get("action"))
            elif op == "outcome":
                result = episode.outcome()
            elif op == "trace":
                result = episode.trace
            else:
                raise ValueError(f"unknown op {op!r}")
            reply = {"ok": True, "result": result}
        except Exception as error:                       # report, keep serving
            reply = {"ok": False, "error": f"{type(error).__name__}: {error}"}
        sys.stdout.write(json.dumps(reply) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
