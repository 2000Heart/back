from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from data.data_models import School, ClassInfo
from data import data_schemas, data_crud
from database import get_db
from utils import checkClass

dataAPI = APIRouter()


@dataAPI.post("/school/all")
async def query_school_all(db: Session = Depends(get_db)):
    school_all = db.query(School).all()
    return {"d": school_all, "t": school_all}


@dataAPI.post("/class/update")
async def update_class_member(data: data_schemas.UpdateClass, db: Session = Depends(get_db)):
    data = data_crud.update_class(db, data)
    return {"d": data, "t": data}


@dataAPI.post("/class/query")
async def query_class(data: data_schemas.QueryClass, db: Session = Depends(get_db)):
    db_data = db.query(ClassInfo).all()
    class_list = checkClass(db_data, data.className.split(","), data.schoolName)
    return {"d": class_list, "t": class_list}
