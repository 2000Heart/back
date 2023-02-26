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
    return db.query(models.User).filter(models.User.userName == name, models.User.school == school).count()


def query_user(db: Session, username: str, password: str):
    return db.query(models.User).filter(models.User.userName == username, models.User.password == password).first()


def create_lesson(db: Session, lesson: schemas.InsertLesson):
    db_lesson = models.Lesson(**lesson.dict())
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson


def check_lesson(db: Session, lesson: schemas.InsertLesson):
    return db.query(models.Lesson).filter(
        models.Lesson.lessonName == lesson.lessonName,
        models.Lesson.classroom == lesson.classroom,
        models.Lesson.startWeek == lesson.startWeek,
        models.Lesson.endWeek == lesson.endWeek
    ).first()


def insert_user_to_lesson(db: Session, e: schemas.InsertUserToLesson):
    db_e = models.UserToLesson(**e.dict())
    db.add(db_e)
    db.commit()
    db.refresh(db_e)
    return db_e

# def query_user_lessons():
#

