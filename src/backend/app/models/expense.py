from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

from app.models.expense_split import ExpenseSplit

class Expense(BaseModel):
    id: int
    amount: float
    date: datetime
    description: str
    paid_by_id: int
    splits: List[ExpenseSplit]

# Overloaded class for generation of new expenses. mustn't accept an id, since this is assigned within the backend. This
# is used for request bodies in POST /expense
class ExpenseRequest(Expense):
    id: None = Field(default=None, exclude=True)