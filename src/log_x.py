import sys
# from settings import LOG_FORMAT, LOG_FILE, LOG_DIR, MQTT_PASSWORD, MQTT_SERVER, MQTT_PORT, MQTT_CHANEL, MQTT_USERNAME, MQTT_PASSWORD, SECURED
from logging.handlers import TimedRotatingFileHandler
import logging

from omegaconf import DictConfig, OmegaConf


class log_arbiter:
    logger_name: str = ''
    formatter_str: str = ''

    def __init__(self, logger_name: str = '', cfg: DictConfig = None):
        self.formatter_str = str(OmegaConf.to_object(cfg)['app']['log_format'])
        self.logger_name = logger_name
        x = self.log_arbiter(logger_name=logger_name)

    def console_handler(self, formatter_str: str = formatter_str):
        tmp_handler = logging.StreamHandler(sys.stdout)
        tmp_handler.setFormatter(logging.Formatter(formatter_str))

    def log_arbiter(self, logger_name: str = logger_name):
        tmp_logger = logging.getLogger(logger_name)
        tmp_logger.setLevel(logging.DEBUG)
        tmp_logger.addHandler(self.console_handler())
        tmp_logger.propagate = False
        return tmp_logger
