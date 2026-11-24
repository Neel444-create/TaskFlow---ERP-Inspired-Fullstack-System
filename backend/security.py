
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

import jwt
from dotenv import load_dotenv
from pwdlib import PasswordHash


# Load environment variables
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


# JWT configuration
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not configured")

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
)


# Configure Argon2 password hashing
password_hash = PasswordHash.recommended()


# Hash a new password
def get_password_hash(password: str) -> str:

    return password_hash.hash(password)


# Verify a password during login
def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    try:
        return password_hash.verify(
            plain_password,
            hashed_password
        )
    except Exception:
        # Invalid or legacy placeholder hash
        return False


# Generate JWT access token
def create_access_token(
    subject: str
) -> str:

    expiration = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": subject,
        "exp": expiration
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token
