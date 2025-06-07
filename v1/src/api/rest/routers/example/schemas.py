from typing import Any
from pydantic import BaseModel


class ExampleCreateSchema(BaseModel):
    example: Any


class ExampleGetSchema(BaseModel):
    example: Any


class ExampleUpdateSchema(BaseModel):
    example: Any


class ExampleDeleteSchema(BaseModel):
    example: Any


class ExampleResponseSchema1(BaseModel):
    example: Any


class ExampleResponseSchema2(BaseModel):
    example: Any


class ExampleResponseSchema3(BaseModel):
    example: Any


class ExampleResponseSchema4(BaseModel):
    example: Any