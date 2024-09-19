import pytest
from pycu.components.bit import Bit


def test_bit_false():
    bit = Bit(False)
    assert bit.value == False


def test_bit_true():
    bit = Bit(True)
    assert bit.value == True


def test_not_false():
    bit = Bit(False)
    assert ~bit == Bit(True)


def test_not_true():
    bit = Bit(True)
    assert ~bit == Bit(False)


def test_and_false_false():
    bit1 = Bit(False)
    bit2 = Bit(False)
    assert (bit1 and bit2) == Bit(False)


def test_and_false_true():
    bit1 = Bit(False)
    bit2 = Bit(True)
    assert (bit1 and bit2) == Bit(False)


def test_and_true_false():
    bit1 = Bit(True)
    bit2 = Bit(False)
    assert bit1 and bit2 == Bit(False)


def test_and_true_true():
    bit1 = Bit(True)
    bit2 = Bit(True)
    assert bit1 and bit2 == Bit(True)


def test_or_false_false():
    bit1 = Bit(False)
    bit2 = Bit(False)
    assert bit1 or bit2 == Bit(False)


def test_or_false_true():
    bit1 = Bit(False)
    bit2 = Bit(True)
    assert bit1 or bit2 == Bit(True)


def test_or_true_false():
    bit1 = Bit(True)
    bit2 = Bit(False)
    assert bit1 or bit2 == Bit(True)


def test_or_true_true():
    bit1 = Bit(True)
    bit2 = Bit(True)
    assert bit1 or bit2 == Bit(True)
