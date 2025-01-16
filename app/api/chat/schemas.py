from uuid import UUID
from pydantic import BaseModel

class ChatResponse(BaseModel):
    id: UUID
    contact_id: UUID

    class Config:
        orm_mode = True
