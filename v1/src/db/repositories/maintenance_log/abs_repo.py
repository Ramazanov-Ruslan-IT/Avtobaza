from abc import ABC, abstractmethod

from v1.src.app.dto.maintenance_log import MaintenanceLogDTO


class AbsMaintenanceLogRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_maintenance_log(cls, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        raise NotImplementedError("create_maintenance_log() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_maintenance_log(cls, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        raise NotImplementedError("get_maintenance_log() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_maintenance_log(cls, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        raise NotImplementedError("update_maintenance_log() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_maintenance_log(cls, data: MaintenanceLogDTO) -> MaintenanceLogDTO | None | Exception:
        raise NotImplementedError("delete_maintenance_log() must be implemented in subclass")
