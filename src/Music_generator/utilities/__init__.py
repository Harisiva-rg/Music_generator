import os
from music_generator.constants import MODEL_DIR
from music_generator import logger

def train_log(epochs, loss, acc):
    # logger.info("Training Log:")
    logger.info('Epoch %d - Loss: %f - Accuracy: %f', epochs, loss, acc)

def save_weights(epoch, model):
    model.save_weights(os.path.join(MODEL_DIR, 'weights.{}.h5'.format(epoch)))

def load_weights(epoch, model):
    model.load_weights(os.path.join(MODEL_DIR, 'weights.{}.h5'.format(epoch)))

