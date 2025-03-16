from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import schemas,models

def create(request:schemas.Blog,db:Session):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def All(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def Particular(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with the {id} was not found")
    return blog

def Delete(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with the {id} was not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail':'delete operation successful'}

def Update(id:int,db:Session,request:schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with the {id} was not found")
    blog.update(request.dict(),synchronize_session=False)
    db.commit()
    return {'detail':'updated successfully'}
