from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL_ASYNC")

# Create the asynchronous engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create the asynchronous session factory
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Base for defining models
Base = declarative_base()

# Dependency to get session in FastAPI or your backend
@asynccontextmanager
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
