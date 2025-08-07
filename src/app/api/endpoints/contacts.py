from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.user import get_user
from app.db.database import get_db
from app.dependancies.auth_d import get_current_user
from app.models import User, Contact
from app.schemas.contact import ContactOut, ContactCreate

router = APIRouter()


@router.post("/", response_model=ContactOut, status_code=status.HTTP_201_CREATED)
def add_contact(contact: ContactCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    contact_user = get_user(db, contact.contact_user_id)
    if not contact_user or contact_user.id == current_user.id:
        raise HTTPException(404, "Contact user not found or invalid")
    existing = db.query(Contact).filter(
        Contact.owner_id == current_user.id,
        Contact.contact_user_id == contact.contact_user_id,
    ).first()
    if existing:
        raise HTTPException(400, "Contact already exists")
    db_contact = Contact(owner_id=current_user.id, contact_user_id=contact.contact_user_id)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


@router.get("/", response_model=List[ContactOut])
def get_contacts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    contacts = db.query(Contact).filter(Contact.owner_id == current_user.id).all()
    return contacts


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(contact_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    contact = db.query(Contact).filter(Contact.id == contact_id, Contact.owner_id == current_user.id).first()
    if not contact:
        raise HTTPException(404, "Contact not found")
    db.delete(contact)
    db.commit()
    return
