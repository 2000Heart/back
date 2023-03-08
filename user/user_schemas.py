from pydantic import BaseModel


class CreateUser(BaseModel):
    userName: str
    password: str
    school: str
    avatar: str
    userType: int
    classId: int
    className: str


class QueryUser(BaseModel):
    userName: str
    userType: int
    password: int
    school: str
    classId: int


class ReadUser(BaseModel):
    userId: str
    userName: str
    school: str
    avatar: str
    userType: int
    classId: int
    className: str
