from v1.src.app.services.example import AbsExampleService
from v1.src.app.solutions.example.abs_solution import AbsExampleSolution
from v1.src.app.dto.example import ExampleDTO


class ExampleSolution(AbsExampleSolution):
    def __init__(self, example_service: AbsExampleService):
        self.example_service = example_service

    async def func_example(self, data: ExampleDTO) -> dict:
        log = vars(data)
        await self.example_service.create_example(data)
        return log
