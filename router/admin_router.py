from fastapi import APIRouter, Depends
from utils.init_data import create_default_categories

admin_router = APIRouter(prefix="/admin", tags=["Админ"])


@admin_router.post("/init-default-categories")
def init_categories():
    create_default_categories()
    return {"message": "Базовые категории созданы (даже если они уже были)"}