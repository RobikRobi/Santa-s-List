from pydantic import BaseModel, Field, ConfigDict
from .tasks_models import LabelEnum


class TaskCreateSchema(BaseModel):
    task: str = Field(min_length=1, max_length=255)
    status: bool = False
    label: LabelEnum = LabelEnum.PERSONAL

# схема для редактирования задачи
class TaskUpdate(BaseModel):
    task: str = Field(min_length=1, max_length=255)
    status: bool = False
    label: LabelEnum = LabelEnum.PERSONAL

class TasksPydantic(BaseModel):
    id: int
    name: str
    price: int
    description: str

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)