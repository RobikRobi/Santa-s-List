from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from ..db import Base
import enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from ..auth.auth_models import User

class LabelEnum(str, enum.Enum):
    JOB = "Работа"
    STUDIES = "Учеба"
    PERSONAL = "Личное"

# модель таблицы с задачами
class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    task: Mapped[str] = mapped_column(String(255))
    status: Mapped[bool] = mapped_column(Boolean, default=False)
    label: Mapped[LabelEnum] = mapped_column(default=LabelEnum.PERSONAL)

    tasks: Mapped["User"] = relationship(back_populates="users")