"""The Python engine against states recorded from the original SUBs under QB64.

tools/qb64-harness/compare.py compiled CWSTRAT.BAS's own SUBs with QB64-PE,
replayed 36 games, and saved a hash of the full game state after every
command. This test replays the same commands in Python and requires every
hash to match, so CI re-checks fidelity without QB64.
"""

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORDED = ROOT / "tools" / "qb64-harness" / "recorded"
sys.path.insert(0, str(ROOT / "tools" / "qb64-harness"))

import compare  # noqa: E402


class RecordedOriginal(unittest.TestCase):
    def test_recordings_exist(self):
        self.assertGreaterEqual(len(list(RECORDED.glob("*.json"))), 36)

    def test_every_state_matches_the_original(self):
        commands_checked = 0
        for path in sorted(RECORDED.glob("*.json")):
            rec = json.loads(path.read_text())
            self.assertTrue(rec["match"], path.name)
            states = compare.python_dumps(rec["scenario"], rec["seed"], rec["commands"])
            hashes = [compare.state_hash([" ".join(l.split()) for l in s]) for s in states]
            for k, (want, got) in enumerate(zip(rec["qb64_state_sha256_16"], hashes)):
                if want != got:
                    where = "start" if k == 0 else f"command {k} ({rec['commands'][k - 1]})"
                    self.fail(f"{path.name}: state differs from QB64 after {where}")
            self.assertEqual(len(hashes), len(rec["qb64_state_sha256_16"]), path.name)
            commands_checked += len(rec["commands"])
        self.assertGreater(commands_checked, 3300)


if __name__ == "__main__":
    unittest.main()
