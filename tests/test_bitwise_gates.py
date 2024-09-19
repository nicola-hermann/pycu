from pycu.components.bit import Bit
from pycu.components.bitwise_gates import (
    bitwise_and,
    bitwise_or,
    bitwise_not,
    bitwise_xor,
)
import pytest


def test_bitwise_and():
    bits1 = [Bit(True), Bit(True), Bit(False), Bit(False)]
    bits2 = [Bit(True), Bit(False), Bit(True), Bit(False)]

    res, carry, overflow, zero, negative = bitwise_and(bits1, bits2)

    assert res == [Bit(True), Bit(False), Bit(False), Bit(False)]
    assert carry == Bit(False)
    assert overflow == Bit(False)
    assert zero == Bit(False)
    assert negative == Bit(True)


def test_bitwise_or():
    bits1 = [Bit(True), Bit(True), Bit(False), Bit(False)]
    bits2 = [Bit(True), Bit(False), Bit(True), Bit(False)]

    res, carry, overflow, zero, negative = bitwise_or(bits1, bits2)

    assert res == [Bit(True), Bit(True), Bit(True), Bit(False)]
    assert carry == Bit(False)
    assert overflow == Bit(False)
    assert zero == Bit(False)
    assert negative == Bit(True)


def test_bitwise_not():
    bits = [Bit(True), Bit(False), Bit(True), Bit(False)]

    res, carry, overflow, zero, negative = bitwise_not(bits)

    assert res == [Bit(False), Bit(True), Bit(False), Bit(True)]
    assert carry == Bit(False)
    assert overflow == Bit(False)
    assert zero == Bit(False)
    assert negative == Bit(False)


def test_bitwise_xor():
    bits1 = [Bit(True), Bit(True), Bit(False), Bit(False)]
    bits2 = [Bit(True), Bit(False), Bit(True), Bit(False)]

    res, carry, overflow, zero, negative = bitwise_xor(bits1, bits2)

    assert res == [Bit(False), Bit(True), Bit(True), Bit(False)]
    assert carry == Bit(False)
    assert overflow == Bit(False)
    assert zero == Bit(False)
    assert negative == Bit(False)
