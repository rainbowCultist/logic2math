from .gate import Gate

class And(Gate):
    def __init__(self, *inputs: Gate):
        return Gate(*inputs)

    def __call__(self):
        return self[0] and self[1]
