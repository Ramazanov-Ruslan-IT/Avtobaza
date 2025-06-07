from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from v1.src.config import config
from v1.src.db.models.base_orm import BaseOrm

_engine = None
_new_postgresql_session = None


def get_engine():
    global _engine
    if _engine is None:
        _engine = create_async_engine(
            config.POSTGRESQL_DB_URL,
            future=True,
            pool_recycle=300,
            pool_pre_ping=True,
        )
    return _engine


def get_sessionmaker():
    global _new_postgresql_session
    if _new_postgresql_session is None:
        _new_postgresql_session = async_sessionmaker(
            get_engine(),
            expire_on_commit=False,
        )
    return _new_postgresql_session


async def create_tables():
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(BaseOrm.metadata.create_all)


async def delete_tables():
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(BaseOrm.metadata.drop_all)
