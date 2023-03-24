import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, errorResponse
from lesson import lesson_schemas, lesson_crud
from schedule import schedule_crud

lessonAPI = APIRouter()


@lessonAPI.post("/check/create")
async def create_check(e: lesson_schemas.CreateCheck, db: Session = Depends(get_db)):
    db_data = lesson_crud.create_check(db, e)
    return {"d": db_data, "t": db_data}


@lessonAPI.post("/check/stu/create")
async def create_check_stu(e: lesson_schemas.CreateCheckStu, db: Session = Depends(get_db)):
    db_data = lesson_crud.create_check_stu(db, e)
    return {"d": db_data, "t": db_data}


@lessonAPI.post("/create")
async def create_lesson(e: lesson_schemas.CreateLessonInfo, db: Session = Depends(get_db)):
    db_data = lesson_crud.create_lesson(db, e)
    return {"d": db_data, "t": db_data}


@lessonAPI.post("/create/all")
async def create_lesson_all(data: lesson_schemas.CreateLessonAll, db: Session = Depends(get_db)):
    lesson_crud.create_lesson_all(db, data)


@lessonAPI.post("/task/create")
async def create_task(e: lesson_schemas.AddLessonTask, db: Session = Depends(get_db)):
    db_data = lesson_crud.update_task(db, e)
    return {"d": db_data, "t": db_data}


@lessonAPI.post("/query")
async def query_lesson(e: lesson_schemas.QueryLessons, db: Session = Depends(get_db)):
    db_data = lesson_crud.query_lesson(db, e)
    if db_data is None:
        return {"d": db_data, "t": "当前用户无课程"}
    return {"d": db_data, "t": None}


@lessonAPI.post("/query/schedule")
async def query_lesson_schedule(e: lesson_schemas.QueryLessons, db: Session = Depends(get_db)):
    db_data = lesson_crud.query_lesson(db, e)
    if db_data is None:
        return {"d": db_data, "t": "未查询到课程"}
    db_data = schedule_crud.query_schedule_all(db, [int(x) for x in db_data.eventId.split(',')])
    return {"d": db_data, "t": None}


@lessonAPI.post("/check/queryList")
async def query_check_list(e: lesson_schemas.QueryCheck, db: Session = Depends(get_db)):
    db_data = lesson_crud.query_check_stu(db, e.userId)
    if db_data is None:
        return {"d": db_data, "t": "当前用户无签到记录"}
    return {"d": db_data, "t": None}


@lessonAPI.post("/check/stu/query")
async def query_check_stu(e: lesson_schemas.QueryCheckStu, db: Session = Depends(get_db)):
    db_data = lesson_crud.query_check_stu(db, e.checkId)
    if db_data is None:
        return {"d": db_data, "t": "无签到人员"}
    return {"d": db_data, "t": None}


@lessonAPI.post("/check/query")
async def query_check(e: lesson_schemas.QueryCheck, db: Session = Depends(get_db)):
    db_data = lesson_crud.query_check(db, e.infoId)
    if db_data is None:
        return {"d": db_data, "t": "当前课程无签到"}
    return {"d": db_data, "t": None}


@lessonAPI.post("/check/update")
async def update_check(e: lesson_schemas.UpdateCheck, db: Session = Depends(get_db)):
    db_data = lesson_crud.update_check(db, e)
    return {"d": db_data, "t": db_data}


@lessonAPI.post("/check/stu/update")
async def update_check_stu(e: lesson_schemas.UpdateCheckStu, db: Session = Depends(get_db)):
    db_data = lesson_crud.update_check_stu(db, e)
    return {"d": db_data, "t": db_data}


@lessonAPI.post("/check/stu/delete")
async def delete_check_stu(e: lesson_schemas.DeleteCheckStu, db: Session = Depends(get_db)):
    db_data = lesson_crud.delete_check_stu(db, e)
    return {"d": db_data, "t": db_data}


@lessonAPI.post("/check/history")
async def query_check_history(e: lesson_schemas.QueryCheckHistory, db: Session = Depends(get_db)):
    db_data = lesson_crud.query_check_history(db, e)
    return {"d": db_data, "t": db_data}
