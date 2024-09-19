from pycu.components.bit import Bit, multi_or


def bitwise_flags(a: list[Bit]) -> tuple[Bit, Bit, Bit, Bit]:
    """
    Calculate the flags for a list of bits for a bitwise logic gate.
    The most significant bit (MSB) is at the front of the list.

    Args:
    a (list[Bit]): List of bits

    Returns:
    tuple[Bit, Bit, Bit, Bit]: Carry, overflow, zero, negative flags
    """
    carry = Bit(False)
    overflow = Bit(False)
    zero = ~multi_or(a)
    negative = a[0]

    return (carry, overflow, zero, negative)


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

    carry, overflow, zero, negative = bitwise_flags(result)

    return (result, carry, overflow, zero, negative)


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

    carry, overflow, zero, negative = bitwise_flags(result)

    return (result, carry, overflow, zero, negative)


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

    carry, overflow, zero, negative = bitwise_flags(result)

    return (result, carry, overflow, zero, negative)


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

    carry, overflow, zero, negative = bitwise_flags(result)

    return (result, carry, overflow, zero, negative)
