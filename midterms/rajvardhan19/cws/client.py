"""The runner's handle on the engine process, and the narrower port a player gets."""

import json
import os
import queue
import subprocess
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


PLAYER_OPERATIONS = ("observe", "legal_actions", "step")


class EngineError(RuntimeError):
    pass


class EngineTimeout(EngineError):
    pass


def engine_environment(environ) -> dict:
    """The engine needs no credentials; drop anything that looks like one."""
    secret = ("_KEY", "_TOKEN", "_SECRET", "CREDENTIALS", "PASSWORD")
    env = {k: v for k, v in environ.items() if not k.upper().endswith(secret)}
    env["PYTHONPATH"] = str(ROOT)
    return env


class EngineProcess:
    """Held by the runner only: reset and outcome live here, not on the port."""

    def __init__(self, timeout: float = 30.0) -> None:
        self.timeout = timeout
        env = engine_environment(os.environ)
        self._proc = subprocess.Popen(
            [sys.executable, "-m", "cws.server"], cwd=ROOT, env=env, text=True,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=1,
        )
        self._lines: queue.Queue = queue.Queue()
        threading.Thread(target=self._read, daemon=True).start()

    def _read(self) -> None:
        for line in self._proc.stdout:
            self._lines.put(line)
        self._lines.put(None)

    def call(self, op: str, **args):
        if self._proc.poll() is not None:
            raise EngineError("engine process has exited")
        self._proc.stdin.write(json.dumps({"op": op, **args}) + "\n")
        self._proc.stdin.flush()
        try:
            line = self._lines.get(timeout=self.timeout)
        except queue.Empty:
            raise EngineTimeout(f"engine did not answer {op!r} within {self.timeout}s") from None
        if line is None:
            raise EngineError("engine process has exited")
        reply = json.loads(line)
        if not reply["ok"]:
            raise EngineError(reply["error"])
        return reply["result"]

    def reset(self, scenario: str, seed: float, max_steps: int) -> dict:
        return self.call("reset", scenario=scenario, seed=seed, max_steps=max_steps)

    def outcome(self) -> dict:
        return self.call("outcome")

    def trace(self) -> list:
        return self.call("trace")

    def port(self, player_id: str = "union") -> "PlayerPort":
        def player_call(op: str, **args):
            if op not in PLAYER_OPERATIONS:
                raise PermissionError(f"a player may not call {op!r}")
            return self.call(op, **args)
        return PlayerPort(player_call, player_id)

    def close(self) -> None:
        if self._proc.poll() is None:
            self._proc.stdin.close()
            try:
                self._proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self._proc.kill()
                self._proc.wait()
        self._proc.stdout.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()


class PlayerPort:
    """The three operations a player may call; its channel refuses reset, outcome and trace."""

    __slots__ = ("_call", "player_id")

    def __init__(self, call, player_id: str) -> None:
        self._call = call
        self.player_id = player_id

    def observe(self) -> dict:
        return self._call("observe", player_id=self.player_id)

    def legal_actions(self) -> list[str]:
        return self._call("legal_actions", player_id=self.player_id)

    def step(self, action) -> dict:
        return self._call("step", player_id=self.player_id, action=action)
