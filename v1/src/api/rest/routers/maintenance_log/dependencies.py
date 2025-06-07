from fastapi import Depends

from v1.src.app.services.maintenance_log import build_maintenance_log_service, AbsMaintenanceLogService

async def get_maintenance_log_service(
    maintenance_log_service: AbsMaintenanceLogService = Depends(build_maintenance_log_service)
) -> AbsMaintenanceLogService:
    return maintenance_log_service
