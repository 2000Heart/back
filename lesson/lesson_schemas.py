import datetime
from typing import List
from xmlrpc.client import DateTime
from schedule import schedule_schemas

from pydantic import BaseModel


class CreateLessonInfo(BaseModel):
    lessonId: int
    lessonName: str
    eventId: str
    schoolName: str


class CreateLesson(BaseModel):
    lesson: CreateLessonInfo
    schedule: List[schedule_schemas.CreateSchedule]


class CreateLessonAll(BaseModel):
    d: List[CreateLessonInfo]


class QueryLessons(BaseModel):
    userId: int = None
    infoId: int = None
    userType: int = None


class QueryLessonInfo(BaseModel):
    lessonName: str
    schoolName: str


class ReadLessonInfo(CreateLessonInfo):
    infoId: int


class AddLessonTask(BaseModel):
    infoId: int
    lessonTask: str


class AddLessonCheck(BaseModel):
    infoId: int
    checkId: int


class AddUser(BaseModel):
    infoId: int
    userId: str


class CreateCheck(BaseModel):
    infoId: int
    lessonName: str
    teacherId: int
    teacherName: str
    postTime: str
    userAll: str
    startTime: str
    endTime: str
    column: str
    row: str


class CreateCheckStu(BaseModel):
    checkId: int
    userId: int
    userName: str
    index: int


class QueryCheck(BaseModel):
    infoId: int
    userId: int


class QueryCheckStu(BaseModel):
    checkId: int


class QueryCheckHistory(BaseModel):
    userId: int
    userType: int


class UpdateCheck(BaseModel):
    checkId: int
    userId: str


class UpdateCheckStu(BaseModel):
    id: int
    index: int


class DeleteCheckStu(BaseModel):
    id: int


class ReadCheck(CreateCheck):
    checkId: int


class ReadHistory(CreateCheck):
    checkId: int
    checked: int = None
    checkNum: int = None
    need: int = None
    miss: str = None
