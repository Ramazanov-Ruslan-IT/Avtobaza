from v1.src.db.repositories.storage_fuel.repo import StorageFuelRepo
from v1.src.db.repositories.storage_fuel.abs_repo import AbsStorageFuelRepo


async def get_storage_fuel_repo() -> AbsStorageFuelRepo:
    return StorageFuelRepo()
