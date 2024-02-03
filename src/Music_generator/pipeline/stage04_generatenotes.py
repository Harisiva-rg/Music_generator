from music_generator.modules.notes_generator import NotesGenerator
from music_generator.constants import *
from music_generator import logger

STAGE_NAME = "NOTES GENERATION STAGE"

class NotesGenerationStage:
    def __init__(self):
        pass
    def main(self):
        NotesGenerator.notes_driver()

if __name__ == '__main__':
    logger.info(f"========== {STAGE_NAME} STARTED ==========")
    obj = NotesGenerationStage()
    obj.main()
    logger.info(f"========== {STAGE_NAME} COMPLETED ==========")
