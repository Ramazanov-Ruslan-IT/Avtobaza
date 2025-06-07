from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.gas_station_fuel.abs_repo import AbsGasStationFuelRepo
from v1.src.db.models.gas_station_fuel_orm import GasStationFuelOrm
from v1.src.app.dto.gas_station_fuel import GasStationFuelDTO


class GasStationFuelRepo(AbsGasStationFuelRepo):
    @classmethod
    async def create_gas_station_fuel(cls, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(GasStationFuelOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(GasStationFuelDTO, orm)

    @classmethod
    async def get_gas_station_fuel(cls, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(GasStationFuelOrm).where(GasStationFuelOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(GasStationFuelDTO, orm) if orm else None

    @classmethod
    async def update_gas_station_fuel(cls, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(GasStationFuelOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(GasStationFuelDTO, orm)

    @classmethod
    async def delete_gas_station_fuel(cls, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(GasStationFuelOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(GasStationFuelDTO, orm)
