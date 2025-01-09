from typing import Optional
from pydantic import BaseModel, Field

class User:
    id: int
    name: str
    age: int
    email: str

    def __init__(self, id, name, age, email):
        self.id = id
        self.name = name
        self.age = age
        self.email = email

class UserRequest(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=1)
    age: int = Field(ge=18)
    email: str = Field(min_length=1)
