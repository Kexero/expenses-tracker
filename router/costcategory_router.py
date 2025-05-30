from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import costcategory_crud
from schema.costcategory_shemas import CostCategoryGet, CostCategoryOut
from typing import List

cost_category_router = APIRouter(prefix="/cost_category", tags=["Категории расходов"])


@cost_category_router.get("/", response_model=List[CostCategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return costcategory_crud.get_all_cost_categories(db)


@cost_category_router.get("/search", response_model=CostCategoryOut)
def get_category_by_name(cost_name: str, db: Session = Depends(get_db)):
    category_db = costcategory_crud.get_cost_category_by_name(db, cost_name)
    if category_db is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return category_db


@cost_category_router.post("/", response_model=CostCategoryOut)
def create_cost_category(cost_category: CostCategoryGet, db: Session = Depends(get_db)):
    category_db = costcategory_crud.get_cost_category_by_name(db, cost_category.name)
    if category_db:
        raise HTTPException(status_code=400, detail="Такая категория уже существует")
    return costcategory_crud.create_cost_category(db, cost_category)
