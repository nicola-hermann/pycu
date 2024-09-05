from pycu.components.bit import Bit
from pycu.components.adder import ripple_carry_adder, incrementer


def ripple_carry_subtractor(
    a: list[Bit], b: list[Bit]
) -> tuple[list[Bit], Bit, Bit, Bit, Bit]:
    """
    Ripple carry subtractor implementation flexible to any length.
    The most significant bit (MSB) is at the front of the list.

    Args:
    a (list[Bit]): First input
    b (list[Bit]): Second input

    Returns:
    tuple[list[Bit], Bit, Bit, Bit, Bit]: Difference, borrow out, underflow, zero flag, negative flag
    """

    # This is just for error checking and does not count to the raw implementation
    if len(a) != len(b):
        raise ValueError("Inputs must be the same length")

    # Get the two's complement of b
    b_complement, _, _, _, _ = incrementer([~bit for bit in b])

    # Perform the addition
    result, borrow_out, underflow, zero, negative = ripple_carry_adder(a, b_complement)

    return (result, borrow_out, underflow, zero, negative)


if __name__ == "__main__":
    a = [Bit(False), Bit(True), Bit(True)]
    b = [Bit(True), Bit(False), Bit(True)]
    result, borrow_out = ripple_carry_subtractor(a, b)
    print(result, borrow_out)
