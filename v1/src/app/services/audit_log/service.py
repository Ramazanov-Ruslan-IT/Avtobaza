from v1.src.app.services.audit_log.abs_service import AbsAuditLogService
from v1.src.db.repositories.audit_log import AbsAuditLogRepo
from v1.src.app.dto.audit_log import AuditLogDTO


class AuditLogService(AbsAuditLogService):
    def __init__(self, audit_log_repo: AbsAuditLogRepo):
        self.audit_log_repo = audit_log_repo

    async def create_audit_log(self, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        return await self.audit_log_repo.create_audit_log(data)

    async def get_audit_log(self, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        result = await self.audit_log_repo.get_audit_log(data)
        if not result:
            raise ValueError("Audit log not found")
        return result

    async def update_audit_log(self, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        result = await self.audit_log_repo.update_audit_log(data)
        if not result:
            raise ValueError("Cannot update: audit log not found")
        return result

    async def delete_audit_log(self, data: AuditLogDTO) -> AuditLogDTO | None | Exception:
        result = await self.audit_log_repo.delete_audit_log(data)
        if not result:
            raise ValueError("Cannot delete: audit log not found")
        return result
