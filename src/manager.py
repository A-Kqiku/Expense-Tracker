from src.expense import Expense


class Manager:
    all_expenses: list
    amount_spent: float

    def __init__(self):
        self.all_expenses = []
        self.amount_spent = 0.0

    def add(self, expense: Expense):
        self.all_expenses.append(expense)
        self.amount_spent += expense.amount

    def remove(self, index: int):
        self.all_expenses[index].remove()
        self.amount_spent -= self.all_expenses[index].amount

    def edit(self, index: int, attr, value):
        expense = self.all_expenses[index]

        if not hasattr(expense, attr):
            raise AttributeError(f"{expense.__class__.__name__} has no attribute {attr!r}")

        setattr(expense, attr, value)

    def list(self):
        if not self.all_expenses:
            print("No expenses recorded.")
            return
        for expense in self.all_expenses:
            print(f"- {self.all_expenses.index(expense)} :  {expense}")

