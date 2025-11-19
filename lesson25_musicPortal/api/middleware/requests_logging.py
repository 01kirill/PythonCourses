import logging
import time

logger = logging.getLogger('request_logger')

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        logger.info(f"Запрос: {request.method} {request.path}")
        response = self.get_response(request)
        duration = time.time() - start_time
        logger.info(f"Ответ: {request.method} {request.path} - статус {response.status_code} - время {duration:.2f} сек\n")
        return response
