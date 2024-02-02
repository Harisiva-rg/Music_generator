import os
import sys
import logging
from music_generator.constants import LOG_DIR

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


log_filepath = os.path.join(LOG_DIR,"runtime_logs.log")

logging.basicConfig(
    level= logging.INFO,                        # Refer documnentation for the logging levels.
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),      # To write in file
        logging.StreamHandler(sys.stdout)       # To display in the terminal
    ]
)

logger = logging.getLogger("Logger")

# logger.info("Custom logging initiated")