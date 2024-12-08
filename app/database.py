from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = "sqlite:///./test.db"

# Создание подключения к базе данных
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Сессия для взаимодействия с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
