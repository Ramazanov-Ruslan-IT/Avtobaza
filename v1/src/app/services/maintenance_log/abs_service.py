from abc import ABC, abstractmethod

from v1.src.app.dto.maintenance_log import MaintenanceLogDTO


class AbsMaintenanceLogService(ABC):
    @abstractmethod
    async def create_maintenance_log(self, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        pass

    @abstractmethod
    async def get_maintenance_log(self, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        pass

    @abstractmethod
    async def update_maintenance_log(self, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_maintenance_log(self, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        pass
