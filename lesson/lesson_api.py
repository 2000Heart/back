import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from lesson import lesson_schemas, lesson_crud

lessonAPI = APIRouter()


@lessonAPI.post("/check/create")
async def create_check(e: lesson_schemas.CreateCheck, db: Session = Depends(get_db)):
    db_data = lesson_crud.create_check(db, e)
    return {"d": db_data, "t": json.dumps(db_data.key_values())}


@lessonAPI.post("/create")
async def create_lesson(e: lesson_schemas.CreateLessonInfo, db: Session = Depends(get_db)):
    db_data = lesson_crud.create_lesson(db, e)
    return {"d": db_data, "t": json.dumps(db_data.key_values())}


@lessonAPI.post("/query")
async def query_lesson(e: lesson_schemas.QueryLessonInfo, db: Session = Depends(get_db)):
    db_data = lesson_crud.query_lesson(db, e.userId, e.userType)
    if db_data is None:
        raise HTTPException(status_code=404, detail="当前用户无课程")
    for item in db_data:
        item.duration = item.duration.split(sep=",")
    return {"d": db_data, "t": db_data}


@lessonAPI.post("/check/queryList")
async def query_check_list(e: lesson_schemas.QueryCheck, db: Session = Depends(get_db)):
    db_data = lesson_crud.query_check_list(db, e.userId)
    if db_data is None:
        raise HTTPException(status_code=404, detail="当前用户无签到记录")
    for item in db_data:
        item.duration = item.duration.split(sep=",")
    return {"d": db_data, "t": db_data}


@lessonAPI.post("/check/query")
async def query_check(e: lesson_schemas.QueryCheck, db: Session = Depends(get_db)):
    db_data = lesson_crud.query_check(db, e.lessonId)
    if db_data is None:
        raise HTTPException(status_code=404, detail="当前课程无签到")
    return {"d": db_data, "t": db_data.key_values()}
