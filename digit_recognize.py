import numpy as np
import random
import pickle
import gzip
import os
import random

class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a

    def SGD(self, training_data, epochs, mini_batch_size, learning_rate, test_data=None):
        if test_data: n_test = len(test_data)
        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size]
                for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, learning_rate)
            if test_data:
                print("Epoch {0}: {1} / {2}".format(
                    j, self.evaluate(test_data), n_test))
            else:
                print("Epoch {0} complete".format(j))

    def update_mini_batch(self, mini_batch, learning_rate):
        temp_biases = [np.zeros(b.shape) for b in self.biases]
        temp_weights = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backpropogation(x, y)
            temp_biases = [nb+dnb for nb, dnb in zip(temp_biases, delta_nabla_b)]
            temp_weights = [nw+dnw for nw, dnw in zip(temp_weights, delta_nabla_w)]
        self.weights = [w-(learning_rate/len(mini_batch))*nw for w, nw in zip(self.weights, temp_weights)]
        self.biases = [b-(learning_rate/len(mini_batch))*nb for b, nb in zip(self.biases, temp_biases)]

    def backpropogation(self, x, y):
        temp_biases = [np.zeros(b.shape) for b in self.biases]
        temp_weights = [np.zeros(w.shape) for w in self.weights]
      
        activation = x
        activations = [x]
        zs = [] 
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        # backward pass
        delta = self.cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
        temp_biases[-1] = delta
        temp_weights[-1] = np.dot(delta, activations[-2].transpose())
        for i in range(2, self.num_layers):
            z = zs[-i]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-i+1].transpose(), delta) * sp
            temp_biases[-i] = delta
            temp_weights[-i] = np.dot(delta, activations[-i-1].transpose())
        return (temp_biases, temp_weights)

    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feedforward(x)), y) for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        return (output_activations-y)

#### Miscellaneous functions
def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))

import mnist_loader
training_data, validation_data, test_data = \
    mnist_loader.load_data_wrapper()
net = Network([784, 100, 10])
net.SGD(training_data, 30, 20, 2.0, test_data=test_data)
