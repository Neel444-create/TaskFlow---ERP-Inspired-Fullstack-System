
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from fastapi.security import OAuth2PasswordRequestForm

from sqlmodel import Session, select

from db_session import get_session
from models import User

from schemas import UserCreate, UserPublic, Token

from security import (
    get_password_hash,
    verify_password,
    create_access_token
)

from auth import get_current_user


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# =================================
# 1. USER REGISTRATION
# =================================

@router.post(
    "/register",
    response_model=UserPublic,
    status_code=status.HTTP_201_CREATED
)
def register_user(
    user_data: UserCreate,
    session: Session = Depends(get_session)
):

    email = str(user_data.email).lower()

    # Check whether email already exists
    statement = select(User).where(
        User.email == email
    )

    existing_user = session.exec(statement).first()

    if existing_user:

        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    # Hash the password
    hashed_password = get_password_hash(
        user_data.password
    )

    # Create user database object
    user = User(
        name=user_data.name,
        email=email,
        hashed_password=hashed_password
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return user


# =================================
# 2. USER LOGIN
# =================================

@router.post(
    "/login",
    response_model=Token
)
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):

    email = form_data.username.lower()

    # Find user using email
    statement = select(User).where(
        User.email == email
    )

    user = session.exec(statement).first()

    # Verify password
    if (
        user is None
        or not verify_password(
            form_data.password,
            user.hashed_password
        )
    ):

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    # Generate JWT
    access_token = create_access_token(
        subject=str(user.id)
    )

    return Token(
        access_token=access_token,
        token_type="bearer"
    )


# =================================
# 3. CURRENT LOGGED-IN USER
# =================================

@router.get(
    "/me",
    response_model=UserPublic
)
def get_my_profile(
    current_user: User = Depends(get_current_user)
):

    return current_user
