from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID

class UserRequest(BaseModel):
    id: Optional[UUID] = None
    name: str = Field(min_length=1)
    age: int = Field(ge=18)
    email: str = Field(min_length=1)

    class Config:
        orm_mode = True
