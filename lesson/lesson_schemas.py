from pydantic import BaseModel


class CreateLessonInfo(BaseModel):
    lessonId: int
    lessonName: str
    teacherId: int
    teacherName: str
    lessonTask: str
    checkId: int
    eventId: int
    checkId: int
    userId: str


class QueryLessonInfo(BaseModel):
    userId: int
    infoId: int
    userType: int


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
    lessonId: int
    teacherId: int
    postTime: str
    checkedUser: str
    userAll: str
    startTime: str
    endTime: str
    status: int


class QueryCheck(BaseModel):
    lessonId: int
    userId: int


class ReadCheck(CreateCheck):
    checkId: int
