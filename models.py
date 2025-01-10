from database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, primary_key=False, index=True)
    age = Column(Integer, primary_key=False, index=True)
    email = Column(String, primary_key=False, index=True)
