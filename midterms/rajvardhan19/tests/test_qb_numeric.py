"""QBasic/QB64 numeric semantics, checked against values QB64-PE 4.7.0 printed.

The expected numbers come from tools/qb64-harness probes compiled and run
with QB64-PE (docs/rule-source-map.md, "Numeric semantics").
"""

import unittest

from cws.qb import QBRandom, S, cint, f32, idiv, qint


class RandomNumbers(unittest.TestCase):
    def test_default_sequence_matches_qbasic(self):
        r = QBRandom()
        self.assertEqual([round(r.rnd(), 7) for _ in range(3)], [0.7055475, 0.533424, 0.5795186])

    def test_randomize_keeps_low_byte_like_qb64(self):
        r = QBRandom()
        for _ in range(3):
            r.rnd()
        r.randomize(12345.678)
        self.assertEqual([round(r.rnd(), 7), round(r.rnd(), 7)], [0.7454798, 0.5435709])

    def test_randomize_one_then_sequence(self):
        r = QBRandom()
        for _ in range(5):
            r.rnd()
        r.randomize(1)
        self.assertEqual(round(r.rnd(), 7), 0.4937953)
        self.assertEqual(round(r.rnd(), 7), 0.1693521)

    def test_values_are_exact_singles(self):
        r = QBRandom()
        for _ in range(100):
            v = r.rnd()
            self.assertEqual(v, f32(v))
            self.assertTrue(0 <= v < 1)


class Rounding(unittest.TestCase):
    def test_integer_assignment_rounds_half_to_even(self):
        self.assertEqual([cint(0.5), cint(1.5), cint(2.5), cint(3.5), cint(-2.5)], [0, 2, 2, 4, -2])

    def test_probe_products(self):
        # x = .01 * 350 -> 4; .7 * 45 -> 32 (double product, rounded once to single, then even)
        self.assertEqual(cint(f32(.01 * 350)), 4)
        self.assertEqual(cint(f32(.7 * 45)), 32)
        self.assertEqual(cint(f32(.5 * 5)), 2)

    def test_victory_point_case_from_differential_run(self):
        # .8 * 742 + .3 * 343 = 696.5 exactly; QB64 printed 696. Rounding each
        # product to single first would give 697 (the bug found on seed 2).
        self.assertEqual(cint(f32(.8 * 742 + .3 * 343)), 696)
        self.assertEqual(cint(f32(f32(S(.8) * 742) + f32(S(.3) * 343))), 697)

    def test_single_accumulation(self):
        p = 0.0
        for _ in range(12):
            p = f32(p + S(.1))
        self.assertEqual(f"{p:.10f}", "1.2000001669")

    def test_integer_division_and_int(self):
        self.assertEqual(idiv(110, 3), 36)
        self.assertEqual(idiv(-7, 2), -3)
        self.assertEqual(qint(-0.5), -1)
        self.assertEqual(qint(6.99), 6)


if __name__ == "__main__":
    unittest.main()
