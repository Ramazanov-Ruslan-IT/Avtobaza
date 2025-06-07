from fastapi import Depends

from v1.src.app.services.system_event import build_system_event_service, AbsSystemEventService

async def get_system_event_service(
    system_event_service: AbsSystemEventService = Depends(build_system_event_service)
) -> AbsSystemEventService:
    return system_event_service
