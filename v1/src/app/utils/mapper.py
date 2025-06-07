from dataclasses import fields
from pydantic import BaseModel
from typing import Type, Any


def pydantic_to_dto(dto_cls: Type, pydantic_obj: BaseModel):
    data = pydantic_obj.dict()
    dto_fields = {f.name for f in fields(dto_cls)}
    filtered_data = {k: v for k, v in data.items() if k in dto_fields}
    return dto_cls(**filtered_data)


def dto_to_pydantic(pydantic_cls: Type[BaseModel], dto_obj: Any):
    data = {f.name: getattr(dto_obj, f.name) for f in fields(dto_obj)}
    return pydantic_cls(**data)


def dto_to_orm(orm_cls: Type, dto_obj: Any):
    data = {f.name: getattr(dto_obj, f.name) for f in fields(dto_obj)}
    return orm_cls(**data)


def orm_to_dto(dto_cls: Type, orm_obj: Any):
    dto_fields = {f.name for f in fields(dto_cls)}
    data = {k: getattr(orm_obj, k) for k in dto_fields if hasattr(orm_obj, k)}
    return dto_cls(**data)
