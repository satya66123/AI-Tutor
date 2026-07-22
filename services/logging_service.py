"""
Logging Service
"""

import logging


class LoggingService:

    logger = logging.getLogger("EnterpriseRAG")

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        handler = logging.FileHandler("logs/rag.log")

        formatter = logging.Formatter(

            "%(asctime)s | %(levelname)s | %(message)s"

        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)

    @classmethod
    def info(cls, message):

        cls.logger.info(message)

    @classmethod
    def error(cls, message):

        cls.logger.error(message)