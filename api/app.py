from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .db import SessionLocal, engine
from .models import Base

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    global db 
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)
    yield
    db.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
    @app.get("/items/")
    async def read_items(db: AsyncSession = Depends(get_db)):
        result = await db.execute("SELECT * FROM items")
        items = result.fetchall()
        return items