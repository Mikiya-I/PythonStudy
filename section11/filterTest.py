import logging

logging.basicConfig(level=logging.INFO)


class NotLoggingFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return '出力しない' not in log_message


logger = logging.getLogger(__name__)
logger.addFilter(NotLoggingFilter())
logger.info('from main')
logger.info('これを出力しない')
