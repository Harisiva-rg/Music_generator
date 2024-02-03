import os
import json
import numpy as np
# from collections import Counter
import matplotlib.pyplot as plt
from music_generator.constants import *
# import music_generator.constants
from music_generator.utilities import store_value

from music_generator import logger


class DataPreprocessing:
    def __init__(self):
        pass

    def precheck(text):
        logger.info("Started >> precheck")
        characters = list(text)

        # Visualize the frequency distribution of characters
        # Placeholder

        # Calculate and print the length of each sequence
        sequences = text.split("\n\n") # Assuming "\n\n" separates your sequences
        print("The training data contains {} sequences".format(len(sequences)))
        # sequence_lengths = [len(seq) for seq in sequences]

        # # Print the sequence lengths
        # for i, length in enumerate(sequence_lengths):
        #     print(f"Sequence {i+1} length: {length}")
        
        logger.info("Completed >> precheck")


    def char_to_idx_mapper(text):
        logger.info("Started >> char_to_idx_mapper")

        # character to index and vice-versa mappings
        char_to_idx = { ch: i for (i, ch) in enumerate(sorted(list(set(text)))) }
        print("Number of unique characters: " + str(len(char_to_idx))) #86

        with open(os.path.join(EXPORT_DIR, 'char_to_idx.json'), 'w') as f:
            json.dump(char_to_idx, f)

        np_text = np.asarray([char_to_idx[c] for c in text], dtype=np.int32) 
        # idx_to_char = { i: ch for (ch, i) in char_to_idx.items() }
        vocab_size = len(char_to_idx)
        logger.info("Completed >> char_to_idx_mapper")
        return vocab_size, np_text

    def read_batches(self, T, vocab_size):
        logger.info("Started >> read_batches")

        length = T.shape[0]
        print(length)
        batch_chars = int(length / BATCH_SIZE)

        for start in range(0, batch_chars - SEQ_LENGTH, SEQ_LENGTH):
            X = np.zeros((BATCH_SIZE, SEQ_LENGTH)) # 16X64
            Y = np.zeros((BATCH_SIZE, SEQ_LENGTH, vocab_size)) # 16X64X86
            for batch_idx in range(0, BATCH_SIZE): # (0,16)
                for i in range(0, SEQ_LENGTH): #(0,64)
                    X[batch_idx, i] = T[batch_chars * batch_idx + start + i] #
                    Y[batch_idx, i, T[batch_chars * batch_idx + start + i + 1]] = 1
            yield X, Y
        logger.info("Completed >> read_batches")


    # Driver Code
    def datapreprocessing_driver():
        logger.info("<<<<<<<<<<<<<< Initialised >>>>>>>>>>>>>>>>")
        DataPreprocessing.precheck(TEXT)
        vocab_size, np_text = DataPreprocessing.char_to_idx_mapper(TEXT)
        store_value("np_text", np_text)
        store_value("vocab_size", vocab_size)
        # read_batches(np_text, vocab_size)
        logger.info("<<<<<<<<<<<<<< Completed >>>>>>>>>>>>>>>>")