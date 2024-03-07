from fastapi import APIRouter
from bson import ObjectId
from .. import schemas, database, repository
from assets.database import metrics_collection



router = APIRouter(
    prefix='/metrics',
    tags=['metrics']
)

@router.get('/all')
def read_all():
    return schemas.list_serial_metrics(metrics_collection.find())

@router.get('/{id}')
def read_id(id: str):
    return schemas.individual_serial_metrics(metrics_collection.find_one({"_id": ObjectId(id)}))

@router.delete('/{id}')
def delete(id: str):
    metrics_collection.find_one_and_delete({"_id": ObjectId(id)})

@router.post('/{id}')
def create(metrics: schemas.metric):
    metrics_collection.insert_one(dict(metrics))

@router.put('/{id}')
def update(id: str, metrics: schemas.metric):
    metrics_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(metrics)})

@router.get('/insights/downtime')
def downtime():
    metrics = schemas.list_serial_metrics(metrics_collection.find())
    return {"total_downtime": repository.get_total_downtime(metrics)}

@router.get('/insights/maintenance')
def maintenance():
    metrics = schemas.list_serial_metrics(metrics_collection.find())
    return {"total_maintenance_cost": repository.get_maintenance_cost(metrics)}

@router.get('insights/failures')
def high_failure_rates():
    metrics = schemas.list_serial_metrics(metrics_collection.find())
    return {"high_failure_rate_assets": repository.get_high_failure_assets(metrics)}
