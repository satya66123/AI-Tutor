"""
Database connection test.
"""

from sqlalchemy import text

from database.database import engine


def test_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            print("Database Connected Successfully!")

    except Exception as error:
        print(error)


if __name__ == "__main__":
    test_connection()