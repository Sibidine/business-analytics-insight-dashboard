from fastapi import APIRouter, status, HTTPException, Depends
from bson import ObjectId
from .. import schemas, database, models, token
from assets.database import asset_collection



router = APIRouter(
    prefix='/assets',
    tags=['assets']
)

@router.get('/all',status_code=status.HTTP_200_OK)
def read_all():
    query = schemas.list_serial_assets(asset_collection.find())
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'detail': f'assets do not exist'})
    return query


@router.get('/{id}',status_code=status.HTTP_200_OK)
def read_id(id: str):
    query = asset_collection.find_one({"_id": ObjectId(id)})
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'detail': f'asset with id {id} does not exist'})
    return schemas.individual_serial_assets(query)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str, get_current_user: models.users = Depends(token.get_current_user)):
    query = asset_collection.find_one_and_delete({"_id": ObjectId(id)})
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'detail': f'asset with id {id} does not exist'})


@router.post('/create',status_code=status.HTTP_201_CREATED)
def create(asset: schemas.asset, get_current_user: models.users = Depends(token.get_current_user)):
    inserted_result = asset_collection.insert_one(dict(asset))
    return {'detail': {'insertion': 'successful', 'id': f'{inserted_result.inserted_id}'}}
    

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id: str, asset: schemas.asset, get_current_user: models.users = Depends(token.get_current_user)):
    query = asset_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(asset)})
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'detail': f'asset with id {id} does not exist'})
