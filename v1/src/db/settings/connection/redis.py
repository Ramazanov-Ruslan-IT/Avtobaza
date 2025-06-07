from v1.src.config import config


new_redis_session = redis.from_url(
    config.REDIS_DB_URL,
    encoding="utf-8",
    decode_responses=True,
)
