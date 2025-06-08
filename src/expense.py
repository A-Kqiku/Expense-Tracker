from dataclasses import dataclass
from datetime import date as dt_date

@dataclass
class Expense:
    label: str
    date: dt_date
    amount: float
    category: str

    def __str__(self) -> str:
        return (f"\n label: {self.label} "
                f"\n date: {self.date.strftime('%d.%m.%Y')} "
                f"\n amount: {self.amount:.2f}€ "
                f"\n category: {self.category}")



