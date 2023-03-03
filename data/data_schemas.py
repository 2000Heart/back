from pydantic import BaseModel


class CreateLesson(BaseModel):
    lessonName: str


class CreateMajor(BaseModel):
    majorName: str


class CreateClass(BaseModel):
    teacherId: str
    userId: str


class CreateClassroom(BaseModel):
    schoolId: int
    roomName: str
    column: str
    row: str


class CreateSchool(BaseModel):
    schoolName: str
