from app.core.database import Base
from sqlalchemy import Column, ForeignKey, String, Boolean, Date
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    username = Column(String, primary_key=False, index=True)
    birth_date = Column(Date, primary_key=False, index=True)
    email = Column(String, primary_key=False, index=True, unique=True)
    password = Column(String, primary_key=False)
    is_active = Column(Boolean, default=True)
    contacts = relationship('Contact', back_populates='user', cascade='all, delete-orphan')

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, primary_key=False, index=True)
    cpf = Column(String, primary_key=False, index=True)
    phone = Column(String, primary_key=False, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship('User', back_populates='contacts')
