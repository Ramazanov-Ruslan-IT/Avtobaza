from typing import Optional
from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.example.abs_repo import AbsExampleRepo
from v1.src.db.models.example_orm import ExampleOrm
from v1.src.app.dto.example import ExampleDTO


class ExampleRepo(AbsExampleRepo):
    async def create_example(self, data: ExampleDTO) -> Optional[ExampleDTO]:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(ExampleOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(ExampleDTO, orm)

    async def get_example(self, data: ExampleDTO) -> Optional[ExampleDTO]:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(ExampleOrm).where(ExampleOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(ExampleDTO, orm) if orm else None

    async def update_example(self, data: ExampleDTO) -> Optional[ExampleDTO]:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(ExampleOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(ExampleDTO, orm)

    async def delete_example(self, data: ExampleDTO) -> Optional[ExampleDTO]:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(ExampleOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(ExampleDTO, orm)
