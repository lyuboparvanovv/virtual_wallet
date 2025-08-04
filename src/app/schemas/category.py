from pydantic import BaseModel, constr


class CategoryBase(BaseModel):
    name: constr(min_length=1, max_length=50)

class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int

    class Config:
        from_attributes = True