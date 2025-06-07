from fastapi import Depends

from v1.src.app.services.refueling_log import build_refueling_log_service, AbsRefuelingLogService

async def get_refueling_log_service(
    refueling_log_service: AbsRefuelingLogService = Depends(build_refueling_log_service)
) -> AbsRefuelingLogService:
    return refueling_log_service
