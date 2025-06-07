from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.fuel_type.abs_repo import AbsFuelTypeRepo
from v1.src.db.models.fuel_type_orm import FuelTypeOrm
from v1.src.app.dto.fuel_type import FuelTypeDTO


class FuelTypeRepo(AbsFuelTypeRepo):
    @classmethod
    async def create_fuel_type(cls, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(FuelTypeOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(FuelTypeDTO, orm)

    @classmethod
    async def get_fuel_type(cls, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(FuelTypeOrm).where(FuelTypeOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(FuelTypeDTO, orm) if orm else None

    @classmethod
    async def update_fuel_type(cls, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(FuelTypeOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(FuelTypeDTO, orm)

    @classmethod
    async def delete_fuel_type(cls, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(FuelTypeOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(FuelTypeDTO, orm)
