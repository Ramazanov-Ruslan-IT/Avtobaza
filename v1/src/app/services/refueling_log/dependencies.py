from v1.src.app.services.refueling_log.abs_service import AbsRefuelingLogService
from v1.src.app.services.refueling_log.service import RefuelingLogService

from v1.src.db.repositories.refueling_log.dependencies import get_refueling_log_repo


async def build_refueling_log_service() -> AbsRefuelingLogService:
    refueling_log_repo = await get_refueling_log_repo()
    return RefuelingLogService(refueling_log_repo)
