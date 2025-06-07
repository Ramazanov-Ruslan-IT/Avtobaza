"""autobases - Представляет автобазы — территориальные подразделения компании. Хранит название, адрес, координаты, дату создания. С ними связаны автомобили, склады, задания и контракты."""

from sqlalchemy import String, Text, Float, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class AutobaseOrm(BaseOrm):
    __tablename__ = "autobases"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(Text)
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
