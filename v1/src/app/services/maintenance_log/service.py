from v1.src.app.services.maintenance_log.abs_service import AbsMaintenanceLogService
from v1.src.db.repositories.maintenance_log import AbsMaintenanceLogRepo
from v1.src.app.dto.maintenance_log import MaintenanceLogDTO


class MaintenanceLogService(AbsMaintenanceLogService):
    def __init__(self, maintenance_log_repo: AbsMaintenanceLogRepo):
        self.maintenance_log_repo = maintenance_log_repo

    async def create_maintenance_log(self, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        return await self.maintenance_log_repo.create_maintenance_log(data)

    async def get_maintenance_log(self, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        result = await self.maintenance_log_repo.get_maintenance_log(data)
        if not result:
            raise ValueError("Maintenance log not found")
        return result

    async def update_maintenance_log(self, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        result = await self.maintenance_log_repo.update_maintenance_log(data)
        if not result:
            raise ValueError("Cannot update: maintenance log not found")
        return result

    async def delete_maintenance_log(self, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        result = await self.maintenance_log_repo.delete_maintenance_log(data)
        if not result:
            raise ValueError("Cannot delete: maintenance log not found")
        return result
