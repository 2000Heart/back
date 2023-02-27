# coding=utf-8
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy_model_convert.sqlalchemy_model_convert import ModelConvert

from database import Base


class User(Base, ModelConvert):
    __tablename__ = 'User'

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
    __tablename__ = 'Lessons'

    lessonId = Column(Integer, primary_key=True, autoincrement=True)
    lessonName = Column(String(255), unique=True)


class UsersLesson(Base, ModelConvert):
    __tablename__ = 'UsersLesson'

    eventId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('User.userId'))
    userName = Column(String(255), ForeignKey('User.userName'))
    lessonId = Column(Integer, ForeignKey('Lesson.lessonId'))
    lessonName = Column(String(255), ForeignKey('Lessons.lessonName'))
    teacherId = Column(Integer, nullable=True)
    teacherName = Column(String(255), nullable=True)
    startWeek = Column(Integer, nullable=False)
    endWeek = Column(Integer, nullable=False)
    classroom = Column(String(255), nullable=True)
