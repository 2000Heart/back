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


# class CreateLesson(BaseModel):
#     lessonName = str
#     classroom = str
#     startWeek = int
#     endWeek = int


class InsertLesson(BaseModel):
    userId = int
    userType = int
    lessonName = str
    classroom = ""
    startWeek = int
    endWeek = int
    # 添加endweek大于startweek检测
    # teacherName = ""


class InsertUserToLesson(BaseModel):
    userId = int
    userType = int
    lessonId = int
