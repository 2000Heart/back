from sqlalchemy import and_
from sqlalchemy.orm import Session
from user import user_schemas
from user.user_models import User


def create_user(db: Session, user: user_schemas.CreateUser):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_user_exist(db: Session, data: user_schemas.CreateUser):
    return db.query(User).filter(
        and_(User.userName == data.userName, User.school == data.school, User.userType == data.userType)).first()


def query_user(db: Session, username: str, password: str):
    return db.query(User).filter(and_(User.userName == username, User.password == password)).first()
