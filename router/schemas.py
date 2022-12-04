from pydantic import BaseModel
from typing import List


class UserRequestSchema(BaseModel):
    username: str
    avatar: str
    email: str

class UserResponseSchema(UserRequestSchema):
    id: int

    class Config:
        orm_mode = True

class CommResponseSchema(BaseModel):
    id: int
    comm_user: UserResponseSchema
    content: str
    class Config:
        orm_mode = True
class LikeResponseSchema(BaseModel):
    id: int
    like_user: UserResponseSchema

    class Config:
        orm_mode = True

class ArticleRequestSchema(BaseModel):
    title: str
    author: str
    description: str
    description_long: str
    image: str
    article_like: List[LikeResponseSchema]
    article_comm: List[CommResponseSchema]

class ArticleResponseSchema(ArticleRequestSchema):
    id: int

    class Config:
        orm_mode = True