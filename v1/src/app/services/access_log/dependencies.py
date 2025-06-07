from v1.src.app.services.access_log.abs_service import AbsAccessLogService
from v1.src.app.services.access_log.service import AccessLogService

from v1.src.db.repositories.access_log.dependencies import get_access_log_repo


async def build_access_log_service() -> AbsAccessLogService:
    access_log_repo = await get_access_log_repo()
    return AccessLogService(access_log_repo)
