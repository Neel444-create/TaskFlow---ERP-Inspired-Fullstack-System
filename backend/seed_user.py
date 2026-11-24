
from sqlmodel import Session, select

from database import engine
from models import User


DEMO_EMAIL = "demo@taskflow.local"


def create_demo_user():

    with Session(engine) as session:

        # Check if the demo user already exists
        statement = select(User).where(
            User.email == DEMO_EMAIL
        )

        user = session.exec(statement).first()

        if user:
            print("Demo user already exists.")
        else:

            # Create demo user
            user = User(
                name="TaskFlow Demo",
                email=DEMO_EMAIL,
                hashed_password="PHASE3_PLACEHOLDER_ONLY"
            )

            session.add(user)
            session.commit()
            session.refresh(user)

            print("Demo user created!")

        print("User ID:", user.id)


if __name__ == "__main__":
    create_demo_user()
