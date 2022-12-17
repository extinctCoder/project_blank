from config import settings
from log_x import log_arbiter
from test_one import sum, sub

logger = log_arbiter(__name__)

if __name__ == '__main__':
    '''This is the main function or the entrypoint of the project
    '''
    logger.info('Welcome to project blank ... :)')
    logger.info(sum(5.0, 4.2))
    logger.info(sub(5.0, 4.2))
