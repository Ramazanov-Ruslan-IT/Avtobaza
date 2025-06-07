from abc import ABC, abstractmethod

from v1.src.app.dto.part_inventory import PartInventoryDTO


class AbsPartInventoryService(ABC):
    @abstractmethod
    async def create_part_inventory(self, data: PartInventoryDTO) -> PartInventoryDTO | None | Exception:
        pass

    @abstractmethod
    async def get_part_inventory(self, data: PartInventoryDTO) -> PartInventoryDTO | None | Exception:
        pass

    @abstractmethod
    async def update_part_inventory(self, data: PartInventoryDTO) -> PartInventoryDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_part_inventory(self, data: PartInventoryDTO) -> PartInventoryDTO | None | Exception:
        pass
