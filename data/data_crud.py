from typing import List, Type

from sqlalchemy import and_
from sqlalchemy.orm import Session
from data import data_schemas
import utils
from data.data_models import Lessons, ClassInfo, Classroom
from lesson.lesson_models import LessonInfo
from schedule.schedule_models import Schedule
from user.user_crud import query_user_all


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
    db_data: List[data_schemas.ReadClassInfo] = []
    class_all = db.query(ClassInfo).filter(
        and_(ClassInfo.schoolName == data.schoolName, ClassInfo.teacherId.like(f"%{data.teacherId}%"))).all()
    for e in class_all:
        e_data = data_schemas.ReadClassInfo(**e.__dict__)
        e_data.students = query_user_all(db, [int(x) for x in e.userId.split(',')])
        db_data.append(e_data)
    return db_data


def query_class_school_list(db: Session, data: data_schemas.QueryClassList):
    class_list = db.query(ClassInfo).filter_by(schoolName=data.schoolName).all()
    return class_list


def update_class(db: Session, data: data_schemas.UpdateClass):
    db_class = db.query(ClassInfo).filter_by(schoolName=data.schoolName, classId=data.classId).first()
    db_lesson: List[Type[LessonInfo]] = db.query(LessonInfo).filter(LessonInfo.userId.like(f"%{db_class.userId}%")).all()
    db_schedule: List[Type[Schedule]] = db.query(Schedule).filter(Schedule.userId.like(f"%{db_class.userId}%")).all()
    for j in db_lesson:
        j.userId += f"{data.userId}"
    for i in db_schedule:
        i.userId += f"{data.userId}"
    db_class.userId += f"{data.userId}"
    db.commit()
    return db_class


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
