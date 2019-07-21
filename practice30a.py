# AND

import numpy as np

# To create input Array

input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])

# Weight for Inputs
weights = np.array([0.5, 0.5])

# Define Activation Function and Threshold
theta = 1
def activation(s): # Binary Unit Step
    if s >= 0:
        return 1
    else:
        return 0

def summation(x, w):
    s = np.dot(x, w)
    y = activation(s)
    return y

output1 = summation(input1, weights)
output2 = summation(input2, weights)
output3 = summation(input3, weights)
output4 = summation(input4, weights)

print("For", input1, "|", output1)
print("For", input2, "|", output2)
print("For", input3, "|", output3)
print("For", input4, "|", output4)


