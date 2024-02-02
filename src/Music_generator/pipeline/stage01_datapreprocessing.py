from music_generator.modules.data_preprocessing import DataPreprocessing
from music_generator.constants import *
from music_generator import logger

STAGE_NAME = "DATA PREPROCESSING STAGE"

class DataPreprocessingStage:
    def __init__(self):
        pass
    def main(self):
        DataPreprocessing.datapreprocessing_driver()


if __name__ == '__main__':
    logger.info(f"========== {STAGE_NAME} STARTED ==========")
    obj = DataPreprocessingStage()
    obj.main()
    logger.info(f"========== {STAGE_NAME} COMPLETED ==========")


