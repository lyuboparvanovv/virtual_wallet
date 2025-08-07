from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List

from app.crud.card import create_card, get_card_by_number
from app.db.session import get_db
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

