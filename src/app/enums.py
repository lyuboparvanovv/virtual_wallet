from sqlalchemy import Enum

class CardType(Enum):
    debit = "debit"
    credit = "credit"

class UserRole(Enum):
    admin = "admin"
    user = "user"