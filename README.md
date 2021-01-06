# neural_network
 Building my own neural network
This is a demo of building a neural Net from scratch
By Scratch, I mean understanding how the neural nets actually work, what is the mathematics behind this.

Just like in linear regression, where we fit a line onto a data using
 <b> y = theta0 + theta1x, </b>
 and we fit the thetas using cost function and gradient Descent, A neuron's working is more or less like this.
 Every Neuron, which is getting some input from other neurons, has weight and bias, calculated as
 input*weight + bias = output.

 and the whole play of training neural network goes out to find the perfect weights and biases using
 stochastic gradient descent (Normal gradient descent, but drunk.). That's just it.

Another concept is called activation of neuron
 that means we apply a function on it, like
 <ul>
 <li>Sigmoid</li>
 <li>ReLU</li>
 <li>Linear and</li>
 <li>Softmax.</li> </ul>
 These functions determine whether a neuron is firing or not.
 
 <h4> Sigmoid</h4> : This function is pretty basic, it produces the value beteen 0 and 1. 
