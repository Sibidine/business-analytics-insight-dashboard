from fastapi import APIRouter
from bson import ObjectId
from .. import schemas, database, repository
from assets.database import metrics_collection



router = APIRouter(
    prefix='/metrics/insights',
    tags=['insights']
)

@router.get('/downtime')
def downtime():
    metrics = schemas.list_serial_metrics(metrics_collection.find())
    return {"total_downtime": repository.get_total_downtime(metrics)}

@router.get('/maintenance')
def maintenance():
    metrics = schemas.list_serial_metrics(metrics_collection.find())
    return {"total_maintenance_cost": repository.get_maintenance_cost(metrics)}

@router.get('/failures')
def high_failure_rates():
    metrics = schemas.list_serial_metrics(metrics_collection.find())
    return {"high_failure_rate_assets": repository.get_high_failure_assets(metrics)}
