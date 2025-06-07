from v1.src.db.repositories.maintenance_log.repo import MaintenanceLogRepo
from v1.src.db.repositories.maintenance_log.abs_repo import AbsMaintenanceLogRepo


async def get_maintenance_log_repo() -> AbsMaintenanceLogRepo:
    return MaintenanceLogRepo()
