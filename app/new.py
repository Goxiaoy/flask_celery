# -*- coding: utf-8 -*-
# 1.import
import tensorflow as tf
from sklearn import datasets
import numpy as np

def main():
    # train,test
    x_train = datasets.load_iris().data
    y_train = datasets.load_iris().target

    np.random.seed(116)
    np.random.shuffle(x_train)
    np.random.seed(116)
    np.random.shuffle(y_train)
    tf.random.set_seed(116)

    # 3.model.Sequential
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(3, activation='softmax', kernel_regularizer=tf.keras.regularizers.l2())
    ])

    # 4.model.compile
    model.compile(optimizer=tf.keras.optimizers.SGD(lr=0.1),
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                metrics=['sparse_categorical_accuracy'])

    # 5.model.fit
    model.fit(x_train, y_train, batch_size=32, epochs=500, validation_split=0.2, validation_freq=20)

    # 6.model.summary
    model.summary()
    model.save("./model/iris-model")

if __name__ == '__main__':
    main()