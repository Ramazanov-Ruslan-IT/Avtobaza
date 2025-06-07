from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.gps_track.abs_repo import AbsGpsTrackRepo
from v1.src.db.models.gps_track_orm import GpsTrackOrm
from v1.src.app.dto.gps_track import GpsTrackDTO


class GpsTrackRepo(AbsGpsTrackRepo):
    @classmethod
    async def create_gps_track(cls, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(GpsTrackOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(GpsTrackDTO, orm)

    @classmethod
    async def get_gps_track(cls, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(GpsTrackOrm).where(GpsTrackOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(GpsTrackDTO, orm) if orm else None

    @classmethod
    async def update_gps_track(cls, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(GpsTrackOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(GpsTrackDTO, orm)

    @classmethod
    async def delete_gps_track(cls, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(GpsTrackOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(GpsTrackDTO, orm)
