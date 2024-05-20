from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    database_user: str
    database_password: str
    database_host: str
    database_port: int
    database_db: str


settings = Settings()


@lru_cache
def get_settings() -> Settings:
    return Settings()
