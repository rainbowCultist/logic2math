from components.gates.gate import Gate

class Xor(Gate):
    def __call__(self):
        return self[0] ^ self[1]
