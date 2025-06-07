from abc import ABC, abstractmethod

from v1.src.app.dto.ml_suggestion import MlSuggestionDTO


class AbsMlSuggestionRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_ml_suggestion(cls, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        raise NotImplementedError("func_example() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_ml_suggestion(cls, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        raise NotImplementedError("func_example() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_ml_suggestion(cls, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        raise NotImplementedError("func_example() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_ml_suggestion(cls, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        raise NotImplementedError("func_example() must be implemented in subclass")
    