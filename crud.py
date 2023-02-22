from sqlalchemy.orm import Session

import models
import schemas


def create_user(db: Session, user: schemas.CreateUser):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_city_exist(db: Session, name: str, school: str):
    return db.query(models.User).filter(models.User.userName == name, models.User.school == school).first()
