# -*- coding: utf-8 -*-
"""digit_recong.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W67TzDe_yc-0AuOwBRM_9RbB_4KQApMP

Import the library and dataset
"""

import tensorflow as tf
import matplotlib.pyplot as plt
mnist=tf.keras.datasets.mnist

"""Divide the the dataset into training and test dataset"""

(X_train, y_train), (X_test, y_test)=mnist.load_data()

"""Normalize"""

X_train=tf.keras.utils.normalize(X_train, axis=1)
X_test=tf.keras.utils.normalize(X_test, axis=1)

"""Initailising the CNN"""

cnn=tf.keras.models.Sequential()

"""Convolution"""

cnn.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', input_shape=[28, 28,1]))

"""Pooling"""

cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

"""Add second convolution layer"""

cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

"""Flattening"""

cnn.add(tf.keras.layers.Flatten())

"""Full Connection"""

cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))

"""Output layer"""

cnn.add(tf.keras.layers.Dense(units=10, activation='softmax'))

"""Training the CNN"""

cnn.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

"""Training the CNN on the Training set and evaluating it on the Test set"""

cnn.fit(X_train, y_train, epochs = 3)

val_loss, val_acc=cnn.evaluate(X_test, y_test)

predictions=cnn.predict(X_test)

import numpy as np
print(np.argmax(predictions[0]))

plt.imshow(X_test[0], cmap=plt.cm.binary)
plt.show

print(np.argmax(predictions[1]))
plt.imshow(X_test[1], cmap=plt.cm.binary)
plt.show