from fastapi import APIRouter

from v1.src.api.rest.routers.example.router import router as example_router

from v1.src.api.rest.api_route_factory import api_get


base_router = APIRouter(prefix="/v1")

base_router.include_router(example_router)


@api_get(base_router, "/", dict, summary="Базовый эндпоинт сервиса")
async def root():
    return {"message": "Welcome to the Example Service"}


@api_get(base_router, "/ping", dict, summary="Проверка доступности сервиса")
async def ping():
    return {"pong": True}
