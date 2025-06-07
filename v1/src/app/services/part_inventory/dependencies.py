from v1.src.app.services.part_inventory.abs_service import AbsPartInventoryService
from v1.src.app.services.part_inventory.service import PartInventoryService

from v1.src.db.repositories.part_inventory.dependencies import get_part_inventory_repo


async def build_part_inventory_service() -> AbsPartInventoryService:
    part_inventory_repo = await get_part_inventory_repo()
    return PartInventoryService(part_inventory_repo)
