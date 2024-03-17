from sqlalchemy import and_, exc, select

from app.core.db.session import get_session
from app.core.security import get_password_hash, verify_password
from app.dao.base import ConflictError, NotFoundError, ValidationError
from app.models.users import User as UserModel
from app.schemas.auth import UserInDB, UserSchema


class DAOUser:
    @staticmethod
    def create_user(username: str, password: str) -> UserSchema:
        session = get_session()

        user = UserModel(
            username=username,
            password=get_password_hash(password),
        )
        try:
            session.add(user)
            session.commit()
        except exc.IntegrityError:
            raise ConflictError(detail="User already exists")

        return UserSchema(username=user.username)

    @staticmethod
    def get_user_in_db(username: str, password: str) -> UserInDB:
        session = get_session()
        user = (
            session.query(UserModel).where(and_(UserModel.username == username, UserModel.deleted_at.is_(None))).first()
        )
        if not user:
            raise NotFoundError(detail="User not Found")

        if not verify_password(password, user.password):
            raise ValidationError(detail="Wrong password")

        return UserInDB(username=user.username, disables=user.disabled, hashed_password=user.password)


dao_user = DAOUser()
