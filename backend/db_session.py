
from collections.abc import Generator

from sqlmodel import Session

from database import engine


def get_session() -> Generator[Session, None, None]:

    # Create a database session
    with Session(engine) as session:

        # Provide session to the API endpoint
        yield session

    # Session automatically closes after use
