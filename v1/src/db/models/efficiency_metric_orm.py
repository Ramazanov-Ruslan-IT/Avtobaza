"""efficiency_metrics - Показатели эффективности: расход топлива, пробег, стоимость на километр, простой. Вычисляется автоматически и используется в KPI."""
from datetime import datetime

from sqlalchemy import Integer, String, Float, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class EfficiencyMetricOrm(BaseOrm):
    __tablename__ = "efficiency_metrics"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    vehicle_id: Mapped[str] = mapped_column(ForeignKey("vehicles.id"), index=True)
    date: Mapped[datetime] = mapped_column(DateTime, index=True)
    fuel_consumed: Mapped[float] = mapped_column(Float)
    km_travelled: Mapped[float] = mapped_column(Float)
    cost_per_km: Mapped[float] = mapped_column(Float)
    idle_time_minutes: Mapped[int] = mapped_column(Integer)

    __table_args__ = (
        # Уникальность на vehicle_id+date: только одна метрика за одну дату на один автомобиль
        UniqueConstraint("vehicle_id", "date", name="uq_efficiency_vehicle_date"),
        # Композитный индекс — для аналитики метрик авто за период (графики/отчёты)
        Index("ix_efficiency_vehicle_date", "vehicle_id", "date"),
    )
