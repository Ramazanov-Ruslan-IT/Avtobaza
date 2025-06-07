from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.autobase.abs_repo import AbsAutobaseRepo
from v1.src.db.models.autobase_orm import AutobaseOrm
from v1.src.app.dto.autobase import AutobaseDTO


class AutobaseRepo(AbsAutobaseRepo):
    @classmethod
    async def create_autobase(cls, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(AutobaseOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(AutobaseDTO, orm)

    @classmethod
    async def get_autobase(cls, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(AutobaseOrm).where(AutobaseOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(AutobaseDTO, orm) if orm else None

    @classmethod
    async def update_autobase(cls, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(AutobaseOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(AutobaseDTO, orm)

    @classmethod
    async def delete_autobase(cls, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(AutobaseOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(AutobaseDTO, orm)
