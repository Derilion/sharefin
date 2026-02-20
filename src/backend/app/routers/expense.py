from fastapi import APIRouter, HTTPException
from app.models.expense import Expense as ExpenseModel, ExpenseRequest
from app.models.expense_split import ExpenseSplit as ExpenseSplitModel
from datetime import datetime

router = APIRouter(prefix="/expense", tags=["expense"])

# Temporary test data – will be replaced with DB interactions
_expenses: list[ExpenseModel] = [
    ExpenseModel(
        id=1,
        amount=42.50,
        date=datetime(2025, 1, 15, 12, 0, 0),
        description="Grocery shopping",
        paid_by_id=1,
        splits=[ExpenseSplitModel(person_id=1), ExpenseSplitModel(person_id=2)],
    ),
    ExpenseModel(
        id=2,
        amount=18.00,
        date=datetime(2025, 1, 16, 19, 30, 0),
        description="Pizza night",
        paid_by_id=2,
        splits=[ExpenseSplitModel(person_id=1), ExpenseSplitModel(person_id=2), ExpenseSplitModel(person_id=3)],
    ),
]


@router.get("/", response_model=list[ExpenseModel])
def get_all_expenses():
    return _expenses


@router.get("/{expense_id}", response_model=ExpenseModel)
def get_expense_by_id(expense_id: int):
    expense = next((e for e in _expenses if e.id == expense_id), None)
    if expense is None:
        raise HTTPException(status_code=404, detail=f"Expense with id {expense_id} not found")
    return expense

@router.post("/", response_model=ExpenseModel, status_code=201)
def create_expense(expense: ExpenseRequest):
    new_id = max((e.id for e in _expenses if e.id is not None), default=0) + 1
    new_expense = ExpenseModel(id=new_id, **expense.model_dump(exclude={"id"}))
    _expenses.append(new_expense)
    return new_expense