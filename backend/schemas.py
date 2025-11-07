# pydantic schemas
from pydantic import BaseModel
from typing import Optional

class TaskStatus(BaseModel):
    task_id: str
    status: str
    url: Optional[str] = None
