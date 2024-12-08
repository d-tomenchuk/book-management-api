from fastapi.testclient import TestClient
from app.main import app

from app import models, database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Создаем новый движок базы данных для тестов, чтобы не изменять реальную базу
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание тестового клиента FastAPI
client = TestClient(app)

# Убедимся, что для тестов используется отдельная база данных
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[database.get_db] = override_get_db

# Тесты для работы с авторами
def test_create_author():
    response = client.post("/authors/", json={"name": "Author Name"})
    assert response.status_code == 200
    assert response.json()["name"] == "Author Name"

def test_get_authors():
    # Добавим автора для теста
    client.post("/authors/", json={"name": "Author 1"})
    response = client.get("/authors/")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Тесты для работы с книгами
def test_create_book():
    # Создадим автора для книги
    author_response = client.post("/authors/", json={"name": "Author 1"})
    author_id = author_response.json()["id"]

    # Добавим книгу
    response = client.post("/books/", json={"title": "Book Title", "description": "Book Description", "author_id": author_id})
    assert response.status_code == 200
    assert response.json()["title"] == "Book Title"
    assert response.json()["description"] == "Book Description"
    assert response.json()["author"]["name"] == "Author 1"

def test_get_books():
    # Добавим книгу
    response = client.post("/books/", json={"title": "Book Title", "description": "Book Description", "author_id": 1})
    assert response.status_code == 200

    # Получим все книги
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_book_by_id():
    # Добавим книгу
    book_response = client.post("/books/", json={"title": "Book Title", "description": "Book Description", "author_id": 1})
    book_id = book_response.json()["id"]

    # Получим книгу по ID
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Book Title"

def test_update_book():
    # Добавим книгу
    book_response = client.post("/books/", json={"title": "Book Title", "description": "Book Description", "author_id": 1})
    book_id = book_response.json()["id"]

    # Обновим информацию о книге
    response = client.put(f"/books/{book_id}", json={"title": "Updated Title", "description": "Updated Description", "author_id": 1})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"
    assert response.json()["description"] == "Updated Description"

def test_delete_book():
    # Добавим книгу
    book_response = client.post("/books/", json={"title": "Book Title", "description": "Book Description", "author_id": 1})
    book_id = book_response.json()["id"]

    # Удалим книгу
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Book deleted successfully"}

    # Проверим, что книги больше нет, ожидаем 404
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": f"Book with ID {book_id} not found"}

