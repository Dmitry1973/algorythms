from numpy import array, random, dot


class NeuralNetwork:
    def __init__(self):
        random.seed(1)
        # We model a singl neuron, with 3 inpurs and 1 outputs and assign random weight
        self.weights = 2 * random.random((2, 1)) - 1

    def train(self, inputs, outputs, num):
        for iteration in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = 0.01 * dot(inputs.T, error)
            self.weights += adjustment

    def think(self, inputs):
        return dot(inputs, self.weights)


Neural_Network = NeuralNetwork()

# The treining set
inputs = array([[2, 3], [1, 1], [5, 2], [12, 3]])
outputs = array([[10, 4, 14, 30]]).T

# trainin the neural network using the training set
Neural_Network.train(inputs, outputs, 10000)

# ask th eneural network the output
print(Neural_Network.think([15, 2]))
