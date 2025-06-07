from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.vehicle.abs_repo import AbsVehicleRepo
from v1.src.db.models.vehicle_orm import VehicleOrm
from v1.src.app.dto.vehicle import VehicleDTO


class VehicleRepo(AbsVehicleRepo):
    @classmethod
    async def create_vehicle(cls, data: VehicleDTO) -> VehicleDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(VehicleOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(VehicleDTO, orm)

    @classmethod
    async def get_vehicle(cls, data: VehicleDTO) -> VehicleDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(VehicleOrm).where(VehicleOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(VehicleDTO, orm) if orm else None

    @classmethod
    async def update_vehicle(cls, data: VehicleDTO) -> VehicleDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(VehicleOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(VehicleDTO, orm)

    @classmethod
    async def delete_vehicle(cls, data: VehicleDTO) -> VehicleDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(VehicleOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(VehicleDTO, orm)
