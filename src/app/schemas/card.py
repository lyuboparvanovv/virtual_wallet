from datetime import datetime
from typing import Optional

from pydantic import BaseModel, constr


class CardBase(BaseModel):
    card_number: constr(pattern=r'^\d{16}$')
    card_holder: constr(min_length=2, max_length=30)
    expiry_date: datetime
    cvv: constr(pattern=r'^\d{3}$')
    design: Optional[str]

class CardCreate(CardBase):
    pass

class CardOut(CardBase):
    id: int

    class Config:
        from_attributes = True