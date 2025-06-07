from v1.src.app.services.storage_fuel.abs_service import AbsStorageFuelService
from v1.src.app.services.storage_fuel.service import StorageFuelService

from v1.src.db.repositories.storage_fuel.dependencies import get_storage_fuel_repo


async def build_storage_fuel_service() -> AbsStorageFuelService:
    storage_fuel_repo = await get_storage_fuel_repo()
    return StorageFuelService(storage_fuel_repo)
