from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_model_convert.sqlalchemy_model_convert import ModelConvert
from database import Base, engine


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