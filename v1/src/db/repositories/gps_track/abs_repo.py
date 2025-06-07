from abc import ABC, abstractmethod

from v1.src.app.dto.gps_track import GpsTrackDTO


class AbsGpsTrackRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_gps_track(cls, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        raise NotImplementedError("create_gps_track() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_gps_track(cls, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        raise NotImplementedError("get_gps_track() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_gps_track(cls, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        raise NotImplementedError("update_gps_track() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_gps_track(cls, data: GpsTrackDTO) -> GpsTrackDTO | None | Exception:
        raise NotImplementedError("delete_gps_track() must be implemented in subclass")
