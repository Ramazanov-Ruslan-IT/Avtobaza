from abc import ABC, abstractmethod
from typing import Optional

from v1.src.app.dto.example import ExampleDTO


class AbsExampleRepo(ABC):
    @abstractmethod
    async def create_example(self, data: ExampleDTO) -> Optional[ExampleDTO]:
        pass

    @abstractmethod
    async def get_example(self, data: ExampleDTO) -> Optional[ExampleDTO]:
        pass

    @abstractmethod
    async def update_example(self, data: ExampleDTO) -> Optional[ExampleDTO]:
        pass

    @abstractmethod
    async def delete_example(self, data: ExampleDTO) -> Optional[ExampleDTO]:
        pass
