import tensorflow as tf

a = tf.constant(5.0)
b = tf.constant(6.0)
c = a * b

# Evaluate the tensor `c`.
tf.print(c)
