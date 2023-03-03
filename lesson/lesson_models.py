from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_model_convert.sqlalchemy_model_convert import ModelConvert
from database import Base, engine


class CheckInLesson(Base, ModelConvert):
    __tablename__ = 'check_schedule'

    checkId = Column(Integer, primary_key=True, autoincrement=True)
    realLessonId = Column(Integer, ForeignKey('real_lesson.realLessonId'))
    teacherId = Column(Integer)
    postTime = Column(String(255), nullable=True)
    checkedUser = Column(String(255), nullable=True)
    userAll = Column(String(255), nullable=False)
    startTime = Column(String(255), nullable=False)
    endTime = Column(String(255), nullable=False)
    status = Column(Integer)

    Base.metadata.create_all(engine)


class LessonInfo(Base, ModelConvert):
    __tablename__ = 'lesson_info'

    infoId = Column(Integer, primary_key=True, autoincrement=True)
    lessonId = Column(Integer, ForeignKey('lessons.lessonId'))
    lessonName = Column(String(255))
    teacherId = Column(Integer),
    eventId = Column(Integer, ForeignKey('lesson_schedule.eventId'))
    teacherName = Column(String(255))
    lessonTask = Column(String(255))
    checkId = Column(Integer, ForeignKey('check_schedule'), nullable=True)
    userId = Column(String(255))
