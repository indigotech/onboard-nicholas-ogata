from datetime import date
from pydantic import BaseModel, Field
from uuid import UUID

from app.api.contact.schema import ContactResponse

class UserRequest(BaseModel):
    username: str = Field(min_length=1)
    birth_date: date
    email: str = Field(min_length=1)
    password: str = Field(min_length=8)

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: UUID
    username: str
    birth_date: date
    email: str
    is_active: bool
    contacts: list[ContactResponse] = []

    class Config:
        orm_mode = True
