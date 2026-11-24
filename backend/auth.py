
from uuid import UUID

import jwt
from jwt.exceptions import InvalidTokenError

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlmodel import Session

from db_session import get_session
from models import User
from security import SECRET_KEY, ALGORITHM


# Tells FastAPI where users obtain access tokens
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session)
) -> User:

    # Error returned for invalid credentials
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:

        # Verify and decode JWT
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # Extract user ID
        subject = payload.get("sub")

        if not isinstance(subject, str):
            raise credentials_error

        user_id = UUID(subject)

    except (InvalidTokenError, ValueError, TypeError):

        raise credentials_error

    # Retrieve user from PostgreSQL
    user = session.get(User, user_id)

    if user is None:
        raise credentials_error

    return user
