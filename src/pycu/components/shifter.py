from pycu.components.bit import Bit


def logic_shift_left(bits: list[Bit]) -> list[Bit]:
    """
    Shift the bits to the left by 1.
    The most significant bit (MSB) is at the front of the list.

    Args:
    bits (list[Bit]): Bits to shift

    Returns:
    list[Bit]: Shifted bits
    """
    return bits[1:] + [Bit(False)]


def logic_shift_right(bits: list[Bit]) -> list[Bit]:
    """
    Shift the bits to the right by 1.
    The most significant bit (MSB) is at the front of the list.

    Args:
    bits (list[Bit]): Bits to shift

    Returns:
    list[Bit]: Shifted bits
    """
    return [Bit(False)] + bits[:-1]


def arithmetic_shift_right(bits: list[Bit]) -> list[Bit]:
    """
    Shift the bits to the left by 1.
    The most significant bit (MSB) is at the front of the list.

    Args:
    bits (list[Bit]): Bits to shift

    Returns:
    list[Bit]: Shifted bits
    """
    return [bits[0]] + bits[:-1]
