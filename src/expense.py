class Expense:
    __slots__ = ("label", "date", "amount", "category", "__dict__")

    def __init__(self, label: str, date: str, amount: float, category: str) -> None:
        self.label = label
        self.date = date
        self.amount = amount
        self.category = category

    def __str__(self) -> str:
        return f"\n label: {self.label} \n date: {self.date} \n amount: {self.amount}€ \n Category: {self.category}"

    def __setattr__(self, key, value):
        if key in self.__slots__:
            super().__setattr__(key, value)
        else:
            raise AttributeError(f"{key} is not a valid Expense attribute")


