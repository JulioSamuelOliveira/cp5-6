from sqlalchemy.orm import Session
from . import models, schemas
from typing import Optional  # Adicionado

def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Author).offset(skip).limit(limit).all()

def update_author(db: Session, author_id: int, author: schemas.AuthorCreate):
    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if db_author:
        db_author.name = author.name
        db.commit()
        db.refresh(db_author)
        return db_author
    return None

def delete_author(db: Session, author_id: int):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if author:
        db.delete(author)
        db.commit()
        return author
    return None

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Category).offset(skip).limit(limit).all()

def update_category(db: Session, category_id: int, category: schemas.CategoryCreate):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db_category.name = category.name
        db.commit()
        db.refresh(db_category)
        return db_category
    return None

def delete_category(db: Session, category_id: int):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if category:
        db.delete(category)
        db.commit()
        return category
    return None

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(title=book.title, author_id=book.author_id, category_id=book.category_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 10, author_id: Optional[int] = None):
    query = db.query(models.Book)
    if author_id is not None:
        query = query.filter(models.Book.author_id == author_id)
    return query.offset(skip).limit(limit).all()

def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db_book.title = book.title
        db_book.author_id = book.author_id
        db_book.category_id = book.category_id
        db.commit()
        db.refresh(db_book)
        return db_book
    return None

def delete_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return book
    return None

def recommend_books(db: Session, category_id: int):
    return db.query(models.Book).filter(models.Book.category_id == category_id).all()