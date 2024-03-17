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
    repeated_password: str

    @validator("repeated_password")
    def passwords_match(cls, repeated_pwd, values):
        if repeated_pwd != values["password"]:
            raise ValidationError(detail="Passwords do not match")
        return repeated_pwd
