from typing import Annotated
import bcrypt
from sqlalchemy.orm import Session
from starlette import status
from fastapi import FastAPI, Depends
import models
from models import User
from database import engine, SessionLocal
from user import UserRequest, UserResponse

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/users', status_code=status.HTTP_200_OK, response_model=list[UserResponse])
async def get_all_users(db: db_dependency):
    return db.query(User).all()

@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(db: db_dependency, user_request: UserRequest):
    hashed_password = bcrypt.hashpw(user_request.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    new_user = User(
        name=user_request.name,
        age=user_request.age,
        email=user_request.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
