from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.schedule.dependencies import get_schedule_service, AbsScheduleService
from v1.src.app.dto.schedule import ScheduleDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.schedule.schemas import (
    ScheduleCreateSchema, ScheduleGetSchema, ScheduleUpdateSchema, ScheduleDeleteSchema,
    ScheduleResponseSchema1, ScheduleResponseSchema2, ScheduleResponseSchema3, ScheduleResponseSchema4
)

router = APIRouter(prefix="/schedule", tags=["Schedule"])

@api_post(router, "", ScheduleResponseSchema1, summary="Создать плановое задание")
async def create_schedule(
    schedule: ScheduleCreateSchema = Body(...),
    schedule_service: AbsScheduleService = Depends(get_schedule_service),
):
    try:
        result = await schedule_service.create_schedule(pydantic_to_dto(ScheduleDTO, schedule))
        if not result:
            raise_404(data={"errors": "Schedule not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", ScheduleResponseSchema2, summary="Получить плановое задание")
async def get_schedule(
    schedule: ScheduleGetSchema = Query(...),
    schedule_service: AbsScheduleService = Depends(get_schedule_service),
):
    try:
        result = await schedule_service.get_schedule(pydantic_to_dto(ScheduleDTO, schedule))
        if not result:
            raise_404(data={"errors": "Schedule not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", ScheduleResponseSchema3, summary="Обновить плановое задание")
async def update_schedule(
    schedule: ScheduleUpdateSchema = Body(...),
    schedule_service: AbsScheduleService = Depends(get_schedule_service),
):
    try:
        result = await schedule_service.update_schedule(pydantic_to_dto(ScheduleDTO, schedule))
        if not result:
            raise_404(data={"errors": "Schedule not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", ScheduleResponseSchema4, summary="Удалить плановое задание")
async def delete_schedule(
    schedule: ScheduleDeleteSchema = Body(...),
    schedule_service: AbsScheduleService = Depends(get_schedule_service),
):
    try:
        result = await schedule_service.delete_schedule(pydantic_to_dto(ScheduleDTO, schedule))
        if not result:
            raise_404(data={"errors": "Schedule not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
