from math import floor
from math import log

from .component import Component


class Bit(Component):

    __slots__ = ('value', 'name', 'position', 'kind')

    def __init__(self, name: str, position: int):
        self.value = None
        self.kind = "bit"
        self.name = name
        self.position = (
            position
        )

    def __str__(self):
        return f'{self.name}[{self.position}]'

    def change_value(self, new_value: bool):
        self.value = new_value

    def get_value(self) -> bool:
        return self.value

    def __mul__(self, other: int):
        return self.value * other

    def compute(self):
        return self.value

    def convert_python(self, as_list=False):
        return_statement = f'{self.name}//{2**self.position}%2'

        return [return_statement] if as_list else return_statement

    def convert_latex(self, as_list=False):
        left = "{"
        right = "}"
        return_statement = f'\\operatorname{left}mod{right}\\left(\\operatorname{left}floor{right}\\left(\\frac{left}{self.name}{right}{left}{2**self.position}{right}\\right),2\\right)'

        if self.position == 0:
            return_statement = (
                f'\\operatorname{left}mod{right}\\left({self.name},2\\right)'
            )

        return [return_statement] if as_list else return_statement


class Input:

    __slots__ = ('bit_list', 'name', 'bits')

    def __init__(self, bits: int, name: str):
        self.bits = bits
        self.name = name
        self.bit_list = [Bit(name, i) for i in range(bits)]

    def __getitem__(self, index: int) -> Bit:
        return self.bit_list[index]

    def set_number(self, new_number: int):
        if new_number != 0:
            if floor(log(new_number, 2)) >= self.bits:
                raise ValueError("This number has too many bits!")

        for i, bit in enumerate(self.bit_list):
            bit.change_value(floor(new_number / 2 ** i) % 2)

    def get_number(self) -> int:
        return sum([bit * 2 ** i for i, bit in enumerate(self.bit_list)])

    number = property(get_number, set_number)
