from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class Expenses(Base):
    __tablename__ = "expenses"

    expense_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), index=True, nullable=False)
    category_id = Column(Integer, ForeignKey("cost_categories.cost_category_id"), index=True, nullable=False)
    amount = Column(Integer, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now(), index=True)
