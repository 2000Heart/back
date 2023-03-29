import json
from fastapi import APIRouter, Depends
from sqlalchemy import and_
from sqlalchemy.orm import Session
from data import data_crud, data_schemas
from starlette.responses import JSONResponse
from database import get_db, errorResponse
from schedule import schedule_crud
from schemas import Block
from user import user_crud, user_schemas
from user.user_models import User

userAPI = APIRouter()


@userAPI.post("/create")
async def create_user(user: user_schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = user_crud.user_create_check(db=db, data=user)
    if db_user:
        return {"d": None, "t": "用户已存在"}
    else:
        db_class = data_schemas.QueryClass(className=user.className, schoolName=user.school)
        class_info = data_crud.query_class(db, db_class)
        if class_info is None:
            class_info = data_crud.create_class(db, data_schemas.CreateClass(
                className=user.className, schoolName=user.school))
        db_user = user
        db_user.classId = class_info.classId
        c_user = user_crud.create_user(db=db, user=user)
        schedule_crud.create_default_table(db, c_user.userId)
        data_crud.update_class(db, data_schemas.UpdateClass(
            classId=class_info.classId, userId=c_user.userId, schoolName=db_user.school))
    return {"d": c_user, "t": None}


@userAPI.post("/update")
async def update_user(user: user_schemas.UpdateUser, db: Session = Depends(get_db)):
    data = user
    if user.account is not None:
        check = db.query(User).filter(and_(User.userId != user.userId, User.account == user.account)).first()
        if check is not None:
            return {"d": None, "t": "账号已存在"}
    if user.className is not None and user.classId is None:
        db_class = data_schemas.QueryClass(className=user.className, schoolName=user.school)
        class_info = data_crud.query_class(db, db_class)
        if class_info is None:
            class_info = data_crud.create_class(db, data_schemas.CreateClass(
                className=user.className, schoolName=user.school))
        data.classId = class_info.classId
    db_data = user_crud.update_user(db, data)
    return {"d": db_data, "t": None}


@userAPI.post("/login")
async def login(data: user_schemas.Login, db: Session = Depends(get_db)):
    db_user = user_crud.user_account_check(db=db, data=data)
    if db_user is None:
        return {"d": None, "t": "用户不存在"}
    check = user_crud.query_user(db=db, username=data.userName, password=data.password)
    if check is None:
        return {"d": None, "t": "密码错误"}
    else:
        return {"d": check, "t": None}
