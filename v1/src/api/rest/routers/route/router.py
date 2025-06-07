from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.route.dependencies import get_route_service, AbsRouteService
from v1.src.app.dto.route import RouteDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.route.schemas import (
    RouteCreateSchema, RouteGetSchema, RouteUpdateSchema, RouteDeleteSchema,
    RouteResponseSchema1, RouteResponseSchema2, RouteResponseSchema3, RouteResponseSchema4
)

router = APIRouter(prefix="/route", tags=["Route"])

@api_post(router, "", RouteResponseSchema1, summary="Создать маршрут")
async def create_route(
    route: RouteCreateSchema = Body(...),
    route_service: AbsRouteService = Depends(get_route_service),
):
    try:
        result = await route_service.create_route(pydantic_to_dto(RouteDTO, route))
        if not result:
            raise_404(data={"errors": "Route not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", RouteResponseSchema2, summary="Получить маршрут")
async def get_route(
    route: RouteGetSchema = Query(...),
    route_service: AbsRouteService = Depends(get_route_service),
):
    try:
        result = await route_service.get_route(pydantic_to_dto(RouteDTO, route))
        if not result:
            raise_404(data={"errors": "Route not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", RouteResponseSchema3, summary="Обновить маршрут")
async def update_route(
    route: RouteUpdateSchema = Body(...),
    route_service: AbsRouteService = Depends(get_route_service),
):
    try:
        result = await route_service.update_route(pydantic_to_dto(RouteDTO, route))
        if not result:
            raise_404(data={"errors": "Route not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", RouteResponseSchema4, summary="Удалить маршрут")
async def delete_route(
    route: RouteDeleteSchema = Body(...),
    route_service: AbsRouteService = Depends(get_route_service),
):
    try:
        result = await route_service.delete_route(pydantic_to_dto(RouteDTO, route))
        if not result:
            raise_404(data={"errors": "Route not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
