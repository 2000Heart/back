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
    unit: int
    classroom: str


class QuerySchedule(BaseModel):
    userId: str
