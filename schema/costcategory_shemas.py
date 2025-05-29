from pydantic import BaseModel, Field
from typing import Optional


class CostCategoryGet(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    description: str = Field(max_length=255)
    is_default: Optional[bool] = False


class CostCategoryOut(CostCategoryGet):
    class Config:
        orm_mode = True