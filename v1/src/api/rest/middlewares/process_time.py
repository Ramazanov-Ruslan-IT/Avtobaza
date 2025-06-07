# v1/src/api/rest/middlewares/process_time.py
import time

from fastapi import Request


async def process_time_middleware(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = (time.perf_counter() - start_time) * 1000
    response.headers["X-Process-Time"] = f"{process_time:.2f}ms"
    print(f"Path: {request.url.path}, Process time: {process_time:.2f}ms")
    return response
