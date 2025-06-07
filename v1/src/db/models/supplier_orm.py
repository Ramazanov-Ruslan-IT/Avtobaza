"""suppliers - Поставщики запчастей. Связан с parts_inventory. Содержит контакты, адрес, для автоматизации закупок."""

from sqlalchemy import String, Text, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class SupplierOrm(BaseOrm):
    __tablename__ = "suppliers"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    contact_email: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(Text)
