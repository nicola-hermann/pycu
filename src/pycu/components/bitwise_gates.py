from pycu.components.bit import Bit


def bitwise_and(a: list[Bit], b: list[Bit]) -> list[Bit]:
    """
    Perform bitwise AND operation on two lists of bits.
    The most significant bit (MSB) is at the front of the list.

    Args:
    a (list[Bit]): First list of bits
    b (list[Bit]): Second list of bits

    Returns:
    list[Bit]: Result of the bitwise AND operation

    Raises:
    ValueError: If the inputs are not the same length
    """
    if len(a) != len(b):
        raise ValueError("Inputs must be the same length")

    result = [Bit(False) for _ in range(len(a))]

    for i in range(len(a)):
        result[i] = a[i] and b[i]

    return result


def bitwise_or(a: list[Bit], b: list[Bit]) -> list[Bit]:
    """
    Perform bitwise OR operation on two lists of bits.
    The most significant bit (MSB) is at the front of the list.

    Args:
    a (list[Bit]): First list of bits
    b (list[Bit]): Second list of bits

    Returns:
    list[Bit]: Result of the bitwise OR operation

    Raises:
    ValueError: If the inputs are not the same length
    """
    if len(a) != len(b):
        raise ValueError("Inputs must be the same length")

    result = [Bit(False) for _ in range(len(a))]

    for i in range(len(a)):
        result[i] = a[i] or b[i]

    return result


def bitwise_not(a: list[Bit]) -> list[Bit]:
    """
    Perform bitwise NOT operation on a list of bits.
    The most significant bit (MSB) is at the front of the list.

    Args:
    a (list[Bit]): List of bits

    Returns:
    list[Bit]: Result of the bitwise NOT operation
    """
    result = [Bit(False) for _ in range(len(a))]

    for i in range(len(a)):
        result[i] = ~a[i]

    return result


def bitwise_xor(a: list[Bit], b: list[Bit]) -> list[Bit]:
    """
    Perform bitwise XOR operation on two lists of bits.
    The most significant bit (MSB) is at the front of the list.

    Args:
    a (list[Bit]): First list of bits
    b (list[Bit]): Second list of bits

    Returns:
    list[Bit]: Result of the bitwise XOR operation

    Raises:
    ValueError: If the inputs are not the same length
    """
    if len(a) != len(b):
        raise ValueError("Inputs must be the same length")

    result = [Bit(False) for _ in range(len(a))]

    for i in range(len(a)):
        result[i] = a[i] and ~b[i] or ~a[i] and b[i]

    return result
