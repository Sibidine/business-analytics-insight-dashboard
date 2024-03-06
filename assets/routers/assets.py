from fastapi import APIRouter
from bson import ObjectId
from assets import schemas, database


router = APIRouter(
    prefix='/assets',
    tags=['assets']
)

@router.get('/{id}')
def read(id: int):
    return {'asset number':f'test output {id}'}

@router.delete('/{id}')
def delete():
    return {'asset number': f'remove test {id}'}

@router.post('/{id}')
def create():
    return {'asset number': f'create test {id}'}

@router.put('/{id}')
def update():
    return {'asset number': f'remove test {id}'}