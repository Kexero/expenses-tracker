from sqlalchemy.orm import Session
from sqlalchemy import or_
from model.user_model import Users
from schema.user_schemas import UserGet, UserEmailUpdate
from typing import List, Optional


def create_user(db: Session, user: UserGet) -> Users:
    new_user = Users(
        first_name = user.first_name,
        last_name = user.last_name,
        email = user.email,
        gender = user.gender,
        password = user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_id(db: Session, user_id: int) -> Optional[Users]:
    return db.query(Users).filter(Users.user_id == user_id).first()


def get_all_users(db: Session) -> List[Users]:
    return db.query(Users).all()


def get_user_by_name(db: Session, first_name: str, last_name: str) -> List[Users]:
    return db.query(Users).filter(or_(Users.first_name == first_name, Users.last_name == last_name)).all()


def get_user_by_gender(db: Session, gender: str) -> List[Users]:
    return db.query(Users).filter(Users.gender == gender).all()


def get_user_by_email(db: Session, email: str) -> Optional[Users]:
    return db.query(Users).filter(Users.email == email).first()


def update_user_admin(db: Session, user_id: int, user_data: UserGet) -> Optional[Users]:
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if user:
        user.first_name = user_data.first_name
        user.last_name = user_data.last_name
        user.email = user_data.email
        user.gender = user_data.gender
        user.password = user_data.password
        db.commit()
        db.refresh(user)
        return user
    return None


def update_user(db: Session, db_user: Users, user_data: UserGet) -> Users:
    db_user.first_name = user_data.first_name
    db_user.last_name = user_data.last_name
    db_user.gender = user_data.gender
    db_user.password = user_data.password
    db.commit()
    db.refresh(db_user)
    return db_user


def change_email(db: Session, db_user: Users, new_email: str) -> Users:
    db_user.email = new_email
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int) -> bool:
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False