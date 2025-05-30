from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from database import get_db
from crud import user_crud
from schema.user_schemas import UserGet, UserOut, UserEmailUpdate, UserUpdateData
from typing import List
from template import templates


user_router = APIRouter(prefix="/user", tags=["Пользователи"])


@user_router.get("/", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    return user_crud.get_all_users(db)


@user_router.get("/search-email", response_model=UserOut)
def get_users_by_email(user_email: str, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_email(db, user_email)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


@user_router.get("/search-name", response_model=List[UserOut])
def get_user_by_name(first_name: str, last_name: str, db: Session = Depends(get_db)):
    users = user_crud.get_user_by_name(db, first_name, last_name)
    if not users:
        raise HTTPException(status_code=404, detail="Пользователи не найдены")
    return users


@user_router.get("/search-gender", response_model=List[UserOut])
def get_users_by_gender(gender: str, db: Session = Depends(get_db)):
    return user_crud.get_user_by_gender(db, gender)


@user_router.get("/register")
def show_register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@user_router.post("/", response_model=UserOut)
def create_user(user: UserGet, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует")
    return user_crud.create_user(db, user)


@user_router.put("/update", response_model=UserOut)
def update_user(email: str, user_data: UserUpdateData, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_email(db, email)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    updated_user = user_crud.update_user(db, user, user_data)
    return updated_user


@user_router.put("/change-email", response_model=UserOut)
def change_email(email: str, user_data: UserEmailUpdate, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_email(db, email)
    if user is None:
        raise HTTPException(status_code=404, detail="Почта не найдена")
    changed_email = user_crud.change_email(db, user, user_data.email)
    return changed_email
