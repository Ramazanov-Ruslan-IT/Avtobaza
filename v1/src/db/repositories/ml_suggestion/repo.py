from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.ml_suggestion.abs_repo import AbsMlSuggestionRepo
from v1.src.db.models.ml_suggestion_orm import MlSuggestionOrm
from v1.src.app.dto.ml_suggestion import MlSuggestionDTO


class MlSuggestionRepo(AbsMlSuggestionRepo):
    @classmethod
    async def create_ml_suggestion(cls, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(MlSuggestionOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(MlSuggestionDTO, orm)

    @classmethod
    async def get_ml_suggestion(cls, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(MlSuggestionOrm).where(MlSuggestionOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(MlSuggestionDTO, orm) if orm else None

    @classmethod
    async def update_ml_suggestion(cls, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(MlSuggestionOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(MlSuggestionDTO, orm)

    @classmethod
    async def delete_ml_suggestion(cls, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(MlSuggestionOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(MlSuggestionDTO, orm)
