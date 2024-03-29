# coding=utf-8
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from starlette.responses import JSONResponse

url = "mysql+pymysql://back444:as4793552@47.115.211.39:3306/back444"
engine = create_engine(url, echo=True)

# 在SQLAlchemy中，CRUD都是通过会话(session)进行的，所以我们必须要先创建会话，每一个SessionLocal实例就是一个数据库session
# flush()是指发送数据库语句到数据库，但数据库不一定执行写入磁盘；commit()是指提交事务，将变更保存到数据库文件
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=True)

# 创建基本映射类
Base = declarative_base(name='Base')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def body(value):
    return {
        "d": value,
        "t": json.dumps(value.key_values())
    }


def errorResponse(value):
    return JSONResponse(content={"d": {"msg": value}}, status_code=250)
