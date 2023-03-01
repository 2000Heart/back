# coding=utf-8

from sqlalchemy import insert, and_
from sqlalchemy.orm import Session

import schemas
from models import Schedule, User, Lessons


def create_user(db: Session, user: schemas.CreateUser):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_user_exist(db: Session, data: schemas.CreateUser):
    return db.query(User).filter(
        and_(User.userName == data.userName, User.school == data.school, User.userType == data.userType)).first()


def query_user(db: Session, username: str, password: str):
    return db.query(User).filter(and_(User.userName == username, User.password == password)).first()


def create_lesson(db: Session, lesson: schemas.CreateLesson):
    db_lesson = Lessons(**lesson.dict())
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson


def create_schedule(db: Session, schedule: schemas.CreateSchedule):
    db_schedule = Schedule(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule


def query_schedule(db: Session, userId: int):
    db_all: list = db.query(Schedule).all()
    db_e = []
    for e in db_all:
        if e.userId is None:
            if e.userId == userId:
                db_e.append(e)
        else:
            if any(f"{userId}" in item for item in e.userId.split(",")):
                db_e.append(e)
    return db_e


def check_schedule(db: Session, e: schemas.CreateSchedule):
    return db.query(Schedule).filter(
        and_(Schedule.lessonId == e.lessonId, Schedule.duration == e.duration, Schedule.weekTime == e.weekTime,
             Schedule.unit == e.unit)).first()


def update_schedule(db: Session, eventId: int, e):
    num = db.query(Schedule).filter_by(eventId=eventId).update(e.dict())
    db.commit()
    return num
