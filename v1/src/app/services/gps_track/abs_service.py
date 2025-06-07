from abc import ABC, abstractmethod

from v1.src.app.dto.gps_track import GpsTrackDTO


class AbsGpsTrackService(ABC):
    @abstractmethod
    async def create_gps_track(self, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        pass

    @abstractmethod
    async def get_gps_track(self, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        pass

    @abstractmethod
    async def update_gps_track(self, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_gps_track(self, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        pass
