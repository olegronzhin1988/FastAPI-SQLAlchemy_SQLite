# tasks.py router file, contains router and its endpoints

from fastapi import APIRouter, status, HTTPException
from schemas.tasks import STaskAdd, STaskGet, STask, STaskUpdate
from datetime import datetime
from database import SessionDep
from sqlalchemy import select, update, delete
from models.tasks import TasksModel

# router for tasks db
tasks_router = APIRouter(prefix = "/tasks",
                        tags = ["Tasks"])

# ENDPOINTS:

# add task by user
@tasks_router.post("/",
                   status_code = status.HTTP_201_CREATED,
                   description="add new task to database")
async def task_add(task_in: STaskAdd,
                   session: SessionDep) -> STask:

# creating a dict for a new task to add to database
    task_dict = task_in.model_dump()
    task_dict["task_creation_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task_dict["task_completion_time"] = None
    task_dict["is_completed"] = False
    task_dict["is_deleted"] = False
    task_dict["task_deleted_time"] = None
    task_dict["task_id"]  = None
    task_dict["title"] = task_dict["title"].strip().lower()
# check if there is task with such name in database
    query = select(TasksModel).where(TasksModel.title == task_dict["title"])
    result = await session.execute(query)
    task = result.scalar_one_or_none()
    if task is not None:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = f"Task with name {task_dict["title"]} already exists")
    else:
# creating new model object from dict
# to add it to session and commit to database
        new_task = TasksModel(**task_dict)
        session.add(new_task)
        await session.commit()
        await session.refresh(new_task)
        return new_task

# get task by its name from database
@tasks_router.get("/{task_name}",
                   status_code = status.HTTP_200_OK,
                     description="get task by its name")
async def task_get(task_name: str,
                   session: SessionDep) -> STask:
    
# creating request to get task from database
    query = select(TasksModel).where(TasksModel.title == task_name.lower().strip())
    result = await session.execute(query)
    task = result.scalars().first()

# checking results of request
    if task is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Task with name {task_name.lower().strip()} not found")
    else:
        return task

# update task description by its name: change its description or close it
@tasks_router.patch("/{task_name}",
                     status_code = status.HTTP_202_ACCEPTED,
                     description="update task description by its name") 
async def task_update(task_name: str,
                      task_update: STaskUpdate,
                      session: SessionDep) -> STask:
    
# check if there is task with such name in database
    query = select(TasksModel).where(TasksModel.title == task_name.lower().strip())
    result = await session.execute(query)
    task = result.scalars().first()

# Exception if there is no such task
    if task is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Task with name {task_name.lower().strip()} not found")
    
# Update task if it is not absent    
    else:

# update task description or completion status
        update_data = {}
        if task_update.description not in [None, ""]:
            update_data["description"] = task_update.description

        if task_update.close_task:
            update_data["is_completed"] = task_update.close_task
            update_data["task_completion_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if update_data:
            query = update(TasksModel).where(TasksModel.title == task_name).values(**update_data)
            await session.execute(query)

# commit changes to database and return updated task
        await session.commit()
        await session.refresh(task)
        return task

# soft delete task by its id
@tasks_router.delete("/{task_id}",
                        status_code=status.HTTP_204_NO_CONTENT,
                        description="soft delete task by its id")
async def task_delete(task_id: int, 
                      session: SessionDep):
    
# check if there is task with such id in database
    query = select(TasksModel).where(TasksModel.task_id == task_id)
    result = await session.execute(query)
    task = result.scalar_one_or_none()

# Exception if there is no such task or it is deleted
    if task is None or task.is_deleted is True:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Task with id {task_id} not found")
    
# Update/soft delete task if it is not absent    
    else:
        query = update(TasksModel).where(TasksModel.task_id == task_id).values(
            is_deleted = True,
            task_deleted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        await session.execute(query)

# commit changes to database
        await session.commit()

# hard delete task by its id
@tasks_router.delete("/hard_del/{task_id}",
                        status_code=status.HTTP_204_NO_CONTENT,
                        description="hard delete task by its id")
async def task_hard_delete(task_id: int, 
                      session: SessionDep): 
    
# check if there is task with such id in database
    query = select(TasksModel).where(TasksModel.task_id == task_id)
    result = await session.execute(query)
    task = result.scalar_one_or_none()

# Exception if there is no such task
    if task is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Task with id {task_id} not found")

#hard delete task
    else:
        query = delete(TasksModel).where(TasksModel.task_id == task_id)
        await session.execute(query)

# commit changes to database
        await session.commit()

