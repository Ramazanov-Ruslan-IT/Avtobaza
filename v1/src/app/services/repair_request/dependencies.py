from v1.src.app.services.repair_request.abs_service import AbsRepairRequestService
from v1.src.app.services.repair_request.service import RepairRequestService

from v1.src.db.repositories.repair_request.dependencies import get_repair_request_repo


async def build_repair_request_service() -> AbsRepairRequestService:
    repair_request_repo = await get_repair_request_repo()
    return RepairRequestService(repair_request_repo)
