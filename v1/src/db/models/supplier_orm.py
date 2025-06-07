"""suppliers - Поставщики запчастей. Связан с parts_inventory. Содержит контакты, адрес, для автоматизации закупок."""

from sqlalchemy import String, Text, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class SupplierOrm(BaseOrm):
    __tablename__ = "suppliers"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    contact_email: Mapped[str] = mapped_column(String, index=True)
    phone: Mapped[str] = mapped_column(String, index=True)
    address: Mapped[str] = mapped_column(Text)

    __table_args__ = (
        # Уникальный поставщик по имени и email (или только по email, если email уникален)
        UniqueConstraint("name", "contact_email", name="uq_supplier_name_email"),
    )
