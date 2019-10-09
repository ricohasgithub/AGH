
import numpy as np

import keras
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Convolution2D, MaxPooling2D, Dropout
from keras.layers import Flatten, Dense
from keras.optimizers import SGD, RMSprop, Adagrad, Adadelta, Adam, Adamax, Nadam

def generate_model ():

    '''
    The network accepts a 128 by 48 grayscale image as input, it should
    output a vector with 8 entries, corresponding to the isolated contour box 
    areas of the fingering (neck of guitar) and the strumming (pick of guitar)
    '''

    model = Sequential()
    model.add(Convolution2D(32,(5,5)), input_shape = (128,48,1), activation = 'relu')
    model.add(MaxPooling2D(pool_size(2, 2)))

print("Hello World!")