from abc import ABC, abstractmethod

from v1.src.app.dto.storage_fuel import StorageFuelDTO


class AbsStorageFuelRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_storage_fuel(cls, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        raise NotImplementedError("create_storage_fuel() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_storage_fuel(cls, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        raise NotImplementedError("get_storage_fuel() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_storage_fuel(cls, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        raise NotImplementedError("update_storage_fuel() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_storage_fuel(cls, data: StorageFuelDTO) -> StorageFuelDTO | None | Exception:
        raise NotImplementedError("delete_storage_fuel() must be implemented in subclass")
