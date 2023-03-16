import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from database import get_db
from schedule import schedule_schemas, schedule_models, schedule_crud
from data import data_schemas, data_crud

scheduleAPI = APIRouter()


@scheduleAPI.post("/create")
async def create_schedule(data: schedule_schemas.CreateSchedule, db: Session = Depends(get_db)):
    if data.lessonId is None:
        db_lesson = data_crud.query_lesson(db, data.lessonName)
        if db_lesson.lessonId is None:
            data.lessonId = data_crud.create_lesson(db, data_schemas.CreateLesson(lessonName=data.lessonName))
        data.lessonId = db_lesson.lessonId
    db_schedule: schedule_models.Schedule = schedule_crud.check_schedule(db, data)
    if db_schedule is None:
        db_create = schedule_crud.create_schedule(db, data)
        return {"d": db_create, "t": db_create}
    else:
        db_data = db_schedule
        if db_schedule.userId is not None:
            e: list = db_schedule.userId.split(",")
            e.append(data.userId)
            db_data.userId = ",".join(e)
        db_update = schedule_crud.update_schedule(db, schedule_schemas.UpdateSchedule(userId=db_data.userId))
        return {"d": db_update, "t": db_update}


@scheduleAPI.post("/create/all")
async def create_schedule_all(data: schedule_schemas.CreateScheduleAll, db: Session = Depends(get_db)):
    schedule_crud.create_schedule_all(db, data)


@scheduleAPI.post("/update")
async def update_schedule(data: schedule_schemas.UpdateSchedule, db: Session = Depends(get_db)):
    db_data = schedule_crud.update_schedule(db, data)
    return {"d": db_data, "t": db_data}


@scheduleAPI.post("/query")
async def query_schedule(data: schedule_schemas.QuerySchedule, db: Session = Depends(get_db)):
    db_schedule: list = schedule_crud.query_schedule(db, data.userId)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="当前用户无课程表")
    return {"d": db_schedule, "t": db_schedule}


@scheduleAPI.post("/query/list")
async def query_schedule_list(data: schedule_schemas.QueryScheduleList, db: Session = Depends(get_db)):
    db_schedule: list = schedule_crud.query_schedule_list(db, data)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="暂无数据")
    return {"d": db_schedule, "t": db_schedule}


@scheduleAPI.post("/table/query")
async def query_table(data: schedule_schemas.QueryTable, db: Session = Depends(get_db)):
    db_schedule: list = schedule_crud.query_table(db, data.userId)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="当前用户无设置")
    return {"d": db_schedule, "t": db_schedule}


@scheduleAPI.post("/table/update")
async def update_table(data: schedule_schemas.UpdateTable, db: Session = Depends(get_db)):
    db_data = schedule_crud.update_table(db, data)
    if db_data <= 0:
        raise HTTPException(status_code=404, detail="课表获取错误")
    return {"d": db_data, "t": db_data}
