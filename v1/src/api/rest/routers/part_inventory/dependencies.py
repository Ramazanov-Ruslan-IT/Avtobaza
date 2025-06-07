from fastapi import Depends

from v1.src.app.services.part_inventory import build_part_inventory_service, AbsPartInventoryService

async def get_part_inventory_service(
    part_inventory_service: AbsPartInventoryService = Depends(build_part_inventory_service)
) -> AbsPartInventoryService:
    return part_inventory_service
