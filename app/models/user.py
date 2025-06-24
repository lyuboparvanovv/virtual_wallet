# from sqlalchemy import Column, Integer, String, Boolean, DateTime
# from app.db.base import Base
#
#
# class User(Base):
#
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     username = Column(String(100), unique=True, nullable=False)
#     first_name = Column(String(100), nullable=False)
#     last_name = Column(String(100), nullable=False)
#     email = Column(String, unique=True, nullable=False)
#     phone_number = Column(String(20), unique=True, nullable=False)
#     country = Column(String(100), nullable=False)
#     city = Column(String(100), nullable=False)
#     password = Column(String(100), nullable=False)
#     is_active = Column(Boolean, default=True)
#     is_admin = Column(Boolean, default=False)
#     created_at = Column(DateTime, nullable=False)
