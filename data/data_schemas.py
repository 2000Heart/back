from typing import Any, List

from fastapi import UploadFile, Form
from pydantic import BaseModel

from user.user_models import User
from user.user_schemas import ReadUser


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
    teacherId: int = None


class UpdateClass(BaseModel):
    classId: int
    userId: int = 0
    schoolName: str


class QueryClassroom(BaseModel):
    roomName: str
    schoolName: str


class QueryClassroomList(BaseModel):
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


class ReadClassInfo(CreateClass):
    students: List[ReadUser] = []
