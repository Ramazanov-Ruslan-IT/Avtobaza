from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.maintenance_log.abs_repo import AbsMaintenanceLogRepo
from v1.src.db.models.maintenance_log_orm import MaintenanceLogOrm
from v1.src.app.dto.maintenance_log import MaintenanceLogDTO


class MaintenanceLogRepo(AbsMaintenanceLogRepo):
    @classmethod
    async def create_maintenance_log(cls, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(MaintenanceLogOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(MaintenanceLogDTO, orm)

    @classmethod
    async def get_maintenance_log(cls, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(MaintenanceLogOrm).where(MaintenanceLogOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(MaintenanceLogDTO, orm) if orm else None

    @classmethod
    async def update_maintenance_log(cls, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(MaintenanceLogOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(MaintenanceLogDTO, orm)

    @classmethod
    async def delete_maintenance_log(cls, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(MaintenanceLogOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(MaintenanceLogDTO, orm)
