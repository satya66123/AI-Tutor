"""
Database configuration using SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from config.config import Config


DATABASE_URL = (
    f"mysql+pymysql://{Config.MYSQL_USER}:"
    f"{Config.MYSQL_PASSWORD}@"
    f"{Config.MYSQL_HOST}:"
    f"{Config.MYSQL_PORT}/"
    f"{Config.MYSQL_DATABASE}"
)


engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


Base = declarative_base()


def get_db():
    """
    Returns a database session.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()