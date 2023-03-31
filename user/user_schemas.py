from pydantic import BaseModel


class CreateUser(BaseModel):
    userName: str
    password: str
    school: str
    avatar: str = None
    userType: int
    academy: str = None
    major: str = None
    classId: int = None
    className: str
    account: str


class QueryUser(BaseModel):
    userName: str
    userType: int
    password: str
    school: str
    classId: int


class UpdateUser(BaseModel):
    userId: int
    userName: str = None
    password: str = None
    school: str = None
    avatar: str = None
    academy: str = None
    major: str = None
    classId: int = None
    className: str = None
    account: str = None


class Login(BaseModel):
    account: str
    password: str


class ReadUser(BaseModel):
    userId: int
    userName: str
    school: str
    avatar: str
    userType: int
    academy: str
    major: str
    classId: int
    className: str
    account: str
