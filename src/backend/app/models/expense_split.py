from pydantic import BaseModel

class ExpenseSplit(BaseModel):
    person_id: int
