class Bit:
    def __init__(self, value: bool) -> None:
        self.value = bool(value)

    def __bool__(self) -> bool:
        return self.value

    def __invert__(self) -> "Bit":
        return Bit(not self.value)

    def __eq__(self, other: object) -> bool:
        # Only used for testing
        if isinstance(other, Bit):
            return self.value == other.value
        return False

    def __str__(self) -> str:
        return "1" if self.value else "0"

    def __repr__(self) -> str:
        return "1" if self.value else "0"


def xor(a: Bit, b: Bit) -> Bit:
    """
    The exclusive OR (XOR) gives true if only one of the inputs is true.

    Args:
    a (Bit): First input
    b (Bit): Second input

    Returns:
    Bit: XOR output
    """
    return a and ~b or ~a and b


def multi_and(a: list[Bit]) -> Bit:
    """
    And Gate implementation for multiple inputs.

    Args:
    a (list[Bit]): Inputs

    Returns:
    Bit: AND output
    """
    result = a[0]
    for bit in a[1:]:
        result = result and bit
    return result


def multi_or(a: list[Bit]) -> Bit:
    """
    Or Gate implementation for multiple inputs.

    Args:
    a (list[Bit]): Inputs

    Returns:
    Bit: OR output
    """
    result = a[0]
    for bit in a[1:]:
        result = result or bit
    return result
