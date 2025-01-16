from uuid import UUID
from starlette import status
from fastapi import APIRouter, Depends, HTTPException
from app.api.message.schemas import MessageRequest, MessageResponse
from app.api.user.service import get_current_active_user
from app.core.utils import db_dependency
from fastapi import APIRouter
from app.models import Message

router = APIRouter()

@router.post('/{id}', status_code=status.HTTP_201_CREATED, response_model=MessageResponse, dependencies=[Depends(get_current_active_user)])
async def create_message(db: db_dependency, contact_request: MessageRequest, id: UUID):
    new_message = Message(origin=contact_request.origin,
                          content=contact_request.content,
                          chat_id=id
                          )
    
    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    return new_message

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[MessageResponse], dependencies=[Depends(get_current_active_user)])
async def get_all_messages(db: db_dependency):
    return db.query(Message).all()

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=MessageResponse, dependencies=[Depends(get_current_active_user)])
async def get_message_by_id(db: db_dependency, id: UUID):
    message = db.query(Message).filter(Message.id == id).first()
    if message is not None:
        return message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Message not found')
