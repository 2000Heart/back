from typing import Any

from pydantic import BaseModel


class CreateLesson(BaseModel):
    lessonName: str


class CreateMajor(BaseModel):
    majorName: str


class CreateClass(BaseModel):
    teacherId: str
    userId: str
    className: str
    schoolName: str


class QueryClass(BaseModel):
    className: str
    schoolName: str


class QueryClassList(BaseModel):
    schoolName: str


class UpdateClass(BaseModel):
    classId: int
    teacherId: int = 0
    userId: int = 0
    schoolName: str


class CreateClassroom(BaseModel):
    schoolName: str
    roomName: str
    column: str
    row: str


class CreateSchool(BaseModel):
    schoolName: str


class Return(BaseModel):
    d: dict
    t: dict

