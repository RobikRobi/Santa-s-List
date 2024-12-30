from sqlalchemy import text
from ..db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..tasks.tasks_models import Tasks

# модель таблицы с данными пользователей
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[bytes]
    name: Mapped[str]

# связь пользователя с задачами 
    users: Mapped[list["Tasks"]] = relationship(uselist=True, back_populates="tasks")