from sqlalchemy import select

from v1.src.db.settings.connection.postgresql import get_sessionmaker
from v1.src.app.utils.mapper import dto_to_orm, orm_to_dto

from v1.src.db.repositories.efficiency_metric.abs_repo import AbsEfficiencyMetricRepo
from v1.src.db.models.efficiency_metric_orm import EfficiencyMetricOrm
from v1.src.app.dto.efficiency_metric import EfficiencyMetricDTO


class EfficiencyMetricRepo(AbsEfficiencyMetricRepo):
    @classmethod
    async def create_efficiency_metric(cls, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = dto_to_orm(EfficiencyMetricOrm, data)
            session.add(orm)
            await session.flush()
            await session.commit()
            await session.refresh(orm)
            return orm_to_dto(EfficiencyMetricDTO, orm)

    @classmethod
    async def get_efficiency_metric(cls, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            result = await session.execute(select(EfficiencyMetricOrm).where(EfficiencyMetricOrm.id == data.id))
            orm = result.scalar_one_or_none()
            return orm_to_dto(EfficiencyMetricDTO, orm) if orm else None

    @classmethod
    async def update_efficiency_metric(cls, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(EfficiencyMetricOrm, data.id)
            if not orm:
                return None
            for field, value in data.__dict__.items():
                setattr(orm, field, value)
            await session.commit()
            return orm_to_dto(EfficiencyMetricDTO, orm)

    @classmethod
    async def delete_efficiency_metric(cls, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        new_postgresql_session = get_sessionmaker()
        async with new_postgresql_session() as session:
            orm = await session.get(EfficiencyMetricOrm, data.id)
            if not orm:
                return None
            await session.delete(orm)
            await session.commit()
            return orm_to_dto(EfficiencyMetricDTO, orm)
