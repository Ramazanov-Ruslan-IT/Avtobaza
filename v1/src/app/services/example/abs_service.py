from abc import ABC, abstractmethod

from v1.src.app.dto.example import ExampleDTO


class AbsExampleService(ABC):
    @abstractmethod
    async def create_example(self, data: ExampleDTO) -> ExampleDTO:
        pass

    @abstractmethod
    async def get_example(self, data: ExampleDTO) -> ExampleDTO:
        pass

    @abstractmethod
    async def update_example(self, data: ExampleDTO) -> ExampleDTO:
        pass

    @abstractmethod
    async def delete_example(self, data: ExampleDTO) -> ExampleDTO:
        pass
