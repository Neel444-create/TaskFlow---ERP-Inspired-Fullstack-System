
from uuid import uuid4

from sqlmodel import Session, select

from database import engine
from models import User, Task


def main():

    # Create one database session
    with Session(engine) as session:

        # =================================
        # 1. CREATE A USER
        # =================================

        print("\n--- CREATE USER ---")

        user = User(
            name="TaskFlow Demo",
            email=f"demo-{uuid4().hex[:8]}@example.com",
            hashed_password="DEMO_ONLY_NOT_A_REAL_HASH"
        )

        session.add(user)
        session.commit()
        session.refresh(user)

        print("User created:", user.name)
        print("User ID:", user.id)

        user_id = user.id


        # =================================
        # 2. CREATE A TASK
        # =================================

        print("\n--- CREATE TASK ---")

        task = Task(
            title="Complete assignment",
            description="Finish the database assignment",
            completed=False,
            owner_id=user_id
        )

        session.add(task)
        session.commit()
        session.refresh(task)

        task_id = task.id

        print("Task created:", task.title)
        print("Task ID:", task.id)


        # =================================
        # 3. READ USER
        # =================================

        print("\n--- READ USER ---")

        stored_user = session.get(User, user_id)

        print("Retrieved user:", stored_user)


        # =================================
        # 4. READ TASKS
        # =================================

        print("\n--- READ TASKS ---")

        statement = select(Task).where(
            Task.owner_id == user_id
        )

        tasks = session.exec(statement).all()

        for task_item in tasks:
            print(task_item.title)


        # =================================
        # 5. UPDATE TASK
        # =================================

        print("\n--- UPDATE TASK ---")

        task_to_update = session.get(Task, task_id)

        if task_to_update is not None:

            task_to_update.completed = True

            session.add(task_to_update)
            session.commit()
            session.refresh(task_to_update)

            print("Task updated:", task_to_update.title)
            print("Completed:", task_to_update.completed)


        # =================================
        # 6. DELETE TASK
        # =================================

        print("\n--- DELETE TASK ---")

        task_to_delete = session.get(Task, task_id)

        if task_to_delete is not None:

            session.delete(task_to_delete)
            session.commit()

            print("Task deleted successfully!")


        # Verify deletion
        deleted_task = session.get(Task, task_id)

        print("Task after deletion:", deleted_task)


        # Remove demo user as cleanup
        session.delete(user)
        session.commit()

        print("Demo user cleaned up.")


if __name__ == "__main__":
    main()
