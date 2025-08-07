from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.db.database import Base


def utc_now():
    return datetime.now(timezone.utc)

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
    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)
    cards = relationship("Card", back_populates="user", cascade="all, delete-orphan")
    transactions_sent = relationship("Transaction", foreign_keys='Transaction.sender_id', back_populates="sender")
    transactions_received = relationship("Transaction", foreign_keys='Transaction.receiver_id',
                                         back_populates="receiver")
    contacts = relationship("Contact",back_populates="owner",foreign_keys="Contact.owner_id", cascade="all, delete-orphan"
    )
    categories = relationship("Category", back_populates="user", cascade="all, delete-orphan")
