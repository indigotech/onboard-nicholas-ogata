from datetime import datetime
from enum import Enum
from uuid import UUID
from pydantic import BaseModel, Field

class Origin(str, Enum):
    Contact = 'Contact'
    LLM = 'LLM'

class MessageRequest(BaseModel):
    origin: Origin
    content: str = Field(min_length=1, max_length=50)

    class Config:
        orm_mode = True

class MessageResponse(BaseModel):
    id: UUID
    origin: Origin
    content: str
    timestamp: datetime
    chat_id: UUID

    class Config:
        orm_mode = True
