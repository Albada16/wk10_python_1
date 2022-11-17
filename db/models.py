from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class DbArticle(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String(30), nullable=False)
    description = Column(String(100), nullable=False)
    description_long = Column(String, nullable=True)
    image = Column(String, nullable=False)



