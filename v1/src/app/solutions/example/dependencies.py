from v1.src.app.solutions.example.abs_solution import AbsExampleSolution
from v1.src.app.solutions.example.solution import ExampleSolution

from v1.src.app.services.example.abs_service import AbsExampleService
from v1.src.app.services.example import build_example_service


async def build_example_solution() -> AbsExampleSolution:
    example_service: AbsExampleService = await build_example_service()
    return ExampleSolution(example_service)
