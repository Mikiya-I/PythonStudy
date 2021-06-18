import logging

logger = logging.getLogger(__name__)

logger.error({
    'action': 'create',
    'status': 'fail',
    'message': 'Api call is failed'
})
