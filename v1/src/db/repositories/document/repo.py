from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.document.abs_repo import AbsDocumentRepo
from v1.src.db.models.document_orm import DocumentOrm
from v1.src.app.dto.document import DocumentDTO


class DocumentRepo(AbsDocumentRepo):
    @classmethod
    async def create_document(cls, data: DocumentDTO) -> DocumentDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(DocumentOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(DocumentDTO, orm)

    @classmethod
    async def get_document(cls, data: DocumentDTO) -> DocumentDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(DocumentOrm).where(DocumentOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(DocumentDTO, orm) if orm else None

    @classmethod
    async def update_document(cls, data: DocumentDTO) -> DocumentDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(DocumentOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(DocumentDTO, orm)

    @classmethod
    async def delete_document(cls, data: DocumentDTO) -> DocumentDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(DocumentOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(DocumentDTO, orm)
