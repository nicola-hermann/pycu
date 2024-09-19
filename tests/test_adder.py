import pytest
from pycu.components.bit import Bit
from pycu.components.adder import (
    half_adder,
    full_adder,
    ripple_carry_adder,
    incrementer,
)


def test_half_adder_00():
    a = Bit(False)
    b = Bit(False)
    sum, carry_out = half_adder(a, b)
    assert sum == Bit(False)
    assert carry_out == Bit(False)


def test_half_adder_01():
    a = Bit(False)
    b = Bit(True)
    sum, carry_out = half_adder(a, b)
    assert sum == Bit(True)
    assert carry_out == Bit(False)


def test_half_adder_10():
    a = Bit(True)
    b = Bit(False)
    sum, carry_out = half_adder(a, b)
    assert sum == Bit(True)
    assert carry_out == Bit(False)


def test_half_adder_11():
    a = Bit(True)
    b = Bit(True)
    sum, carry_out = half_adder(a, b)
    assert sum == Bit(False)
    assert carry_out == Bit(True)


def test_full_adder_000():
    a = Bit(False)
    b = Bit(False)
    carry_in = Bit(False)
    sum, carry_out = full_adder(a, b, carry_in)
    assert sum == Bit(False)
    assert carry_out == Bit(False)


def test_full_adder_001():
    a = Bit(False)
    b = Bit(True)
    carry_in = Bit(False)
    sum, carry_out = full_adder(a, b, carry_in)
    assert sum == Bit(True)
    assert carry_out == Bit(False)


def test_full_adder_010():
    a = Bit(True)
    b = Bit(False)
    carry_in = Bit(False)
    sum, carry_out = full_adder(a, b, carry_in)
    assert sum == Bit(True)
    assert carry_out == Bit(False)


def test_full_adder_011():
    a = Bit(True)
    b = Bit(True)
    carry_in = Bit(False)
    sum, carry_out = full_adder(a, b, carry_in)
    assert sum == Bit(False)
    assert carry_out == Bit(True)


def test_full_adder_100():
    a = Bit(False)
    b = Bit(False)
    carry_in = Bit(True)
    sum, carry_out = full_adder(a, b, carry_in)
    assert sum == Bit(True)
    assert carry_out == Bit(False)


def test_full_adder_101():
    a = Bit(False)
    b = Bit(True)
    carry_in = Bit(True)
    sum, carry_out = full_adder(a, b, carry_in)
    assert sum == Bit(False)
    assert carry_out == Bit(True)


def test_full_adder_110():
    a = Bit(True)
    b = Bit(False)
    carry_in = Bit(True)
    sum, carry_out = full_adder(a, b, carry_in)
    assert sum == Bit(False)
    assert carry_out == Bit(True)


def test_full_adder_111():
    a = Bit(True)
    b = Bit(True)
    carry_in = Bit(True)
    sum, carry_out = full_adder(a, b, carry_in)
    assert sum == Bit(True)
    assert carry_out == Bit(True)


def test_ripple_carry_adder_1():
    a = [Bit(False), Bit(True), Bit(True), Bit(False)]
    b = [Bit(False), Bit(False), Bit(True), Bit(True)]
    sum, carry, overflow, zero, negative = ripple_carry_adder(a, b)
    assert sum == [Bit(True), Bit(False), Bit(False), Bit(True)]
    assert carry == Bit(False)
    assert overflow == Bit(True)
    assert zero == Bit(False)
    assert negative == Bit(True)


def test_ripple_carry_adder_2():
    a = [Bit(False), Bit(False), Bit(False), Bit(False)]
    b = [Bit(False), Bit(False), Bit(False), Bit(False)]
    sum, carry, overflow, zero, negative = ripple_carry_adder(a, b)
    assert sum == [Bit(False), Bit(False), Bit(False), Bit(False)]
    assert carry == Bit(False)
    assert overflow == Bit(False)
    assert zero == Bit(True)
    assert negative == Bit(False)


def test_ripple_carry_adder_3():
    a = [Bit(False), Bit(False), Bit(True), Bit(True)]
    b = [Bit(False), Bit(False), Bit(True), Bit(True)]
    sum, carry, overflow, zero, negative = ripple_carry_adder(a, b)
    assert sum == [Bit(False), Bit(True), Bit(True), Bit(False)]
    assert carry == Bit(False)
    assert overflow == Bit(False)
    assert zero == Bit(False)
    assert negative == Bit(False)


def test_incrementer_1():
    a = [Bit(False), Bit(True), Bit(True), Bit(False)]
    sum, carry, overflow, zero, negative = incrementer(a)
    assert sum == [Bit(False), Bit(True), Bit(True), Bit(True)]
    assert carry == Bit(False)
    assert overflow == Bit(False)
    assert zero == Bit(False)
    assert negative == Bit(False)


def test_incrementer_2():
    a = [Bit(False), Bit(False), Bit(False), Bit(False)]
    sum, carry, overflow, zero, negative = incrementer(a)
    assert sum == [Bit(False), Bit(False), Bit(False), Bit(True)]
    assert carry == Bit(False)
    assert overflow == Bit(False)
    assert zero == Bit(False)
    assert negative == Bit(False)


def test_incrementer_3():
    a = [Bit(True), Bit(True), Bit(True), Bit(True)]
    sum, carry, overflow, zero, negative = incrementer(a)
    assert sum == [Bit(False), Bit(False), Bit(False), Bit(False)]
    assert carry == Bit(True)
    assert overflow == Bit(False)
    assert zero == Bit(True)
    assert negative == Bit(False)
