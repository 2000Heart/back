from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_model_convert.sqlalchemy_model_convert import ModelConvert
from database import Base, engine


class Lessons(Base, ModelConvert):
    __tablename__ = 'lessons'

    lessonId = Column(Integer, primary_key=True, autoincrement=True)
    lessonName = Column(String(255), unique=True)

    Base.metadata.create_all(engine)


class Majors(Base, ModelConvert):
    __tablename__ = 'majors'

    majorId = Column(Integer, primary_key=True, autoincrement=True)
    majorName = Column(String(255), unique=True)

    Base.metadata.create_all(engine)


class ClassInfo(Base, ModelConvert):
    __tablename__ = 'class_info'

    classId = Column(Integer, primary_key=True, autoincrement=True)
    className = Column(String(255))
    teacherId = Column(String(255))
    userId = Column(String(255))
    schoolName = Column(String(255))


class Classroom(Base, ModelConvert):
    __tablename__ = 'classroom'

    roomId = Column(Integer, primary_key=True, autoincrement=True)
    schoolName = Column(Integer)
    roomName = Column(String(255))
    column = Column(String(255))
    row = Column(String(255))


class School(Base, ModelConvert):
    __tablename__ = 'school'

    schoolId = Column(Integer, primary_key=True, autoincrement=True)
    schoolName = Column(String(255))
