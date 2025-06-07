"""parts_inventory - Склад запчастей: наименование, код, категория, единица измерения, количество, порог пополнения. Управляет запасами для ремонта."""
from datetime import datetime

from sqlalchemy import Integer, String, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class PartInventoryOrm(BaseOrm):
    __tablename__ = "parts_inventory"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    part_number: Mapped[str] = mapped_column(String)
    category: Mapped[str] = mapped_column(String)
    unit: Mapped[str] = mapped_column(String)
    quantity: Mapped[int] = mapped_column(Integer)
    reorder_threshold: Mapped[int] = mapped_column(Integer)
    last_updated: Mapped[datetime] = mapped_column(DateTime)
    supplier_id: Mapped[str] = mapped_column(ForeignKey("suppliers.id"))
