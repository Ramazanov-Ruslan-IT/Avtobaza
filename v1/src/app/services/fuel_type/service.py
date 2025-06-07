from v1.src.app.services.fuel_type.abs_service import AbsFuelTypeService
from v1.src.db.repositories.fuel_type import AbsFuelTypeRepo
from v1.src.app.dto.fuel_type import FuelTypeDTO


class FuelTypeService(AbsFuelTypeService):
    def __init__(self, fuel_type_repo: AbsFuelTypeRepo):
        self.fuel_type_repo = fuel_type_repo

    async def create_fuel_type(self, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        return await self.fuel_type_repo.create_fuel_type(data)

    async def get_fuel_type(self, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        result = await self.fuel_type_repo.get_fuel_type(data)
        if not result:
            raise ValueError("Fuel type not found")
        return result

    async def update_fuel_type(self, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        result = await self.fuel_type_repo.update_fuel_type(data)
        if not result:
            raise ValueError("Cannot update: fuel type not found")
        return result

    async def delete_fuel_type(self, data: FuelTypeDTO) -> FuelTypeDTO | None | Exception:
        result = await self.fuel_type_repo.delete_fuel_type(data)
        if not result:
            raise ValueError("Cannot delete: fuel type not found")
        return result
