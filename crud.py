from sqlalchemy.orm import Session
from sqlalchemy.sql import exists
import models
import schemas


def create_user(db: Session, user: schemas.CreateUser):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_user_exist(db: Session, name: str, school: str):
    return db.query(models.User).filter(models.User.userName == name, models.User.school == school).scalar()


def check_user(db: Session, username: str, password: str):
    return db.query(models.User).filter(models.User.userName == username, models.User.password == password).first()