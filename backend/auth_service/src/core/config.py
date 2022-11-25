import os

from pydantic import BaseSettings, Field


class Config(BaseSettings):
    project_name: str = Field(env='PROJECT_NAME', default='auth')

    redis_host: str = Field(env='REDIS_HOST', default='redis_auth')
    redis_port: int = Field(env='REDIS_PORT', default=6379)

    postrges_user: str = Field(env='POSTGRES_USER', default='user')
    postrges_pass: str = Field(env='POSTGRES_PASS', default='pass')
    postrges_db: str = Field(env='POSTGRES_DATABASE', default='db')
    postrges_host: str = Field(env='POSTGRES_HOST', default='localhost')

    jwt_algorithm: str = Field(env='JWT_ALGORITHM', default='HS256')
    jwt_access_expire: int = Field(env="JWT_ACCESS_EXPIRE", default=600)
    jwt_expire: int = Field(env="JWT_EXPIRE", default=6000)

    salt: str = Field(env='SALT', default='salt')

    secret_key: str = Field(env='SECRET_KEY', default='secret_key')
    limit_requests: int = Field(env="LIMIT_REQUESTS", default=100)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = Config()
