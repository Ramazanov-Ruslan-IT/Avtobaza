from v1.src.db.repositories.part_inventory.repo import PartInventoryRepo
from v1.src.db.repositories.part_inventory.abs_repo import AbsPartInventoryRepo


async def get_part_inventory_repo() -> AbsPartInventoryRepo:
    return PartInventoryRepo()
