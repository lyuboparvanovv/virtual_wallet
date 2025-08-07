from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import app.models
from app.services.get_settings import get_settings

settings = get_settings()
DATABASE_URL = (f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}"
                f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

DB_CONFIG = {
    "dbname": settings.DB_NAME,
    "user": settings.DB_USER,
    "password": settings.DB_PASSWORD,
    "host": settings.DB_HOST,
    "port": settings.DB_PORT
}
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
