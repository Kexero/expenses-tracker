import datetime
from sqlalchemy.orm import Session
from model.expense_model import Expenses
from schema.expenses_schemas import ExpensesGet
from typing import List, Optional


def create_expense(db: Session, user_id: int, cost_category_id: int, expense: ExpensesGet) -> Expenses:
    new_expense = Expenses(
        user_id = user_id,
        cost_category_id = cost_category_id,
        amount = expense.amount,
        description = expense.description,
        date = expense.date
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


def get_expense_by_id(db: Session, expense_id: int) -> Optional[Expenses]:
    return db.query(Expenses).filter(Expenses.expense_id == expense_id).first()


def get_all_expenses(db: Session) -> List[Expenses]:
    return db.query(Expenses).all()


def get_expenses_by_description(db: Session, expenses_description: str) -> List[Expenses]:
    return db.query(Expenses).filter(Expenses.description.ilike(f"%{expenses_description}%")).all()


def get_expenses_by_amount(db: Session, expenses_amount: int) -> List[Expenses]:
    return db.query(Expenses).filter(Expenses.amount == expenses_amount).all()


def get_expenses_by_date(db: Session, expenses_date: datetime.datetime) -> List[Expenses]:
    return db.query(Expenses).filter(Expenses.date == expenses_date).all()


def update_expense(db: Session, expense_id: int, user_data: ExpensesGet) -> Optional[Expenses]:
    expense = db.query(Expenses).filter(Expenses.expense_id == expense_id).first()
    if expense:
        expense.amount = user_data.amount
        expense.description = user_data.description
        expense.date = user_data.date
        db.commit()
        db.refresh(expense)
        return expense
    return None


def delete_expense(db: Session, expense_id: int) -> bool:
    expense = db.query(Expenses).filter(Expenses.expense_id == expense_id).first()
    if expense:
        db.delete(expense)
        db.commit()
        return True
    return False