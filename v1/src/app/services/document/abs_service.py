from abc import ABC, abstractmethod

from v1.src.app.dto.document import DocumentDTO


class AbsDocumentService(ABC):
    @abstractmethod
    async def create_document(self, data: DocumentDTO) -> DocumentDTO | None | Exception:
        pass

    @abstractmethod
    async def get_document(self, data: DocumentDTO) -> DocumentDTO | None | Exception:
        pass

    @abstractmethod
    async def update_document(self, data: DocumentDTO) -> DocumentDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_document(self, data: DocumentDTO) -> DocumentDTO | None | Exception:
        pass
