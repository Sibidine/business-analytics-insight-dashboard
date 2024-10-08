from fastapi import APIRouter,status,HTTPException
from bson import ObjectId
from .. import schemas, database, repository
from assets.database import metrics_collection



router = APIRouter(
    prefix='/metrics/insights',
    tags=['insights']
)

@router.get('/downtime',status_code=status.HTTP_200_OK)
def downtime():
    metrics = schemas.list_serial_metrics(metrics_collection.find())
    if not metrics:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'detail': 'empty collection'})

    return {"total_downtime": repository.get_total_downtime(metrics)}

@router.get('/maintenance',status_code=status.HTTP_200_OK)
def maintenance():
    metrics = schemas.list_serial_metrics(metrics_collection.find())
    if not metrics:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'detail': 'empty collection'})
    return {"total_maintenance_cost": repository.get_maintenance_cost(metrics)}

@router.get('/failures',status_code=status.HTTP_200_OK)
def high_failure_rates():
    metrics = schemas.list_serial_metrics(metrics_collection.find())
    if not metrics:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'detail': 'empty collection'})
    return {"high_failure_rate_assets": repository.get_high_failure_assets(metrics)}
