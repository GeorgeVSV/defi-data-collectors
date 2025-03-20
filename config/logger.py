import logging
import os
import time

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("collectorLogger")

if not logger.hasHandlers():
    logger.setLevel(logging.INFO)

    # Ensure UTC time is used in logs
    class UTCFormatter(logging.Formatter):
        converter = time.gmtime  # Forces all log timestamps to use UTC

    formatter = UTCFormatter("%(asctime)s - %(levelname)s - %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(os.path.join(LOG_DIR, "collector.log"))
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

def get_logger():
    return logger
