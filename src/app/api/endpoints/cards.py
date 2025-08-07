from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List

from app.crud.card import create_card, get_card_by_number, get_cards_by_user, delete_card
from app.db.database import get_db
from app.dependancies.auth_d import get_current_user
from app.models import User
from app.schemas.card import CardOut, CardCreate

router = APIRouter()

@router.post("/", response_model=CardOut, status_code=status.HTTP_201_CREATED)
def add_card(card: CardCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if get_card_by_number(db, card.card_number):
        raise HTTPException(400, "Card number already exists")
    db_card = create_card(db, current_user.id, card)
    return db_card

@router.get("/", response_model=List[CardOut])
def get_cards(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_cards_by_user(db, current_user.id)

@router.delete("/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cardd(card_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    card = delete_card(db, card_id, current_user.id)
    if not card:
        raise HTTPException(404, "Card not found")
    return