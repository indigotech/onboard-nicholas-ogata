from uuid import UUID
from starlette import status
from fastapi import APIRouter, Depends, HTTPException
from app.api.contact.schema import ContactRequest, ContactResponse
from app.api.user.service import get_current_active_user
from app.core.utils import db_dependency
from app.models import Contact

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

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ContactResponse, dependencies=[Depends(get_current_active_user)])
async def get_by_id(db: db_dependency, id: UUID):
    contact = db.query(Contact).filter(Contact.id == id).first()
    if contact is not None:
        return contact
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact not found')

@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=ContactResponse, dependencies=[Depends(get_current_active_user)])
async def update_contact(db: db_dependency, contact_request: ContactRequest, id: UUID):
    contact = db.query(Contact).filter(Contact.id == id).first()
    if contact is not None:
        for var, value in vars(contact_request).items():
            setattr(contact, var, value) if value else None
        db.commit()
        db.refresh(contact)

        return contact
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact not found')

@router.delete('/{id}', status_code=status.HTTP_200_OK, dependencies=[Depends(get_current_active_user)])
async def delete_contact(db: db_dependency, id: UUID):
    contact = db.query(Contact).filter(Contact.id == id).first()
    if contact is not None:
        db.delete(contact)
        db.commit()
        return
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact not found')
