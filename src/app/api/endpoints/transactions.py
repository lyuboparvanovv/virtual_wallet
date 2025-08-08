from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.crud.transaction import get_transactions_by_user
from app.db.database import get_db
from app.dependancies.auth_d import get_current_user
from app.models import User
from app.schemas.transaction import TransactionCreate, TransactionOut

router = APIRouter()

@router.post("/", response_model=TransactionOut, status_code=status.HTTP_201_CREATED)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if transaction.amount <= 0:
        raise HTTPException(400, "Amount must be positive")
    db_transaction = create_transaction(db, current_user.id, transaction)
    return db_transaction

@router.get("/", response_model=List[TransactionOut])
def get_transactions(
    skip: int = 0,
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    transactions = get_transactions_by_user(db, current_user.id, limit=limit, skip=skip)
    return transactions

