from v1.src.db.repositories.refueling_log.repo import RefuelingLogRepo
from v1.src.db.repositories.refueling_log.abs_repo import AbsRefuelingLogRepo


async def get_refueling_log_repo() -> AbsRefuelingLogRepo:
    return RefuelingLogRepo()
