from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class DbArticle(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    description_long = Column(String)
    image = Column(String)
    article_like = relationship('DbLike', back_populates ='like_article')
    article_comm = relationship('DbComm', back_populates ='comm_article')

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    avatar = Column(String)
    email = Column(String)
    press_like = relationship('DbLike', back_populates='like_user')
    write_comm = relationship('DbComm', back_populates='comm_user')

class DbLike(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey('article.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    like_article = relationship('DbArticle', back_populates='article_like')
    like_user = relationship('DbUser', back_populates='press_like')

class DbComm(Base):
    __tablename__ = 'comm'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    article_id = Column(Integer, ForeignKey('article.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    comm_article = relationship('DbArticle', back_populates='article_comm')
    comm_user = relationship('DbUser', back_populates='write_comm')