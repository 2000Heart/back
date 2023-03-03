from pydantic import BaseModel


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


class QueryLessonInfo(BaseModel):
    userId: int
    infoId: int
    teacherId: int


class ReadLessonInfo(CreateLessonInfo):
    infoId: int


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
    userId: int
    lessonId: int


class ReadCheck(CreateCheck):
    checkId: int
