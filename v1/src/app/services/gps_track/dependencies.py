from v1.src.app.services.gps_track.abs_service import AbsGpsTrackService
from v1.src.app.services.gps_track.service import GpsTrackService

from v1.src.db.repositories.gps_track.dependencies import get_gps_track_repo


async def build_gps_track_service() -> AbsGpsTrackService:
    gps_track_repo = await get_gps_track_repo()
    return GpsTrackService(gps_track_repo)
