from nn import Module


class DummyLayer(Module):
    def __init__(self):
        super(DummyLayer, self).__init__(None)

    def forward(self, data):
        return data

    def backward(self, previous_partial_gradient):
        return previous_partial_gradient
