#!/usr/bin/env python3
"""Cache class"""

import redis
import uuid
from typing import Callable, Optional


class Cache:
    """Cache class"""

    def __init__(self) -> None:
        """initialize"""
        self._redis = redis.Redis(host='localhost', port=6379)
        self._redis.flushdb()

    def store(self, data: str) -> str | None:
        """Store"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """class get method"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)

        return data
