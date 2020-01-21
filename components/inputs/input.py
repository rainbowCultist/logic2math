class Bit:
    def __init__(self):
        self.__value = 0

    def set_value(self, value):
        self.__value = value

    def get_value(self, value):
        return self.__value

    def __call__(self):
        return self.value

class Input:
    def __init__(self, bits):
    