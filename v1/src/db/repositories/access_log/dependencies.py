from v1.src.db.repositories.access_log.repo import AccessLogRepo
from v1.src.db.repositories.access_log.abs_repo import AbsAccessLogRepo


async def get_access_log_repo() -> AbsAccessLogRepo:
    return AccessLogRepo()
