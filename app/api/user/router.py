from typing import Annotated
from uuid import UUID
from starlette import status
from fastapi import APIRouter, Depends, HTTPException
from app.api.user.schemas import UserRequest, UserResponse
from app.api.user.service import get_current_active_user
from app.core.security import get_password_hash
from app.models import User
from app.core.utils import db_dependency

router = APIRouter()

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[UserResponse])
async def get_all_users(db: db_dependency):
    return db.query(User).all()

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_by_id(db: db_dependency, id: UUID):
    user = db.query(User).filter(User.id == id).first()
    if user is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

@router.get('/user/me', status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(db: db_dependency, user_request: UserRequest):
    hashed_password = get_password_hash(user_request.password)

    new_user = User(
        username=user_request.username,
        birth_date=user_request.birth_date,
        email=user_request.email,
        password=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
