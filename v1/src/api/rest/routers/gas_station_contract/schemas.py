from datetime import datetime
from pydantic import BaseModel, ConfigDict

class GasStationContractCreateSchema(BaseModel):
    autobase_id: str
    gas_station_id: str
    start_date: datetime
    end_date: datetime
    terms: str

    model_config = ConfigDict(from_attributes=True)

class GasStationContractGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class GasStationContractUpdateSchema(BaseModel):
    id: str
    autobase_id: str | None = None
    gas_station_id: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    terms: str | None = None

    model_config = ConfigDict(from_attributes=True)

class GasStationContractDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class GasStationContractResponseSchema1(BaseModel):
    id: str
    autobase_id: str
    gas_station_id: str
    start_date: datetime
    end_date: datetime
    terms: str

    model_config = ConfigDict(from_attributes=True)

class GasStationContractResponseSchema2(GasStationContractResponseSchema1): pass
class GasStationContractResponseSchema3(GasStationContractResponseSchema1): pass
class GasStationContractResponseSchema4(GasStationContractResponseSchema1): pass
