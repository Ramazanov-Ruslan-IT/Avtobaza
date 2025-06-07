from v1.src.app.services.document.abs_service import AbsDocumentService
from v1.src.app.services.document.service import DocumentService

from v1.src.db.repositories.document.dependencies import get_document_repo


async def build_document_service() -> AbsDocumentService:
    document_repo = await get_document_repo()
    return DocumentService(document_repo)
