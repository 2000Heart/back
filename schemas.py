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
    password: str
    school: str


class CreateLesson(BaseModel):
    lessonName = str
    classroom = str
    startWeek = int
    endWeek = int


class InsertLesson(BaseModel):
    userId = int
    lessonName = str
    classroom = str
    startWeek = int
    endWeek = int
