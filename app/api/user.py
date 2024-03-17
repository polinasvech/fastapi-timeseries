from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.core.config import settings
from app.core.security import create_access_token, get_current_active_user
from app.dao.dao_user import dao_user
from app.schemas.auth import (CreateUserSchema, Token, UpdateUserSchema,
                              UserSchema)

router = APIRouter(prefix="/user", tags=["user"])


@router.patch("/change_username/", response_model=UserSchema)
async def change_username(username: str, current_user: UserSchema = Depends(get_current_active_user)):
    return dao_user.change_user(UpdateUserSchema(id=current_user.id, username=username))


@router.patch("/change_password/", response_model=UserSchema)
async def change_password(
    password: str, repeated_password: str, current_user: UserSchema = Depends(get_current_active_user)
):
    return dao_user.change_user(
        UpdateUserSchema(id=current_user.id, password=password, repeated_password=repeated_password)
    )
