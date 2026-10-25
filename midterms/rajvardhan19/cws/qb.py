"""QBasic/QB64 numeric semantics the original game depends on.

CWSTRAT.BAS starts with DEFINT A-Z, so every unsuffixed variable is a 16-bit
INTEGER. QB64 compiles the rest as follows (read from its generated C++;
docs/rule-source-map.md, "Numeric semantics"):

- decimal literals are C doubles, and arithmetic involving them is double;
- `!` variables and RND are floats; float with integer is float arithmetic;
- integer / integer is long double;
- an INTEGER assignment converts the result to float once, then rounds half
  to even: `cint(f32(expr))`;
- a SINGLE assignment is `f32(expr)`;
- a comparison casts both sides to float: `f32(lhs) op S(literal)`.

So write `.8 * v`, not `S(.8) * v`: rounding each product to SINGLE first is
the bug the QB64 comparison caught (697 where the original gives 696).
"""

import math
import struct

# QB64-PE internal/c/libqb.cpp: rnd_seed = 327680 and func_rnd's LCG.
DEFAULT_SEED = 327680
_MULT = 16598013
_INC = 12820163
_MASK = 0xFFFFFF


def f32(value: float) -> float:
    """Round to IEEE single precision, as a QB64 SINGLE stores it."""
    return struct.unpack("f", struct.pack("f", value))[0]


def cint(value: float) -> int:
    """Assignment to INTEGER: round half to even (QB64 qbr, FE_TONEAREST)."""
    return int(round(value))


def idiv(a: float, b: float) -> int:
    """QBasic integer division `\\`: round both operands, then truncate."""
    a, b = cint(a), cint(b)
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b >= 0) else -q


def qint(value: float) -> int:
    """QBasic INT(): the largest integer not greater than the value."""
    return math.floor(value)


def S(literal: float) -> float:
    """A literal as it is compared or stored in a SINGLE: only for comparisons and `!` assignments."""
    return f32(literal)


class QBRandom:
    """RND and RANDOMIZE exactly as QB64-PE implements them.

    Every call is counted so a trace can say how many dice a step used.
    """

    def __init__(self) -> None:
        self.state = DEFAULT_SEED
        self.calls = 0

    def rnd(self) -> float:
        self.state = (self.state * _MULT + _INC) & _MASK
        self.calls += 1
        return f32(self.state / 0x1000000)

    def randomize(self, seed: float) -> None:
        """RANDOMIZE seed: high word of the double, folded, keeps the low byte."""
        m = struct.unpack("<II", struct.pack("<d", float(seed)))[1]
        m ^= m >> 16
        self.state = ((m & 0xFFFF) << 8) | (self.state & 0xFF)


class ScriptedDice:
    """Test double: returns a fixed list of RND values, then fails loudly.

    Used to hand-trace a mechanic against the source: the test states which
    rolls the source consumes and in what order.
    """

    def __init__(self, values: list[float]) -> None:
        self.values = [f32(v) for v in values]
        self.calls = 0

    def rnd(self) -> float:
        if self.calls >= len(self.values):
            raise AssertionError(f"mechanic consumed more than {len(self.values)} rolls")
        value = self.values[self.calls]
        self.calls += 1
        return value

    def randomize(self, seed: float) -> None:
        raise AssertionError("scripted dice cannot be reseeded")
