from datetime import datetime

from sqlalchemy.orm import Session
from lesson import lesson_schemas
from lesson.lesson_models import LessonInfo, CheckInLesson, CheckStu
from message import message_crud
from message.message_schemas import CreateMessage
from schedule import schedule_crud
from user.user_crud import trans_name
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


def create_check_stu(db: Session, data: lesson_schemas.CreateCheckStu):
    db_data = CheckStu(**data.dict())
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
        if data.userType == 0:
            db_e = db.query(LessonInfo).filter(LessonInfo.userId.like(f"%{data.userId}%")).all()
        else:
            db_e = db.query(LessonInfo).filter(LessonInfo.teacherId.like(f"%{data.userId}")).all()
    return db_e


def query_check_list(db: Session, data: int):
    data_all = db.query(CheckInLesson).filter(CheckInLesson.userAll.like(f"%{data}%")).all()
    return data_all


def query_check_history(db: Session, data: lesson_schemas.QueryCheckHistory):
    db_data = []
    if data.userType == 1:
        check_all = db.query(CheckInLesson).filter_by(teacherId=data.userId).all()
    else:
        check_all = db.query(CheckInLesson).filter(CheckInLesson.userAll.like(f"%{data.userId}%")).all()
    for e in check_all:
        need = [int(x) for x in e.userAll.split(',')]
        checked = query_check_stu(db, e.checkId)
        i = lesson_schemas.ReadHistory(**e.__dict__)
        i.need = need.__len__()
        i.checkNum = checked.__len__()
        if [check.userId for check in checked].__contains__(data.userId):
            i.checked = 1
        else:
            i.checked = 0
        i.miss = trans_name(db, list(set(need).symmetric_difference(set([check.userId for check in checked]))))
        db_data.append(i)
    return db_data


def query_check_stu(db: Session, data: int):
    data_all = db.query(CheckStu).filter_by(checkId=data).all()
    return data_all


def query_check(db: Session, data: int):
    return db.query(CheckInLesson).filter_by(infoId=data).order_by(CheckInLesson.startTime.asc()).filter(
        CheckInLesson.startTime >= datetime.now()).first()


def update_check(db: Session, data: lesson_schemas.UpdateCheck):
    num = db.query(CheckInLesson).filter_by(checkId=data.checkId).update({CheckInLesson.checkedUser: data.userId})
    db.commit()
    return num


def update_check_stu(db: Session, data: lesson_schemas.UpdateCheckStu):
    num = db.query(CheckStu).filter_by(id=data.id).update({CheckStu.index: data.index})
    db.commit()
    return num


def query_lesson_info(db: Session, data: lesson_schemas.QueryLessonInfo):
    return db.query(LessonInfo).filter_by(lessonName=data.lessonName, schoolName=data.schoolName).first()


def delete_check_stu(db: Session, data: lesson_schemas.DeleteCheckStu):
    num = db.query(CheckStu).filter_by(id=data.id).delete()
    db.commit()
    return num
