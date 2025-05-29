from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class CostCategory(Base):
    __tablename__ = "cost_categories"

    cost_category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=False)
    is_default = Column(Boolean, default=False)
