from abc import ABC, abstractmethod

from v1.src.app.dto.vehicle import VehicleDTO


class AbsVehicleRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_vehicle(cls, data: VehicleDTO) -> VehicleDTO | None | Exception:
        raise NotImplementedError("create_vehicle() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_vehicle(cls, data: VehicleDTO) -> VehicleDTO | None | Exception:
        raise NotImplementedError("get_vehicle() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_vehicle(cls, data: VehicleDTO) -> VehicleDTO | None | Exception:
        raise NotImplementedError("update_vehicle() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_vehicle(cls, data: VehicleDTO) -> VehicleDTO | None | Exception:
        raise NotImplementedError("delete_vehicle() must be implemented in subclass")
