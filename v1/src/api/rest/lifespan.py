from contextlib import asynccontextmanager

from fastapi import FastAPI

from v1.src.api.rest.exceptions.app_exceptions import AppException, app_exception_handler
from v1.src.api.rest.middlewares.register import register_middlewares
from v1.src.api.rest.routers.base_router import base_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("Machine Service REST API started")
        yield
    except Exception as e:
        print(e)
        raise
    finally:
        print("finally")

app = FastAPI(lifespan=lifespan)

app.include_router(base_router)

app.add_exception_handler(AppException, app_exception_handler)

register_middlewares(app)
