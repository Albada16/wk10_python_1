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



