from v1.src.app.services.vehicle.abs_service import AbsVehicleService
from v1.src.app.services.vehicle.service import VehicleService

from v1.src.db.repositories.vehicle.dependencies import get_vehicle_repo


async def build_vehicle_service() -> AbsVehicleService:
    vehicle_repo = await get_vehicle_repo()
    return VehicleService(vehicle_repo)
