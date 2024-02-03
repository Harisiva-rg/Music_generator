from music_generator.modules.model_builder import RNN_model
from music_generator.constants import *
from music_generator import logger

STAGE_NAME = "MODEL BUILDING STAGE"

class BuildModelStage:
    def __init__(self):
        pass
    def main(self):
        RNN_model.model_driver()

if __name__ == '__main__':
    logger.info(f"========== {STAGE_NAME} STARTED ==========")
    obj = BuildModelStage()
    obj.main()
    logger.info(f"========== {STAGE_NAME} COMPLETED ==========")
