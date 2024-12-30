from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from ..src.auth.auth_router import app as auth_router
from ..src.tasks.tasks_router import app as tasks_router
from .db import app as db_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(tasks_router)
app.include_router(db_router)

templates = Jinja2Templates(directory="src/templates")
app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "titel": "Главная страница"})