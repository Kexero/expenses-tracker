from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
from utils.init_data import validate_password


class UserBase(BaseModel):
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)
    email: EmailStr = Field(min_length=4)
    gender: Optional[str] = None


class UserGet(UserBase):
    password: str = Field(min_length=7)

    @field_validator("password")
    def validate(cls, value):
        return validate_password(value)


class UserOut(UserBase):
    class Config:
        orm_mode = True


class UserEmailUpdate(BaseModel):
    email: EmailStr
    class Config:
        orm_mode = True


class UserUpdateData(BaseModel):
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)
    gender: Optional[str] = None
    password: str = Field(min_length=7)

    @field_validator("password")
    def validate(cls, value):
        return validate_password(value)
    class Config:
        orm_mode = True