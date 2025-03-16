from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import schemas,models
from .. hashing import Hash

def Create(request:schemas.User,db:Session):
    newUser = models.User(name=request.name,email=request.email,password=Hash.hashPwd(request.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

def All(db:Session):
    users = db.query(models.User).all()
    return users

def Particular(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with this {id} not found")
    return user