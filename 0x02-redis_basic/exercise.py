#!/usr/bin/env python3
""" Cache class  """
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count calls decorator """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Call history decorator """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{method.__qualname__}:outputs", str(output))
        return output
    return wrapper


class Cache:
    """ Cache class """
    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis """
        key = str(uuid.uuid4())
        self._redis.mset(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float]:
        """ Get data from redis """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """ Convert bytes to str """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Convert bytes to int """
        return int.from_bytes(data, byteorder='big')

    def get_str_upper(self, data: bytes) -> str:
        """ Convert bytes to str and return it in uppercase """
        return data.decode('utf-8').upper()

    def __call__(self, fn: Callable):
        """ Call instance """
        @wraps(fn)
        def wrapper(*args, **kwargs):
            key = str(uuid.uuid4())
            data = self._redis.get(key)
            if data:
                return data
            data = fn(*args, **kwargs)
            self._redis.set(key, data)
            return data
        return wrapper
