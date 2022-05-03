import logging
import sys

import utils.config


def setup():
    config = utils.config.load()  # Load our config.yaml

    # Configure logging format
    format = logging.Formatter(
        fmt="[%(asctime)s] %(levelname)s (%(module)s): %(message)s",
        datefmt="%m-%d-%Y %H:%M:%S",
    )

    file_handler = logging.FileHandler(
        f'./{config["log_file"]}.log', encoding="utf-8", mode="w"
    )  # save to file
    file_handler.setFormatter(format)  # Configure the handler

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(format)

    logger = logging.getLogger(config["log_file"])
    logger.setLevel(logging.DEBUG)  # default log level
    logger.addHandler(file_handler)  # save logs to file
    logger.addHandler(stream_handler)  # also output to console

    return logger


def get():
    config = utils.config.load()
    logger = logging.getLogger(config["log_file"])
    return logger
