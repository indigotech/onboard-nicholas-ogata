from sqlalchemy.orm import Session
from app.api.user.service import get_by_username
from app.core.security import verify_password

async def authenticate(db: Session, username: str, password: str):
    user = await get_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
