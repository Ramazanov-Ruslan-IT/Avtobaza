from datetime import datetime
from pydantic import BaseModel, ConfigDict

class GpsTrackCreateSchema(BaseModel):
    vehicle_id: str
    recorded_at: datetime
    latitude: float
    longitude: float
    speed_kmh: float
    event_type: str

    model_config = ConfigDict(from_attributes=True)

class GpsTrackGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class GpsTrackUpdateSchema(BaseModel):
    id: str
    vehicle_id: str | None = None
    recorded_at: datetime | None = None
    latitude: float | None = None
    longitude: float | None = None
    speed_kmh: float | None = None
    event_type: str | None = None

    model_config = ConfigDict(from_attributes=True)

class GpsTrackDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class GpsTrackResponseSchema1(BaseModel):
    id: str
    vehicle_id: str
    recorded_at: datetime
    latitude: float
    longitude: float
    speed_kmh: float
    event_type: str

    model_config = ConfigDict(from_attributes=True)

class GpsTrackResponseSchema2(GpsTrackResponseSchema1): pass
class GpsTrackResponseSchema3(GpsTrackResponseSchema1): pass
class GpsTrackResponseSchema4(GpsTrackResponseSchema1): pass
