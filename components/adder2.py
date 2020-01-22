from .gates import And
from .gates import Or
from .gates import Xor
from .inputs import Input

class HalfAdder:
    def __init__(self, a, b):
        self.o = Xor(a, b)
        self.c = And(a, b)

class FullAdder:
    def __init__(self, a, b, c):
        add0 = HalfAdder(a, b)
        add1 = HalfAdder(add0.o, c)
        or0 = Or(add0.c0, add1.c)
        self.o = add1.o
        self.c = or0


