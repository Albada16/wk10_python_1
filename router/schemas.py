from pydantic import BaseModel


class ArticleRequestSchema(BaseModel):
    title: str
    author: str
    description: str
    description_long: str
    image: str


class ArticleResponseSchema(ArticleRequestSchema):
    id: int

    class Config:
        orm_mode = True