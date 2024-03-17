from datetime import datetime

from sqlalchemy import and_, exc

from app.core.db.session import SessionLocal
from app.core.security import get_password_hash, verify_password
from app.dao.base import ConflictError, NotFoundError, ValidationError
from app.models.users import User as UserModel
from app.schemas.auth import UpdateUserSchema, UserInDB, UserSchema


class DAOUser:
    @staticmethod
    def get_user_by_id(user_id: int) -> UserModel:
        with SessionLocal() as session:
            user = session.query(UserModel).where(and_(UserModel.id == user_id, UserModel.deleted_at.is_(None))).first()
        if not user:
            raise NotFoundError(detail="User not Found")
        return user

    @staticmethod
    def create_user(username: str, password: str) -> UserSchema:
        user = UserModel(
            username=username,
            password=get_password_hash(password),
        )
        with SessionLocal() as session:
            try:
                session.add(user)
                session.commit()
                session.refresh(user)
            except exc.IntegrityError:
                raise ConflictError(detail="User already exists")

        return UserSchema(username=user.username)

    @classmethod
    def get_user_in_db(cls, username: str, password: str) -> UserInDB:
        with SessionLocal() as session:
            user = (
                session.query(UserModel)
                .where(and_(UserModel.username == username, UserModel.deleted_at.is_(None)))
                .first()
            )
        if not user:
            raise NotFoundError(detail="User not Found")

        if not verify_password(password, user.password):
            raise ValidationError(detail="Wrong password")

        return UserInDB(username=user.username, disables=user.disabled, hashed_password=user.password)

    @classmethod
    def change_user(cls, data: UpdateUserSchema) -> UserSchema:
        if data.password:
            data.password = get_password_hash(data.password)

        with SessionLocal() as session:
            user = session.query(UserModel).where(and_(UserModel.id == data.id, UserModel.deleted_at.is_(None))).first()
            for key, value in data.model_dump(mode="json", exclude_unset=True).items():
                setattr(user, key, value)
            user.updated_at = datetime.now()
            session.commit()
            session.refresh(user)

        return UserSchema(username=user.username)

    @classmethod
    def delete_user(cls, user_id: int) -> bool:
        with SessionLocal() as session:
            user = session.query(UserModel).where(and_(UserModel.id == user_id, UserModel.deleted_at.is_(None))).first()
            user.disabled = True
            user.deleted_at = datetime.now()
            session.commit()
            session.refresh(user)

        return True


dao_user = DAOUser()
