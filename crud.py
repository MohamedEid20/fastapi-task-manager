from datetime import datetime
from typing import List, Optional
from sqlmodel import Session, select
from models import Task, TaskCreate, TaskUpdate, TaskStatus, TaskPriority


class TaskCRUD:
    def __init__(self, session: Session):
        self.session = session

    def create_task(self, task_data: TaskCreate) -> Task:
        task = Task(**task_data.dict())
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        statement = select(Task).where(Task.id == task_id)
        return self.session.exec(statement).first()

    def get_tasks(
        self, 
        skip: int = 0, 
        limit: int = 100, 
        status: Optional[TaskStatus] = None,
        priority: Optional[TaskPriority] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = "asc"
    ) -> List[Task]:
        statement = select(Task)
        
        if status:
            statement = statement.where(Task.status == status)
        if priority:
            statement = statement.where(Task.priority == priority)
        
        # Add sorting if specified
        if sort_by:
            # Get the attribute to sort by
            sort_attr = getattr(Task, sort_by, None)
            if sort_attr:
                # Apply sort direction
                if sort_order.lower() == "desc":
                    statement = statement.order_by(sort_attr.desc())
                else:
                    statement = statement.order_by(sort_attr.asc())
            
        statement = statement.offset(skip).limit(limit)
        return list(self.session.exec(statement).all())

    def update_task(self, task_id: int, task_data: TaskUpdate) -> Optional[Task]:
        task = self.get_task(task_id)
        if not task:
            return None
        
        update_data = task_data.model_dump(exclude_unset=True)
        if update_data:
            update_data["updated_at"] = datetime.utcnow()
            for field, value in update_data.items():
                setattr(task, field, value)
            
            self.session.add(task)
            self.session.commit()
            self.session.refresh(task)
        
        return task

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if not task:
            return False
        
        self.session.delete(task)
        self.session.commit()
        return True
