# from fastapi import APIRouter, Depends, Request
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles

# from .tasks_models import Tasks
# from .tasks_shema import TaskCreateSchema, TaskUpdate, TasksPydantic
# from ..db import get_session


# app = APIRouter(prefix="/episodes", tags=["Episodes"])

# templates = Jinja2Templates(directory="src/templates")
# app.mount("/static", StaticFiles(directory="src/static"), name="static")

# # список задач
# @app.get("/", response_model=TasksPydantic, response_class=HTMLResponse)
# async def list_products(request: Request, session: AsyncSession = Depends(get_session)):
#     tasks = await session.scalars(select(Tasks))
#     tasks = tasks.all()
#     context = {
#         "request": request,
#         "title": "Ваши задачи",
#         "tasks": tasks
# }
#     return templates.TemplateResponse("index.html", context=context)
    
# # добавление задачи
# @app.get("/task-add", response_class=HTMLResponse)
# async def add_product(request: Request):
#     context = {
#     "request": request,
#     "title": "Добавление задачи"
#     }
#     return templates.TemplateResponse("index.html", context=context)

# @app.post("/task-add", response_class=HTMLResponse)
# async def add_product(request: Request, session: AsyncSession = Depends(get_session)):
#     form = await request.form()
#     form_data = form._dict
#     price = int(form_data["price"])
#     product = Tasks(task=form_data["task"], price=price, description=form_data["description"])
    
#     try:
#         session.add(product)
#         await session.commit()
#         context = {
#             "request": request,
#             "title": "Продукт успешно добавлен",
#             "message": "Продукт был успешно добавлен."
#         }
#         return templates.TemplateResponse("productadd.html", context=context)
#     except Exception as e:
#         print(f"Error saving product to the database: {e}")
#         context = {
#             "request": request,
#             "title": "Ошибка при добавлении продукта",
#             "error_message": "Произошла ошибка при добавлении продукта. Попробуйте снова позже."
#         }
#         return templates.TemplateResponse("productadd.html", context=context)