import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from database import get_db
from schedule import schedule_schemas, schedule_models, schedule_crud
from data import data_schemas, data_crud

scheduleAPI = APIRouter()


@scheduleAPI.post("/create", response_model=schedule_schemas.ReadSchedule)
async def create_schedule(data: schedule_schemas.CreateSchedule, db: Session = Depends(get_db)):
    if data.lessonId is None:
        data.lessonId = data_crud.create_lesson(db, data_schemas.CreateLesson(lessonName=data.lessonName)).lessonId
    db_schedule: schedule_models.Schedule = schedule_crud.check_schedule(db, data)
    if db_schedule is None:
        db_create = schedule_crud.create_schedule(db, data)
        return {"d": db_create, "t": json.dumps(db_create.key_values())}
    else:
        db_data = data
        if db_schedule.userId is not None:
            e: list = db_schedule.userId.split(",")
            e.append(data.userId)
            db_data.userId = ",".join(e)
        db_insert = schedule_crud.update_schedule(db, db_schedule.eventId, db_data)
        return {"d": db_insert, "t": db_insert}


@scheduleAPI.post("/query", response_model=schedule_schemas.ReadSchedule)
async def query_schedule(userId: int, db: Session = Depends(get_db)):
    db_schedule: list = schedule_crud.query_schedule(db, userId)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="当前用户无课程表")
    for item in db_schedule:
        item.duration = item.duration.split(sep=",")
    return {"d": db_schedule, "t": db_schedule}
