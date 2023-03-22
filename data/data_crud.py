from sqlalchemy import and_
from sqlalchemy.orm import Session
from data import data_schemas
import utils
from data.data_models import Lessons, ClassInfo, Classroom


def create_lesson(db: Session, data: data_schemas.CreateLesson):
    db_lesson = Lessons(**data.dict())
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson


def query_lesson(db: Session, data: str):
    return db.query(Lessons).filter(Lessons.lessonName == data).first()


def get_lesson(db: Session, data: data_schemas.CreateLesson):
    db_data = db.query(Lessons).filter_by(lessonName=data.lessonName).first()
    if db_data is None:
        db_data = Lessons(**data.dict())
        db.add(db_data)
        db.commit()
        db.refresh(db_data)
    return db_data


def create_class(db: Session, data: data_schemas.CreateClass):
    db_class = ClassInfo(**data.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class


def query_class(db: Session, data: data_schemas.QueryClass):
    return db.query(ClassInfo).filter(
        and_(ClassInfo.className == data.className, ClassInfo.schoolName == data.schoolName)).first()


def query_class_list(db: Session, data: data_schemas.QueryClassList):
    return db.query(ClassInfo).filter(
        and_(ClassInfo.schoolName == data.schoolName, ClassInfo.teacherId.like(f"%{data.teacherId}%"))).all()


def update_class(db: Session, data: data_schemas.UpdateClass):
    db_data = db.query(ClassInfo).filter_by(classId=data.classId)
    e = db_data.first().userId
    s = db_data.first().teacherId
    if data.schoolName is None:
        db_data.update({"userId": utils.updateList(e, data.userId), "teacherId": utils.updateList(s, data.teacherId)})
    else:
        db_data.update({"userId": utils.updateList(e, data.userId), "teacherId": utils.updateList(s, data.teacherId),
                        "schoolName": data.schoolName})
    db.commit()
    return db_data.first()


def create_classroom(db: Session, data: data_schemas.CreateClassroom):
    db_classroom = Classroom(**data.dict())
    db.add(db_classroom)
    db.commit()
    db.refresh(db_classroom)
    return db_classroom


def query_classroom(db: Session, data: data_schemas.QueryClassroom):
    return db.query(Classroom).filter(
        and_(Classroom.roomName == data.roomName, ClassInfo.schoolName == data.schoolName)).first()


def create_major(db: Session, data: data_schemas.CreateMajor):
    db_major = Classroom(**data.dict())
    db.add(db_major)
    db.commit()
    db.refresh(db_major)
    return db_major


def create_school(db: Session, data: data_schemas.CreateSchool):
    db_school = Classroom(**data.dict())
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school
