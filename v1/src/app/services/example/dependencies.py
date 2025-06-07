from v1.src.app.services.example.abs_service import AbsExampleService
from v1.src.app.services.example.service import ExampleService

from v1.src.db.repositories.example.dependencies import get_example_repo


async def build_example_service() -> AbsExampleService:
    example_repo = await get_example_repo()
    return ExampleService(example_repo)
