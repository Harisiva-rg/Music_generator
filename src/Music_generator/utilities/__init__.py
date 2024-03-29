import os
import pickle
from music_generator.constants import MODEL_DIR
from music_generator import logger

def train_log(epochs, loss, acc):
    # logger.info("Training Log:")
    logger.info('Epoch %d - Loss: %f - Accuracy: %f', epochs, loss, acc)


def save_weights(epoch, model):
    model.save_weights(os.path.join(MODEL_DIR, 'weights.{}.h5'.format(epoch)))


def load_weights(epoch, model):
    model.load_weights(os.path.join(MODEL_DIR, 'weights.{}.h5'.format(epoch)))


def store_value(variable_name, value):
    if os.path.exists('exports\stored_variables.pkl'):
        with open('exports\stored_variables.pkl', 'rb') as f:
            data = pickle.load(f)
    else:
        data = {}
    # Update or add the new variable and its value
    data[variable_name] = value
    with open('exports\stored_variables.pkl', 'wb') as f:
        pickle.dump(data, f)


def load_value(variable_name):
    if os.path.exists('exports\stored_variables.pkl'):
        with open('exports\stored_variables.pkl', 'rb') as f:
            data = pickle.load(f)
        return data.get(variable_name)
    else:
        return None

def store_notes(value):
    with open('exports\gen_notes.txt', 'w') as f:
        f.write(value)

def music_split(generated_notes):
    if "X:" in generated_notes:
        split_notes = generated_notes.split('X:')
        if len(split_notes) >  1:
            music_pick = split_notes[1].strip()
            music_pick = 'X:' + music_pick
            return music_pick
        else:
            return "No content found"
    else:
        return "No X in content, invalid format"