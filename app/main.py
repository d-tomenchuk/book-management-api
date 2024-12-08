from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud, database

# Создание приложения FastAPI
app = FastAPI()

# Инициализация базы данных
models.Base.metadata.create_all(bind=database.engine)

# Эндпоинты для работы с авторами
@app.post("/authors/", response_model=schemas.AuthorResponse)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(database.get_db)):
    return crud.create_author(db=db, author=author)

@app.get("/authors/", response_model=List[schemas.AuthorResponse])
def read_authors(db: Session = Depends(database.get_db)):
    return crud.get_authors(db=db)

# Эндпоинты для работы с книгами
@app.post("/books/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=List[schemas.BookResponse])  # Используем List
def read_books(db: Session = Depends(database.get_db)):
    return crud.get_books(db=db)

@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(database.get_db)):
    db_book = crud.get_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    db_book = crud.update_book(db=db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(database.get_db)):
    db_book = crud.delete_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
