# logger.py

import logging
import os


def setup_logger(name, log_file, level=logging.DEBUG):
    """Function to setup as many loggers as you want"""

    # Create logs directory if it doesn't exist
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Create file handler which logs even debug messages
    fh = logging.FileHandler(os.path.join(log_dir, log_file))
    fh.setLevel(level)
    fh.setFormatter(formatter)

    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    ch.setFormatter(formatter)

    # Create logger and add handlers
    new_logger = logging.getLogger(name)
    new_logger.setLevel(level)
    new_logger.addHandler(fh)
    new_logger.addHandler(ch)

    return new_logger


# Create a default logger
logger = setup_logger("default", "game.log")
