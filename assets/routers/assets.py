from fastapi import APIRouter
from bson import ObjectId
from .. import schemas, database
from assets.database import asset_collection, metrics_collection



router = APIRouter(
    prefix='/assets',
    tags=['assets']
)

@router.get('/all')
def read_all():
    return schemas.list_serial_assets(asset_collection.find())

@router.get('/{id}')
def read_id(id: str):
    return schemas.individual_serial_assets(asset_collection.find_one({"_id": ObjectId(id)}))

@router.delete('/{id}')
def delete(id: str):
    asset_collection.find_one_and_delete({"_id": ObjectId(id)})

@router.post('/{id}')
def create(asset: schemas.asset):
    asset_collection.insert_one(dict(asset))

@router.put('/{id}')
def update(id: str, asset: schemas.asset):
    asset_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(asset)})