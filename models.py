from sqlalchemy import Column, String, Integer

from database import Base


class User(Base):
    __tablename__ = 'user'

    userId = Column(Integer, primary_key=True, autoincrement=True)
    userName = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    school = Column(String(255), nullable=False)
    avatar = Column(String(255), nullable=True)
    userType = Column(Integer, nullable=False)

    def __repr__(self):
        return f"{self.userId}-{self.userName}"
