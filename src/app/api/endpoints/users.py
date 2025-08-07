from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.user import update_user, get_user
from app.db.database import get_db
from app.dependancies.auth_d import get_current_user, get_current_active_admin
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


@router.get("/", response_model=List[UserOut], dependencies=[Depends(get_current_active_admin)])
def list_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.post("/{user_id}/approve", dependencies=[Depends(get_current_active_admin)])
def approve_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    user.is_approved = True
    db.commit()
    return {"msg": f"User {user.username} approved"}


@router.post("/{user_id}/deactivate", dependencies=[Depends(get_current_active_admin)])
def deactivate_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    user.is_active = False
    db.commit()
    return {"msg": f"User {user.username} deactivated"}

@router.post("/{user_id}/activate", dependencies=[Depends(get_current_active_admin)])
def activate_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    user.is_active = True
    db.commit()
    return {"msg": f"User {user.username} activated"}