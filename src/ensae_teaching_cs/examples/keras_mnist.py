"""
@file
@brief Taken from `mnist_cnn.py <https://github.com/fchollet/keras/blob/master/examples/mnist_cnn.py>`_

Trains a simple convnet on the MNIST dataset.

Gets to 99.25% test accuracy after 12 epochs
(there is still a lot of margin for parameter tuning).
16 seconds per epoch on a GRID K520 GPU.
"""
from pyquickhelper.loghelper import noLOG
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K

# numpy.random.seed(1337)  # for reproducibility


def keras_mnist_data():
    """
    retrieve the MNIST database for keras
    """
    # the data, shuffled and split between train and test sets
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    img_rows, img_cols = 28, 28    # should be cmputed from the data

    if K.image_dim_ordering() == 'th':
        X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols)
        X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
    else:
        X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
        X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)

    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    X_train /= 255
    X_test /= 255

    # convert class vectors to binary class matrices
    nb_classes = len(set(y_train))
    Y_train = np_utils.to_categorical(y_train, nb_classes)
    Y_test = np_utils.to_categorical(y_test, nb_classes)

    return (X_train, Y_train), (X_test, Y_test)


def keras_build_mnist_model(nb_classes, fLOG=noLOG):
    """
    build a CNN for MNIST with keras

    @param      nb_classes      number of classes
    @param      fLOG            logging function
    @return                     the model
    """
    model = Sequential()

    nb_filters = 32
    pool_size = (2, 2)
    kernel_size = (3, 3)
    img_rows, img_cols = 28, 28    # should be cmputed from the data

    fLOG("[keras_build_mnist_model] K.image_dim_ordering()={0}".format(
        K.image_dim_ordering()))
    if K.image_dim_ordering() == 'th':
        input_shape = (1, img_rows, img_cols)
    else:
        input_shape = (img_rows, img_cols, 1)

    model.add(Convolution2D(nb_filters, kernel_size[0], kernel_size[1],
                            border_mode='valid',
                            input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(Convolution2D(nb_filters, kernel_size[0], kernel_size[1]))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=pool_size))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adadelta',
                  metrics=['accuracy'])
    return model


def keras_fit(model, X_train, Y_train, X_test, Y_test, batch_size=128,
              nb_classes=None, nb_epoch=12, fLOG=noLOG):
    """
    fits a keras model

    @param      X_train     training features
    @param      Y_train     training target
    @param      X_test      test features
    @param      Y_test      test target
    @param      batch_size  batch size
    @param      nb_classes  nb_classes
    @param      nb_epoch    number of iterations
    @param      fLOG        logging function
    """
    if nb_classes is None:
        nb_classes = Y_train.shape[1]
        fLOG("[keras_fit] nb_classes=%d" % nb_classes)
    model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch,
              verbose=1, validation_data=(X_test, Y_test))


def keras_predict(model, X_test, Y_test):
    """
    prediction with a keras model

    @param      X_test      test features
    @param      Y_test      test target
    @return                 score
    """
    score = model.evaluate(X_test, Y_test, verbose=0)
    return score
