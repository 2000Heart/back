import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from database import get_db
from user import user_crud, user_schemas

userAPI = APIRouter()


@userAPI.post("/create", response_model=user_schemas.ReadUser)
async def create_user(user: user_schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = user_crud.check_user_exist(db=db, data=user)
    if db_user:
        return JSONResponse(content={"msg": "用户已存在"}, status_code=300)
    return user_crud.create_user(db=db, user=user)


@userAPI.post("/login", response_model=user_schemas.ReadUser)
async def login(data: user_schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = user_crud.check_user_exist(db=db, data=data)
    if db_user is None:
        return JSONResponse(content={"d": {"msg": "用户不存在"}}, status_code=300)
    check = user_crud.query_user(db=db, username=data.userName, password=data.password)
    if check is None:
        return JSONResponse(content={"d": {"msg": "密码错误"}}, status_code=300)
    else:
        return {"d": check, "t": json.dumps(check.key_values())}
