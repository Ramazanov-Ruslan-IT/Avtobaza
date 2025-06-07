from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.schedule.abs_repo import AbsScheduleRepo
from v1.src.db.models.schedule_orm import ScheduleOrm
from v1.src.app.dto.schedule import ScheduleDTO


class ScheduleRepo(AbsScheduleRepo):
    @classmethod
    async def create_schedule(cls, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(ScheduleOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(ScheduleDTO, orm)

    @classmethod
    async def get_schedule(cls, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(ScheduleOrm).where(ScheduleOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(ScheduleDTO, orm) if orm else None

    @classmethod
    async def update_schedule(cls, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(ScheduleOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(ScheduleDTO, orm)

    @classmethod
    async def delete_schedule(cls, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(ScheduleOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(ScheduleDTO, orm)
