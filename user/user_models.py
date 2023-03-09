from sqlalchemy import Column, Integer, String
from sqlalchemy_model_convert.sqlalchemy_model_convert import ModelConvert
from database import Base, engine


class User(Base, ModelConvert):
    __tablename__ = 'user'

    userId = Column(Integer, primary_key=True, autoincrement=True)
    userName = Column(String(255), nullable=False)
    password = Column(String(255), nullable=True)
    school = Column(String(255), nullable=False)
    avatar = Column(String(255), nullable=True)
    userType = Column(Integer, nullable=False)
    academy = Column(String(255))
    major = Column(String(255))
    classId = Column(Integer, nullable=True)
    className = Column(String(255), nullable=True)
    account = Column(String(255))

    def __repr__(self):
        return f"{self.userId}-{self.userName}"

    Base.metadata.create_all(engine)
