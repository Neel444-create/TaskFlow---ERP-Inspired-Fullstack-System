
from sqlmodel import SQLModel

from database import engine

# Import models so SQLModel registers their tables
from models import User, Task


def create_db_and_tables():

    # Create all registereṇd tables
    SQLModel.metadata.create_all(engine)

    print("Database tables created successfully!")


if __name__ == "__main__":
    create_db_and_tables()
