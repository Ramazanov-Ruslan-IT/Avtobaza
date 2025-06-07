from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.scheduled_task.dependencies import get_scheduled_task_service, AbsScheduledTaskService
from v1.src.app.dto.scheduled_task import ScheduledTaskDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.scheduled_task.schemas import (
    ScheduledTaskCreateSchema, ScheduledTaskGetSchema, ScheduledTaskUpdateSchema, ScheduledTaskDeleteSchema,
    ScheduledTaskResponseSchema1, ScheduledTaskResponseSchema2, ScheduledTaskResponseSchema3, ScheduledTaskResponseSchema4
)

router = APIRouter(prefix="/scheduled_task", tags=["ScheduledTask"])

@api_post(router, "", ScheduledTaskResponseSchema1, summary="Создать системную задачу")
async def create_scheduled_task(
    scheduled_task: ScheduledTaskCreateSchema = Body(...),
    scheduled_task_service: AbsScheduledTaskService = Depends(get_scheduled_task_service),
):
    try:
        result = await scheduled_task_service.create_scheduled_task(pydantic_to_dto(ScheduledTaskDTO, scheduled_task))
        if not result:
            raise_404(data={"errors": "ScheduledTask not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", ScheduledTaskResponseSchema2, summary="Получить системную задачу")
async def get_scheduled_task(
    scheduled_task: ScheduledTaskGetSchema = Query(...),
    scheduled_task_service: AbsScheduledTaskService = Depends(get_scheduled_task_service),
):
    try:
        result = await scheduled_task_service.get_scheduled_task(pydantic_to_dto(ScheduledTaskDTO, scheduled_task))
        if not result:
            raise_404(data={"errors": "ScheduledTask not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", ScheduledTaskResponseSchema3, summary="Обновить системную задачу")
async def update_scheduled_task(
    scheduled_task: ScheduledTaskUpdateSchema = Body(...),
    scheduled_task_service: AbsScheduledTaskService = Depends(get_scheduled_task_service),
):
    try:
        result = await scheduled_task_service.update_scheduled_task(pydantic_to_dto(ScheduledTaskDTO, scheduled_task))
        if not result:
            raise_404(data={"errors": "ScheduledTask not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", ScheduledTaskResponseSchema4, summary="Удалить системную задачу")
async def delete_scheduled_task(
    scheduled_task: ScheduledTaskDeleteSchema = Body(...),
    scheduled_task_service: AbsScheduledTaskService = Depends(get_scheduled_task_service),
):
    try:
        result = await scheduled_task_service.delete_scheduled_task(pydantic_to_dto(ScheduledTaskDTO, scheduled_task))
        if not result:
            raise_404(data={"errors": "ScheduledTask not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
