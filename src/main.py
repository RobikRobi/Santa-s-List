from fastapi import FastAPI

from .auth.auth_router import app as auth_router
from .tasks.tasks_router import app as tasks_router
from .db import app as db_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(tasks_router)
app.include_router(db_router)


@app.get("/")
def read_root():
    return {"message": "Hello, To Do list!"}