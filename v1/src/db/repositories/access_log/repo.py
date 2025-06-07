from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.access_log.abs_repo import AbsAccessLogRepo
from v1.src.db.models.access_log_orm import AccessLogOrm
from v1.src.app.dto.access_log import AccessLogDTO


class AccessLogRepo(AbsAccessLogRepo):
    @classmethod
    async def create_access_log(cls, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(AccessLogOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(AccessLogDTO, orm)

    @classmethod
    async def get_access_log(cls, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(AccessLogOrm).where(AccessLogOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(AccessLogDTO, orm) if orm else None

    @classmethod
    async def update_access_log(cls, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(AccessLogOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(AccessLogDTO, orm)

    @classmethod
    async def delete_access_log(cls, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(AccessLogOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(AccessLogDTO, orm)
