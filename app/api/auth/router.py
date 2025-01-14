from starlette import status
from datetime import timedelta
from app.api.auth.schema import Token
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.api.auth.service import authenticate
from app.core.config import settings
from app.core.security import create_access_token
from app.core.utils import db_dependency

router = APIRouter()

@router.post('/')
async def login(db: db_dependency, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = await authenticate(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={'sub': user.username}, expires_delta=access_token_expires)

    return Token(access_token=access_token, token_type='bearer') 
