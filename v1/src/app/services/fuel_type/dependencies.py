from v1.src.app.services.fuel_type.abs_service import AbsFuelTypeService
from v1.src.app.services.fuel_type.service import FuelTypeService

from v1.src.db.repositories.fuel_type.dependencies import get_fuel_type_repo


async def build_fuel_type_service() -> AbsFuelTypeService:
    fuel_type_repo = await get_fuel_type_repo()
    return FuelTypeService(fuel_type_repo)
