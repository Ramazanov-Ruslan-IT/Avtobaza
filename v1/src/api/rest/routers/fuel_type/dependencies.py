from fastapi import Depends

from v1.src.app.services.fuel_type import build_fuel_type_service, AbsFuelTypeService

async def get_fuel_type_service(
    fuel_type_service: AbsFuelTypeService = Depends(build_fuel_type_service)
) -> AbsFuelTypeService:
    return fuel_type_service
