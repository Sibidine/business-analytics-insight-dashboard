from pydantic import BaseModel

class asset(BaseModel):
    asset_name: str
    asset_type: str
    location: str
    purchase_date: str
    initial_cost: int
    operational_status: str

class metric(BaseModel):
    asset_id: str
    uptime: str
    downtime: str
    maintenance_cost: int
    failure_rate: float
    efficiency: float 

class users(BaseModel):
    username: str
    password: str

class user_in_db(users):
    hashed_password: str

class token(BaseModel):
    access_token: str
    token_type: str

class token_data(BaseModel):
    username: str or None = None
