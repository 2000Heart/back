from sqlalchemy import and_
from sqlalchemy.orm import Session
from schedule import schedule_schemas
from schedule.schedule_models import Schedule, Table
from utils import checkUser, checkTeacher


def create_schedule(db: Session, schedule: schedule_schemas.CreateSchedule):
    db_schedule = Schedule(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule


def create_schedule_all(db: Session, data: schedule_schemas.CreateScheduleAll):
    db.bulk_save_objects(Schedule(), data.d)
    db.commit()
    db_list = []
    for i in data.d:
        db_list.append(db.query(Schedule).filter_by(userId=i.userId, teacherId=i.teacherId, lessonName=i.lessonName))
    return db_list


def query_schedule(db: Session, userId: int, userType: int):
    db_all: list = db.query(Schedule).order_by(Schedule.startUnit.asc()).all()
    if userType == 0:
        return checkUser(db_all, userId)
    else:
        return checkTeacher(db_all, userId)


def query_schedule_list(db: Session, data: schedule_schemas.QueryScheduleList):
    if data.userType == 0:
        db_data = db.query(Schedule).where(
            and_(Schedule.userId.like(data.userId), Schedule.weekTime == data.weekTime,
                 Schedule.startUnit <= data.startUnit, Schedule.endUnit > data.startUnit)).all()
        return db_data
    else:
        db_data = db.query(Schedule).filter(
            and_(Schedule.teacherId.like(data.userId), Schedule.weekTime == data.weekTime,
                 Schedule.startUnit <= data.startUnit, Schedule.endUnit > data.startUnit)).all()
        return db_data


def check_schedule(db: Session, e: schedule_schemas.CreateSchedule):
    return db.query(Schedule).filter(
        and_(Schedule.lessonId == e.lessonId, Schedule.duration == e.duration, Schedule.weekTime == e.weekTime,
             Schedule.startUnit == e.startUnit, Schedule.endUnit == e.endUnit)).first()


def update_schedule(db: Session, e: schedule_schemas.UpdateSchedule):
    num = db.query(Schedule).filter_by(eventId=e.eventId).update(e.dict(exclude_none=True))
    db.commit()
    return num


def create_default_table(db: Session, userId: int):
    db_data = Table(userId=userId, currentWeek=1, lessonNum=12, totalWeek=7)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


def query_table(db: Session, userId: int):
    db_data = db.query(Table).filter_by(userId=userId).first()
    return db_data


def update_table(db: Session, table: schedule_schemas.UpdateTable):
    num = db.query(Table).filter_by(tableId=table.tableId).update(table.dict())
    db.commit()
    return num
