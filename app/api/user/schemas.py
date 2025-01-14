from pydantic import BaseModel, Field
from uuid import UUID

class UserRequest(BaseModel):
    username: str = Field(min_length=1)
    birth_date: str = Field(min_length=1)
    email: str = Field(min_length=1)
    password: str = Field(min_length=8)

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: UUID
    username: str
    birth_date: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True
