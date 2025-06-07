"""documents - Файлы, связанные с автомобилем: акты, путевые листы, накладные и пр. Указывает тип, ссылку на файл, кто загрузил."""
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class DocumentOrm(BaseOrm):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    vehicle_id: Mapped[str] = mapped_column(ForeignKey("vehicles.id"), index=True)
    doc_type: Mapped[str] = mapped_column(String, index=True)
    file_url: Mapped[str] = mapped_column(String)
    uploaded_by: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    uploaded_at: Mapped[datetime] = mapped_column(DateTime, index=True)

    __table_args__ = (
        # Уникальное ограничение — на один автомобиль и один тип документа не может быть дубликатов (например, только один оригинал ПТС)
        UniqueConstraint("vehicle_id", "doc_type", "file_url", name="uq_vehicle_doctype_file"),
        # Композитный индекс для частого поиска документов по типу и авто
        Index("ix_documents_vehicle_doctype", "vehicle_id", "doc_type"),
        # Индекс для быстрого поиска всех документов, загруженных пользователем в период
        Index("ix_documents_uploadedby_date", "uploaded_by", "uploaded_at"),
    )
