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
    school: str


class CreateLesson(BaseModel):
    lessonName: str


class CreateSchedule(BaseModel):
    lessonId: int
    lessonName: str
    teacherId: int = None
    teacherName = ""
    userId = ""
    duration: str
    weekTime: int
    unit: int
    classroom = ""


class QuerySchedule(BaseModel):
    userId: str
