from abc import ABC, abstractmethod

from v1.src.app.dto.example import ExampleDTO


class AbsExampleSolution(ABC):

    @abstractmethod
    async def func_example(self, data: ExampleDTO) -> dict:
        raise NotImplementedError("func_example() must be implemented in subclass")
