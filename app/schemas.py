from pydantic import BaseModel, constr
from typing import List, Optional

class BookBase(BaseModel):
    title: str
    author_id: int
    category_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True  # Corrigido para a nova configuração do Pydantic V2

class AuthorBase(BaseModel):
    name: constr(min_length=1, max_length=100)

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: constr(min_length=1, max_length=100)

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True