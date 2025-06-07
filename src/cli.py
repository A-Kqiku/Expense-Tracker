from manager import *


manager = Manager()

menu: str = """
(1) Show expenses
(2) Add expense
(3) Edit expense
(4) Delete expense
(5) Exit
"""

def show_expenses() -> None:
    manager.list()

def add_expenses() -> None:
    label = input("What did you buy? ")
    date = input("Purchase date (DD-MM-YYYY): ")
    amount = float (input("Amount paid (€): "))
    category = input("Expense category (e.g., food, transport, etc.): ")

    manager.add(Expense(label, date, amount, category))



def is_finished(mode: str)-> bool:
        user_is_finished: str = input(f"Would you like to stop {mode}? (y/n): ").lower()

        match user_is_finished:
            case 'y':
                return True
            case 'n':
                return False
            case _:
                print("Invalid input.")
                return False


def edit_expenses() -> None:
    manager.list()
    index: int = int(input("Which expense do you want to edit?"))
    finished_editing = False

    while not finished_editing:
        manager.list()
        attr: str = input("What attribute do you want to edit?")
        value = input("What value do you want to assign?")
        manager.edit(index, attr, value)
        finished_editing = is_finished("editing")


def delete_expenses() -> None:
    finished_deleting = False
    while not finished_deleting:
        manager.list()

        index: int = int(input("Which expense do you want to delete?"))

        is_sure = input(f"You want to delete {manager.all_expenses[index]}").lower()
        if is_sure == 'y':
            manager.remove(index)
        else:
            continue

        finished_deleting = is_finished("deleting")

while True:
    user_input: int = int(input(menu))

    match user_input:
        case 1: show_expenses()
        case 2: add_expenses()
        case 3: edit_expenses()
        case 4: delete_expenses()
        case 5: break
        case _: print("Invalid input")

