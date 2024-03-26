from pydantic import BaseModel, validator

from app.dao.base import ValidationError


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str or None = None


class UserSchema(BaseModel):
    username: str


class UserInDB(UserSchema):
    hashed_password: str


class CreateUserSchema(BaseModel):
    username: str
    password: str


class UpdateUserSchema(BaseModel):
    id: int
    username: str | None = None
    password: str | None = None


class UserChangeName(BaseModel):
    username: str


class UserChangePassword(BaseModel):
    password: str
