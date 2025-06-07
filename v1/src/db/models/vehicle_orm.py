"""vehicles - Основная таблица с транспортными средствами: номер, марка, модель, тип кузова, VIN, пробег, состояние. Привязаны к автобазе и типу топлива. Используется в логистике, обслуживании, заправках."""

from sqlalchemy import String, Float, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class VehicleOrm(BaseOrm):
    __tablename__ = "vehicles"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    license_plate: Mapped[str] = mapped_column(String, index=True)
    brand: Mapped[str] = mapped_column(String, index=True)
    model: Mapped[str] = mapped_column(String, index=True)
    body_type: Mapped[str] = mapped_column(String, index=True)
    vin: Mapped[str] = mapped_column(String, index=True)
    fuel_type_id: Mapped[int] = mapped_column(ForeignKey("fuel_types.id"), index=True)
    autobase_id: Mapped[str] = mapped_column(ForeignKey("autobases.id"), index=True)
    status: Mapped[str] = mapped_column(String, index=True)
    mileage: Mapped[float] = mapped_column(Float, index=True)

    __table_args__ = (
        # Госномер уникален в рамках всей базы
        UniqueConstraint("license_plate", name="uq_vehicle_license_plate"),
        # VIN уникален (международный идентификатор)
        UniqueConstraint("vin", name="uq_vehicle_vin"),
        # Композитный индекс для быстрого поиска по типу топлива и базе
        Index("ix_vehicle_fuel_autobase", "fuel_type_id", "autobase_id"),
    )
