from abc import ABC, abstractmethod

from v1.src.app.dto.vehicle import VehicleDTO


class AbsVehicleService(ABC):
    @abstractmethod
    async def create_vehicle(self, data: VehicleDTO) -> VehicleDTO | None | Exception:
        pass

    @abstractmethod
    async def get_vehicle(self, data: VehicleDTO) -> VehicleDTO | None | Exception:
        pass

    @abstractmethod
    async def update_vehicle(self, data: VehicleDTO) -> VehicleDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_vehicle(self, data: VehicleDTO) -> VehicleDTO | None | Exception:
        pass
