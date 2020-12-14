import tensorflow as tf
from matplotlib import pyplot as plt

# get mnist handwritten dataset from keras datasets
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# show the first element of training
example_image = (x_train[0])
plt.imshow(example_image)
plt.show()

# show to first element of test
example_image_value = y_train[0]
print(example_image_value)

# number of nodes in hidden layers
n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10
batch_size = 100

# we got 28w 28h pixels so total 784 pixels
# these 784 pixels are our input
x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float')


