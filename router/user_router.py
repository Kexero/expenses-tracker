from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import user_crud
from schema.user_schemas import UserGet, UserOut
from typing import List


user_router = APIRouter(prefix="/user", tags=["Пользователи"])


@user_router.post("/", response_model=UserOut)
def create_user(user: UserGet, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует")
    return user_crud.create_user(db, user)


@user_router.get("/", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    return user_crud.get_all_users(db)


@user_router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return db_user


@user_router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, user_data: UserGet, db: Session = Depends(get_db)):
    updated_user = user_crud.update_user(db, user_id, user_data)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return updated_user


@user_router.delete("/{user_id}", response_model=UserOut)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    success = user_crud.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return {"message": "Пользователь удалён"}