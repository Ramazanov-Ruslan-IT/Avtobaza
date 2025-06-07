from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.role.abs_repo import AbsRoleRepo
from v1.src.db.models.role_orm import RoleOrm
from v1.src.app.dto.role import RoleDTO


class RoleRepo(AbsRoleRepo):
    @classmethod
    async def create_role(cls, data: RoleDTO) -> RoleDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(RoleOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(RoleDTO, orm)

    @classmethod
    async def get_role(cls, data: RoleDTO) -> RoleDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(RoleOrm).where(RoleOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(RoleDTO, orm) if orm else None

    @classmethod
    async def update_role(cls, data: RoleDTO) -> RoleDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(RoleOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(RoleDTO, orm)

    @classmethod
    async def delete_role(cls, data: RoleDTO) -> RoleDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(RoleOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(RoleDTO, orm)
