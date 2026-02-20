from pydantic import BaseModel

class ExpenseSplit(BaseModel):
    _person_id: int
