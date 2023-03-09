import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from data import data_crud, data_schemas
from starlette.responses import JSONResponse
from database import get_db
from schedule import schedule_crud
from user import user_crud, user_schemas

userAPI = APIRouter()


@userAPI.post("/create")
async def create_user(user: user_schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = user_crud.user_create_check(db=db, data=user)
    if db_user:
        return JSONResponse(content={"msg": "用户已存在"}, status_code=300)
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

    return {"d": c_user, "t": c_user.key_values()}


@userAPI.post("/login")
async def login(data: user_schemas.Login, db: Session = Depends(get_db)):
    db_user = user_crud.user_account_check(db=db, data=data)
    if db_user is None:
        return JSONResponse(content={"d": {"msg": "用户不存在"}}, status_code=300)
    check = user_crud.query_user(db=db, username=data.userName, password=data.password)
    if check is None:
        return JSONResponse(content={"d": {"msg": "密码错误"}}, status_code=300)
    else:
        return {"d": check, "t": check}
