from abc import ABC, abstractmethod

from v1.src.app.dto.document import DocumentDTO


class AbsDocumentRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_document(cls, data: DocumentDTO) -> DocumentDTO | None | Exception:
        raise NotImplementedError("create_document() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_document(cls, data: DocumentDTO) -> DocumentDTO | None | Exception:
        raise NotImplementedError("get_document() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_document(cls, data: DocumentDTO) -> DocumentDTO | None | Exception:
        raise NotImplementedError("update_document() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_document(cls, data: DocumentDTO) -> DocumentDTO | None | Exception:
        raise NotImplementedError("delete_document() must be implemented in subclass")
