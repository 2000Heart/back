from sqlalchemy import Column, Integer, String
from sqlalchemy_model_convert.sqlalchemy_model_convert import ModelConvert

from database import Base


class Message(Base, ModelConvert):
    __tablename__ = 'message'

    messageId = Column(Integer, primary_key=True, autoincrement=True)
    posterId = Column(Integer)
    posterName = Column(String(255))
    userAll = Column(String(255))
    title = Column(String(255))
    content = Column(String(255))
    postTime = Column(String(255))
    type = Column(String(255))
