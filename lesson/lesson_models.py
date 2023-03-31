from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_model_convert.sqlalchemy_model_convert import ModelConvert
from database import Base, engine


class CheckInLesson(Base, ModelConvert):
    __tablename__ = 'check_schedule'

    checkId = Column(Integer, primary_key=True, autoincrement=True)
    infoId = Column(Integer, ForeignKey('lesson_info.infoId'))
    lessonName = Column(String(255))
    teacherId = Column(Integer)
    teacherName = Column(String(255))
    postTime = Column(String(255), nullable=True)
    checkedUser = Column(String(648), nullable=True)
    userAll = Column(String(648), nullable=False)
    startTime = Column(String(255), nullable=False)
    endTime = Column(String(255), nullable=False)
    column = Column(String(255))
    row = Column(String(255))
    status = Column(Integer)

    Base.metadata.create_all(engine)


class CheckStu(Base, ModelConvert):
    __tablename__ = 'check_stu'

    id = Column(Integer, primary_key=True, autoincrement=True)
    checkId = Column(Integer)
    userId = Column(Integer)
    userName = Column(String(255))
    index = Column(Integer)


class LessonInfo(Base, ModelConvert):
    __tablename__ = 'lesson_info'

    infoId = Column(Integer, primary_key=True, autoincrement=True)
    lessonId = Column(Integer, ForeignKey('lessons.lessonId'))
    lessonName = Column(String(255))
    teacherId = Column(String(255))
    eventId = Column(String(255))
    teacherName = Column(String(255))
    lessonTask = Column(String(255))
    userId = Column(String(255))
    schoolName = Column(String(255))
