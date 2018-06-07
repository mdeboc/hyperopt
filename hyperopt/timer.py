# -*- coding: utf-8 -*-
import logging
from functools import wraps
from time import time

logger = logging.getLogger(__name__)

class Timer(object):

    @staticmethod
    def time_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            ts = time()
            result = function(*args, **kwargs)
            te = time()
            logger.info('[TIMING] {0}() function time: {1}'.format(
                function.__name__, te - ts))
            return result
        return wrapper

