from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ExpensesGet(BaseModel):
    amount: int = Field(gt=0)
    description: str = Field(min_length=1, max_length=255)
    date: datetime = Field(default_factory=datetime.utcnow)


class ExpensesOut(ExpensesGet):
    class Config:
        orm_mode = True