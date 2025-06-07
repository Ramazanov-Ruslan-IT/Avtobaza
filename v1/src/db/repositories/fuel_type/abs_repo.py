from abc import ABC, abstractmethod

from v1.src.app.dto.fuel_type import FuelTypeDTO


class AbsFuelTypeRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_fuel_type(cls, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        raise NotImplementedError("create_fuel_type() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_fuel_type(cls, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        raise NotImplementedError("get_fuel_type() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_fuel_type(cls, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        raise NotImplementedError("update_fuel_type() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_fuel_type(cls, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        raise NotImplementedError("delete_fuel_type() must be implemented in subclass")
