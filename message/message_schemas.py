from pydantic import BaseModel


class CreateMessage(BaseModel):
    posterId: int
    posterName: str
    userAll: str
    title: str
    content: str
    postTime: str
    type: int


class QueryMessage(BaseModel):
    userId: int
