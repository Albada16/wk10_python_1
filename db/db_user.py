from fastapi import HTTPException, status
from router.schemas import ArticleRequestSchema
from sqlalchemy.orm.session import Session
from db.models import DbUser
from .users_feed import users

def db_feed(db: Session):
    new_user_list = [DbUser(
        username=user["username"],
        avatar=user["avatar"],
        email=user["email"]
    ) for user in users]
    db.query(DbUser).delete()
    db.commit()
    db.add_all(new_user_list)
    db.commit()
    return db.query(DbUser).all()


def create(db: Session, request: UserRequestSchema):
    new_user = DbUser(
        username=request.username,
        avatar=request.avatar,
        email=request.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all(db: Session):
    return db.query(DbUser).all()

