"""documents - Файлы, связанные с автомобилем: акты, путевые листы, накладные и пр. Указывает тип, ссылку на файл, кто загрузил."""
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class DocumentOrm(BaseOrm):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    vehicle_id: Mapped[str] = mapped_column(ForeignKey("vehicles.id"))
    doc_type: Mapped[str] = mapped_column(String)
    file_url: Mapped[str] = mapped_column(String)
    uploaded_by: Mapped[str] = mapped_column(ForeignKey("users.id"))
    uploaded_at: Mapped[datetime] = mapped_column(DateTime)
