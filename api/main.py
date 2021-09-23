# external libraries
import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import Session

# internal libraries
from routes.user import user
from models import models
from config.db import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API chat",
    description="saves messages sent by a user in the database (SQLite)",
    version="0.0.1",
    openapi_tags=[{
        "name":"users",
        "description":"Users routes",
    },
    {
        "name":"chat",
        "description":"Chat routes",
    },
    {
        "name":"data-chat",
        "description":"Data chat routes",
    }]
)

app.include_router(user)

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8010, reload=True)