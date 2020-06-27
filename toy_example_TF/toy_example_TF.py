#%%
import numpy as np
import tensorflow as tf

#%%
# =============================================================================
# Without trianing data, the cost is a fix function
# =============================================================================
# optimize the cost function 
# J = w^2 -10*w + 25
w=tf.Variable(0, dtype=tf.float32)
#cost = tf.add(tf.add(w**2, tf.multiply(-10., w)), 25)
# another way to write the cost, we can use the common way
cost = w**2 - 10*w + 25
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

#%%
init = tf.global_variables_initializer()
session = tf.Session()
session.run(init)
print(session.run(w)) 
# this printout 0, since we have not done anything yet

#%%
# here we run one step of gradient descent
session.run(train)
print(session.run(w))

#%%
# run 1000 gradient descent
for _ in range(1000):
    session.run(train)
print(session.run(w))

# =============================================================================
# consider we need to implement a training data x
# =============================================================================
#%%
coefficients = np.array([[1.0], [-20.0], [100.0]])
w=tf.Variable(0, dtype=tf.float32)
x=tf.placeholder(dtype=tf.float32, shape=[3,1])
cost = x[0][0]*w**2 + x[1][0]*w + x[2][0]
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
#%%
init = tf.global_variables_initializer()
session = tf.Session()
session.run(init)
print(session.run(w)) 

#%%
# here we run one step of gradient descent
session.run(train, feed_dict={x:coefficients})
print(session.run(w))

#%%
# run 1000 gradient descent
for _ in range(1000):
    session.run(train, feed_dict={x:coefficients})
print(session.run(w))

