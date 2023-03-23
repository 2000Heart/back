from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from message import message_schemas, message_crud

messageAPI = APIRouter()


@messageAPI.post("/create")
async def create_check(e: message_schemas.CreateMessage, db: Session = Depends(get_db)):
    db_data = message_crud.create_message(db, e)
    return {"d": db_data, "t": db_data}


@messageAPI.post("/query")
async def query_message(e: message_schemas.QueryMessage, db: Session = Depends(get_db)):
    db_data = message_crud.query_message(db, e)
    if db_data is None:
        return {"d": db_data, "t": "当前用户无消息"}
    return {"d": db_data, "t": None}
