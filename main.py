from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from fastapi import FastAPI, Depends
import models
from models import User
from database import engine, SessionLocal
from user import User, UserRequest

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/')
async def welcome():
    return {'message': 'Hello World!'}

@app.get('/users', status_code=status.HTTP_200_OK)
async def get_all_users(db: db_dependency):
    return db.query(User).all()

@app.post('/users', status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_request: UserRequest):
    new_user = User(**user_request.model_dump())
    db.add(new_user)
    db.commit()
    return new_user
