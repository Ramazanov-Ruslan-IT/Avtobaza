from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.system_event.dependencies import get_system_event_service, AbsSystemEventService
from v1.src.app.dto.system_event import SystemEventDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.system_event.schemas import (
    SystemEventCreateSchema, SystemEventGetSchema, SystemEventUpdateSchema, SystemEventDeleteSchema,
    SystemEventResponseSchema1, SystemEventResponseSchema2, SystemEventResponseSchema3, SystemEventResponseSchema4
)

router = APIRouter(prefix="/system_event", tags=["SystemEvent"])

@api_post(router, "", SystemEventResponseSchema1, summary="Создать системное событие")
async def create_system_event(
    system_event: SystemEventCreateSchema = Body(...),
    system_event_service: AbsSystemEventService = Depends(get_system_event_service),
):
    try:
        result = await system_event_service.create_system_event(pydantic_to_dto(SystemEventDTO, system_event))
        if not result:
            raise_404(data={"errors": "SystemEvent not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", SystemEventResponseSchema2, summary="Получить системное событие")
async def get_system_event(
    system_event: SystemEventGetSchema = Query(...),
    system_event_service: AbsSystemEventService = Depends(get_system_event_service),
):
    try:
        result = await system_event_service.get_system_event(pydantic_to_dto(SystemEventDTO, system_event))
        if not result:
            raise_404(data={"errors": "SystemEvent not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", SystemEventResponseSchema3, summary="Обновить системное событие")
async def update_system_event(
    system_event: SystemEventUpdateSchema = Body(...),
    system_event_service: AbsSystemEventService = Depends(get_system_event_service),
):
    try:
        result = await system_event_service.update_system_event(pydantic_to_dto(SystemEventDTO, system_event))
        if not result:
            raise_404(data={"errors": "SystemEvent not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", SystemEventResponseSchema4, summary="Удалить системное событие")
async def delete_system_event(
    system_event: SystemEventDeleteSchema = Body(...),
    system_event_service: AbsSystemEventService = Depends(get_system_event_service),
):
    try:
        result = await system_event_service.delete_system_event(pydantic_to_dto(SystemEventDTO, system_event))
        if not result:
            raise_404(data={"errors": "SystemEvent not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
