from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.user import update_user
from app.db.session import get_db
from app.dependancies.auth_d import get_current_user
from app.models import User
from app.schemas.user import UserOut, UserUpdate

router = APIRouter()


@router.get("/me", response_model=UserOut)
def read_own_profile(current_user: User = Depends(get_current_user)):
    return current_user


@router.put("/me", response_model=UserOut)
def update_own_profile(user_update: UserUpdate, db: Session = Depends(get_db),
                       current_user: User = Depends(get_current_user)):
    updated_user = update_user(db, current_user, user_update)
    return updated_user
