from sqlalchemy import and_
from sqlalchemy.orm import Session
from schedule import schedule_schemas
from schedule.schedule_models import Schedule, Table
from utils import checkUser


def create_schedule(db: Session, schedule: schedule_schemas.CreateSchedule):
    db_schedule = Schedule(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule


def query_schedule(db: Session, userId: int):
    db_all: list = db.query(Schedule).order_by(Schedule.startUnit.asc()).all()
    return checkUser(db_all, userId)


def check_schedule(db: Session, e: schedule_schemas.CreateSchedule):
    return db.query(Schedule).filter(
        and_(Schedule.lessonId == e.lessonId, Schedule.duration == e.duration, Schedule.weekTime == e.weekTime,
             Schedule.startUnit == e.startUnit, Schedule.endUnit == e.endUnit)).first()


def update_schedule(db: Session, eventId: int, e):
    num = db.query(Schedule).filter_by(eventId=eventId).update(e.dict())
    db.commit()
    return num


def create_default_table(db: Session, userId: int):
    db_data = Table(userId=userId, currentWeek=1, lessonNum=12, totalWeek=7)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


def query_table(db: Session, userId: int):
    db_data = db.query(Schedule).filter_by(userId=userId).first()
    return db_data
