import logging


def create_logger(logging_level = logging.INFO):
    logger = logging.getLogger("Alarmmonitor_logger")
    logger.setLevel(logging_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging_level)

    formatter = logging.Formatter("%(asctime)s; %(levelname)s; %(message)s", "%Y-%m-%d %H:%M:%S")

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger

logger: logging.Logger = create_logger(logging.INFO)