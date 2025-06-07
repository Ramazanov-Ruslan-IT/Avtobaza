from v1.src.app.services.maintenance_log.abs_service import AbsMaintenanceLogService
from v1.src.app.services.maintenance_log.service import MaintenanceLogService

from v1.src.db.repositories.maintenance_log.dependencies import get_maintenance_log_repo


async def build_maintenance_log_service() -> AbsMaintenanceLogService:
    maintenance_log_repo = await get_maintenance_log_repo()
    return MaintenanceLogService(maintenance_log_repo)
