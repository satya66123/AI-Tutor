from utils.logger import get_logger

logger = get_logger()


def test_logger():
    logger.info("Application started.")
    logger.warning("This is a warning.")
    logger.error("This is an error.")
    logger.success("Logger is working successfully!")


if __name__ == "__main__":
    test_logger()