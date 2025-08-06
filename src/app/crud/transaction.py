from app.models import Transaction
from sqlalchemy.orm import Session

from app.schemas.transaction import TransactionCreate


def create_transaction(db: Session, sender_id: int, transaction: TransactionCreate):
    db_transaction = Transaction(
        sender_id=sender_id,
        receiver_id=transaction.receiver_id,
        amount=transaction.amount,
        category_id=transaction.category_id,
        description=transaction.description,
        is_recurring=transaction.is_recurring or False,
        recurrence_interval=transaction.recurrence_interval,
        next_recurrence_date=transaction.next_recurrence_date,
        card_from_id=transaction.card_from_id,
        card_to_id=transaction.card_to_id,
        status="pending"
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transactions_by_user(db: Session, user_id: int, limit: int = 10, skip: int = 0):
    return db.query(Transaction).filter(
        (Transaction.sender_id == user_id) | (Transaction.receiver_id == user_id)
    ).order_by(Transaction.date.desc()).offset(skip).limit(limit).all()
