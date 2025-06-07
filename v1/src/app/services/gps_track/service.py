from v1.src.app.services.gps_track.abs_service import AbsGpsTrackService
from v1.src.db.repositories.gps_track import AbsGpsTrackRepo
from v1.src.app.dto.gps_track import GpsTrackDTO


class GpsTrackService(AbsGpsTrackService):
    def __init__(self, gps_track_repo: AbsGpsTrackRepo):
        self.gps_track_repo = gps_track_repo

    async def create_gps_track(self, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        return await self.gps_track_repo.create_gps_track(data)

    async def get_gps_track(self, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        result = await self.gps_track_repo.get_gps_track(data)
        if not result:
            raise ValueError("GPS track not found")
        return result

    async def update_gps_track(self, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        result = await self.gps_track_repo.update_gps_track(data)
        if not result:
            raise ValueError("Cannot update: GPS track not found")
        return result

    async def delete_gps_track(self, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        result = await self.gps_track_repo.delete_gps_track(data)
        if not result:
            raise ValueError("Cannot delete: GPS track not found")
        return result
