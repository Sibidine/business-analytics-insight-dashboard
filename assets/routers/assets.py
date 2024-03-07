from fastapi import APIRouter
from bson import ObjectId
from .. import schemas, database
from assets.database import asset_collection, metrics_collection



router = APIRouter(
    prefix='/assets',
    tags=['assets']
)

@router.get('/{id}')
def read(id: int):
    return schemas.list_serial_assets(asset_collection.find())

@router.delete('/{id}')
def delete():
    return {'asset number': f'remove test {id}'}

@router.post('/{id}')
def create():
    return {'asset number': f'create test {id}'}

@router.put('/{id}')
def update():
    return {'asset number': f'remove test {id}'}