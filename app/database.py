from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv

# Загрузка переменных из файла .env (если он есть)
load_dotenv()

# Получаем строку подключения из переменной окружения
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Создание подключения к базе данных
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Сессия для взаимодействия с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Функция для получения сессии базы данных с обработкой ошибок
def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        # Логирование или обработка ошибки подключения
        print(f"Database error occurred: {e}")
        raise e
    finally:
        db.close()
