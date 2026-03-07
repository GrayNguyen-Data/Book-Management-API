from pydantic import BaseModel

class CategoryBase(BaseModel):
    name:str
    description:str | None = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name:str | None = None
    description:str | None = None

class CategoryInDBBase(CategoryBase):
    id: int
    class Config:
        orm_mode = True

class Category(CategoryInDBBase):
    pass