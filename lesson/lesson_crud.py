from sqlalchemy.orm import Session
from lesson import lesson_schemas
from lesson.lesson_models import LessonInfo, CheckInLesson
from utils import checkUser, checkTeacher


def create_lesson(db: Session, data: lesson_schemas.CreateLessonInfo):
    db_data = LessonInfo(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


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


def query_lesson(db: Session, data: lesson_schemas.QueryLessonInfo):
    data_all = db.query(LessonInfo).all()
    if data.infoId != 0:
        return db.query(LessonInfo).filter_by(infoId=data.infoId).first()
    else:
        if data.userType == 0:
            return checkUser(data_all, data.userId)
        else:
            return checkTeacher(data_all, data.userId)


def query_check_list(db: Session, data: int):
    data_all = db.query(CheckInLesson).all()
    return checkUser(data_all, data)


def query_check(db: Session, data: int):
    return db.query(CheckInLesson).filter_by(infoId=data).first()
