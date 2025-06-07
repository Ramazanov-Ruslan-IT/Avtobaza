from v1.src.app.services.vehicle.abs_service import AbsVehicleService
from v1.src.db.repositories.vehicle import AbsVehicleRepo
from v1.src.app.dto.vehicle import VehicleDTO


class VehicleService(AbsVehicleService):
    def __init__(self, vehicle_repo: AbsVehicleRepo):
        self.vehicle_repo = vehicle_repo

    async def create_vehicle(self, data: VehicleDTO) -> VehicleDTO | None | Exception:
        return await self.vehicle_repo.create_vehicle(data)

    async def get_vehicle(self, data: VehicleDTO) -> VehicleDTO | None | Exception:
        result = await self.vehicle_repo.get_vehicle(data)
        if not result:
            raise ValueError("Vehicle not found")
        return result

    async def update_vehicle(self, data: VehicleDTO) -> VehicleDTO | None | Exception:
        result = await self.vehicle_repo.update_vehicle(data)
        if not result:
            raise ValueError("Cannot update: vehicle not found")
        return result

    async def delete_vehicle(self, data: VehicleDTO) -> VehicleDTO | None | Exception:
        result = await self.vehicle_repo.delete_vehicle(data)
        if not result:
            raise ValueError("Cannot delete: vehicle not found")
        return result
