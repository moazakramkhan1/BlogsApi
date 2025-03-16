from fastapi import APIRouter,status,Depends,HTTPException
from typing import List
from .. import schemas,database,models
from sqlalchemy.orm import Session
from ..worker import blog
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def creatBlog(request:schemas.Blog, db:Session=Depends(database.get_db),get_current_user:schemas.User = Depends(get_current_user)):
    return blog.create(request,db)


@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.ShowBlog])
def getAllBlogs(db:Session=Depends(database.get_db),get_current_user:schemas.User = Depends(get_current_user)):
   return blog.All(db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def getBlog(id:int,db:Session=Depends(database.get_db),get_current_user:schemas.User = Depends(get_current_user)):
    return blog.Particular(id,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def deleteBlog(id:int,db:Session=Depends(database.get_db),get_current_user:schemas.User = Depends(get_current_user)):
    return blog.Delete(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def updateBlog(id:int,request:schemas.Blog,db:Session=Depends(database.get_db),get_current_user:schemas.User = Depends(get_current_user)):
   return blog.Update(id,db,request)
