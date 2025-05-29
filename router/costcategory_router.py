from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import costcategory_crud
from schema.costcategory_shemas import CostCategoryGet, CostCategoryOut

cost_category_router = APIRouter(prefix="/cost_category", tags=["Категории расходов"])


@cost_category_router.post("/", response_model=CostCategoryOut)
def create_cost_category(cost_category: CostCategoryGet, db: Session = Depends(get_db)):
    db_user = costcategory_crud.get_cost_category_by_name(db, cost_category.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Такая категория уже существует")
    return costcategory_crud.create_cost_category(db, cost_category)