from fastapi import Depends

from v1.src.app.services.access_log import build_access_log_service, AbsAccessLogService


async def get_access_log_service(access_log_service: AbsAccessLogService = Depends(build_access_log_service)) -> AbsAccessLogService:
    return access_log_service
