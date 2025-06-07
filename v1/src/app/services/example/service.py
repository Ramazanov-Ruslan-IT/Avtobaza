from v1.src.app.services.example.abs_service import AbsExampleService
from v1.src.db.repositories.example import AbsExampleRepo
from v1.src.app.dto.example import ExampleDTO


class ExampleService(AbsExampleService):
    def __init__(self, example_repo: AbsExampleRepo):
        self.example_repo = example_repo

    async def create_example(self, data: ExampleDTO) -> ExampleDTO:
        return await self.example_repo.create_example(data)

    async def get_example(self, data: ExampleDTO) -> ExampleDTO:
        result = await self.example_repo.get_example(data)
        if not result:
            raise ValueError("Example not found")
        return result

    async def update_example(self, data: ExampleDTO) -> ExampleDTO:
        result = await self.example_repo.update_example(data)
        if not result:
            raise ValueError("Cannot update: example not found")
        return result

    async def delete_example(self, data: ExampleDTO) -> ExampleDTO:
        result = await self.example_repo.delete_example(data)
        if not result:
            raise ValueError("Cannot delete: example not found")
        return result
