from enum import Enum
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import field_validator


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"


class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    urgent = "urgent"


class TaskBase(SQLModel):
    title: str = Field(max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    status: TaskStatus = Field(default=TaskStatus.pending)
    priority: TaskPriority = Field(default=TaskPriority.medium)
    due_date: Optional[datetime] = Field(default=None)
    assigned_to: Optional[str] = Field(default=None, max_length=100)


class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)


class TaskCreate(TaskBase):
    @field_validator('title')
    @classmethod
    def validate_title(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError('Title cannot be empty or whitespace only')
        return v.strip()
    
    @field_validator('due_date')
    @classmethod
    def validate_due_date(cls, v: datetime) -> datetime:
        if v and v <= datetime.utcnow():
            raise ValueError('Due date must be in the future')
        return v
    
    @field_validator('assigned_to')
    @classmethod
    def validate_assigned_to(cls, v: str) -> str:
        if v:
            return v.strip()
        return v


class TaskUpdate(SQLModel):
    title: Optional[str] = Field(default=None, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    status: Optional[TaskStatus] = Field(default=None)
    priority: Optional[TaskPriority] = Field(default=None)
    due_date: Optional[datetime] = Field(default=None)
    assigned_to: Optional[str] = Field(default=None, max_length=100)


class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
