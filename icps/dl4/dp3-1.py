#
#   simple_ae.py
#
#   Autoencoder tutorial code
#
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import ssl
import matplotlib as mpl

#mpl.use('Agg')
import matplotlib.pyplot as plt
import tensorflow as tf


from tensorflow.examples.tutorials.mnist import input_data

context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Variables
x = tf.placeholder("float", [None, 784])
y_ = tf.placeholder("float", [None, 10])

w_enc = tf.Variable(tf.random_normal([784, 625], mean=0.0, stddev=0.05))
w_dec = tf.Variable(tf.random_normal([625, 784], mean=0.0, stddev=0.05))

b_enc = tf.Variable(tf.zeros([625]))
b_dec = tf.Variable(tf.zeros([784]))


# Create the model
def model(X, w_e, b_e, w_d, b_d):
    encoded = tf.sigmoid(tf.matmul(X, w_e) + b_e)
    decoded = tf.sigmoid(tf.matmul(encoded, w_d) + b_d)

    return encoded, decoded


encoded, decoded = model(x, w_enc, b_enc, w_dec, b_dec)

# Cost Function basic term
cross_entropy = -1. * x * tf.log(decoded) - (1. - x) * tf.log(1. - decoded)
loss = tf.reduce_mean(cross_entropy)


#train_step = tf.train.AdagradOptimizer(0.2).minimize(loss)
#train_step = tf.train.AdagradOptimizer(0.1).minimize(loss)
# train_step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)
train_step = tf.train.GradientDescentOptimizer(0.3).minimize(loss)
# train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)
# train_step = tf.train.GradientDescentOptimizer(0.3).minimize(loss)
# train_step = tf.train.AdagradOptimizer(0.5).minimize(loss)
# train_step = tf.train.AdagradOptimizer(0.1).minimize(loss)
# train_step = tf.train.AdagradOptimizer(0.2).minimize(loss)
# train_step = tf.train.AdagradOptimizer(0.3).minimize(loss)
# train_step = tf.train.RMSPropOptimizer(0.5).minimize(loss)
# train_step = tf.train.RMSPropOptimizer(0.4).minimize(loss)
# train_step = tf.train.RMSPropOptimizer(0.3).minimize(loss)
# train_step = tf.train.RMSPropOptimizer(0.2).minimize(loss)
# train_step = tf.train.AdamOptimizer(0.5).minimize(loss)
# train_step = tf.train.AdamOptimizer(0.4).minimize(loss)
# train_step = tf.train.AdamOptimizer(0.3).minimize(loss)
#train_step = tf.train.AdamOptimizer(0.07).minimize(loss)
# Train
init = tf.initialize_all_variables()
batch_xs, batch_ys = mnist.train.next_batch(128)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    writer = tf.summary.FileWriter('./graphs1/MNIST_data', sess.graph)
    tf.summary.scalar("loss", loss)
    merged_sum_op = tf.summary.merge_all()
    summary_writer = tf.summary.FileWriter('./graphs3/MNIST_data', sess.graph)


    sess.run(init)
    print('Training...')
    for i in range(10000):
        batch_xs, batch_ys = mnist.train.next_batch(128)
        train_step.run({x: batch_xs, y_: batch_ys})
        # Run optimization op (backprop), cost op (to get loss value)
        # and summary nodes
        _, c, summary = sess.run([train_step, loss, merged_sum_op],
                                 feed_dict={x: batch_xs, y_: batch_ys})
        # Write logs at every iteration
        summary_writer.add_summary(summary,i )
        if i % 100 == 0:
            train_loss = loss.eval({x: batch_xs, y_: batch_ys})
            print('  step, loss = %6d: %6.3f' % (i, train_loss))

    # generate decoded image with test data
    test_fd = {x: mnist.test.images, y_: mnist.test.labels}
    decoded_imgs = decoded.eval(test_fd)
    print('loss (test) = ', loss.eval(test_fd))


x_test = mnist.test.images

n = 10  # how many digits we will display
plt.figure(figsize=(20, 4))
for i in range(n):
    # display original
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(x_test[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # display reconstruction
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)




plt.savefig('simple_ae.png')