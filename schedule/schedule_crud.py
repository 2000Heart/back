from sqlalchemy import and_
from sqlalchemy.orm import Session
from schedule import schedule_schemas
from schedule.schedule_models import Schedule


def create_schedule(db: Session, schedule: schedule_schemas.CreateSchedule):
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


def check_schedule(db: Session, e: schedule_schemas.CreateSchedule):
    return db.query(Schedule).filter(
        and_(Schedule.lessonId == e.lessonId, Schedule.duration == e.duration, Schedule.weekTime == e.weekTime,
             Schedule.startUnit == e.startUnit, Schedule.endUnit == e.endUnit)).first()


def update_schedule(db: Session, eventId: int, e):
    num = db.query(Schedule).filter_by(eventId=eventId).update(e.dict())
    db.commit()
    return num
