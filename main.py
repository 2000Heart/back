from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
import crud
import schemas
from database import SessionLocal

application = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@application.get("/")
async def root():
    return {"message": "Hello World"}


@application.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@application.post("/user")
async def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = crud.check_user_exist(db=db, name=user.userName, school=user.school)
    if db_user:
        return "用户已存在"
    return crud.create_user(db=db, user=user)


@application.post("/login")
async def login(username: str, password: str, school: str, db: Session = Depends(get_db)):
    db_user = crud.check_user_exist(db=db, name=username, school=school)
    if not db_user:
        return "用户不存在"
    return crud.check_user(db=db, username=username, password=password)
