from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: str = ""
    POSTGRESQL_DB_URL: str = "postgresql+asyncpg://gen_user:vvCZ//md~$;?6S@89.223.124.34:3306/default_db"
    REDIS_DB_URL: str = ""
    SECRET_KEY: str = ""
    CORE_SERVICE_SECRET_TOKEN: str = ""
    CORE_API_IP: str = ""

    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    BOT_TOKEN: str = ""

    model_config = SettingsConfigDict(env_file='.env')


config = Config()
