import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd
#define the data set of housing details
DATA_FILE = r'/Users/nlns/Downloads/DeepLearning_Lesson2/data/USA_Housing.xls'
# read in data from the .xls file
book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
#make sure that index is starting from 0
sheet = book.sheet_by_index(0)
#define an array with column values HouseAge and price from xls file
data = np.asarray([[sheet.row_values(i)[1],sheet.row_values(i)[5]] for i in range(1, sheet.nrows)])
n_samples = sheet.nrows - 1
#create placeholders for input X (House Age) and label Y (Price)

X = tf.placeholder(tf.float32, name='HouseAge')

Y = tf.placeholder(tf.float32, name='Price')

#create weight and bias, initialized to 0
w = tf.Variable(0.0, name='weights')
b = tf.Variable(0.0, name='bias')

# Step 4: build model to predict Y
Y_predicted = X * w + b

# Step 5: use the square error as the loss function
loss = tf.square(Y - Y_predicted, name='loss')

# Step 6: using gradient descent with learning rate of 0.01 to minimize loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(loss)

with tf.Session() as sess:
    # Step 7: initialize the necessary variables, in this case, w and b
    sess.run(tf.global_variables_initializer())

    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)

    # Step 8: train the model
    for i in range(50):  # train the model 50 epochs
        total_loss = 0
        for x, y in data:
            # Session runs train_op and fetch values of loss
            _, l = sess.run([optimizer, loss], feed_dict={X: x, Y: y})
            total_loss += l
        print('Epoch {0}: {1}'.format(i, total_loss / n_samples))

    # close the writer when you're done using it
    writer.close()

    # Step 9: output the values of w and b
    w, b = sess.run([w, b])

# plot the results
X, Y = data.T[0], data.T[1]
plt.plot(X, Y, 'bo', label='Real data')
plt.plot(X, X * w + b, 'r', label='Predicted data')
plt.legend()
plt.show()


#----------------------------------------
data1 = np.asarray([[sheet.row_values(i)[2],sheet.row_values(i)[5]] for i in range(1, sheet.nrows)])
n_samples = sheet.nrows - 1
# Step 2: create placeholders for input X Numberofrooms and label Y Price

A = tf.placeholder(tf.float32, name='NumberofRooms')

B = tf.placeholder(tf.float32, name='Price')

# Step 3: create weight and bias, initialized to 0
w = tf.Variable(0.0, name='weights')
b = tf.Variable(0.0, name='bias')

# Step 4: build model to predict Y
Y_predicted = A * w + b

# Step 5: use the square error as the loss function
loss = tf.square(B - Y_predicted, name='loss')

# Step 6: using gradient descent with learning rate of 0.01 to minimize loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(loss)


with tf.Session() as sess:
    # Step 7: initialize the necessary variables, in this case, w and b
    sess.run(tf.global_variables_initializer())

    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)

    # Step 8: train the model
    for i in range(50):  # train the model 50 epochs
        total_loss = 0
        for x, y in data1:
            # Session runs train_op and fetch values of loss
            _, l = sess.run([optimizer, loss], feed_dict={A: x, B: y})
            total_loss += l
        print('Epoch {0}: {1}'.format(i, total_loss / n_samples))

    # close the writer when you're done using it
    writer.close()

    # Step 9: output the values of w and b
    w, b = sess.run([w, b])


A, B = data1.T[0], data1.T[1]
plt.plot(A, B, 'bo', label='Real data')
plt.plot(A, A * w + b, 'r', label='Predicted data')
plt.legend()
plt.show()