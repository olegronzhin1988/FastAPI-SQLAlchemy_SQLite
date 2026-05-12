# tasks.py schema file, contains task schemas

from pydantic import BaseModel, Field, ConfigDict

# task Schema as it is added BY user, data that user sends to database
class STaskAdd(BaseModel):
    title:str = Field(default = ...,
                      title = "Task title",
                      description = "Task title, given by user",
                      min_length = 3,
                      max_length = 50)
    description: str|None = Field(default = None,
                                  title = "Task description",
                                  description= "Task description, given by user",
                                  max_length = 300)
    
# setting up config for pydantic model, to work with ORM models    
    model_config = ConfigDict(from_attributes=True)

# task Schema for update
class STaskUpdate(BaseModel):
    description: str|None = Field(default = None,
                                  title = "Task description",
                                  description= "Task description, given by user",
                                  max_length = 300)
    close_task: bool = Field(default = False,
                             title = "Close task",
                             description = "Set task as completed")
    
# task Schema as it is given TO user, data that user receives from database
class STaskGet(STaskAdd):
    task_creation_time: str = Field(default = None,
                                    title = "Task creation time",
                                    description = "Task creation time, as it is added to database")
    
    task_completion_time: str|None = Field(default = None,
                                           title = "Task completion time",
                                           description = "Task completion time")

    is_completed: bool = Field(default = False,
                               title = "Task completion status",
                               description = "Task completion status, given by user")

    
# task Schema as it is in database
class STask(STaskGet):
    task_id: int = Field(default = ...,
                         title = "Task ID",
                         description = "Task ID, as it is added to database",
                         ge = 1)
    
    is_deleted: bool = Field(default = False,
                            title = "Task soft delete status",
                            description = "Task soft delete status, given by user")

    task_deleted_time: str|None = Field(default = None,
                                        title = "Task deleted time",
                                        description = "Task deleted time")

    model_config = ConfigDict(from_attributes = True)