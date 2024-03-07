from fastapi import APIRouter, status, HTTPException
from bson import ObjectId
from .. import schemas, database
from assets.database import asset_collection



router = APIRouter(
    prefix='/assets',
    tags=['assets']
)

@router.get('/all',status_code=status.HTTP_200_OK)
def read_all():
    return schemas.list_serial_assets(asset_collection.find())

@router.get('/{id}',status_code=status.HTTP_200_OK)
def read_id(id: str):
    return schemas.individual_serial_assets(asset_collection.find_one({"_id": ObjectId(id)}))

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str):
    asset_collection.find_one_and_delete({"_id": ObjectId(id)})

@router.post('/{id}',status_code=status.HTTP_201_CREATED)
def create(asset: schemas.asset):
    asset_collection.insert_one(dict(asset))

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id: str, asset: schemas.asset):
    asset_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(asset)})