from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.gps_track.dependencies import get_gps_track_service, AbsGpsTrackService
from v1.src.app.dto.gps_track import GpsTrackDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.gps_track.schemas import (
    GpsTrackCreateSchema, GpsTrackGetSchema, GpsTrackUpdateSchema, GpsTrackDeleteSchema,
    GpsTrackResponseSchema1, GpsTrackResponseSchema2, GpsTrackResponseSchema3, GpsTrackResponseSchema4
)

router = APIRouter(prefix="/gps_track", tags=["GpsTrack"])

@api_post(router, "", GpsTrackResponseSchema1, summary="Создать GPS-трек")
async def create_gps_track(
    gps_track: GpsTrackCreateSchema = Body(...),
    gps_track_service: AbsGpsTrackService = Depends(get_gps_track_service),
):
    try:
        result = await gps_track_service.create_gps_track(pydantic_to_dto(GpsTrackDTO, gps_track))
        if not result:
            raise_404(data={"errors": "GpsTrack not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", GpsTrackResponseSchema2, summary="Получить GPS-трек")
async def get_gps_track(
    gps_track: GpsTrackGetSchema = Query(...),
    gps_track_service: AbsGpsTrackService = Depends(get_gps_track_service),
):
    try:
        result = await gps_track_service.get_gps_track(pydantic_to_dto(GpsTrackDTO, gps_track))
        if not result:
            raise_404(data={"errors": "GpsTrack not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", GpsTrackResponseSchema3, summary="Обновить GPS-трек")
async def update_gps_track(
    gps_track: GpsTrackUpdateSchema = Body(...),
    gps_track_service: AbsGpsTrackService = Depends(get_gps_track_service),
):
    try:
        result = await gps_track_service.update_gps_track(pydantic_to_dto(GpsTrackDTO, gps_track))
        if not result:
            raise_404(data={"errors": "GpsTrack not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", GpsTrackResponseSchema4, summary="Удалить GPS-трек")
async def delete_gps_track(
    gps_track: GpsTrackDeleteSchema = Body(...),
    gps_track_service: AbsGpsTrackService = Depends(get_gps_track_service),
):
    try:
        result = await gps_track_service.delete_gps_track(pydantic_to_dto(GpsTrackDTO, gps_track))
        if not result:
            raise_404(data={"errors": "GpsTrack not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
