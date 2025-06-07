from abc import ABC, abstractmethod

from v1.src.app.dto.fuel_type import FuelTypeDTO


class AbsFuelTypeService(ABC):
    @abstractmethod
    async def create_fuel_type(self, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        pass

    @abstractmethod
    async def get_fuel_type(self, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        pass

    @abstractmethod
    async def update_fuel_type(self, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_fuel_type(self, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        pass
