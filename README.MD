# Task Manager 

Simple project with FastAPI, SQLAlchemy 2 and SQLite database.
Date amd time added to tasks via datetime.
Each task is required to have unique title, it`s used to select task for update or delete.

## Description
SQLite database tasks.db contains one sheet, tasks.

tasks:
task_id, PK, INTEGER, Autoincrement.
title, VARCHAR.
description, VARCHAR.
is_completed, BOOLEAN.
is_deleted, BOOLEAN.
task_creation_time, VARCHAR.
task_completion_time, VARCHAR.
task_deleted_time, VARCHAR.

Task is created by user, by sending its title(nessessary) and description(unnessessary). 
Creation date and time automatically added by API.
Task_id automatically set by database.
After that user can change description of the task or change its status to completed.
User can soft delete or hard delete task.


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