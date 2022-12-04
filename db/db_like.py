# from router.schemas import LikeRequestSchema
from sqlalchemy.orm.session import Session
from db.models import DbLike
from .likes_feed import likes

def db_feed(db: Session):
    new_like_list = [DbLike(
        article_id=like["article_id"],
        user_id = like["user_id"]
    ) for like in likes]
    db.query(DbLike).delete()
    db.commit()
    db.add_all(new_like_list)
    db.commit()
    return db.query(DbLike).all()


# def create(db: Session, request: LikeRequestSchema):
#     new_like = DbLike(
#         article_id=request.article_id,
#         user_id=request.user_id
#     )
#     db.add(new_like)
#     db.commit()
#     db.refresh(new_like)
#     return new_like
#
#
# def get_all(db: Session):
#     return db.query(DbLike).all()