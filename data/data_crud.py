from sqlalchemy.orm import Session
from data import data_schemas
from data.data_models import Lessons, ClassInfo, Classroom


def create_lesson(db: Session, data: data_schemas.CreateLesson):
    db_lesson = Lessons(**data.dict())
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson


def create_class(db: Session, data: data_schemas.CreateClass):
    db_class = ClassInfo(**data.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class


def create_classroom(db: Session, data: data_schemas.CreateClass):
    db_classroom = Classroom(**data.dict())
    db.add(db_classroom)
    db.commit()
    db.refresh(db_classroom)
    return db_classroom


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
