from sqlalchemy.orm import Session
from app.api.user.service import get_by_email
from app.core.security import verify_password

async def authenticate(db: Session, email: str, password: str):
    user = await get_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
