class Expense:
    __slots__ = ("label", "date", "amount", "category")

    def __init__(self, label: str, date: str, amount: float, category: str) -> None:
        self.label = label
        self.date = date
        self.amount = amount
        self.category = category

    def __str__(self) -> str:
        return f"\n label: {self.label} \n date: {self.date} \n amount: {self.amount:.2f}€ \n Category: {self.category}"



