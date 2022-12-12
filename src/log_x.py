from sys import stdout
from config import settings
from logging import Formatter, StreamHandler, getLogger, DEBUG, ERROR


def formatter(format: str = settings.LOG_FORMAT):
    return Formatter(format)


def console_handler():
    tmp_handler = StreamHandler(stdout)
    tmp_handler.setFormatter(formatter())
    return tmp_handler


def log_arbiter(logger_name: str = ''):
    tmp_logger = getLogger(logger_name)
    tmp_logger.setLevel(
        DEBUG) if settings.DEBUG else tmp_logger.setLevel(ERROR)
    tmp_logger.addHandler(console_handler())
    tmp_logger.propagate = False
    return tmp_logger
