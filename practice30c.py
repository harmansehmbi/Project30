import numpy as np

# To create input Array

input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])

# Weight for Inputs
weights = np.array([0.5, 0.5])

class Perceptron:

    theta = 1

    def __init__(self, inputs, weights):
        self.inputs = inputs
        self.weights = weights

    def activation(self, sum):
        if sum >= Perceptron.theta:
            return 1
        else:
            return 0

    def summation(self):
        s = np.dot(self.inputs, self.weights)
        y = self.activation(s)
        return y

model = Perceptron(input1, weights)

output = model.summation()

print("For", input1, "|", output)

