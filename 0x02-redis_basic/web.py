#!/usr/bin/env python3
"""" Expiring web cache and tracker """
from functools import wraps
import redis
import requests
from typing import Callable

redis = redis.Redis()
def request_counter(method: Callable) -> Callable:
    """ Count request decorator """
    @wraps(method)
    def wrapper(url: str) -> str:
        """ Wrapper function """
        redis.incr(f"count:{url}")
        response = redis.get(f"cached:{url}")
        if response:
            return response.decode('utf-8')
        result = method(url)
        redis.setex(f"cached:{url}", 10, result)
        return result
    return wrapper


@request_counter
def  get_page(url: str) -> str:
    """ Get page """
    return requests.get(url).text
