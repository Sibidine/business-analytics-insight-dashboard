from fastapi import APIRouter, status, HTTPException, Depends
from bson import ObjectId
from .. import schemas, database, repository, token, models
from assets.database import metrics_collection



router = APIRouter(
    prefix='/metrics',
    tags=['metrics']
)

@router.get('/all', status_code=status.HTTP_200_OK)
def read_all():
    query = schemas.list_serial_metrics(metrics_collection.find())
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'detail': f'empty collection'})
    return query

@router.get('/{id}', status_code=status.HTTP_200_OK)
def read_id(id: str):
    query = metrics_collection.find_one({"_id": ObjectId(id)})
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'detail': f'metric with {id} does not exist'})
    return schemas.individual_serial_metrics(query)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str,get_current_user: models.users = Depends(token.get_current_user)):
    query = metrics_collection.find_one_and_delete({"_id": ObjectId(id)})
    query = metrics_collection.find_one({"_id": ObjectId(id)})
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'detail': f'metric with {id} does not exist'})

@router.post('/create/{id}', status_code= status.HTTP_201_CREATED)
def create_using_asset_id(metrics: schemas.metric,get_current_user: models.users = Depends(token.get_current_user)):
    query = metrics_collection.find_one({"_id": ObjectId(id)})
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'detail': f'asset with {id} does not exist'})
 
    metrics_collection.insert_one(dict(metrics))
    

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: str, metrics: schemas.metric,get_current_user: models.users = Depends(token.get_current_user)):
    query=metrics_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(metrics)})
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'detail': f'metric with {id} does not exist'})

