import unittest
from pycu.components.bit import Bit


class TestBit(unittest.TestCase):

    def test_bit(self):
        bit = Bit(False)
        self.assertEqual(bit.value, False)
        bit = Bit(True)
        self.assertEqual(bit.value, True)

    def test_not(self):
        bit = Bit(False)
        self.assertEqual(~bit, Bit(True))
        bit = Bit(True)
        self.assertEqual(~bit, Bit(False))

    def test_and(self):
        bit1 = Bit(False)
        bit2 = Bit(False)
        self.assertEqual(bit1 and bit2, Bit(False))
        bit1 = Bit(False)
        bit2 = Bit(True)
        self.assertEqual(bit1 and bit2, Bit(False))
        bit1 = Bit(True)
        bit2 = Bit(False)
        self.assertEqual(bit1 and bit2, Bit(False))
        bit1 = Bit(True)
        bit2 = Bit(True)
        self.assertEqual(bit1 and bit2, Bit(True))

    def test_or(self):
        bit1 = Bit(False)
        bit2 = Bit(False)
        self.assertEqual(bit1 or bit2, Bit(False))
        bit1 = Bit(False)
        bit2 = Bit(True)
        self.assertEqual(bit1 or bit2, Bit(True))
        bit1 = Bit(True)
        bit2 = Bit(False)
        self.assertEqual(bit1 or bit2, Bit(True))
        bit1 = Bit(True)
        bit2 = Bit(True)
        self.assertEqual(bit1 or bit2, Bit(True))


if __name__ == "__main__":
    unittest.main()
