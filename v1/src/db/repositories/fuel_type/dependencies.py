from v1.src.db.repositories.fuel_type.repo import FuelTypeRepo
from v1.src.db.repositories.fuel_type.abs_repo import AbsFuelTypeRepo


async def get_fuel_type_repo() -> AbsFuelTypeRepo:
    return FuelTypeRepo()
