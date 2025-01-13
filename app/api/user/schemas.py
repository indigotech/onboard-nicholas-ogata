from pydantic import BaseModel, Field
from uuid import UUID

class UserRequest(BaseModel):
    username: str = Field(min_length=1)
    age: int = Field(ge=18)
    email: str = Field(min_length=1)
    password: str = Field(min_length=8)

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: UUID
    name: str
    age: int
    email: str

    class Config:
        orm_mode = True
