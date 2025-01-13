from app.core.database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    username = Column(String, primary_key=False, index=True)
    age = Column(Integer, primary_key=False, index=True)
    email = Column(String, primary_key=False, index=True, unique=True)
    password = Column(String, primary_key=False)
    is_active = Column(Boolean, default=True)
