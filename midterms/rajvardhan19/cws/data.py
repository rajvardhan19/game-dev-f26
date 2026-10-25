"""Read the original game's data files with QBasic INPUT # rules.

The files in data/original/ are byte-for-byte copies from the MIT-licensed
QB64 port (see data/original/LICENSE). INPUT # splits on commas and line
breaks, strips surrounding spaces and takes a quoted field verbatim.
"""

from dataclasses import dataclass
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "original"


def tokens(path: Path) -> list[str]:
    out: list[str] = []
    for line in path.read_text(encoding="latin-1").splitlines():
        field, quoted, in_quotes = "", False, False
        for ch in line:
            if ch == '"':
                if not in_quotes and not quoted:
                    field = ""                             # INPUT # skips blanks before a quote
                in_quotes = not in_quotes
                quoted = True
            elif ch == "," and not in_quotes:
                out.append(field if quoted else field.strip())
                field, quoted = "", False
            else:
                field += ch
        if field.strip() or quoted:
            out.append(field if quoted else field.strip())
    return out


class Reader:
    def __init__(self, path: Path) -> None:
        self.items = tokens(path)
        self.pos = 0

    def take(self) -> str:
        item = self.items[self.pos]
        self.pos += 1
        return item

    def num(self) -> float:
        return float(self.take())

    def int(self) -> int:
        return int(float(self.take()))


@dataclass(frozen=True)
class MapFiles:
    """One playable setup: the files ALTMAP.BAT swaps as a set."""

    name: str
    cities: str
    ini: str
    leaders: str


STANDARD = MapFiles("standard", "CITIES.GRD", "CWS.INI", "CWSLEAD.DAT")
ALTERNATE = MapFiles("alternate", "ALTMAP.GRD", "ALTMAP.INI", "ALTLEAD.DAT")
MAPS = {m.name: m for m in (STANDARD, ALTERNATE)}
