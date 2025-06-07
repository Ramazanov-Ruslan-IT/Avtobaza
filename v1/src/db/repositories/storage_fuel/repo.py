from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.storage_fuel.abs_repo import AbsStorageFuelRepo
from v1.src.db.models.storage_fuel_orm import StorageFuelOrm
from v1.src.app.dto.storage_fuel import StorageFuelDTO


class StorageFuelRepo(AbsStorageFuelRepo):
    @classmethod
    async def create_storage_fuel(cls, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(StorageFuelOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(StorageFuelDTO, orm)

    @classmethod
    async def get_storage_fuel(cls, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(StorageFuelOrm).where(StorageFuelOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(StorageFuelDTO, orm) if orm else None

    @classmethod
    async def update_storage_fuel(cls, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(StorageFuelOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(StorageFuelDTO, orm)

    @classmethod
    async def delete_storage_fuel(cls, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(StorageFuelOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(StorageFuelDTO, orm)
