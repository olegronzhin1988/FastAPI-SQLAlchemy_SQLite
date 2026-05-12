# tasks.py model file, contains table model from database
# file tasks.db

from sqlalchemy.orm import Mapped, mapped_column
from database import Model
class TasksModel(Model):
    __tablename__ = "tasks"

# task id, primary key, autoincremented
    task_id: Mapped[int] = mapped_column(primary_key = True, 
                                    autoincrement = True)
# task title, string type, not nullable
    title: Mapped[str] = mapped_column(nullable=False)
# task description
    description: Mapped[str|None] = mapped_column(default=None)
# task status, finished or not
    is_completed: Mapped[bool] = mapped_column(default=False)
# soft delete status
    is_deleted: Mapped[bool]= mapped_column(default=False)
# task creation date and time
    task_creation_time: Mapped[str|None] = mapped_column(default=None)
# task finished date and time
    task_completion_time: Mapped[str|None] = mapped_column(default=None)
# task deleted date and time
    task_deleted_time: Mapped[str|None] = mapped_column(default=None)    
