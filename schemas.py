# coding=utf-8
from pydantic import BaseModel


class CreateUser(BaseModel):
    userName: str
    password: str
    school: str
    avatar: str
    userType: int
    classId: int


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
    startTime: str
    endTime: str
    status: int


class CreateMajor(BaseModel):
    majorName: str


class CreateLessonInfo(BaseModel):
    lessonId: int
    teacherId: int
    teacherName: str
    lessonTask: str
    checkId: int
    lessonName: str
    eventId: int
    checkId: int
    userId: str


class CreateClass(BaseModel):
    teacherId: str
    userId: str


class CreateClassroom(BaseModel):
    schoolId: int
    roomName: str
    column: str
    row: str
