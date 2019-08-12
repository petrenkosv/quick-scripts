import numpy as np
def signoid(x):
    return 1 / (1 + np.exp(-x))
training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

def signoid_derivative(x):
    return x * (1-x)

traning_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.randn((3,1))-1

print('Random starting symantic weights: ')
print(synaptic_weights)

for iteraction in range(20000):
    input_layer = training_inputs
    outputs = signoid(np.dot(input_layer, synaptic_weights))
    error = training_inputs - outputs
    ajustments = error * signoid_derivative(outputs)
    synaptic_weights += np.dot(input_layer.T, ajustments)

print('Symantic weights after traning: ')
print(synaptic_weights)

print('Output after traning')
print(outputs)