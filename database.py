# database.py file contains SQLAlchemy SQlite database

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

# database connection url for sqlite type database
# with aiosqlite driver for asynchronous operations
# tasks.db is the file`s name
DATABASE_URL = "sqlite+aiosqlite:///tasks.db"

# engine for db
engine = create_async_engine(DATABASE_URL)

# session for engine,
# expire_on_commit is set to False to prevent automatic 
# expiration of objects after commit
new_session = async_sessionmaker(engine, expire_on_commit=False)

# parent class for other chart/sheet/etc classes
class Model(MappedAsDataclass, DeclarativeBase):
    pass

# dependency function to get a database session
async def get_db():
    async with new_session() as session:
        yield session

# database session dependency, aotomatically provides 
# a session to database and closes it after
SessionDep = Annotated[AsyncSession, Depends(get_db)]

