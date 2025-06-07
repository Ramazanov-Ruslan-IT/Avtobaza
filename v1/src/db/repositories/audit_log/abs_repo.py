from abc import ABC, abstractmethod

from v1.src.app.dto.audit_log import AuditLogDTO


class AbsAuditLogRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_audit_log(cls, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        raise NotImplementedError("create_audit_log() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_audit_log(cls, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        raise NotImplementedError("get_audit_log() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_audit_log(cls, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        raise NotImplementedError("update_audit_log() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_audit_log(cls, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        raise NotImplementedError("delete_audit_log() must be implemented in subclass")
