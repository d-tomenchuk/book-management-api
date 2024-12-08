from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

from . import models, schemas

# Функция для создания автора
def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

# Функция для получения авторов
def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Author).offset(skip).limit(limit).all()

# Функция для создания книги
def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(title=book.title, description=book.description, author_id=book.author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Функция для получения всех книг
def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()

# Функция для получения книги по ID
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

# Функция для обновления книги
def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db_book.title = book.title
        db_book.description = book.description
        db.commit()
        db.refresh(db_book)
    return db_book

# Функция для удаления книги
def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
