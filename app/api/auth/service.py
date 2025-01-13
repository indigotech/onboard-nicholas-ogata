from sqlalchemy.orm import Session
from app.api.user.router import get_by_username
from app.core.security import verify_password

def authenticate(db: Session, username: str, password: str):
    user = get_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
