from pydantic import BaseModel

class Person(BaseModel):
    id: int
    first_name: str
    last_name: str