from .component import Component
import functools
import itertools
import operator

m = lambda x : abs(int(x**2+0.5*x-1.5)) # m for magic ;)

class Gate(Component):
    __slots__ = ('inputs', 'op')

    def __getitem__(self, index: int):
        return self.inputs[index]

    def compute(self):
        return functools.reduce(self.op, [i.compute() for i in self.inputs])

    def __str__(self):
        return f'{self.__class__.__name__}({", ".join([str(i) for i in self.inputs])})'

    def convert_latex(self):
        raise NotImplementedError("This internal class isn't meant to be used.")


class And(Gate):
    def __init__(self, *inputs):
        self.inputs = inputs
        self.op = operator.__and__

    def convert_latex(self, as_lists=False):
        pieces = [[m((-1)**sum(j[0] for j in i)), ''.join(j for j in set([k[1] for k in i]) if not (j == '1' and len(set([k[1] for k in i]))>1))] for i in itertools.product(*[i.convert_latex(as_lists=True) for i in self.inputs])]
        if as_lists == True:
            return pieces


        puzzle = ''.join([['+', '-'][i[0]] + i[1] for i in pieces])
        puzzle = puzzle[1:len(puzzle)] if puzzle[0] == '+' else puzzle

        return puzzle


class Or(Gate):
    def __init__(self, *inputs):
        self.inputs = inputs
        self.op = operator.__or__

    def convert_latex(self, as_lists=False):
        pieces = list(itertools.chain(*[i.convert_latex(as_lists=True) for i in self.inputs]))

        puzzle = ''.join([['+', '-'][i[0]] + i[1] for i in pieces])
        puzzle = puzzle[1:len(puzzle)] if puzzle[0] == '+' else puzzle

        conversion = r'\operatorname{sign}\left(' +puzzle+ r'\right)'

        return [[0, conversion]] if as_lists else conversion


class Xor(Gate):
    def __init__(self, *inputs):
        if len(inputs) != 2:
            raise KeyError('Too {0} inputs: 2 required.'.format(['many', 'few'][len(inputs) > 2]))
        self.inputs = inputs
        self.op = operator.xor

    def convert_latex(self, as_lists=False):
        pieces = self[1].convert_latex(as_lists=True)
        pieces = [[1 - i[0], i[1]] for i in pieces]
        puzzle = ''.join([['+', '-'][i[0]] + i[1] for i in pieces])
        puzzle = puzzle[1:len(puzzle)] if puzzle[0] == '+' else puzzle

        conversion = r'\left|'+self[0].convert_latex()+puzzle+r'\right|'

        return [[0, conversion]] if as_lists else conversion

class Not(Gate):
    def __init__(self, input):
        self.inputs = [input]
        self.op = operator.__not__

    def convert_latex(self, as_lists=False):
        pieces = list(itertools.chain(*[i.convert_latex(as_lists=True) for i in self.inputs]))

        pieces = [[1, '1']]+pieces
        pieces = [[1-i[0], i[1]] for i in pieces]

        if as_lists:
            return pieces

        else:
            return_statement = ''.join([['+', '-'][i[0]]+i[1] for i in pieces])
            return_statement = return_statement[1:len(return_statement)] if return_statement[0]=='+' else return_statement

        return return_statement

