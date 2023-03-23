from sqlalchemy import and_
from sqlalchemy.orm import Session

from message import message_schemas
from message.message_model import Message


def create_message(db: Session, data: message_schemas.CreateMessage):
    db_data = Message(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


def query_message(db: Session, data: message_schemas.QueryMessage):
        return db.query(Message).filter(
            Message.userAll.like(f"%{data.userId}%")).order_by(Message.posterId.desc()).all()
