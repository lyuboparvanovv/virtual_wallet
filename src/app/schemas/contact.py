from pydantic import BaseModel

from app.schemas.user import UserOut


class ContactBase(BaseModel):
    contact_user_id: int

class ContactCreate(ContactBase):
    pass

class ContactOut(BaseModel):
    id: int
    contact_user: UserOut

    class Config:
        from_attributes = True