import logging

import loggerTest

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.info('from main')
