#!/usr/bin/env python3
"""Cache class"""

import redis
import uuid


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
