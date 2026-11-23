from pydantic import BaseModel

class Book(BaseModel):
    book_id: str
    title: str
    author: str | None = None
    publication_year: int | None = None
    documentation_url: str | None = None
    