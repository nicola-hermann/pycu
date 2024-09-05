from pycu.components.bit import Bit
from pycu.components.adder import (
    half_adder,
    full_adder,
    ripple_carry_adder,
    incrementer,
)
import unittest


class TestAdder(unittest.TestCase):

    def test_half_adder(self):
        a = Bit(False)
        b = Bit(False)
        sum, carry_out = half_adder(a, b)
        self.assertEqual(sum, Bit(False))
        self.assertEqual(carry_out, Bit(False))

        a = Bit(False)
        b = Bit(True)
        sum, carry_out = half_adder(a, b)
        self.assertEqual(sum, Bit(True))
        self.assertEqual(carry_out, Bit(False))

        a = Bit(True)
        b = Bit(False)
        sum, carry_out = half_adder(a, b)
        self.assertEqual(sum, Bit(True))
        self.assertEqual(carry_out, Bit(False))

        a = Bit(True)
        b = Bit(True)
        sum, carry_out = half_adder(a, b)
        self.assertEqual(sum, Bit(False))
        self.assertEqual(carry_out, Bit(True))

    def test_full_adder(self):
        a = Bit(False)
        b = Bit(False)
        carry_in = Bit(False)
        sum, carry_out = full_adder(a, b, carry_in)
        self.assertEqual(sum, Bit(False))
        self.assertEqual(carry_out, Bit(False))

        a = Bit(False)
        b = Bit(True)
        carry_in = Bit(False)
        sum, carry_out = full_adder(a, b, carry_in)
        self.assertEqual(sum, Bit(True))
        self.assertEqual(carry_out, Bit(False))

        a = Bit(True)
        b = Bit(False)
        carry_in = Bit(False)
        sum, carry_out = full_adder(a, b, carry_in)
        self.assertEqual(sum, Bit(True))
        self.assertEqual(carry_out, Bit(False))

        a = Bit(True)
        b = Bit(True)
        carry_in = Bit(False)
        sum, carry_out = full_adder(a, b, carry_in)
        self.assertEqual(sum, Bit(False))
        self.assertEqual(carry_out, Bit(True))

        a = Bit(False)
        b = Bit(False)
        carry_in = Bit(True)
        sum, carry_out = full_adder(a, b, carry_in)
        self.assertEqual(sum, Bit(True))
        self.assertEqual(carry_out, Bit(False))

        a = Bit(False)
        b = Bit(True)
        carry_in = Bit(True)
        sum, carry_out = full_adder(a, b, carry_in)
        self.assertEqual(sum, Bit(False))
        self.assertEqual(carry_out, Bit(True))

        a = Bit(True)
        b = Bit(False)
        carry_in = Bit(True)
        sum, carry_out = full_adder(a, b, carry_in)
        self.assertEqual(sum, Bit(False))
        self.assertEqual(carry_out, Bit(True))

        a = Bit(True)
        b = Bit(True)
        carry_in = Bit(True)
        sum, carry_out = full_adder(a, b, carry_in)
        self.assertEqual(sum, Bit(True))
        self.assertEqual(carry_out, Bit(True))

    def test_ripple_carry_adder(self):
        a = [Bit(False), Bit(True), Bit(True), Bit(False)]
        b = [Bit(False), Bit(False), Bit(True), Bit(True)]
        sum, carry, overflow, zero, negative = ripple_carry_adder(a, b)
        self.assertEqual(sum, [Bit(True), Bit(False), Bit(False), Bit(True)])
        self.assertEqual(carry, Bit(False))
        self.assertEqual(overflow, Bit(True))
        self.assertEqual(zero, Bit(False))
        self.assertEqual(negative, Bit(True))

        a = [Bit(False), Bit(False), Bit(False), Bit(False)]
        b = [Bit(False), Bit(False), Bit(False), Bit(False)]
        sum, carry, overflow, zero, negative = ripple_carry_adder(a, b)
        self.assertEqual(sum, [Bit(False), Bit(False), Bit(False), Bit(False)])
        self.assertEqual(carry, Bit(False))
        self.assertEqual(overflow, Bit(False))
        self.assertEqual(zero, Bit(True))
        self.assertEqual(negative, Bit(False))

        a = [Bit(False), Bit(False), Bit(True), Bit(True)]
        b = [Bit(False), Bit(False), Bit(True), Bit(True)]
        sum, carry, overflow, zero, negative = ripple_carry_adder(a, b)
        self.assertEqual(sum, [Bit(False), Bit(True), Bit(True), Bit(False)])
        self.assertEqual(carry, Bit(False))
        self.assertEqual(overflow, Bit(False))
        self.assertEqual(zero, Bit(False))
        self.assertEqual(negative, Bit(False))

    def test_incrementer(self):
        a = [Bit(False), Bit(True), Bit(True), Bit(False)]
        sum, carry, overflow, zero, negative = incrementer(a)
        self.assertEqual(sum, [Bit(False), Bit(True), Bit(True), Bit(True)])
        self.assertEqual(carry, Bit(False))
        self.assertEqual(overflow, Bit(False))
        self.assertEqual(zero, Bit(False))
        self.assertEqual(negative, Bit(False))

        a = [Bit(False), Bit(False), Bit(False), Bit(False)]
        sum, carry, overflow, zero, negative = incrementer(a)
        self.assertEqual(sum, [Bit(False), Bit(False), Bit(False), Bit(True)])
        self.assertEqual(carry, Bit(False))
        self.assertEqual(overflow, Bit(False))
        self.assertEqual(zero, Bit(False))
        self.assertEqual(negative, Bit(False))

        a = [Bit(True), Bit(True), Bit(True), Bit(True)]
        sum, carry, overflow, zero, negative = incrementer(a)
        self.assertEqual(sum, [Bit(False), Bit(False), Bit(False), Bit(False)])
        self.assertEqual(carry, Bit(True))
        self.assertEqual(overflow, Bit(False))
        self.assertEqual(zero, Bit(True))
        self.assertEqual(negative, Bit(False))


if __name__ == "__main__":
    unittest.main()
