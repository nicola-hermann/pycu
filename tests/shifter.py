import pytest
from pycu.components.bit import Bit
from pycu.components.shifter import (
    logic_shift_left,
    logic_shift_right,
    arithmetic_shift_right,
)


def test_logic_shift_left_1():
    bits = [Bit(False), Bit(True), Bit(False)]
    assert logic_shift_left(bits) == [Bit(True), Bit(False), Bit(False)]


def test_logic_shift_left_2():
    bits = [Bit(True), Bit(False), Bit(True)]
    assert logic_shift_left(bits) == [Bit(False), Bit(True), Bit(False)]


def test_logic_shift_left_3():
    bits = [Bit(True), Bit(True), Bit(True)]
    assert logic_shift_left(bits) == [Bit(True), Bit(True), Bit(False)]


def test_logic_shift_left_4():
    bits = [Bit(False), Bit(False), Bit(False)]
    assert logic_shift_left(bits) == [Bit(False), Bit(False), Bit(False)]


def test_logic_shift_right_1():
    bits = [Bit(False), Bit(True), Bit(False)]
    assert logic_shift_right(bits) == [Bit(False), Bit(False), Bit(True)]


def test_logic_shift_right_2():
    bits = [Bit(True), Bit(False), Bit(True)]
    assert logic_shift_right(bits) == [Bit(False), Bit(True), Bit(False)]


def test_logic_shift_right_3():
    bits = [Bit(True), Bit(True), Bit(True)]
    assert logic_shift_right(bits) == [Bit(False), Bit(True), Bit(True)]


def test_logic_shift_right_4():
    bits = [Bit(False), Bit(False), Bit(False)]
    assert logic_shift_right(bits) == [Bit(False), Bit(False), Bit(False)]


def test_arithmetic_shift_right_1():
    bits = [Bit(False), Bit(True), Bit(False)]
    assert arithmetic_shift_right(bits) == [Bit(False), Bit(False), Bit(True)]


def test_arithmetic_shift_right_2():
    bits = [Bit(True), Bit(False), Bit(True)]
    assert arithmetic_shift_right(bits) == [Bit(True), Bit(True), Bit(False)]


def test_arithmetic_shift_right_3():
    bits = [Bit(True), Bit(True), Bit(True)]
    assert arithmetic_shift_right(bits) == [Bit(True), Bit(True), Bit(True)]


def test_arithmetic_shift_right_4():
    bits = [Bit(False), Bit(False), Bit(False)]
    assert arithmetic_shift_right(bits) == [Bit(False), Bit(False), Bit(False)]
