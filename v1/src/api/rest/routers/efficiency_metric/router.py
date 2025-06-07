from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.efficiency_metric.dependencies import get_efficiency_metric_service, AbsEfficiencyMetricService
from v1.src.app.dto.efficiency_metric import EfficiencyMetricDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.efficiency_metric.schemas import (
    EfficiencyMetricCreateSchema, EfficiencyMetricGetSchema, EfficiencyMetricUpdateSchema, EfficiencyMetricDeleteSchema,
    EfficiencyMetricResponseSchema1, EfficiencyMetricResponseSchema2, EfficiencyMetricResponseSchema3, EfficiencyMetricResponseSchema4
)

router = APIRouter(prefix="/efficiency_metric", tags=["EfficiencyMetric"])

@api_post(router, "", EfficiencyMetricResponseSchema1, summary="Создать метрику эффективности")
async def create_efficiency_metric(
    efficiency_metric: EfficiencyMetricCreateSchema = Body(...),
    efficiency_metric_service: AbsEfficiencyMetricService = Depends(get_efficiency_metric_service),
):
    try:
        result = await efficiency_metric_service.create_efficiency_metric(pydantic_to_dto(EfficiencyMetricDTO, efficiency_metric))
        if not result:
            raise_404(data={"errors": "EfficiencyMetric not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", EfficiencyMetricResponseSchema2, summary="Получить метрику эффективности")
async def get_efficiency_metric(
    efficiency_metric: EfficiencyMetricGetSchema = Query(...),
    efficiency_metric_service: AbsEfficiencyMetricService = Depends(get_efficiency_metric_service),
):
    try:
        result = await efficiency_metric_service.get_efficiency_metric(pydantic_to_dto(EfficiencyMetricDTO, efficiency_metric))
        if not result:
            raise_404(data={"errors": "EfficiencyMetric not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", EfficiencyMetricResponseSchema3, summary="Обновить метрику эффективности")
async def update_efficiency_metric(
    efficiency_metric: EfficiencyMetricUpdateSchema = Body(...),
    efficiency_metric_service: AbsEfficiencyMetricService = Depends(get_efficiency_metric_service),
):
    try:
        result = await efficiency_metric_service.update_efficiency_metric(pydantic_to_dto(EfficiencyMetricDTO, efficiency_metric))
        if not result:
            raise_404(data={"errors": "EfficiencyMetric not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", EfficiencyMetricResponseSchema4, summary="Удалить метрику эффективности")
async def delete_efficiency_metric(
    efficiency_metric: EfficiencyMetricDeleteSchema = Body(...),
    efficiency_metric_service: AbsEfficiencyMetricService = Depends(get_efficiency_metric_service),
):
    try:
        result = await efficiency_metric_service.delete_efficiency_metric(pydantic_to_dto(EfficiencyMetricDTO, efficiency_metric))
        if not result:
            raise_404(data={"errors": "EfficiencyMetric not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
