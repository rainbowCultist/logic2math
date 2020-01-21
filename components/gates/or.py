from components.gates.gate import Gate

class Or(Gate):
    def __call__(self):
        return self[0] | self[1]
