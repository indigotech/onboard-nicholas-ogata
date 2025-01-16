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

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, primary_key=False, index=True)
    cpf = Column(String, primary_key=False, index=True)
    phone = Column(String, primary_key=False, index=True)
    chats = relationship('Chat', back_populates='contact', cascade='all, delete-orphan')

class Chat(Base):
    __tablename__ = 'chats'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    contact_id = Column(UUID(as_uuid=True), ForeignKey('contacts.id'))
    contact = relationship('Contact', back_populates='chats')
