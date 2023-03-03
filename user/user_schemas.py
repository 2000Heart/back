from pydantic import BaseModel


class CreateUser(BaseModel):
    userName: str
    password: str
    school: str
    avatar: str
    userType: int
    classId: int


class QueryUser(BaseModel):
    userName: str
    userType: int
    password: int
    school: str


class ReadUser(BaseModel):
    userId: str
    userName: str
    school: str
    avatar: str
    userType: int
    classId: int
