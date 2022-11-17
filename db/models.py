from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class DbArticle(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String(30))
    description = Column(String(100))
    description_long = Column(String)
    image = Column(String)



