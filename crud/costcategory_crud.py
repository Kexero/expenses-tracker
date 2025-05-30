from sqlalchemy.orm import Session
from model.costcategory_model import CostCategory
from schema.costcategory_shemas import CostCategoryGet
from typing import List, Optional


def create_cost_category(db: Session, cost_category: CostCategoryGet) -> CostCategory:
    new_cost_category = CostCategory(
        name = cost_category.name,
        description = cost_category.description,
        is_default = cost_category.is_default
    )
    db.add(new_cost_category)
    db.commit()
    db.refresh(new_cost_category)
    return new_cost_category


def get_cost_category_by_id(db: Session, cost_category_id: int) -> Optional[CostCategory]:
    return db.query(CostCategory).filter(CostCategory.cost_category_id == cost_category_id).first()


def get_all_cost_categories(db: Session) -> List[CostCategory]:
    return db.query(CostCategory).all()


def get_cost_category_by_description(db: Session, cost_category_description: str) -> List[CostCategory]:
    return db.query(CostCategory).filter(CostCategory.description.ilike(f"%{cost_category_description}%")).all()


def get_cost_category_by_name(db: Session, cost_category_name: str) -> Optional[CostCategory]:
    return db.query(CostCategory).filter(CostCategory.name == cost_category_name).first()


def update_cost_categories(db: Session, cost_category_id: int, user_data: CostCategoryGet) -> Optional[CostCategory]:
    cost_category = db.query(CostCategory).filter(CostCategory.cost_category_id == cost_category_id).first()
    if cost_category:
        cost_category.name = user_data.name
        cost_category.description = user_data.description
        db.commit()
        db.refresh(cost_category)
        return cost_category
    return None


def delete_cost_category(db: Session, cost_category_id: int) -> bool:
    cost_category = db.query(CostCategory).filter(CostCategory.cost_category_id == cost_category_id).first()
    if cost_category:
        db.delete(cost_category)
        db.commit()
        return True
    return False