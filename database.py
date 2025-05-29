from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from settings import settings
from typing import Generator


DATABASE_URL = (f"postgresql://{settings.db_user}:{settings.db_password}@"
                f"{settings.db_host}:{settings.db_port}/{settings.db_name}")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()