from music_generator.modules.model_trainer import ModelTrainer
from music_generator.constants import *
from music_generator import logger

STAGE_NAME = "MODEL TRAINING STAGE"

class TrainModelStage:
    def __init__(self):
        pass
    def main(self):
        ModelTrainer.trainer_driver()

if __name__ == '__main__':
    logger.info(f"========== {STAGE_NAME} STARTED ==========")
    obj = TrainModelStage()
    obj.main()
    logger.info(f"========== {STAGE_NAME} COMPLETED ==========")
