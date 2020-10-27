import os
import logging


def get_log_level():
    log_level = os.environ.get('LOG_LEVEL')
    if log_level == "DEBUG":
        return logging.DEBUG
    elif log_level == "ERROR":
        return logging.ERROR
    else:
        return logging.INFO


def get_logger():
    logger = logging.getLogger("parser-main")
    logger.setLevel(get_log_level())

    # create the logging file handler
    fh = logging.FileHandler("parser.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)
    return logger

