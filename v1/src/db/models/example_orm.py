from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class ExampleOrm(BaseOrm):
    __tablename__ = "examples"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
