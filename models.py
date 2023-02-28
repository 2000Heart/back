# coding=utf-8
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy_model_convert.sqlalchemy_model_convert import ModelConvert

from database import Base


class User(Base, ModelConvert):
    __tablename__ = 'user'

    userId = Column(Integer, primary_key=True, autoincrement=True)
    userName = Column(String(255), nullable=False)
    password = Column(String(255), nullable=True)
    school = Column(String(255), nullable=False)
    avatar = Column(String(255), nullable=True)
    userType = Column(Integer, nullable=False)
    className = Column(String(255), nullable=True)

    def __repr__(self):
        return f"{self.userId}-{self.userName}"


class Lessons(Base, ModelConvert):
    __tablename__ = 'lessons'

    lessonId = Column(Integer, primary_key=True, autoincrement=True)
    lessonName = Column(String(255), unique=True)


class Schedule(Base, ModelConvert):
    __tablename__ = 'lesson_schedule'

    eventId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(String(255), nullable=True)
    lessonId = Column(Integer, ForeignKey('Lesson.lessonId'))
    lessonName = Column(String(255), ForeignKey('Lessons.lessonName'))
    teacherId = Column(Integer, nullable=True)
    teacherName = Column(String(255), nullable=True)
    duration = Column(String(255), nullable=False)
    weekTime = Column(Integer, nullable=False)
    unit = Column(Integer, nullable=False)
    classroom = Column(String(255), nullable=True)


class CheckInLesson(Base, ModelConvert):
    __tablename__ = 'check_schedule'

    checkId = Column(Integer, primary_key=True, autoincrement=True)
    lessonId = Column(Integer, ForeignKey('Lesson.lessonId'))
    teacherId = Column(Integer)
    postTime = Column(String(255), nullable=True)
    checkedUser = Column(String(255), nullable=True)
    userAll = Column(String(255), nullable=False)
