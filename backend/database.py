import os
from pathlib import Path

from dotenv import load_dotenv
from sqlmodel import create_engine

# Load environment variables from backend/.env
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# Read the PostgreSQL connection URL
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not configured")

# Create the database engine
engine = create_engine(
    DATABASE_URL,
    echo=True
)