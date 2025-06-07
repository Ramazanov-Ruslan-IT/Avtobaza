from v1.src.db.repositories.ml_suggestion.repo import MlSuggestionRepo
from v1.src.db.repositories.ml_suggestion.abs_repo import AbsMlSuggestionRepo


async def get_ml_suggestion_repo() -> AbsMlSuggestionRepo:
    return MlSuggestionRepo()
