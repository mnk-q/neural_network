import numpy as np
import matplotlib.pyplot as plt
#from dataset import generateSpiralData
ips = [[1,2,3,2.5], [2.0,5.0,-1.0, 2.0], [-1.5,2.7,3.3,-0.8]]

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0,inputs)
class Activation_Sigmoid:
    def forward(self, inputs):
        self.output = 1/(1 + np.exp(-inputs)) 
class Activation_LinearStep:    
    def forward(self,inputs):
        self.output = np.piecewise(inputs, [inputs < 0, inputs >= 0], [0, 1])
class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs -np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities
'''X, y = generateSpiralData(100,3)
active = Activation()
active.reLU(X)
print(active.output)'''

