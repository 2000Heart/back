from fastapi import APIRouter
from sqlalchemy.orm import Session

from data.data_models import School

dataAPI = APIRouter()


@dataAPI.post("/school/all")
async def query_school_all(db: Session):
    school_all = db.query(School).all()
    return {"d": school_all, "t": school_all}
