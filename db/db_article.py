from fastapi import HTTPException, status
from router.schemas import ArticleRequestSchema
from sqlalchemy.orm.session import Session
from db.models import DbArticle
from .articles_feed import article

def db_feed(db: Session):
    new_article_list = [DbArticle(
        title=articles["title"],
        author=articles["author"],
        description=articles["description"],
        description_long=articles["description_long"],
        image=articles["image"]
    ) for articles in article]
    db.query(DbArticle).delete()
    db.commit()
    db.add_all(new_article_list)
    db.commit()
    return db.query(DbArticle).all()


def create(db: Session, request: ArticleRequestSchema):
    new_article = DbArticle(
        title=request.title,
        author=request.author,
        description=request.description,
        description_long=request.description_long,
        image=request.image
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_all(db: Session):
    return db.query(DbArticle).all()


def get_article_by_id(article_id: int, db: Session):
    articles = db.query(DbArticle).filter(DbArticle.id == article_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with id = {id} not found')
    return article


def get_article_by_category(title: str, db: Session):
    article = db.query(DbArticle).filter(DbArticle.title == title ).all()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with title = {id} not found')
    return article
