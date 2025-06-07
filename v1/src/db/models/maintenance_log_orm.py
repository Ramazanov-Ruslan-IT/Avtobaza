"""maintenance_logs - История техобслуживания машин: что, когда, за сколько, на каком пробеге, кто провёл. Помогает планировать ТО и контролировать техсостояние."""
from datetime import datetime

from sqlalchemy import String, Text, Float, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class MaintenanceLogOrm(BaseOrm):
    __tablename__ = "maintenance_logs"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    vehicle_id: Mapped[str] = mapped_column(ForeignKey("vehicles.id"), index=True)
    maintenance_type: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(Text)
    cost: Mapped[float] = mapped_column(Float)
    performed_at: Mapped[datetime] = mapped_column(DateTime, index=True)
    mileage_at_maintenance: Mapped[float] = mapped_column(Float, index=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)

    __table_args__ = (
        # Уникальность для ТО на авто по дате и типу (исключает дублировки)
        UniqueConstraint("vehicle_id", "maintenance_type", "performed_at", name="uq_maintenance_vehicle_type_time"),
        # Индекс для выборки истории всех ТО по авто и типу
        Index("ix_maintenance_vehicle_type", "vehicle_id", "maintenance_type"),
        # Индекс для анализа пробега по ТО
        Index("ix_maintenance_vehicle_mileage", "vehicle_id", "mileage_at_maintenance"),
    )
