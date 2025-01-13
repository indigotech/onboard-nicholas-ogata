from starlette import status
from fastapi import APIRouter, HTTPException, Path
from app.api.user.schemas import UserRequest, UserResponse
from app.core.security import get_password_hash
from app.models import User
from app.core.utils import db_dependency

router = APIRouter()

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[UserResponse])
async def get_all_users(db: db_dependency):
    return db.query(User).all()

@router.get('/getByUsername/{username}', status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_by_username(db: db_dependency, username: str = Path(min_length=1)):
    user = db.query(User).filter(User.username == username).first()
    if user is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(db: db_dependency, user_request: UserRequest):
    hashed_password = get_password_hash(user_request.password)

    new_user = User(
        username=user_request.username,
        age=user_request.age,
        email=user_request.email,
        password=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
