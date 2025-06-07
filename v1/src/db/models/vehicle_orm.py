"""vehicles - Основная таблица с транспортными средствами: номер, марка, модель, тип кузова, VIN, пробег, состояние. Привязаны к автобазе и типу топлива. Используется в логистике, обслуживании, заправках."""

from sqlalchemy import String, Float, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class VehicleOrm(BaseOrm):
    __tablename__ = "vehicles"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    license_plate: Mapped[str] = mapped_column(String, index=True)
    brand: Mapped[str] = mapped_column(String)
    model: Mapped[str] = mapped_column(String)
    body_type: Mapped[str] = mapped_column(String)
    vin: Mapped[str] = mapped_column(String)
    fuel_type_id: Mapped[int] = mapped_column(ForeignKey("fuel_types.id"), index=True)
    autobase_id: Mapped[str] = mapped_column(ForeignKey("autobases.id"), index=True)
    status: Mapped[str] = mapped_column(String)
    mileage: Mapped[float] = mapped_column(Float)
