from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class IncomeGet(BaseModel):
    amount: int = Field(gt=0)
    source: str = Field(min_length=1, max_length=100)
    date: datetime = Field(default_factory=datetime.utcnow)


class IncomeOut(IncomeGet):
    class Config:
        orm_mode = True
