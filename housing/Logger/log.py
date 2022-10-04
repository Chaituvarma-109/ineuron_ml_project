import logging
import os
from datetime import datetime

LOG_DIR = "Logs"

CURR_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

LOG_FILE_NAME = f"log_{CURR_TIME_STAMP}.log"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH, filemode="w", format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,)
