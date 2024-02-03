from music_generator.constants import *
from music_generator import logger
from music_generator.pipeline.stage01_datapreprocessing import DataPreprocessingStage
from music_generator.pipeline.stage02_buildmodel import BuildModelStage
from music_generator.pipeline.stage03_trainmodel import TrainModelStage
from music_generator.pipeline.stage04_generatenotes import NotesGenerationStage

STAGE_NAME = "DATA PREPROCESSING STAGE"

logger.info(f"========== {STAGE_NAME} STARTED ==========")
obj = DataPreprocessingStage()
obj.main()
logger.info(f"========== {STAGE_NAME} COMPLETED ==========\n")


STAGE_NAME = "MODEL BUILDING STAGE"

logger.info(f"========== {STAGE_NAME} STARTED ==========")
obj = BuildModelStage()
obj.main()
logger.info(f"========== {STAGE_NAME} COMPLETED ==========\n")


STAGE_NAME = "MODEL TRAINING STAGE"

logger.info(f"========== {STAGE_NAME} STARTED ==========")
obj = TrainModelStage()
obj.main()
logger.info(f"========== {STAGE_NAME} COMPLETED ==========\n")

STAGE_NAME = "NOTES GENERATION STAGE"

logger.info(f"========== {STAGE_NAME} STARTED ==========")
obj = NotesGenerationStage()
obj.main()
logger.info(f"========== {STAGE_NAME} COMPLETED ==========\n")