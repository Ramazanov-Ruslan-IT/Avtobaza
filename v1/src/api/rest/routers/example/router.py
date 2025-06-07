from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete

from v1.src.api.rest.routers.example.dependencies import get_example_service
from v1.src.app.services.example.abs_service import AbsExampleService, ExampleDTO

from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.example.schemas import (
    ExampleCreateSchema, ExampleGetSchema, ExampleUpdateSchema, ExampleDeleteSchema,
    ExampleResponseSchema1, ExampleResponseSchema2, ExampleResponseSchema3, ExampleResponseSchema4
)


router = APIRouter(prefix="/example", tags=["Example"])


@api_post(router, "", ExampleResponseSchema1, summary="Создать example")
async def create_example(
    example: ExampleCreateSchema = Body(...),
    example_service: AbsExampleService = Depends(get_example_service),
):
    return await example_service.create_example(pydantic_to_dto(ExampleDTO, example))


@api_get(router, "", ExampleResponseSchema2, summary="Получить example")
async def get_example(
    example: ExampleGetSchema = Query(...),
    example_service: AbsExampleService = Depends(get_example_service),
):
    return await example_service.get_example(pydantic_to_dto(ExampleDTO, example))


@api_put(router, "", ExampleResponseSchema3, summary="Обновить example")
async def update_example(
    example: ExampleUpdateSchema = Body(...),
    example_service: AbsExampleService = Depends(get_example_service),
):
    return await example_service.update_example(pydantic_to_dto(ExampleDTO, example))


@api_delete(router, "", ExampleResponseSchema4, summary="Удалить example")
async def delete_example(
    example: ExampleDeleteSchema = Body(...),
    example_service: AbsExampleService = Depends(get_example_service),
):
    return await example_service.delete_example(pydantic_to_dto(ExampleDTO, example))
