import numpy as np
from basic2 import Layer_Dense
from dataset import generateSpiralData
from activation import Activation_ReLU
np.random.seed(0)
x = [[1,2,3,2.5], [2.0,5.0,-1.0, 2.0], [-1.5,2.7,3.3,-0.8]]
X, y = generateSpiralData(100,3)

layer1 = Layer_Dense(2,5)
activate = Activation_ReLU()
layer1.forward(X)
activate.forward(layer1.output)
print(activate.output)

