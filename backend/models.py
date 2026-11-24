
from typing import List, Optional
from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field, Relationship


# -------------------------
# USER TABLE
# -------------------------

class User(SQLModel, table=True):

    __tablename__ = "users"

    # Unique identifier
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True
    )

    # Basic user information
    name: str = Field(max_length=100)

    email: str = Field(
        index=True,
        unique=True,
        max_length=255
    )

    # Never store the original password
    hashed_password: str = Field(max_length=255)

    # One user can have multiple tasks
    tasks: List["Task"] = Relationship(
        back_populates="owner"
    )


# -------------------------
# TASK TABLE
# -------------------------

class Task(SQLModel, table=True):

    __tablename__ = "tasks"

    # Unique identifier
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True
    )

    title: str = Field(max_length=200)

    description: Optional[str] = None

    completed: bool = Field(default=False)

    # Connect task to its user
    owner_id: UUID = Field(
        foreign_key="users.id"
    )

    # Relationship with User model
    owner: Optional[User] = Relationship(
        back_populates="tasks"
    )
