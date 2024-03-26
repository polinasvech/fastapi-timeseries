from fastapi import APIRouter, Depends

from app.core.security import get_current_active_user
from app.dao.dao_user import dao_user
from app.schemas.auth import UpdateUserSchema, UserSchema, UserChangeName

router = APIRouter(prefix="/users", tags=["user"])


@router.patch("/change_username/", response_model=UserSchema)
async def change_username(data: UserChangeName, current_user: UserSchema = Depends(get_current_active_user)):
    return dao_user.change_user(UpdateUserSchema(id=current_user.id, username=data.username))


@router.delete("/delete/{user_id}", response_model=bool)
async def delete_user(user_id: int, current_user: UserSchema = Depends(get_current_active_user)):
    return dao_user.delete_user(current_user.id)
