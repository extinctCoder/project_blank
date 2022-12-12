from config import settings
from log_x import log_arbiter

logger = log_arbiter(__name__)

if __name__ == '__main__':
    logger.info('hello world ... ... ... :)')
    logger.error('hello world is not working ... ... ... :)')
