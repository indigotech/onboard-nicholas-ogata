from uuid import UUID
from starlette import status
from fastapi import APIRouter, Depends
from app.api.chat.schemas import ChatResponse
from app.api.user.service import get_current_active_user
from app.core.utils import db_dependency
from app.models import Chat

router = APIRouter()

@router.post('/{id}', status_code=status.HTTP_201_CREATED, response_model=ChatResponse, dependencies=[Depends(get_current_active_user)])
async def create_chat(db: db_dependency, id: UUID):
    new_chat = Chat(contact_id=id)
    
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)

    return new_chat

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[ChatResponse], dependencies=[Depends(get_current_active_user)])
async def get_all_chats(db: db_dependency):
    return db.query(Chat).all()
