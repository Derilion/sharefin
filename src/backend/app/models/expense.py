from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.models.expense_split import ExpenseSplit

class Expense(BaseModel):
    id: int
    amount: float
    date: datetime
    description: str
    paid_by_id: int
    splits: List[ExpenseSplit]