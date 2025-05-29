from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class Income(Base):
    __tablename__ = "income"

    income_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), index=True)
    amount = Column(Integer, index=True, nullable=False)
    source = Column(String, index=True, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now(), index=True)