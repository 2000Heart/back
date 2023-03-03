# coding=utf-8
import json

from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import crud
import models
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
async def login(data: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = crud.check_user_exist(db=db, data=data)
    if db_user is None:
        return JSONResponse(content={"d": {"msg": "用户不存在"}}, status_code=300)
    check = crud.query_user(db=db, username=data.userName, password=data.password)
    if check is None:
        return JSONResponse(content={"d": {"msg": "密码错误"}}, status_code=300)
    else:
        return {"d": check, "t": json.dumps(check.key_values())}


@application.post("/schedule/create")
async def create_schedule(data: schemas.CreateSchedule, db: Session = Depends(get_db)):
    if data.lessonId is None:
        data.lessonId = crud.create_lesson(db, schemas.CreateLesson(lessonName=data.lessonName)).lessonId
    db_schedule: models.Schedule = crud.check_schedule(db, data)
    if db_schedule is None:
        db_create = crud.create_schedule(db, data)
        return {"d": db_create, "t": json.dumps(db_create.key_values())}
    else:
        db_data = data
        if db_schedule.userId is not None:
            e: list = db_schedule.userId.split(",")
            e.append(data.userId)
            db_data.userId = ",".join(e)
        db_insert = crud.update_schedule(db, db_schedule.eventId, db_data)
        return {"d": db_insert, "t": db_insert}


@application.post("/schedule/query")
async def query_schedule(userId: int, db: Session = Depends(get_db)):
    db_schedule: list = crud.query_schedule(db, userId)
    if db_schedule is None:
        return JSONResponse(content={"d": {"msg": "当前用户无课程"}}, status_code=300)
    for item in db_schedule:
        item.duration = item.duration.split(sep=",")
    return {"d": db_schedule, "t": db_schedule}


@application.post("/check/create")
async def create_check(e: schemas.CreateCheckIn, db: Session = Depends(get_db)):
    return e
