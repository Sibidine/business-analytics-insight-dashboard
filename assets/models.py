from pydantic import BaseModel

class asset(BaseModel):
    asset_name: str
    asset_type: str
    location: str
    purchase_date: str
    initial_cost: int
    operational_status: str

class metrics(BaseModel):
    uptime: str
    downtime: str
    maintenance_cost: int
    failure_rate: float
    efficiency: float 