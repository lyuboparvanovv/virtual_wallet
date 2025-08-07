from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    card_number = Column(String(16), unique=True, nullable=False, index=True)
    card_holder = Column(String(30), nullable=False)
    expiry_date = Column(DateTime, nullable=False)
    cvv = Column(String(3), nullable=False)
    design = Column(String(255), nullable=True)

    user = relationship("User", back_populates="cards")