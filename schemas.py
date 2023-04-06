from pydantic import BaseModel


class AuthorCreate(BaseModel):
    name: str
    age: int


class Author(AuthorCreate):
    id: int

    class Config:
        orm_mode = True


class Book(BaseModel):
    title: str
    rating: str
    author_id = Author

    class Config:
        orm_mode = True
