# coding=utf-8
from pydantic import BaseModel


class CreateUser(BaseModel):
    userName: str
    password: str
    school: str
    avatar: str
    userType: int


class ReadUser(CreateUser):
    userId: int

    class Config:
        orm_mode = True


class QueryUser(BaseModel):
    userName: str
    userType: int
    password: int
    school: str


class CreateLesson(BaseModel):
    lessonName: str


class CreateSchedule(BaseModel):
    lessonId: int = None
    lessonName: str
    teacherId: int
    teacherName: str
    userId: str
    duration: str
    weekTime: int
    startUnit: int
    endUnit: int
    classroom: str


class QuerySchedule(BaseModel):
    userId: str


class CreateCheckIn(BaseModel):
    lessonId: int
    teacherId: int
    postTime: str
    checkedUser: str
    userAll: str


class CreateMajor(BaseModel):
    majorName: str


class CreateLessonInfo(BaseModel):
    lessonId: int
    teacherId: int
    teacherName: str
    lessonTask: str
    checkId: int


class ClassInfo(Base, ModelConvert):
    __tablename__ = 'class_info'

    classId = Column(Integer, primary_key=True, autoincrement=True)
    teacherId = Column(String(255))
    userId = Column(String(255))
