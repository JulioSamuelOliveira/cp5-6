from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Gestão de Livraria!"}

@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)

@app.get("/authors/", response_model=List[schemas.Author])
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    authors = crud.get_authors(db=db, skip=skip, limit=limit)
    return authors

@app.put("/authors/{author_id}", response_model=schemas.Author)
def update_author(author_id: int, author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    updated_author = crud.update_author(db=db, author_id=author_id, author=author)
    if updated_author is None:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return updated_author

@app.delete("/authors/{author_id}", response_model=schemas.Author)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = crud.delete_author(db=db, author_id=author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return author

@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

@app.get("/categories/", response_model=List[schemas.Category])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    categories = crud.get_categories(db=db, skip=skip, limit=limit)
    return categories

@app.put("/categories/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    updated_category = crud.update_category(db=db, category_id=category_id, category=category)
    if updated_category is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return updated_category

@app.delete("/categories/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.delete_category(db=db, category_id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return category

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, author_id: Optional[int] = None, db: Session = Depends(get_db)):
    books = crud.get_books(db=db, skip=skip, limit=limit, author_id=author_id)
    return books

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    updated_book = crud.update_book(db=db, book_id=book_id, book=book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return updated_book

@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return book

@app.get("/recommendations/{category_id}", response_model=List[schemas.Book])
async def get_recommendations(category_id: int, db: Session = Depends(get_db)):
    return crud.recommend_books(db, category_id)