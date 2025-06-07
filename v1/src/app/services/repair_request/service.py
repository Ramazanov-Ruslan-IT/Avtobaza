from v1.src.app.services.repair_request.abs_service import AbsRepairRequestService
from v1.src.db.repositories.repair_request import AbsRepairRequestRepo
from v1.src.app.dto.repair_request import RepairRequestDTO


class RepairRequestService(AbsRepairRequestService):
    def __init__(self, repair_request_repo: AbsRepairRequestRepo):
        self.repair_request_repo = repair_request_repo

    async def create_repair_request(self, data: RepairRequestDTO) -> RepairRequestDTO | None | Exception:
        return await self.repair_request_repo.create_repair_request(data)

    async def get_repair_request(self, data: RepairRequestDTO) -> RepairRequestDTO | None | Exception:
        result = await self.repair_request_repo.get_repair_request(data)
        if not result:
            raise ValueError("Repair request not found")
        return result

    async def update_repair_request(self, data: RepairRequestDTO) -> RepairRequestDTO | None | Exception:
        result = await self.repair_request_repo.update_repair_request(data)
        if not result:
            raise ValueError("Cannot update: repair request not found")
        return result

    async def delete_repair_request(self, data: RepairRequestDTO) -> RepairRequestDTO | None | Exception:
        result = await self.repair_request_repo.delete_repair_request(data)
        if not result:
            raise ValueError("Cannot delete: repair request not found")
        return result
