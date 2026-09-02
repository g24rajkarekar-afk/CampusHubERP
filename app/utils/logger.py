import logging
import os


# Create logs folder if it does not exist
os.makedirs("logs", exist_ok=True)


# Create logger
logger = logging.getLogger("CampusHubERP")
logger.setLevel(logging.INFO)


# Prevent duplicate handlers
if not logger.handlers:

    # Store logs in logs/application.log
    file_handler = logging.FileHandler(
        "logs/application.log"
    )

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


def log_info(message):
    logger.info(message)


def log_error(message):
    logger.error(message)