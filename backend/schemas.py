
from uuid import UUID

from pydantic import EmailStr
from sqlmodel import SQLModel, Field


# =================================
# USER SCHEMAS
# =================================

class UserCreate(SQLModel):

    name: str = Field(
        min_length=1,
        max_length=100
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128
    )


class UserPublic(SQLModel):

    id: UUID
    name: str
    email: EmailStr


# =================================
# TOKEN SCHEMA
# =================================

class Token(SQLModel):

    access_token: str

    token_type: str = "bearer"


# =================================
# TASK SCHEMAS
# =================================

class TaskCreate(SQLModel):

    title: str = Field(
        min_length=1,
        max_length=200
    )

    description: str | None = Field(
        default=None,
        max_length=500
    )


class TaskUpdate(SQLModel):

    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=200
    )

    description: str | None = Field(
        default=None,
        max_length=500
    )

    completed: bool | None = None


class TaskPublic(SQLModel):

    id: UUID

    title: str

    description: str | None

    completed: bool

    owner_id: UUID
