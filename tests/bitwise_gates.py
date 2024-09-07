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

    assert bitwise_and(bits1, bits2) == [Bit(True), Bit(False), Bit(False), Bit(False)]


def test_bitwise_or():
    bits1 = [Bit(True), Bit(True), Bit(False), Bit(False)]
    bits2 = [Bit(True), Bit(False), Bit(True), Bit(False)]

    assert bitwise_or(bits1, bits2) == [Bit(True), Bit(True), Bit(True), Bit(False)]


def test_bitwise_not():
    bits = [Bit(True), Bit(False), Bit(True), Bit(False)]

    assert bitwise_not(bits) == [Bit(False), Bit(True), Bit(False), Bit(True)]


def test_bitwise_xor():
    bits1 = [Bit(True), Bit(True), Bit(False), Bit(False)]
    bits2 = [Bit(True), Bit(False), Bit(True), Bit(False)]

    assert bitwise_xor(bits1, bits2) == [Bit(False), Bit(True), Bit(True), Bit(False)]
