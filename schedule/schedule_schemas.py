from pydantic import BaseModel


class CreateSchedule(BaseModel):
    lessonId: int = None
    lessonName: str
    teacherId: int
    teacherName: str
    userId: str
    duration: str
    weekTime: int
    startUnit: int
    endUnit: int
    classroom: str


class QuerySchedule(BaseModel):
    userId: int


class UpdateSchedule(BaseModel):
    eventId: int
    lessonId: int = None
    lessonName: str = None
    teacherId: int = None
    teacherName: str = None
    userId: str = None
    duration: str = None
    weekTime: int = None
    startUnit: int = None
    endUnit: int = None
    classroom: str = None


class ReadSchedule(CreateSchedule):
    eventId: int


class CreateTable(BaseModel):
    userId: int
    currentWeek: int
    lessonNum: int
    totalWeek: int


class UpdateTable(BaseModel):
    tableId: int
    userId: int
    currentWeek: int
    lessonNum: int
    totalWeek: int


class QueryTable(BaseModel):
    userId: int


class ReadTable(CreateTable):
    tableId: int
