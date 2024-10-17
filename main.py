from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, Sessionlocal
from sqlalchemy.orm import Session


app = FastAPI()
# models.Base.metadata.create_all(bind=engine)
models.Base.metadata.create_all(bind = engine)

class PostBase(BaseModel):
    title: str
    content: str
    user_Id: int

class UserBase(BaseModel):
    #id: int
    username: str

def get_db():
    db = Sessionlocal()
    try: 
        yield db

    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/posts/{post_Id}", status_code= status.HTTP_200_OK)
async def read_post(post_Id: int, db: db_dependency):
    post = db.query(models.Post).filter(models.Post.id == post_Id).first()
    if post is None:
        HTTPException(status_code=404, detail='Post was not found')
    return post


@app.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase, db: db_dependency):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()

@app.delete("/posts/{post_Id}", status_code= status.HTTP_200_OK)
async def delete_post(post_Id: int, db: db_dependency):
    db_post = db.query(models.Post).filter(models.Post.id == post_Id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post was not found')
    db.delete(db_post)
    db.commit()


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()


@app.get("/users/{user_Id}", status_code= status.HTTP_201_CREATED)
async def read_user(user_Id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_Id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user

@app.delete("/users/{user_Id}", status_code= status.HTTP_200_OK)
async def delete_post(user_Id: int, db: db_dependency):
    db_user = db.query(models.User).filter(models.User.id == user_Id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User was not found')
    db.delete(db_user)
    db.commit()