from fastapi import Depends

from v1.src.app.services.repair_request import build_repair_request_service, AbsRepairRequestService

async def get_repair_request_service(
    repair_request_service: AbsRepairRequestService = Depends(build_repair_request_service)
) -> AbsRepairRequestService:
    return repair_request_service
