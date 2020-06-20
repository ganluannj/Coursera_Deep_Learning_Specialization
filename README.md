# Deep Learning Practice
### Programming assignment for Deep Learning Specialization on Coursera

### * Logistic Regression
  * Proprocessing the dataset is imporant (reshape the data so that it can fit into the model)
  * Implement each function separately: initialize(), propagate(), optimize(). Then built a model()
  * Tuning the learning rate (which is an example of a "hyperparameter") can make a big difference to the algorithm.
  
### * Shallow Neural Network for Binary Classification
  * Build a complete neural network with a hidden layer
  * Make a good use of a non-linear unit
  * Implemented forward propagation and backpropagation, and trained a neural network
  * See the impact of varying the hidden layer size, including overfitting
  
### * Deep Neural Network for Binary Classification
  * Use non-linear units like ReLU to improve your model
  * Build a deeper neural network (with more than 1 hidden layer)
  * Implement an easy-to-use neural network class
  * Apply the deep nerual network to a image classification
  
### * Initialization, Regularization, and Gradient Checking
  * Initialization: 
      * Different initialization lead to different result
      * Random initialization is used to break symmetry and make sure different hidden units can learn different things
      * Don't initialize to values that are too large
      * He initialization works well for networks with ReLU activation
  * Regularization:
      * Regularization will help you reduce overfitting
      * Regularization will drive your weights to lower values
      * L2 regularization and Dropout (Inverted Dropout implemented here) are two very effective regularization techniques. 
  * Gradient Checking
      * Gradient checking verifies closeness between the gradients from backpropagation and the numerical approximation of the gradient (computed using forward propagation).
      * Gradient checking is slow, so we don't run it in every iteration of training. You would usually run it only to make sure your code is correct, then turn it off and use backprop for the actual learning process.

* Optimization Methods
  * Mini-batch gradient descent
    * The difference between gradient descent, mini-batch gradient descent and stochastic gradient descent is the number of examples you use to perform one update step.
    * You have to tune a learning rate hyperparameter $\alpha$.
    * With a well-turned mini-batch size, usually it outperforms either gradient descent or stochastic gradient descent (particularly when the training set is large).
  * Momentum
    * Momentum takes past gradients into account to smooth out the steps of gradient descent. It can be applied with batch gradient descent, mini-batch gradient descent or stochastic gradient descent.
    * You have to tune a momentum hyperparameter  $\beta$  and a learning rate  $\alpha$.
  * Adam
    * Adam usually outperforms mini-batch gradient descent and Momentum. It converages a lot faster. 
    * It has relatively low memory requirements (though higher than gradient descent and gradient descent with momentum)
    * It usually works well even with little tuning of hyperparameters (except learning rate $\alpha$).
      

