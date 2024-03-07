from fastapi import APIRouter, status, HTTPException
from bson import ObjectId
from .. import schemas, database, repository
from assets.database import metrics_collection



router = APIRouter(
    prefix='/metrics',
    tags=['metrics']
)

@router.get('/all', status_code=status.HTTP_200_OK)
def read_all():
    return schemas.list_serial_metrics(metrics_collection.find())

@router.get('/{id}', status_code=status.HTTP_200_OK)
def read_id(id: str):
    return schemas.individual_serial_metrics(metrics_collection.find_one({"_id": ObjectId(id)}))

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str):
    metrics_collection.find_one_and_delete({"_id": ObjectId(id)})

@router.post('/{id}', status_code= status.HTTP_201_CREATED)
def create(metrics: schemas.metric):
    metrics_collection.insert_one(dict(metrics))

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: str, metrics: schemas.metric):
    metrics_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(metrics)})

