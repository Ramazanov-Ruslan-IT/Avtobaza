"""refueling_logs - Журнал всех заправок: кто, когда, где, сколько, на какую сумму. Также сохраняет пробег машины на момент заправки. Используется для отчётности, контроля расходов и аудита."""
from datetime import datetime

from sqlalchemy import String, Float, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class RefuelingLogOrm(BaseOrm):
    __tablename__ = "refueling_logs"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    vehicle_id: Mapped[str] = mapped_column(ForeignKey("vehicles.id"), index=True)
    gas_station_id: Mapped[str] = mapped_column(ForeignKey("gas_stations.id"), index=True)
    fuel_type_id: Mapped[int] = mapped_column(ForeignKey("fuel_types.id"), index=True)
    litres: Mapped[float] = mapped_column(Float)
    total_cost: Mapped[float] = mapped_column(Float)
    refueled_at: Mapped[datetime] = mapped_column(DateTime, index=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    mileage_at_refuel: Mapped[float] = mapped_column(Float, index=True)

    __table_args__ = (
        # Уникальность заправки для машины в конкретный момент времени (исключает дублировки)
        UniqueConstraint("vehicle_id", "refueled_at", name="uq_refuel_vehicle_time"),
        # Композитный индекс для быстрого поиска заправок по машине и времени
        Index("ix_refuel_vehicle_time", "vehicle_id", "refueled_at"),
        # Индекс для анализа заправок по АЗС и топливу (например, для построения отчётов по АЗС)
        Index("ix_refuel_station_fuel", "gas_station_id", "fuel_type_id"),
    )
