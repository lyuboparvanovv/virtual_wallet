from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, DECIMAL

from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class User(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True)
        username = Column(String(20), unique=True, nullable=False, index=True)
        password_hash = Column(String(255), nullable=False)
        email = Column(String(255), unique=True, nullable=False, index=True)
        phone = Column(String(10), unique=True, nullable=False, index=True)
        photo = Column(String, nullable=True)
        is_active = Column(Boolean, default=True)
        is_admin = Column(Boolean, default=False)
        is_approved = Column(Boolean, default=False)
        created_at = Column(DateTime, default=datetime.utcnow)

        cards = relationship("Card", back_populates="user", cascade="all, delete-orphan")
        transactions_sent = relationship("Transaction", foreign_keys='Transaction.sender_id', back_populates="sender")
        transactions_received = relationship("Transaction", foreign_keys='Transaction.receiver_id',
                                             back_populates="receiver")
        contacts = relationship("Contact", back_populates="owner", cascade="all, delete-orphan")
        categories = relationship("Category", back_populates="user", cascade="all, delete-orphan")