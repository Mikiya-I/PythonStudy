import logging.config
import configparser

logging.config.fileConfig('logging.ini')
# dict型で設定することもできる
# logging.config.dictConfig({
#
# })
logger = logging.getLogger('simpleExample')

logger.critical('critical')
logger.warning('warning')
logger.error('error')
logger.info('info')
logger.debug('debug')
