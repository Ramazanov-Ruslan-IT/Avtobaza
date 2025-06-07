from abc import ABC, abstractmethod

from v1.src.app.dto.audit_log import AuditLogDTO


class AbsAuditLogService(ABC):
    @abstractmethod
    async def create_audit_log(self, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        pass

    @abstractmethod
    async def get_audit_log(self, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        pass

    @abstractmethod
    async def update_audit_log(self, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_audit_log(self, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        pass
