from typing import List
from pydantic import BaseModel


class CreateSchedule(BaseModel):
    lessonId: int = None
    lessonName: str
    teacherId: str = None
    teacherName: str = ""
    userId: str
    duration: str
    weekTime: int
    startUnit: int
    endUnit: int
    classroom: str = None


class QuerySchedule(BaseModel):
    userId: int
    userType: int


class QueryScheduleList(BaseModel):
    userId: str
    userType: int
    weekTime: int
    startUnit: int


class UpdateSchedule(BaseModel):
    eventId: int
    lessonId: int = None
    lessonName: str = None
    teacherId: str = None
    teacherName: str = None
    userId: str = None
    duration: str = None
    weekTime: int = None
    startUnit: int = None
    endUnit: int = None
    classroom: str = None


class ReadSchedule(CreateSchedule):
    eventId: int


class CreateScheduleAll(BaseModel):
    d: List[CreateSchedule]


class CreateTable(BaseModel):
    userId: int
    currentWeek: int
    lessonNum: int
    totalWeek: int


class UpdateTable(BaseModel):
    tableId: int
    userId: int
    currentWeek: int
    lessonNum: int
    totalWeek: int


class QueryTable(BaseModel):
    userId: int


class ReadTable(CreateTable):
    tableId: int
