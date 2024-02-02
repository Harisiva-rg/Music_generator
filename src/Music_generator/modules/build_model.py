# Tensorflow config:
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['NUMEXPR_MAX_THREADS'] = '8'

from music_generator.constants import *
from music_generator import logger
import tensorflow as tf
from keras.models import Sequential, load_model
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
    
    # Driver Code
    def model_driver():
        logger.info("<<<<<<<<<<<<<< Initialised >>>>>>>>>>>>>>>>")
        model = RNN_model.build_model(BATCH_SIZE, SEQ_LENGTH, MODEL_VOCAB_SIZE)
        model.summary()
        logger.info("<<<<<<<<<<<<<< Completed >>>>>>>>>>>>>>>>")