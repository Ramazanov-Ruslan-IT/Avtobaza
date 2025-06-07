from v1.src.app.services.document.abs_service import AbsDocumentService
from v1.src.db.repositories.document import AbsDocumentRepo
from v1.src.app.dto.document import DocumentDTO


class DocumentService(AbsDocumentService):
    def __init__(self, document_repo: AbsDocumentRepo):
        self.document_repo = document_repo

    async def create_document(self, data: DocumentDTO) -> DocumentDTO | None | Exception:
        return await self.document_repo.create_document(data)

    async def get_document(self, data: DocumentDTO) -> DocumentDTO | None | Exception:
        result = await self.document_repo.get_document(data)
        if not result:
            raise ValueError("Document not found")
        return result

    async def update_document(self, data: DocumentDTO) -> DocumentDTO | None | Exception:
        result = await self.document_repo.update_document(data)
        if not result:
            raise ValueError("Cannot update: document not found")
        return result

    async def delete_document(self, data: DocumentDTO) -> DocumentDTO | None | Exception:
        result = await self.document_repo.delete_document(data)
        if not result:
            raise ValueError("Cannot delete: document not found")
        return result
