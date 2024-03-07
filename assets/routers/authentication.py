from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models
from ..database import users_collection
from .. import token

router = APIRouter(tags=['authentication'])

@router.post('/user/create')
def create_user(request: models.users, get_current_user: models.users = Depends(token.get_current_user)):
    password = token.Hash.bcrypt(request.password)
    users_collection.insert_one({"username":request.username, "password":password})


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends()):
    user = users_collection.find_one({"username": request.username})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"invalid credentials")
    if not token.Hash.verify(user["password"],request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"incorrect password")
       
    access_token = token.create_access_token(data={"sub": user["username"]})
    return {"access_token":access_token,"token_type": "bearer"}

