from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.refueling_log.abs_repo import AbsRefuelingLogRepo
from v1.src.db.models.refueling_log_orm import RefuelingLogOrm
from v1.src.app.dto.refueling_log import RefuelingLogDTO


class RefuelingLogRepo(AbsRefuelingLogRepo):
    @classmethod
    async def create_refueling_log(cls, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(RefuelingLogOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(RefuelingLogDTO, orm)

    @classmethod
    async def get_refueling_log(cls, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(RefuelingLogOrm).where(RefuelingLogOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(RefuelingLogDTO, orm) if orm else None

    @classmethod
    async def update_refueling_log(cls, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(RefuelingLogOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(RefuelingLogDTO, orm)

    @classmethod
    async def delete_refueling_log(cls, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(RefuelingLogOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(RefuelingLogDTO, orm)
