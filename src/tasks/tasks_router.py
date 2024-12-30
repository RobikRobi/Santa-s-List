from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .tasks_models import Tasks
from .tasks_shema import TaskCreateSchema, TaskUpdate, TasksPydantic
from ..db import get_session


app = APIRouter(prefix="/tasks", tags=["Tasks"])

# список задач
@app.get("/", response_model=list[TasksPydantic])
async def list_products(session: AsyncSession = Depends(get_session)):
    tasks = await session.scalars(select(Tasks))
    tasks = tasks.all()
    return tasks
    
# добавление задачи
@app.post("/addtask")
async def add_task(task_create:TaskCreateSchema, session: AsyncSession = Depends(get_session)):
    task_data = Tasks(task=task_create.task, status=task_create.status, label=task_create.label)
    session.add(task_data)
    await session.commit()
    await session.refresh(task_data)
    return task_data

# редактирование задачи
@app.put("/{task_id}/put")
async def task_put(task_id: int, task_update: TaskUpdate, session: AsyncSession = Depends(get_session)):
    task_data = await session.scalar(select(Tasks).filter(Tasks.id == task_id))
    if not task_data:
        raise HTTPException(status_code=404, detail="Task not found")

    task_data.task = task_update.task
    task_data.status = task_update.status
    task_data.label = task_update.label
    await session.commit()
    await session.refresh(task_data)

    return task_data

# удаление задачи
@app.delete("/deltask/{task_id}")
async def delete_task(task_id: int, session: AsyncSession = Depends(get_session)):
    task_data = await session.scalar(select(Tasks).filter(Tasks.id == task_id))
    if not task_data:
        raise HTTPException(status_code=404, detail="Task not found")
    await session.delete(task_data)
    await session.commit()
    return {"message": f"Task with ID {task_id} delete"}
