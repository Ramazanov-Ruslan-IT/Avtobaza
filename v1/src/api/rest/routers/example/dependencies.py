from fastapi import Depends

from v1.src.app.services.example import build_example_service, AbsExampleService


async def get_example_service(example_service: AbsExampleService = Depends(build_example_service)) -> AbsExampleService:
    return example_service
