# coding=utf-8
import json

from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import crud
import schemas
from database import SessionLocal

application = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@application.get("/")
async def root():
    return {"message": "Hello World"}


@application.post("/user")
async def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = crud.check_user_exist(db=db, data=user)
    if db_user:
        return JSONResponse(content={"msg": "用户已存在"}, status_code=300)
    return crud.create_user(db=db, user=user)


@application.post("/login")
async def login(data: schemas.QueryUser, db: Session = Depends(get_db)):
    db_user = crud.check_user_exist(db=db, data=data)
    if db_user is None:
        return JSONResponse(content={"d": {"msg": "用户不存在"}}, status_code=300)
    check = crud.query_user(db=db, username=data.userName, password=data.password)
    if check is None:
        return JSONResponse(content={"d": {"msg": "密码错误"}}, status_code=300)
    else:
        return {"d": check, "t": json.dumps(check.key_values())}


@application.post("/schedule")
async def insert_schedule(data: schemas.CreateUsersLesson, db: Session = Depends(get_db)):
    db_lesson = crud.create_user_s_lesson(db=db, e=data)
    db_teacher = crud.check_user_exist(db=db, data=schemas.QueryUser(userName=data.teacherName, userType=1,
                                                                     school=data.school))
    if db_lesson is None:
        db_lesson = crud.create_lesson(db=db, lesson=schemas.CreateLesson(lessonName=data.lessonName))
    insert = crud.create_user_s_lesson(
        db=db, e=schemas.CreateUsersLesson(
            userId=data.userId,
            userName=data.userName,
            lessonId=db_lesson.lessonId,
            lessonName=data.lessonName,
            teacherId=db_teacher.userId,
            teacherName=db_teacher.userName,
            startWeek=data.startWeek,
            endWeek=data.endWeek,
            classroom=data.classroom))
    return {"d": insert, "t": json.dumps(insert.key_values())}
