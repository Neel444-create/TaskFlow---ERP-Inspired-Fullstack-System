
from sqlalchemy import text

from database import engine

# Open a connection to PostgreSQL
with engine.connect() as connection:

    # Execute a simple SQL query
    result = connection.execute(
        text("SELECT current_database(), current_user")
    )

    # Fetch the result
    database_name, username = result.one()

    print("Database connected successfully!")
    print("Database:", database_name)
    print("User:", username)
