from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.core.config import settings
from app.core.security import create_access_token, get_current_active_user
from app.dao.dao_user import dao_user
from app.schemas.auth import CreateUserSchema, Token, UserSchema, UpdateUserSchema, UserChangePassword

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token/", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = dao_user.get_user_in_db(
        form_data.username,
        form_data.password,
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me/", response_model=UserSchema)
async def read_users_me(current_user: UserSchema = Depends(get_current_active_user)):
    return current_user


@router.post("/register/", response_model=UserSchema)
async def create_new_user(data: CreateUserSchema):
    return dao_user.create_user(data.username, data.password)


@router.post("/login/", response_model=UserSchema)
async def login(data: CreateUserSchema):
    return dao_user.create_user(data.username, data.password)


@router.patch("/change_password/", response_model=UserSchema)
async def change_password(data: UserChangePassword, current_user: UserSchema = Depends(get_current_active_user)):
    return dao_user.change_user(UpdateUserSchema(id=current_user.id, password=data.password))
