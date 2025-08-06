from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.crud.user import get_user_by_username, get_user_by_email, get_user_by_phone, create_user
from app.db.session import get_db
from app.schemas.user import UserOut, UserCreate
from app.schemas.auth import *

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already exists")
    if get_user_by_phone(db, user.phone):
        raise HTTPException(status_code=400, detail="Phone already exists")
    db_user = create_user(db, user)
    return db_user

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
   pass

@router.post("/logout")
def logout():
    return {"msg": "Logout successful"}