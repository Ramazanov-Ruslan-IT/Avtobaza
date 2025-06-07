"""gas_station_contracts - Договора между автобазой и АЗС. Хранит сроки действия и условия. Нужно для юридического и финансового управления поставками."""
from datetime import datetime

from sqlalchemy import String, Text, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class GasStationContractOrm(BaseOrm):
    __tablename__ = "gas_station_contracts"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    autobase_id: Mapped[str] = mapped_column(ForeignKey("autobases.id"), index=True)
    gas_station_id: Mapped[str] = mapped_column(ForeignKey("gas_stations.id"), index=True)
    start_date: Mapped[datetime] = mapped_column(DateTime, index=True)
    end_date: Mapped[datetime] = mapped_column(DateTime, index=True)
    terms: Mapped[str] = mapped_column(Text)

    __table_args__ = (
        # Уникальный договор между одной автобазой и одной АЗС за указанный срок
        UniqueConstraint("autobase_id", "gas_station_id", "start_date", name="uq_contract_autobase_gasstation_date"),
        # Композитный индекс для поиска всех активных контрактов определённой базы по АЗС и периоду
        Index("ix_contract_autobase_gasstation_period", "autobase_id", "gas_station_id", "start_date", "end_date"),
    )
