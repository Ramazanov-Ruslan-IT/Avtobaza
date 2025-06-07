from v1.src.app.services.part_inventory.abs_service import AbsPartInventoryService
from v1.src.db.repositories.part_inventory import AbsPartInventoryRepo
from v1.src.app.dto.part_inventory import PartInventoryDTO


class PartInventoryService(AbsPartInventoryService):
    def __init__(self, part_inventory_repo: AbsPartInventoryRepo):
        self.part_inventory_repo = part_inventory_repo

    async def create_part_inventory(self, data: PartInventoryDTO) -> PartInventoryDTO | None | Exception:
        return await self.part_inventory_repo.create_part_inventory(data)

    async def get_part_inventory(self, data: PartInventoryDTO) -> PartInventoryDTO | None | Exception:
        result = await self.part_inventory_repo.get_part_inventory(data)
        if not result:
            raise ValueError("Part inventory not found")
        return result

    async def update_part_inventory(self, data: PartInventoryDTO) -> PartInventoryDTO | None | Exception:
        result = await self.part_inventory_repo.update_part_inventory(data)
        if not result:
            raise ValueError("Cannot update: part inventory not found")
        return result

    async def delete_part_inventory(self, data: PartInventoryDTO) -> PartInventoryDTO | None | Exception:
        result = await self.part_inventory_repo.delete_part_inventory(data)
        if not result:
            raise ValueError("Cannot delete: part inventory not found")
        return result
