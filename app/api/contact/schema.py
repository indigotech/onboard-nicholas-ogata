from pydantic import BaseModel, Field
from uuid import UUID

class ContactRequest(BaseModel):
    name: str = Field(min_length=1)
    cpf: str = Field(min_length=1)
    phone: str = Field(min_length=1)
    
    class Config:
        orm_mode = True

class ContactResponse(BaseModel):
    id: UUID
    name: str
    cpf: str
    phone: str
    
    class Config:
        orm_mode = True
