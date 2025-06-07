from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.scheduled_task.abs_repo import AbsScheduledTaskRepo
from v1.src.db.models.scheduled_task_orm import ScheduledTaskOrm
from v1.src.app.dto.scheduled_task import ScheduledTaskDTO


class ScheduledTaskRepo(AbsScheduledTaskRepo):
    @classmethod
    async def create_scheduled_task(cls, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(ScheduledTaskOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(ScheduledTaskDTO, orm)

    @classmethod
    async def get_scheduled_task(cls, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(ScheduledTaskOrm).where(ScheduledTaskOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(ScheduledTaskDTO, orm) if orm else None

    @classmethod
    async def update_scheduled_task(cls, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(ScheduledTaskOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(ScheduledTaskDTO, orm)

    @classmethod
    async def delete_scheduled_task(cls, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(ScheduledTaskOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(ScheduledTaskDTO, orm)
