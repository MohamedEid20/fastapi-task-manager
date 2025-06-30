from sqlmodel import create_engine, SQLModel, Session
from typing import Generator
from config import get_settings

settings = get_settings()
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
