from fastapi import Depends

from v1.src.app.services.storage_fuel import build_storage_fuel_service, AbsStorageFuelService

async def get_storage_fuel_service(
    storage_fuel_service: AbsStorageFuelService = Depends(build_storage_fuel_service)
) -> AbsStorageFuelService:
    return storage_fuel_service
