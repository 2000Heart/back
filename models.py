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


class Lesson(Base, ModelConvert):
    __tablename__ = 'lesson'

    lessonId = Column(Integer, primary_key=True, autoincrement=True)
    lessonName = Column(String(255))
    classroom = Column(String(255))
    startWeek = Column(Integer)
    endWeek = Column(Integer)


class UserToLesson(Base, ModelConvert):
    __tablename__ = 'userToLesson'

    eventId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.userId'))
    userType = Column(Integer, ForeignKey('user.userType'))
    lessonId = Column(Integer, ForeignKey('lesson.lessonId'))

