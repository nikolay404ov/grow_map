from sqlalchemy import create_engine, MetaData
from core.config import config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (
    f"postgresql://{config.db_user}:{config.db_pass}@{config.db_host}:{config.db_port}/{config.db_name}"
)


engine = create_engine(
    DATABASE_URL
)
Base = declarative_base(metadata=MetaData(schema="grow_map"))
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


def get_session():
    db = session()
    try:
        yield db
    finally:
        db.close()
