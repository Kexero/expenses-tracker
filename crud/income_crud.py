import datetime
from sqlalchemy.orm import Session
from model.income_model import Income
from schema.income_schemas import IncomeGet
from typing import List, Optional


def create_income(db: Session, user_id: int, income: IncomeGet) -> Income:
    new_income = Income(
        user_id = user_id,
        amount = income.amount,
        source = income.source,
        date = income.date
    )
    db.add(new_income)
    db.commit()
    db.refresh(new_income)
    return new_income


def get_income_by_id(db: Session, income_id: int) -> Optional[Income]:
    return db.query(Income).filter(Income.income_id == income_id).first()


def get_all_income(db: Session) -> List[Income]:
    return db.query(Income).all()


def get_income_by_source(db: Session, income_source: str) -> List[Income]:
    return db.query(Income).filter(Income.source == income_source).all()


def get_income_by_amount(db: Session, income_amount: int) -> List[Income]:
    return db.query(Income).filter(Income.amount == income_amount).all()


def get_income_by_date(db: Session, income_date: datetime.datetime) -> List[Income]:
    return db.query(Income).filter(Income.date == income_date).all()


def update_income(db: Session, income_id: int, user_data: IncomeGet) -> Optional[Income]:
    income = db.query(Income).filter(Income.income_id == income_id).first()
    if income:
        income.amount = user_data.amount
        income.source = user_data.source
        income.date = user_data.date
        db.commit()
        db.refresh(income)
        return income
    return None


def delete_income(db: Session, income_id: int) -> bool:
    income = db.query(Income).filter(Income.income_id == income_id).first()
    if income:
        db.delete(income)
        db.commit()
        return True
    return False
