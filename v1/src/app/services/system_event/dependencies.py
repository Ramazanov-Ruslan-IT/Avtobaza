from v1.src.app.services.system_event.abs_service import AbsSystemEventService
from v1.src.app.services.system_event.service import SystemEventService

from v1.src.db.repositories.system_event.dependencies import get_system_event_repo


async def build_system_event_service() -> AbsSystemEventService:
    system_event_repo = await get_system_event_repo()
    return SystemEventService(system_event_repo)
