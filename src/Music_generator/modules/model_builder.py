# Tensorflow config:
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['NUMEXPR_MAX_THREADS'] = '8'

from music_generator.constants import *
import music_generator.constants
from music_generator import logger
from music_generator import utilities
import tensorflow as tf
from keras.models import Sequential, load_model
from music_generator.utilities import store_value
from keras.layers import LSTM, Dropout, TimeDistributed, Dense, Activation, Embedding


class RNN_model:
    def __init__(self):
        pass

    def build_model(batch_size, seq_len, vocab_size):
        model = Sequential()
        model.add(Embedding(vocab_size, 512, batch_input_shape=(batch_size, seq_len)))
        model.add(LSTM(256, return_sequences=True, stateful=True))
        model.add(Dropout(0.2))
        model.add(LSTM(256, return_sequences=True, stateful=True))
        model.add(Dropout(0.2))
        model.add(LSTM(256, return_sequences=True, stateful=True))
        model.add(Dropout(0.2))
        model.add(TimeDistributed(Dense(vocab_size)))
        model.add(Activation('softmax'))
        return model
    
    def build_generator_model(vocab_size):
        model = Sequential()
        model.add(Embedding(vocab_size, 512, batch_input_shape=(1,1)))
        model.add(LSTM(256, return_sequences=True, stateful=True))
        model.add(Dropout(0.2))
        model.add(LSTM(256, return_sequences=True, stateful=True))
        model.add(Dropout(0.2))
        model.add(LSTM(256, return_sequences=False, stateful=True))
        model.add(Dropout(0.2))
        model.add(Dense(vocab_size))
        model.add(Activation('softmax'))
        return model
    
    # Driver Code
    def model_driver():
        logger.info("<<<<<<<<<<<<<< Initialised >>>>>>>>>>>>>>>>")
        vocab_size = utilities.load_value('vocab_size')
        model = RNN_model.build_model(BATCH_SIZE, SEQ_LENGTH, vocab_size)
        music_generator.constants.MODEL = model
        model.summary()
        store_value("model", model)
        logger.info("<<<<<<<<<<<<<< Completed >>>>>>>>>>>>>>>>")