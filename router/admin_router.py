from utils.init_data import create_default_categories
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from database import get_db
from schema.user_schemas import UserGet, UserOut
from schema.costcategory_shemas import CostCategoryOut
from crud import user_crud, costcategory_crud

admin_router = APIRouter(prefix="/admin", tags=["Админ"])


@admin_router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return db_user


# @admin_router.get("/{cost_id}", response_model=CostCategoryOut)
# def get_category(category_id: int, db: Session = Depends(get_db)):
#     db_category = costcategory_crud.get_cost_category_by_id(db, category_id)
#     if db_category is None:
#         raise HTTPException(status_code=404, detail="Пользователь не найден")
#     return db_category


@admin_router.post("/init-default-categories")
def init_categories():
    create_default_categories()
    return {"message": "Базовые категории созданы (даже если они уже были)"}


# @cost_category_router.put("/{cost_id}", response_model=CostCategoryOut)
# def update_category(cost_id: int, user_data: CostCategoryGet, db: Session = Depends(get_db)):
#     updated_cost = costcategory_crud.update_cost_categories(db, cost_id, user_data)
#     if updated_cost is None:
#         raise HTTPException(status_code=404, detail="Категория не найдена")
#     return updated_cost
#
#
# @cost_category_router.delete("/{cost_id}", response_model=CostCategoryOut)
# def delete_category(cost_id: int, db: Session = Depends(get_db)):
#     success = costcategory_crud.delete_cost_category(db, cost_id)
#     if not success:
#         raise HTTPException(status_code=404, detail="Категория не найдена")
#     return {"message": "Категория удалена"}
#
#
# @user_router.delete("/{user_id}", response_model=UserOut)
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     success = user_crud.delete_user(db, user_id)
#     if not success:
#         raise HTTPException(status_code=404, detail="Пользователь не найден")
#     return {"message": "Пользователь удалён"}
#
#
# @user_router.put("/{user_id}", response_model=UserOut)
# def update_user(user_id: int, user_data: UserGet, db: Session = Depends(get_db)):
#     updated_user = user_crud.update_user(db, user_id, user_data)
#     if updated_user is None:
#         raise HTTPException(status_code=404, detail="Пользователь не найден")
#     return updated_user