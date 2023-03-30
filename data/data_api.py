import os.path
import shutil

from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy import and_
from sqlalchemy.orm import Session
from starlette.responses import FileResponse

from data.data_models import School, ClassInfo, Classroom
from data import data_schemas, data_crud
from database import get_db
from user import user_crud, user_schemas
from utils import checkClass

dataAPI = APIRouter()


@dataAPI.post("/school/all")
async def query_school_all(db: Session = Depends(get_db)):
    school_all = db.query(School).all()
    return {"d": school_all, "t": None}


@dataAPI.post("/class/update")
async def update_class_member(data: data_schemas.UpdateClass, db: Session = Depends(get_db)):
    data = data_crud.update_class(db, data)
    return {"d": data, "t": None}


@dataAPI.post("/class/query")
async def query_class(data: data_schemas.QueryClass, db: Session = Depends(get_db)):
    db_data = db.query(ClassInfo).all()
    class_list = checkClass(db_data, data.className.split(","), data.schoolName)
    return {"d": class_list, "t": None}


@dataAPI.post("/class/query/list")
async def query_class_list(data: data_schemas.QueryClassList, db: Session = Depends(get_db)):
    class_list = data_crud.query_class_list(db, data)
    return {"d": class_list, "t": None}


@dataAPI.post("/class/query/school/list")
async def query_class_list(data: data_schemas.QueryClassList, db: Session = Depends(get_db)):
    class_list = data_crud.query_class_list(db, data)
    return {"d": class_list, "t": None}


@dataAPI.post("/classroom/list")
async def query_classroom_list(data: data_schemas.QueryClassroomList, db: Session = Depends(get_db)):
    db_data = db.query(Classroom).filter_by(schoolName=data.schoolName).all()
    return {"d": db_data, "t": None}


@dataAPI.post("/classroom/create")
async def create_classroom(data: data_schemas.CreateClassroom, db: Session = Depends(get_db)):
    db_data = data_crud.create_classroom(db, data)
    return {"d": db_data, "t": None}


@dataAPI.post("/classroom/query")
async def query_classroom(data: data_schemas.QueryClassroom, db: Session = Depends(get_db)):
    db_data = data_crud.query_classroom(db, data)
    return {"d": db_data, "t": None}


@dataAPI.post("/avatar/upload")
async def create_upload_file(userId: int = Form(...), file: UploadFile = Form(...), db: Session = Depends(get_db)):
    content = await file.read()
    with open("test/" + file.filename, "wb") as f:
        f.write(content)
    url = "http://192.168.1.104:8888/avatar/" + file.filename
    db_data = user_crud.update_user(db, user_schemas.UpdateUser(userId=userId, avatar=url))
    return {"d": db_data, "t": None}
