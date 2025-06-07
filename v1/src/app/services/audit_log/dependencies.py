from v1.src.app.services.audit_log.abs_service import AbsAuditLogService
from v1.src.app.services.audit_log.service import AuditLogService

from v1.src.db.repositories.audit_log.dependencies import get_audit_log_repo


async def build_audit_log_service() -> AbsAuditLogService:
    audit_log_repo = await get_audit_log_repo()
    return AuditLogService(audit_log_repo)
