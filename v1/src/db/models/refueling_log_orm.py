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
    refueled_at: Mapped[datetime] = mapped_column(DateTime)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    mileage_at_refuel: Mapped[float] = mapped_column(Float)
