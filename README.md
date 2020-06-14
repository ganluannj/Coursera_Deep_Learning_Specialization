# Deep Learning Practice
### Programming assignment for Deep Learning Specialization on Coursera

### * Logistic Regression
  * Proprocessing the dataset is imporant (reshape the data so that it can fit into the model)
  * Implement each function separately: initialize(), propagate(), optimize(). Then built a model()
  * Tuning the learning rate (which is an example of a "hyperparameter") can make a big difference to the algorithm.
  
* 

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
      

