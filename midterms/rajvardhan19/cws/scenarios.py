"""Starting situations for the declared suite (SUITE.md).

Each is a setup the original ships or exposes in its Utility menu; none
changes a rule.
"""

from dataclasses import dataclass

from .data import ALTERNATE, STANDARD, MapFiles
from .engine import Settings


@dataclass(frozen=True)
class Scenario:
    name: str
    summary: str
    map_files: MapFiles
    settings: Settings


SCENARIOS = {
    s.name: s for s in (
        Scenario("standard", "CWS.INI: March 1861, original map and leaders, opponent aggression NORMAL (3)",
                 STANDARD, Settings(bold=3)),
        Scenario("alternate", "ALTMAP.INI: April 1861, the alternate map and leaders ALTMAP.BAT installs, aggression NORMAL (3)",
                 ALTERNATE, Settings(bold=3)),
        Scenario("reckless", "CWS.INI with the Utility menu's opponent aggression at RECKLESS (5); held out from tuning",
                 STANDARD, Settings(bold=5)),
    )
}
