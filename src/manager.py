from dataclasses import dataclass, field
from src.expense import Expense

@dataclass
class Manager:
    all_expenses: list[Expense]= field(default_factory=list)

    def is_empty(self) -> bool:
        if len(self.all_expenses) == 0:
            return True
        else:
            return False

    def add(self, expense: Expense):
        self.all_expenses.append(expense)

    def remove(self, index: int):
        self.all_expenses.pop(index)

    def edit(self, index: int, attr, value):
        expense = self.all_expenses[index]

        if not hasattr(expense, attr):
            raise AttributeError(f"{expense.__class__.__name__} has no attribute {attr!r}")
        if attr == "amount":
            setattr(expense, attr, value)
        else:
            setattr(expense, attr, value)

    def list(self) -> None:
        if not self.all_expenses:
            print("No expenses recorded.")
            return
        for expense in self.all_expenses:
            print(f"- {self.all_expenses.index(expense)} :  {expense}")

    def get_expenses(self) -> list:
        return self.all_expenses

    @property
    def amount_spent(self) -> float:
        return sum(exp.amount for exp in self.all_expenses)