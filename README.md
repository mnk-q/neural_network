# Neural_Network
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
 <br>
 <h4> Linear</h4> : y = x ,it is the default one.<br> 
 <br><h4> Step </h4> : A Basic improvement over Linear. y = 1 if x > 0 else y = 0  
 <br><h4> Sigmoid</h4> : This function is pretty basic, it produces the value beteen 0 and 1. This one is old and not used because this function has some beef with gradient descent. This, and tanh both, they saturate, meaning larger values snap to 1 and smaller values snap to -1 or 0.<br>
 <img src="https://mathworld.wolfram.com/images/equations/SigmoidFunction/NumberedEquation1.gif"><br>
 <br><h4> ReLU</h4> :The function, which every basic neural net uses. Recitfier Linear unit. this one is fast, and powerful. <br> y = x if x>0 else y = 0 <br> <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2018/10/Line-Plot-of-Rectified-Linear-Activation-for-Negative-and-Positive-Inputs.png"><br>
 
 <br><h4> Hyperbolic Tangent</h4> : tanh(x). It is a non linear function. an improvement over Sigmoid. Sigmoid stays between 0 and 1, tanh stays between -1 and 1. the values, that they give, are called granular values.<br><img src="https://mathworld.wolfram.com/images/interactive/TanhReal.gif"><br>

 What comes out after activation functions of the neuron becomes an input for the next layer ones.
 
 <h4>Softmax</h4>
<br>This one is currently most used, because it gives the probabilities of all the the nodes, with sum of all probabilities being 1. This one is primarily used for Handwriting Recognition (As we will do it.), because it gives the probabilities of all digits, and we choose highest one.
<img src = 'https://www.gstatic.com/education/formulas2/-1/en/softmax_function.svg' >

<hr>
That was about the Activation function, but that was just a tip. Still, we gotta figure out how Neural Networks Learn. More Specifically, BackPropagation <br>
Here, Learning means changing their weights and biases appropriately so that It recognizes right digit every time.<br>
For that , we use something called <br>
<strong>Cost Function</strong>
The cost function is a function derived by, squaring the difference between neural network's output and correct output, adding them all, and then taking their average. Notice, that it is a function of our parameters (ie weigths and biases). There is no specific formula for this. Every Algorithm calculates Cost Function differently. 
