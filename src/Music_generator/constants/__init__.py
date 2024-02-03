#Dependencies
# import os
# import sys
# import logging
# import json
# import numpy as np
# from collections import Counter
# import matplotlib.pyplot as plt
# from music_generator import logger
# from keras.models import Sequential, load_model
# from keras.layers import LSTM, Dropout, TimeDistributed, Dense, Activation, Embedding

# Directories
LOG_DIR = 'logs'
DATA_DIR = 'data'
MODEL_DIR = 'models'
EXPORT_DIR = 'exports'
DATA_FILE = 'data\\raw\\Music_Input_Notts.txt'
OUT_FILE = 'exports\\gen_out.abc'
TRAINED_MODEL = 'models\weights.100.h5'
CONVERTED_FILE = 'exports\char_to_idx.json'

#Hyperparameters
BATCH_SIZE = 16
SEQ_LENGTH = 64
MODEL_VOCAB_SIZE = 50
EPOCHS = 5


# Runtime Variables
TEXT = open(DATA_FILE).read()
SAVE_FREQ = 10
SEED = 29
NUM_CHARS = 512