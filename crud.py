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


def check_user(db: Session, username: str, password: str):
    return db.query(models.User).filter(models.User.userName == username, models.User.password == password).first()

def create_lesson(db:Session, lesson: schemas.CreateLesson):
    db_lesson = models.Lesson(**lesson.dict())
    db.add(db_lesson)
    db.commit()
    db.refresh()
    return  db_lesson


def check_lesson(db: Session, lessonName=str, classroom=str, startWeek=int, endWeek=int):
    return db.query(models.Lesson).filter(models.Lesson.lessonName == lessonName, models.Lesson.classroom == classroom,
                                          models.Lesson.startWeek == startWeek,
                                          models.Lesson.endWeek == endWeek).first()
