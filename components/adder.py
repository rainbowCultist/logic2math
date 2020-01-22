from .component import Component
from .gates import And
from .gates import Or
from .gates import Xor
from .inputs import Input


class Adder(Component):
    __slots__ = ('bits', 'outputs', 'carries', 'a', 'b')

    def __init__(self, bits: int, var_name_1: str = 'x', var_name_2: str = 'y'):
        self.bits = bits

        self.a = Input(bits, name=var_name_1)
        self.b = Input(bits, name=var_name_2)

        self.carries = [And(self.a[0], self.b[0])]
        self.outputs = [Xor(self.a[0], self.b[0])]

        for i in range(1, bits):
            self.carries.append(
                Or(
                    And(self.a[i], self.b[i]),
                    And(Xor(self.a[i], self.b[i]), self.carries[i - 1]),
                )
            )
            self.outputs.append(Xor(Xor(self.a[i], self.b[i]), self.carries[i - 1]))

    def __call__(self, x, y):
        self.a.number = x
        self.b.number = y

        return sum(
            [
                output.compute() * 2 ** i
                for i, output in enumerate(self.outputs + [self.carries[-1]])
            ]
        )

    def convert_latex(self):
        return '+'.join(
            f'{2**i}{output.convert_latex()}'
            for i, output in enumerate(self.outputs + [self.carries[-1]])
        )

    def __str__(self):
        return '+'.join(
            [
                f'{2**i}*{output}'
                for i, output in enumerate(self.outputs + [self.carries[-1]])
            ]
        )
