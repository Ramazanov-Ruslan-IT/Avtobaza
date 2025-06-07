"""parts_inventory - Склад запчастей: наименование, код, категория, единица измерения, количество, порог пополнения. Управляет запасами для ремонта."""
from datetime import datetime

from sqlalchemy import Integer, String, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class PartInventoryOrm(BaseOrm):
    __tablename__ = "parts_inventory"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)  # поиск по наименованию
    part_number: Mapped[str] = mapped_column(String, index=True)  # уникальный номер детали
    category: Mapped[str] = mapped_column(String, index=True)
    unit: Mapped[str] = mapped_column(String)
    quantity: Mapped[int] = mapped_column(Integer)
    reorder_threshold: Mapped[int] = mapped_column(Integer)
    last_updated: Mapped[datetime] = mapped_column(DateTime, index=True)
    supplier_id: Mapped[str] = mapped_column(ForeignKey("suppliers.id"), index=True)

    __table_args__ = (
        # Уникальность детали по номеру и поставщику (или по номеру в целом, если он глобальный)
        UniqueConstraint("part_number", "supplier_id", name="uq_part_partnumber_supplier"),
        # Индекс для быстрого поиска дефицитных запчастей по категории и количеству
        Index("ix_parts_category_quantity", "category", "quantity"),
    )
