# coding=utf-8
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy_model_convert.sqlalchemy_model_convert import ModelConvert

from database import Base, engine


class User(Base, ModelConvert):
    __tablename__ = 'user'

    userId = Column(Integer, primary_key=True, autoincrement=True)
    userName = Column(String(255), nullable=False)
    password = Column(String(255), nullable=True)
    school = Column(String(255), nullable=False)
    avatar = Column(String(255), nullable=True)
    userType = Column(Integer, nullable=False)

    # className = Column(String(255), nullable=True)

    def __repr__(self):
        return f"{self.userId}-{self.userName}"

    Base.metadata.create_all(engine)


class Lessons(Base, ModelConvert):
    __tablename__ = 'lessons'

    lessonId = Column(Integer, primary_key=True, autoincrement=True)
    lessonName = Column(String(255), unique=True)

    Base.metadata.create_all(engine)


class Schedule(Base, ModelConvert):
    __tablename__ = 'lesson_schedule'

    eventId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(String(255), nullable=True)
    lessonId = Column(Integer, ForeignKey('lessons.lessonId'))
    lessonName = Column(String(255), ForeignKey('lessons.lessonName'))
    teacherId = Column(Integer, nullable=True)
    teacherName = Column(String(255), nullable=True)
    duration = Column(String(255), nullable=False)
    weekTime = Column(Integer, nullable=False)
    startUnit = Column(Integer, nullable=False)
    endUnit = Column(Integer, nullable=False)
    classroom = Column(String(255), nullable=True)

    Base.metadata.create_all(engine)


class CheckInLesson(Base, ModelConvert):
    __tablename__ = 'check_schedule'

    checkId = Column(Integer, primary_key=True, autoincrement=True)
    lessonId = Column(Integer, ForeignKey('lessons.lessonId'))
    teacherId = Column(Integer)
    postTime = Column(String(255), nullable=True)
    checkedUser = Column(String(255), nullable=True)
    userAll = Column(String(255), nullable=False)
    startTime = Column(String(255), nullable=False)
    endTime = Column(String(255), nullable=False)
    status = Column(Integer)

    Base.metadata.create_all(engine)


class Majors(Base, ModelConvert):
    __tablename__ = 'majors'

    majorId = Column(Integer, primary_key=True, autoincrement=True)
    majorName = Column(String(255), unique=True)

    Base.metadata.create_all(engine)


class LessonInfo(Base, ModelConvert):
    __tablename__ = 'lesson_info'

    infoId = Column(Integer, primary_key=True, autoincrement=True)
    lessonId = Column(Integer, ForeignKey('lessons.lessonId'))
    teacherId = Column(Integer)
    teacherName = Column(String(255))
    lessonTask = Column(String(255))
    checkId = Column(Integer, ForeignKey('check_schedule'), nullable=True)


class ClassInfo(Base, ModelConvert):
    __tablename__ = 'class_info'

    classId = Column(Integer, primary_key=True, autoincrement=True)
    teacherId = Column(String(255))
    userId = Column(String(255))
