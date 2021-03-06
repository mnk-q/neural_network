import numpy as np

ips = [[1,2,3,2.5], [2.0,5.0,-1.0, 2.0], [-1.5,2.7,3.3,-0.8]]
weights1 = [ [0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]
bias1 = [2,3,0.5]


weights2 = [ [0.1, -0.14, 0.5],
            [-0.5, 0.12, -0.33],
            [ -0.44, 0.73, -0.13]]
bias2 = [-1, 2, -0.5]


layer1_output = np.dot(ips, np.array(weights1).T) + bias1

layer2_output = np.dot(layer1_output, np.array(weights2).T) + bias2

print(layer2_output)
'''
layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, bias):
    neuron_output=0
    for n_input, weight in zip(ips, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)
'''
#print(layer_outputs)