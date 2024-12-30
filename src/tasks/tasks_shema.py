from pydantic import BaseModel, Field
from .tasks_models import LabelEnum


class TaskCreateSchema(BaseModel):
    task: str = Field(min_length=1, max_length=255)
    status: bool = False
    label: LabelEnum = LabelEnum.PERSONAL

# схема для пополнения баланса счёта
class TaskUpdate(BaseModel):
    task: str = Field(min_length=1, max_length=255)
    status: bool = False
    label: LabelEnum = LabelEnum.PERSONAL