from typing import List

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


def user_create_check(db: Session, data: user_schemas.CreateUser):
    return db.query(User).filter(
        and_(User.userName == data.userName, User.school == data.school, User.userType == data.userType,
             User.className == data.className)).first()


def user_account_check(db: Session, data: user_schemas.Login):
    return db.query(User).filter(
        and_(User.userName == data.userName)).first()


def update_user(db: Session, data: user_schemas.UpdateUser):
    num = db.query(User).filter_by(userId=data.userId).update(data.dict(exclude_none=True))
    if num > 0:
        db_data = db.query(User).filter_by(userId=data.userId).first()
        print(db_data.key_values())
        return db_data
    else:
        return None


def query_user(db: Session, username: str, password: str):
    return db.query(User).filter(and_(User.userName == username, User.password == password)).first()


def trans_name(db: Session, userId: List[int]):
    username = db.query(User).filter(User.userId.in_(userId)).with_entities(User.userName).all()
    return ','.join([i[0] for i in username])


def query_user_all(db: Session, userId: List[int]):
    return db.query(User).filter(User.userId.in_(userId)).all()
