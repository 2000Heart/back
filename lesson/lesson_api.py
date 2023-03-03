from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from lesson import lesson_schemas

lessonAPI = APIRouter()


@lessonAPI.post("/check/create", response_model=lesson_schemas.ReadCheck)
async def create_check(e: lesson_schemas.CreateCheck, db: Session = Depends(get_db)):
    return e


@lessonAPI.post("/create", response_model=lesson_schemas.ReadLessonInfo)
async def create_check(e: lesson_schemas.CreateLessonInfo, db: Session = Depends(get_db)):
    return e
