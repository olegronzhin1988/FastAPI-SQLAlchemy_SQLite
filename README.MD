# Task Manager 

Simple project with FastAPI, SQLAlchemy 2 and SQLite database.
Date amd time added to tasks via datetime.
Each task is required to have unique title, it`s used to select task for update or delete.

## Features
- CRUD: Create, Read, Update and Delete(soft & hard) tasks.
- SQLite database
- Swagger UI
- Uvicorn and database autostart from main.py file

## Tech
- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite 
- Pydantic
- datetime

## install and start
- Clone repository
- Create virtual environment(venv) in project folder(python -m venv venv) and activate it(venv\Scripts\activate)
- Install all from requirements.txt (pip install -r requirements.txt)
- start main.py from terminal (python main.py)
- Open Swagger UI to test ( ttp://127.0.0.1:8000/docs)
- To quit uvicorn server, press Ctrl+C