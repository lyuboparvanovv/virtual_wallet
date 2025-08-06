from app.models import Card
from app.schemas.card import CardCreate
from sqlalchemy.orm import Session


def get_card_by_number(db: Session, card_number: str):
    return db.query(Card).filter(Card.card_number == card_number).first()


def get_cards_by_user(db: Session, user_id: int):
    return db.query(Card).filter(Card.user_id == user_id).all()


def create_card(db: Session, user_id: int, card: CardCreate):
    db_card = Card(
        user_id=user_id,
        card_number=card.card_number,
        card_holder=card.card_holder,
        expiry_date=card.expiry_date,
        cvv=card.cvv,
        design=card.design
    )
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


def delete_card(db: Session, card_id: int, user_id: int):
    card = db.query(Card).filter(Card.id == card_id, Card.user_id == user_id).first()
    if card:
        db.delete(card)
        db.commit()
    return card
