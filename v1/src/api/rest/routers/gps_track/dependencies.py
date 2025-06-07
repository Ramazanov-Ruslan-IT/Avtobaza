from fastapi import Depends

from v1.src.app.services.gps_track import build_gps_track_service, AbsGpsTrackService

async def get_gps_track_service(
    gps_track_service: AbsGpsTrackService = Depends(build_gps_track_service)
) -> AbsGpsTrackService:
    return gps_track_service
