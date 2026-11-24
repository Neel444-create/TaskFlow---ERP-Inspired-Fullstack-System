
from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status
)

from sqlmodel import Session, select

from db_session import get_session
from auth import get_current_user

from models import Task, User

from schemas import (
    TaskCreate,
    TaskUpdate,
    TaskPublic
)


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# =================================
# HELPER: VERIFY TASK OWNERSHIP
# =================================

def get_owned_task(
    session: Session,
    task_id: UUID,
    current_user: User
) -> Task:

    task = session.get(Task, task_id)

    if (
        task is None
        or task.owner_id != current_user.id
    ):

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


# =================================
# 1. CREATE TASK
# =================================

@router.post(
    "/",
    response_model=TaskPublic,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task_data: TaskCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):

    # Create task for authenticated user
    task = Task(
        title=task_data.title,
        description=task_data.description,
        owner_id=current_user.id
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    return task


# =================================
# 2. GET ALL MY TASKS
# =================================

@router.get(
    "/",
    response_model=list[TaskPublic]
)
def get_tasks(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):

    statement = (
        select(Task)
        .where(Task.owner_id == current_user.id)
        .offset(skip)
        .limit(limit)
    )

    tasks = session.exec(statement).all()

    return tasks


# =================================
# 3. GET ONE TASK
# =================================

@router.get(
    "/{task_id}",
    response_model=TaskPublic
)
def get_task(
    task_id: UUID,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):

    return get_owned_task(
        session,
        task_id,
        current_user
    )


# =================================
# 4. UPDATE TASK
# =================================

@router.patch(
    "/{task_id}",
    response_model=TaskPublic
)
def update_task(
    task_id: UUID,
    task_data: TaskUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):

    task = get_owned_task(
        session,
        task_id,
        current_user
    )

    update_data = task_data.model_dump(
        exclude_unset=True
    )

    if not update_data:

        raise HTTPException(
            status_code=400,
            detail="Provide at least one field to update"
        )

    if (
        "title" in update_data
        and update_data["title"] is None
    ):

        raise HTTPException(
            status_code=422,
            detail="Title cannot be null"
        )

    if (
        "completed" in update_data
        and update_data["completed"] is None
    ):

        raise HTTPException(
            status_code=422,
            detail="Completed cannot be null"
        )

    task.sqlmodel_update(update_data)

    session.add(task)
    session.commit()
    session.refresh(task)

    return task


# =================================
# 5. DELETE TASK
# =================================

@router.delete("/{task_id}")
def delete_task(
    task_id: UUID,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):

    task = get_owned_task(
        session,
        task_id,
        current_user
    )

    session.delete(task)
    session.commit()

    return {
        "message": "Task deleted successfully"
    }
