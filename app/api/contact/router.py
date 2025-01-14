from starlette import status
from typing import Annotated
from fastapi import APIRouter, Depends
from app.api.contact.schema import ContactRequest, ContactResponse
from app.api.user.service import get_current_active_user
from app.core.utils import db_dependency
from app.models import Contact, User

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ContactResponse, dependencies=[Depends(get_current_active_user)])
async def create_contact(db: db_dependency, contact_request: ContactRequest):
    new_contact = Contact(name=contact_request.name,
                          cpf=contact_request.cpf,
                          phone=contact_request.phone,
                          )
    
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)

    return new_contact

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[ContactResponse], dependencies=[Depends(get_current_active_user)])
async def get_all_contacts(db: db_dependency):
    return db.query(Contact).all()
