from v1.src.db.repositories.system_event.repo import SystemEventRepo
from v1.src.db.repositories.system_event.abs_repo import AbsSystemEventRepo


async def get_system_event_repo() -> AbsSystemEventRepo:
    return SystemEventRepo()
