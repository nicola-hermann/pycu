from pycu.components.bit import Bit


class Byte:
    def __init__(self, bits: list[Bit]) -> None:
        if len(bits) != 8:
            raise ValueError("Byte must have 8 bits")
        self.bits = bits

    @staticmethod
    def from_int(value: int) -> "Byte":
        if value < 0 or value > 255:
            raise ValueError("Value must be between 0 and 255")
        bits = [Bit((value >> i) & 1) for i in range(7, -1, -1)]
        return Byte(bits)

    @staticmethod
    def from_str(value: str) -> "Byte":
        if len(value) != 8:
            raise ValueError("Value must have 8 bits")
        bits = [Bit(int(bit)) for bit in value]
        return Byte(bits)

    def __str__(self) -> str:
        return "".join(str(bit) for bit in self.bits)

    def __repr__(self) -> str:
        return "".join(str(bit) for bit in self.bits)
