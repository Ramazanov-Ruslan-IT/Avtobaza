from abc import ABC, abstractmethod

from v1.src.app.dto.storage_fuel import StorageFuelDTO


class AbsStorageFuelService(ABC):
    @abstractmethod
    async def create_storage_fuel(self, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        pass

    @abstractmethod
    async def get_storage_fuel(self, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        pass

    @abstractmethod
    async def update_storage_fuel(self, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_storage_fuel(self, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        pass
