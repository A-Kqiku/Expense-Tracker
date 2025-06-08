
from manager import *
from datetime import datetime, date as dt_date
import json

def main() -> None:
    manager = Manager()

    menu: str = """
    (1) Show expenses
    (2) Add expense
    (3) Edit expense
    (4) Delete expense
    (5) Exit
    """
    while True:
        user_input: int = ask_int(menu, min_=1, max_=5)
        match user_input:
            case 1:
                show_expenses(manager)
            case 2:
                add_expenses(manager)
            case 3:
                edit_expenses(manager)
            case 4:
                delete_expenses(manager)
            case 5:
                break


# Manager Helper Functions

def show_expenses(manager: Manager) -> None:
    manager.list()

def add_expenses(manager: Manager) -> None:
    label = ask_str("What did you buy? ")
    date = ask_date("Purchase date (DD.MM.YYYY): ")
    amount = ask_float("Amount paid (€): ")
    category = ask_str("Expense category (e.g., food, transport, etc.): ")

    manager.add(Expense(label, date, amount, category))



def is_finished(mode: str)-> bool:
        user_is_finished: str = ask_str(f"Would you like to stop {mode}? (y for yes / n for no): ", choices=["y", "n"])

        match user_is_finished:
            case 'y':
                return True
            case 'n':
                return False
            case _:
                print("Invalid input.")
                return False


def edit_expenses(manager: Manager) -> None:
    if not manager.is_empty():
        manager.list()
        index: int = ask_int("Which expense do you want to edit? (index)",min_= 0, max_=len(manager.get_expenses())-1)
        finished_editing = False

        while not finished_editing:
            manager.list()
            attr: str = ask_str("What attribute do you want to edit?",choices=["label", "date", "amount", "category"])
            value= None
            match attr:
                case "label": value = ask_str("What value do you want to assign?")
                case "date":  value = ask_date("Purchase date (DD.MM.YYYY): ")
                case "amount": value = ask_float("Amount paid (€): ")
                case "category": value = ask_str("Expense category (e.g., food, transport, etc.): ")
            manager.edit(index, attr, value)
            finished_editing = is_finished("editing")
    else:
        print("There is nothing to edit.")


def delete_expenses(manager: Manager) -> None:
    if not manager.is_empty():
        finished_deleting = False
        while not finished_deleting:
            manager.list()

            index: int = ask_int("Which expense do you want to delete? (index)", min_=0,max_=len(manager.get_expenses()) - 1)

            is_sure = ask_str(f"You want to delete {manager.all_expenses[index]}? (y for yes/ n for no)", choices=["y","n"])
            if is_sure == 'y':
                manager.remove(index)
            else:
                finished_deleting = is_finished("deleting")
                continue

            if not manager.is_empty():
                finished_deleting = is_finished("deleting")
            else:
                finished_deleting = True
    else:
        print("There is nothing to delete.")


# Error Handling Helper
def ask_int(prompt: str, *, min_= None, max_= None) -> int:
    while True:
        try:
            value: int = int(input(prompt))
            if min_ is not None and value < min_:
                raise ValueError(f"Value must be >= {min_}")
            if max_ is not None and value > max_:
                raise ValueError(f"Value must be <= {max_}")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

def ask_str(prompt: str,*, choices: []= None, required: bool= True)-> str:
    while True:
        str_value: str = input(prompt).strip().lower()

        if not str_value and not required:
            return str_value
        if not str_value and required:
            print("Input is required.")
            continue
        if choices:
            if str_value not in [c.lower() for c in choices]:
                print(f"Please enter one of :{', '.join(choices)}")
                continue

        return str_value

def ask_float(prompt: str, *, min_= None, max_= None) -> float:
    while True:
        try:
            value: float = float(input(prompt))
            if min_ is not None and value < min_:
                raise ValueError(f"Value must be >= {min_}")
            if max_ is not None and value > max_:
                raise ValueError(f"Value must be <= {max_}")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

def ask_date(prompt: str, *, pattern= "%d.%m.%Y") -> dt_date:
    while True:
        try:
            value = input(prompt).strip()
            date= datetime.strptime(value, pattern).date()
            return date
        except ValueError as e:
            print(f"Invalid input: {e}. PLease use format: {pattern}")





if __name__ == "__main__":
    main()
