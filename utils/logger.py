"""
Application Logger
"""

import os

from loguru import logger

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

os.makedirs(LOG_DIR, exist_ok=True)

logger.remove()

logger.add(
    LOG_FILE,
    rotation="5 MB",
    retention="10 days",
    level="INFO",
    enqueue=True,
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level:<8} | "
        "{name}:{function}:{line} | "
        "{message}"
    ),
)

logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
    format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | {message}",
)


def get_logger():
    """
    Returns the configured application logger.
    """
    return logger