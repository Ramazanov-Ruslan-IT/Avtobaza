# v1/src/api/rest/middlewares/register.py
from fastapi import FastAPI

#from v1.src.api.middlewares.security_headers import SecurityHeadersMiddleware
from v1.src.api.rest.middlewares.cors import add_cors_middleware
from v1.src.api.rest.middlewares.process_time import process_time_middleware


def register_middlewares(app: FastAPI) -> None:
    #app.add_middleware(SecurityHeadersMiddleware)
    add_cors_middleware(app)
    app.middleware("http")(process_time_middleware)

