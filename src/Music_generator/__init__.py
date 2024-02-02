import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"runtime_logs.log")
os.makedirs(log_dir, exist_ok=True)


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