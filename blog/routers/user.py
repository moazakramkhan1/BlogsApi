from fastapi import APIRouter,status,Depends
from typing import List
from .. import schemas,database
from sqlalchemy.orm import Session
from ..worker import user


router = APIRouter(
    prefix="/user",
    tags=['users']
)

@router.post('/',response_model=schemas.ShowUser)
def createUser(request:schemas.User,db:Session=Depends(database.get_db)):
   return user.Create(request,db)

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.ShowUser])
def getAllUsers(db:Session = Depends(database.get_db)):
    return user.All(db)


@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowUser)
def getUser(id:int,db:Session=Depends(database.get_db)):
    return user.Particular(id,db)