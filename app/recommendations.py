import dbm
from typing import List
from sqlalchemy.orm import Session
import app
from .models import Book

def recommend_books(db: Session, category_id: int):
    return db.query(Book).filter(Book.category_id == category_id).all()
@app.get("/recommendations/{category_id}", response_model=List[Book])
async def get_recommendations(category_id: int):
    books = dbm.query(Book).filter(Book.category_id == category_id).all()
    return books  # Retornar apenas os livros