from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from typing import List, Optional
from database import get_session
from models import Task, TaskCreate, TaskUpdate, TaskResponse, TaskStatus, TaskPriority
from crud import TaskCRUD

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Task Management API", "docs": "/docs"}


@router.get("/health")
async def health_check():
    return {"status": "healthy"}


@router.post("/tasks", response_model=TaskResponse, status_code=201)
async def create_task(task_data: TaskCreate, session: Session = Depends(get_session)):
    crud = TaskCRUD(session)
    return crud.create_task(task_data)


@router.get("/tasks", response_model=List[TaskResponse])
async def get_tasks(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    status: Optional[TaskStatus] = None,
    priority: Optional[TaskPriority] = None,
    sort_by: Optional[str] = Query(
        None, 
        description="Field to sort by",
        enum=["id", "title", "description", "status", "priority", "created_at", "updated_at", "due_date", "assigned_to"]
    ),
    sort_order: Optional[str] = Query(
        "asc",
        description="Sort order",
        enum=["asc", "desc"]
    ),
    session: Session = Depends(get_session)
):
    crud = TaskCRUD(session)
    return crud.get_tasks(
        skip=skip, 
        limit=limit, 
        status=status, 
        priority=priority,
        sort_by=sort_by,
        sort_order=sort_order
    )


@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, session: Session = Depends(get_session)):
    crud = TaskCRUD(session)
    task = crud.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task_data: TaskUpdate, session: Session = Depends(get_session)):
    crud = TaskCRUD(session)
    task = crud.update_task(task_id, task_data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, session: Session = Depends(get_session)):
    crud = TaskCRUD(session)
    if not crud.delete_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}


@router.get("/tasks/status/{status}", response_model=List[TaskResponse])
async def get_tasks_by_status(
    status: TaskStatus,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    sort_by: Optional[str] = Query(
        None, 
        description="Field to sort by",
        enum=["id", "title", "description", "status", "priority", "created_at", "updated_at", "due_date", "assigned_to"]
    ),
    sort_order: Optional[str] = Query(
        "asc",
        description="Sort order",
        enum=["asc", "desc"]
    ),
    session: Session = Depends(get_session)
):
    crud = TaskCRUD(session)
    return crud.get_tasks(
        skip=skip,
        limit=limit,
        status=status,
        sort_by=sort_by,
        sort_order=sort_order
    )


@router.get("/tasks/priority/{priority}", response_model=List[TaskResponse])
async def get_tasks_by_priority(
    priority: TaskPriority,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    sort_by: Optional[str] = Query(
        None, 
        description="Field to sort by",
        enum=["id", "title", "description", "status", "priority", "created_at", "updated_at", "due_date", "assigned_to"]
    ),
    sort_order: Optional[str] = Query(
        "asc",
        description="Sort order",
        enum=["asc", "desc"]
    ),
    session: Session = Depends(get_session)
):
    crud = TaskCRUD(session)
    return crud.get_tasks(
        skip=skip,
        limit=limit,
        priority=priority,
        sort_by=sort_by,
        sort_order=sort_order
    )
