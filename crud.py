# coding=utf-8
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


def check_user_exist(db: Session, data: schemas.QueryUser or schemas.CreateUser):
    return db.query(models.User).filter(
        models.User.userName == data.userName,
        models.User.school == data.school,
        models.User.userType == data.userType).first()


def query_user(db: Session, username: str, password: str):
    return db.query(models.User).filter(
        models.User.userName == username,
        models.User.password == password).first()


def create_lesson(db: Session, lesson: schemas.CreateLesson):
    db_lesson = models.Lessons(**lesson.dict())
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson


def create_user_s_lesson(db: Session, e: schemas.CreateUsersLesson):
    db_e = models.UsersLesson(**e.dict())
    db.add(db_e)
    db.commit()
    db.refresh(db_e)
    return db_e
