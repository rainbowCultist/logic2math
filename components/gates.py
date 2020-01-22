from .component import Component


class LogicGate(Component):
    __slots__ = ('inputs', 'kind')

    def __init__(self, kind: str, required_inputs: int, *inputs):
        self.kind = kind
        if len(inputs) == required_inputs:
            self.inputs = inputs
        else:
            raise KeyError('{0}: {1}'.format())

    def __getitem__(self, index: int):
        return self.inputs[index]

    def compute(self):
        raise NotImplementedError("This internal class isn't meant to be used.")

    def __str__(self):
        return f'{self.kind}({", ".join([str(i) for i in self.inputs])})'

    def convert_latex(self):
        raise NotImplementedError("This internal class isn't meant to be used.")


class And(LogicGate):
    def __init__(self, *inputs):
        super().__init__("And", 2, *inputs)

    def compute(self):
        return self[0].compute() & self[1].compute()

    def convert_latex(self):
        I = self[0].convert_latex()
        J = self[1].convert_latex()

        return f'{I}{J}'


class Or(LogicGate):
    def __init__(self, *inputs):
        super().__init__("Or", 2, *inputs)

    def compute(self):
        return self[0].compute() | self[1].compute()

    def convert_latex(self):
        left = '{'
        right = '}'
        return_statement = f'\\operatorname{left}sign{right}\\left({self[0].convert_latex()}+{self[1].convert_latex()}\\right)'

        return return_statement


class Xor(LogicGate):
    def __init__(self, *inputs):
        super().__init__("Xor", 2, *inputs)

    def compute(self):
        return self[0].compute() ^ self[1].compute()

    def convert_latex(self):
        return_statement = f'\\left|{self[0].convert_latex()}-{self[1].convert_latex()}\\right|'

        return return_statement


class Not(LogicGate):
    def __init__(self, input):
        super().__init__("Not", 1, input)

    def compute(self):
        return not self[0].compute()

    def convert_latex(self):
        return_statement = f'1-{self[0].convert_latex()}'

        return return_statement
