from src.utils.logger import get_logger


def main():

    logger = get_logger("test")

    logger.info("Pipeline started")
    logger.warning("This is a warning")
    logger.error("This is an error")


if __name__ == "__main__":
    main()