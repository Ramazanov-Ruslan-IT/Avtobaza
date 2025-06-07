from v1.src.db.repositories.vehicle.repo import VehicleRepo
from v1.src.db.repositories.vehicle.abs_repo import AbsVehicleRepo


async def get_vehicle_repo() -> AbsVehicleRepo:
    return VehicleRepo()
