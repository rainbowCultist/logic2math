class Gate:
    def __init__(self, *inputs):
        self.inputs = inputs

    def set_inputs(self, inputs):
        if len(inputs) == 2:
            self.__inputs = inputs
        else:
            raise ValueError('Too {0} inputs: 2 required.'.format(['many', 'little'][inputs > 2]))

    def get_inputs(self):
        return self.__inputs

    inputs = property(get_inputs, set_inputs)

    def __getitem__(self, item):
        return self.__inputs[item]


