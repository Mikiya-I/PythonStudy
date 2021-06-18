import logging


formatter = '%(asctime)s:%(levelname)s:%(message)s'
logging.basicConfig(filename='test.log', level=logging.INFO, format=formatter)

logging.critical('critical')
logging.warning('warning')
logging.error('error')
logging.info('info')
logging.debug('debug')

logging.info('info %s %s', 'test', 'test2')
