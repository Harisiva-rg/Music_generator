from music_generator.constants import *
from music_generator import logger
import json
import numpy as np
from music_generator.utilities import load_weights, store_value
from music_generator.modules.model_builder import RNN_model
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dropout, TimeDistributed, Dense, Activation, Embedding


class NotesGenerator:
    def __init__(self):
        pass

    def sample(epoch, header, num_chars):
        with open(CONVERTED_FILE) as f:
            char_to_idx = json.load(f)
        idx_to_char = { i: ch for (ch, i) in char_to_idx.items() }
        vocab_size = len(char_to_idx)

        model = RNN_model.build_generator_model(vocab_size)
        load_weights(epoch,model)
    #     model.save(os.path.join(MODEL_DIR, 'model.{}.h5'.format(epoch)))

    #     sampled = [char_to_idx[c] for c in header]
    #     print(sampled)
        sampled = []

        for i in range(num_chars):
            batch = np.zeros((1, 1))
            if sampled:
                batch[0, 0] = sampled[-1]
            else:
                batch[0, 0] = np.random.randint(vocab_size)
            result = model.predict_on_batch(batch).ravel()
            # print(result)
            sample = np.random.choice(range(vocab_size), p=result)
            sampled.append(sample)

        return ''.join(idx_to_char[c] for c in sampled)
    
    # Driver code
    def notes_driver():
        logger.info("<<<<<<<<<<<<<< Initialised >>>>>>>>>>>>>>>>")
        music_notes = NotesGenerator.sample(EPOCHS,SEED,NUM_CHARS)
        store_value("music_notes", music_notes)
        print(music_notes)
        logger.info("<<<<<<<<<<<<<< Completed >>>>>>>>>>>>>>>>")
