from v1.src.app.services.ml_suggestion.abs_service import AbsMlSuggestionService
from v1.src.app.services.ml_suggestion.service import MlSuggestionService

from v1.src.db.repositories.ml_suggestion.dependencies import get_ml_suggestion_repo


async def build_ml_suggestion_service() -> AbsMlSuggestionService:
    ml_suggestion_repo = await get_ml_suggestion_repo()
    return MlSuggestionService(ml_suggestion_repo)
