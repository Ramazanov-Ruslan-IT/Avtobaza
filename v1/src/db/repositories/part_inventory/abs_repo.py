from abc import ABC, abstractmethod

from v1.src.app.dto.part_inventory import PartInventoryDTO


class AbsPartInventoryRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_part_inventory(cls, data: PartInventoryDTO) -> PartInventoryDTO | None | Exception:
        raise NotImplementedError("create_part_inventory() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_part_inventory(cls, data: PartInventoryDTO) -> PartInventoryDTO | None | Exception:
        raise NotImplementedError("get_part_inventory() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_part_inventory(cls, data: PartInventoryDTO) -> PartInventoryDTO | None | Exception:
        raise NotImplementedError("update_part_inventory() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_part_inventory(cls, data: PartInventoryDTO) -> PartInventoryDTO | None | Exception:
        raise NotImplementedError("delete_part_inventory() must be implemented in subclass")
