from sqlalchemy import Column, Integer, String
from database import Base


class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, unique=False, index=True, nullable=False)
    last_name = Column(String, unique=False, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    gender = Column(String, unique=False, index=True, nullable=True)
    password = Column(String, nullable=False)

