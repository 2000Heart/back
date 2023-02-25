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
    db_user = crud.check_user_exist(db=db, name=user.userName, school=user.school)
    if db_user:
        return JSONResponse(content={"msg": "用户已存在"}, status_code=300)
    return crud.create_user(db=db, user=user)


@application.post("/login")
async def login(data: schemas.QueryUser, db: Session = Depends(get_db)):
    db_user = crud.check_user_exist(db=db, name=data.userName, school=data.school)
    if db_user <= 0:
        return JSONResponse(content={"d": {"msg": "用户不存在"}}, status_code=300)
    check = crud.check_user(db=db, username=data.userName, password=data.password)
    if check is None:
        return JSONResponse(content={"d": {"msg": "密码错误"}}, status_code=300)
    else:
        return {"d": check, "t": json.dumps(check.key_values())}
