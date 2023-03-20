from datetime import datetime

from sqlalchemy.orm import Session
from lesson import lesson_schemas
from lesson.lesson_models import LessonInfo, CheckInLesson
from schedule import schedule_crud
from utils import checkUser, checkTeacher


def create_lesson(db: Session, data: lesson_schemas.CreateLessonInfo):
    db_data = LessonInfo(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


def create_lesson_all(db: Session, data: lesson_schemas.CreateLessonAll):
    db.bulk_insert_mappings(LessonInfo(), data.d)
    db.commit()


def create_check(db: Session, data: lesson_schemas.CreateCheck):
    db_data = CheckInLesson(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


def update_task(db: Session, data: lesson_schemas.AddLessonTask):
    db_data = db.query(LessonInfo).filter_by(infoId=data.infoId)
    e = db_data.first().lessonTask
    num: int
    if e is None:
        e = data.lessonTask
        num = db_data.update({"lessonTask": e})
    else:
        e.split(",").append(data.lessonTask)
        num = db_data.update({"lessonTask": ",".join(e)})
    db.commit()
    return num


def insert_check(db: Session, data: lesson_schemas.AddLessonCheck):
    num = db.query(LessonInfo).filter_by(infoId=data.infoId).update({"checkId": data.checkId})
    db.commit()
    return num


def query_lesson(db: Session, data: lesson_schemas.QueryLessons):
    if data.infoId != 0 and data.infoId is not None:
        return db.query(LessonInfo).filter_by(infoId=data.infoId).first()
    else:
        db_data = schedule_crud.query_schedule(db, data.userId, data.userType)
        db_list = []
        for i in db_data:
            db_e = db.query(LessonInfo).filter(LessonInfo.eventId.like(f"%{i.eventId}%")).first()
            if db_e is not None:
                db_list.append(db_e)
        return list(set(db_list))


def query_check_list(db: Session, data: int):
    data_all = db.query(CheckInLesson).all()
    return checkUser(data_all, data)


def query_check(db: Session, data: int):
    return db.query(CheckInLesson).filter_by(infoId=data).order_by(CheckInLesson.startTime.asc()).filter(
        CheckInLesson.startTime >= datetime.now()).first()


def query_lesson_info(db: Session, data: lesson_schemas.QueryLessonInfo):
    return db.query(LessonInfo).filter_by(lessonName=data.lessonName, schoolName=data.schoolName).first()
