from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional


class UserBase(BaseModel):
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)
    email: EmailStr = Field(min_length=4)
    gender: Optional[str] = None


class UserGet(UserBase):
    password: str = Field(min_length=7)

    @field_validator("password")
    def validate_password(cls, value):
        if not any(char.isdigit() for char in value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        if not any(char.isupper() for char in value):
            raise ValueError("Пароль должен содержать хотя бы одну заглавную букву")
        return value


class UserOut(UserBase):
    class Config:
        orm_mode = True
