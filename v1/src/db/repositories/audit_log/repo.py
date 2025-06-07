from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.audit_log.abs_repo import AbsAuditLogRepo
from v1.src.db.models.audit_log_orm import AuditLogOrm
from v1.src.app.dto.audit_log import AuditLogDTO


class AuditLogRepo(AbsAuditLogRepo):
    @classmethod
    async def create_audit_log(cls, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(AuditLogOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(AuditLogDTO, orm)

    @classmethod
    async def get_audit_log(cls, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(AuditLogOrm).where(AuditLogOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(AuditLogDTO, orm) if orm else None

    @classmethod
    async def update_audit_log(cls, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(AuditLogOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(AuditLogDTO, orm)

    @classmethod
    async def delete_audit_log(cls, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(AuditLogOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(AuditLogDTO, orm)
