# main.py file contains app instance and main function to run app

from fastapi import FastAPI
import uvicorn
from models.tasks import TasksModel
from contextlib import asynccontextmanager
from database import engine, Model
from routers.tasks import tasks_router

# decorated function for lifespan of app, to activate database 
# when app/server starts
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
    print("DB is ready")
    yield
    print("DB is turned off")

# creating app
app = FastAPI(lifespan = lifespan,
              title = "Task manager",
              description = "FastAPI + SQLAlchemy SQLite project. Simple task manager.",
              version = "1.0.0")

# connecting tasks router to app
app.include_router(tasks_router)

# default root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to Task Manager"}

# app autostart with uvicorn server, with localhost and port
# set for local PC work only
if __name__ == "__main__":
    uvicorn.run("main:app",
                host = "127.0.0.1",
                port = 8000,
                reload = True)
