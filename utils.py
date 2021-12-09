from typing import Optional
import os
import redis


def get_env_key(key) -> Optional[str]:
	return os.environ[key] if key in os.environ else None

cache = redis.from_url(get_env_key("REDIS_URL"), decode_responses=True)

def set_cache(key, value):
	cache.set(key, value)

def get_cache(key) -> Optional[str]:
	return cache.get(key) if cache.exists(key) else None
	