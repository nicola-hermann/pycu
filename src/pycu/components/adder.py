from pycu.components.bit import Bit, xor, multi_or


def half_adder(a: Bit, b: Bit) -> tuple[Bit, Bit]:
    """
    Half adder implementation

    Args:
    a (Bit): First input
    b (Bit): Second input

    Returns:
    tuple[Bit, Bit]: Sum and carry out
    """
    sum = xor(a, b)
    carry_out = a and b

    return (sum, carry_out)


def full_adder(a: Bit, b: Bit, carry_in) -> tuple[Bit, Bit]:
    """
    Full adder implementation

    Args:
    a (Bit): First input
    b (Bit): Second input
    carry_in (Bit): Carry in

    Returns:
    tuple[Bit, Bit]: Sum and carry out
    """

    sum_1, carry_1 = half_adder(a, b)
    total, carry_2 = half_adder(sum_1, carry_in)
    carry = carry_1 or carry_2
    return (total, carry)


def ripple_carry_adder(
    a: list[Bit], b: list[Bit]
) -> tuple[list[Bit], Bit, Bit, Bit, Bit]:
    """
    Ripple carry adder implementation flexible to any length.
    The most significant bit (MSB) is at the front of the list.

    Args:
    a (list[Bit]): First input
    b (list[Bit]): Second input

    Returns:
    tuple[list[Bit], Bit, Bit, Bit, Bit]: Sum, carry out, overflow, zero flag, negative flag
    """

    # This is just for error checking and does not count to the raw implementation
    if len(a) != len(b):
        raise ValueError("Inputs must be the same length")

    # Initialize the carry to 0 or start with a half adder
    carry_out = Bit(False)
    result = []
    # Iterate over the bits from back to front
    for i in range(len(a) - 1, -1, -1):
        # The carry out of the previous bit is the carry in of the current bit
        carry_in = carry_out
        sum, carry_out = full_adder(a[i], b[i], carry_in)
        result.insert(0, sum)

    # Get all the flags for the ALU
    overflow = xor(carry_in, carry_out)
    zero_flag = ~multi_or(result)
    negative_flag = result[0]

    return (result, carry_out, overflow, zero_flag, negative_flag)


def incrementer(a: list[Bit]) -> tuple[list[Bit], Bit]:
    """
    Incrementer implementation

    Args:
    a (list[Bit]): Input

    Returns:
    tuple[list[Bit], Bit]: Incremented value and carry out
    """

    # Initialize the carry to 1 for any length
    carry_in = Bit(True)
    result = []
    # Iterate over the bits from back to front
    for i in range(len(a) - 1, -1, -1):
        sum, carry_out = full_adder(a[i], Bit(False), carry_in)
        result.insert(0, sum)
        carry_in = carry_out

    # Get all the flags for the ALU
    overflow = xor(carry_in, carry_out)
    zero_flag = ~multi_or(result)
    negative_flag = result[0]

    return (result, carry_out, overflow, zero_flag, negative_flag)

    return (result, carry_out)


if __name__ == "__main__":
    a = [Bit(False), Bit(True), Bit(True), Bit(False)]
    b = [Bit(False), Bit(False), Bit(True), Bit(True)]
    sum, carry, overflow, zero, negative = ripple_carry_adder(a, b)
    print(sum, carry, overflow, zero, negative)
