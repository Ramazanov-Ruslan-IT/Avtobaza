from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ScheduledTaskCreateSchema(BaseModel):
    task_type: str
    target_entity: str
    entity_id: str
    cron_expression: str
    status: str
    last_run: datetime
    next_run: datetime

    model_config = ConfigDict(from_attributes=True)

class ScheduledTaskGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class ScheduledTaskUpdateSchema(BaseModel):
    id: str
    task_type: str | None = None
    target_entity: str | None = None
    entity_id: str | None = None
    cron_expression: str | None = None
    status: str | None = None
    last_run: datetime | None = None
    next_run: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class ScheduledTaskDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class ScheduledTaskResponseSchema1(BaseModel):
    id: str
    task_type: str
    target_entity: str
    entity_id: str
    cron_expression: str
    status: str
    last_run: datetime
    next_run: datetime

    model_config = ConfigDict(from_attributes=True)

class ScheduledTaskResponseSchema2(ScheduledTaskResponseSchema1): pass
class ScheduledTaskResponseSchema3(ScheduledTaskResponseSchema1): pass
class ScheduledTaskResponseSchema4(ScheduledTaskResponseSchema1): pass
