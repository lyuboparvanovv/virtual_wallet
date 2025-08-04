from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, DECIMAL

from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    card_from_id = Column(Integer, ForeignKey("cards.id"), nullable=True)
    card_to_id = Column(Integer, ForeignKey("cards.id"), nullable=True)

    amount = Column(DECIMAL(15, 2), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    status = Column(String(20), default="pending")
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    description = Column(String(255), nullable=True)

    is_recurring = Column(Boolean, default=False)
    recurrence_interval = Column(String(20), nullable=True)
    next_recurrence_date = Column(DateTime, nullable=True)

    sender = relationship("User", foreign_keys=[sender_id], back_populates="transactions_sent")
    receiver = relationship("User", foreign_keys=[receiver_id], back_populates="transactions_received")
    category = relationship("Category", back_populates="transactions")

    card_from = relationship("Card", foreign_keys=[card_from_id])
    card_to = relationship("Card", foreign_keys=[card_to_id])