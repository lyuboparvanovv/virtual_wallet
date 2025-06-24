from sqlalchemy import Column, Integer, String
from src.app.db.base import Base
from src.app.enums import CardType


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    card_number = Column(String(20), nullable=False)
    exp_date = Column(String(20), nullable=False)
    card_holder = Column(String(30), nullable=False)
    cvv = Column(String(3), nullable=False)
    card_type = Column(CardType, nullable=False)

    # user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    # owner = relationship("User", back_populates="cards")
