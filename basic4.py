from activation import Activation_Softmax
from activation import Activation_ReLU
from dataset import generateSpiralData
from basic2 import Layer_Dense

X, y = generateSpiralData(100,3)
dense1 = Layer_Dense(2,3)
activation1 = Activation_ReLU()

dense2 = Layer_Dense(3,3)
activation2=Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output[:5])

