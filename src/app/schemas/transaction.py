from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class TransactionBase(BaseModel):
    amount: Decimal
    category_id: Optional[int]
    description: Optional[str]
    is_recurring: Optional[bool] = False
    recurrence_interval: Optional[str] = None  # e.g. 'daily', 'monthly'
    next_recurrence_date: Optional[datetime]

class TransactionCreate(TransactionBase):
    receiver_id: int
    card_from_id: Optional[int]
    card_to_id: Optional[int]

class TransactionOut(TransactionBase):
    id: int
    sender_id: int
    receiver_id: int
    status: str
    date: datetime

    class Config:
        from_attributes = True