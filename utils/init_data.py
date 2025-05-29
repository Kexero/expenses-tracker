from sqlalchemy.orm import Session
from model.costcategory_model import CostCategory
from database import SessionLocal
from data.default_categories import default_categories


def create_default_categories():
    db: Session = SessionLocal()
    for cat in default_categories:
        exists = db.query(CostCategory).filter_by(name=cat["name"]).first()
        if not exists:
            new_cat = CostCategory(
                name=cat["name"],
                description=cat["description"],
                is_default=True
            )
            db.add(new_cat)
    db.commit()
    db.close()