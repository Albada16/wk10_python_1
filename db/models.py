from .database import Base
from sqlalchemy import Column, Integer, String


class DbArticle(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    description_long = Column(String)
    image = Column(String)

class DbUser(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    avatar = Column(String)
    email = Column(String)
class DbLike(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True, index=True)
    avatar = Column(String)
    username = Column(String)


