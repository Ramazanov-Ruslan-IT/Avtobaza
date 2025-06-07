from fastapi import Depends

from v1.src.app.services.audit_log import build_audit_log_service, AbsAuditLogService


async def get_audit_log_service(audit_log_service: AbsAuditLogService = Depends(build_audit_log_service)) -> AbsAuditLogService:
    return audit_log_service
