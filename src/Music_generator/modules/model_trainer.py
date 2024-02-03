from music_generator.constants import *
from music_generator import logger
from music_generator.modules.data_preprocessing import DataPreprocessing
from music_generator.modules.model_builder import RNN_model
from music_generator import utilities
import numpy as np

class ModelTrainer:
    def __init__(self):
        pass

    def train(model, np_text, vocab_size, epochs = 100, save_freq = 10):
        print("savefreq", epochs, save_freq)
        obj_1 = DataPreprocessing()

        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        steps_per_epoch = (len(TEXT) / BATCH_SIZE - 1) / SEQ_LENGTH

        for epoch in range(epochs):
            print('\nEpoch {}/{}'.format(epoch + 1, epochs))
            losses, accs = [], []
            for i, (X, Y) in enumerate(obj_1.read_batches(np_text, vocab_size)):
                # print(X)
                loss, acc = model.train_on_batch(X, Y)
                print('Batch {}: loss = {}, acc = {}'.format(i + 1, loss, acc))
                losses.append(loss)
                accs.append(acc)

            logger.info(np.average(losses), np.average(accs))

            if (epoch + 1) % save_freq == 0:
                utilities.save_weights(epoch + 1, model)
                print('Saved checkpoint to', 'weights.{}.h5'.format(epoch + 1))

    # Driver code
    def trainer_driver():
        logger.info("<<<<<<<<<<<<<< Initialised >>>>>>>>>>>>>>>>")
        model = utilities.load_value('model')
        np_text = utilities.load_value('np_text')
        vocab_size = utilities.load_value('vocab_size')
        ModelTrainer.train(model, np_text, vocab_size, EPOCHS, SAVE_FREQ)
        logger.info("<<<<<<<<<<<<<< Completed >>>>>>>>>>>>>>>>")

