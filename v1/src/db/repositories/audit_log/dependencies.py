from v1.src.db.repositories.audit_log.repo import AuditLogRepo
from v1.src.db.repositories.audit_log.abs_repo import AbsAuditLogRepo


async def get_audit_log_repo() -> AbsAuditLogRepo:
    return AuditLogRepo()
