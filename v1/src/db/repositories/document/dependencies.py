from v1.src.db.repositories.document.repo import DocumentRepo
from v1.src.db.repositories.document.abs_repo import AbsDocumentRepo


async def get_document_repo() -> AbsDocumentRepo:
    return DocumentRepo()
