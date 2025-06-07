from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.user.abs_repo import AbsUserRepo
from v1.src.db.models.user_orm import UserOrm
from v1.src.app.dto.user import UserDTO


class UserRepo(AbsUserRepo):
    @classmethod
    async def create_user(cls, data: UserDTO) -> UserDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(UserOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(UserDTO, orm)

    @classmethod
    async def get_user(cls, data: UserDTO) -> UserDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(UserOrm).where(UserOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(UserDTO, orm) if orm else None

    @classmethod
    async def update_user(cls, data: UserDTO) -> UserDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(UserOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(UserDTO, orm)

    @classmethod
    async def delete_user(cls, data: UserDTO) -> UserDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(UserOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(UserDTO, orm)
