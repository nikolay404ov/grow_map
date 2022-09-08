import os
from logging import config as logging_config

from core.logger import LOGGING
from pydantic import BaseSettings, Field

logging_config.dictConfig(LOGGING)


class Config(BaseSettings):
    project_name: str = Field(env="PROJECT_NAME", default="card_service")
    db_user: str = Field(env="POSTGRES_USER", default="user")
    db_pass: str = Field(env="POSTGRES_PASSWORD", default="pass")
    db_host: str = Field(env="POSTGRES_HOST", default="postgres")
    db_port: int = Field(env="POSTGRES_PORT", default=5432)
    db_name: str = Field(env="POSTGRES_DB", default="db")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = Config()
