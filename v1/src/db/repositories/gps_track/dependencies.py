from v1.src.db.repositories.gps_track.repo import GpsTrackRepo
from v1.src.db.repositories.gps_track.abs_repo import AbsGpsTrackRepo


async def get_gps_track_repo() -> AbsGpsTrackRepo:
    return GpsTrackRepo()
