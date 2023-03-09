from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from data.data_models import School
from database import get_db

dataAPI = APIRouter()


@dataAPI.post("/school/all")
async def query_school_all(db: Session = Depends(get_db)):
    school_all = db.query(School).all()
    return {"d": school_all, "t": school_all}
