# NOT

import numpy as np

# To create input Array

input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])

# Weight for Inputs
weights = np.array([0.5, 0.5])

# Define Activation Function and Threshold
theta = -0.5
def activation(s): # Binary Unit Step
    if s >= 0:
        return 1
    else:
        return 0

def summation(x, w):
    s = x * w
    y = activation(s)
    return y

input = 0
weight = -1

output = summation(input, weight)
print("For", input, "output is", output)


