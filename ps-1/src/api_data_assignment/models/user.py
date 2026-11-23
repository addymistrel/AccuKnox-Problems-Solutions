from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    phone: str | None = None
    age: int | None = None
    city: str | None = None
    company: str | None = None
