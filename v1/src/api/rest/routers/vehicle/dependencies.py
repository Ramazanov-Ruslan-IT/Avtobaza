from fastapi import Depends

from v1.src.app.services.vehicle import build_vehicle_service, AbsVehicleService

async def get_vehicle_service(
    vehicle_service: AbsVehicleService = Depends(build_vehicle_service)
) -> AbsVehicleService:
    return vehicle_service

