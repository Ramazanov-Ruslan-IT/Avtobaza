from v1.src.app.services.storage_fuel.abs_service import AbsStorageFuelService
from v1.src.db.repositories.storage_fuel import AbsStorageFuelRepo
from v1.src.app.dto.storage_fuel import StorageFuelDTO


class StorageFuelService(AbsStorageFuelService):
    def __init__(self, storage_fuel_repo: AbsStorageFuelRepo):
        self.storage_fuel_repo = storage_fuel_repo

    async def create_storage_fuel(self, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        return await self.storage_fuel_repo.create_storage_fuel(data)

    async def get_storage_fuel(self, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        result = await self.storage_fuel_repo.get_storage_fuel(data)
        if not result:
            raise ValueError("Storage fuel not found")
        return result

    async def update_storage_fuel(self, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        result = await self.storage_fuel_repo.update_storage_fuel(data)
        if not result:
            raise ValueError("Cannot update: storage fuel not found")
        return result

    async def delete_storage_fuel(self, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        result = await self.storage_fuel_repo.delete_storage_fuel(data)
        if not result:
            raise ValueError("Cannot delete: storage fuel not found")
        return result
