from pydantic import BaseModel

# Модель для создания нового автора
class AuthorCreate(BaseModel):
    name: str

# Модель для создания новой книги
class BookCreate(BaseModel):
    title: str
    description: str
    author_id: int

# Модель для ответа с данными об авторе
class AuthorResponse(AuthorCreate):
    id: int

# Модель для ответа с данными о книге
class BookResponse(BookCreate):
    id: int
    title: str
    description: str
    author: AuthorResponse
