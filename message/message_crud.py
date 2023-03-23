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
    if data.userType == 0:
        return db.query(Message).filter(
            and_(Message.userAll.like(f"%{data.userId}%"), Message.type not in [12])).order_by(
            Message.posterId.desc()).all()
    else:
        return db.query(Message).filter(and_(Message.posterId == data.userId, Message.type not in [10, 11])).all()
