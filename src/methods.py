from expense import Expense

def show_expenses(expenses: dict) -> None:
    for key, value in expenses.items():
        print(f"{key}: {expenses[key]}")


def add_expenses(expenses: dict, amount_of_expenses: int) -> int:
    label = input("What did you buy? ")
    date = input("Purchase date (DD-MM-YYYY): ")
    amount = float(input("Amount paid (€): "))
    category = input("Expense category (e.g., food, transport, etc.): ")

    expenses[amount_of_expenses] = Expense(label, date, amount, category)
    return amount_of_expenses + 1


def isFinished(mode: str)-> bool:
        user_is_finished: str = input(f"Would you like to continue {mode}? (y/n): ")

        match user_is_finished:
            case 'y':
                return False
            case 'n':
                return True
            case _:
                print("Invalid input.")
                return False


def edit_expenses(expenses: dict) -> None:
    index: int = int(input("Which expense do you want to edit?"))
    finished_editing = False

    while not finished_editing:
        print(expenses[index])
        attr: str = input("What attribute do you want to edit?")
        value = input("What value do you want to assign?")
        expenses[index].__setattr__(attr, value)

        finished_editing = isFinished("editing")


def delete_expenses(expenses: dict) -> None:
    finished_deleting = False
    while not finished_deleting:
        for key, value in expenses.items():
            print(f"{key}: {expenses[key]}")

        index: int = int(input("Which expense do you want to delete?"))

        is_sure = input(f"You want to delete {expenses[index]}")
        if is_sure.lower() == 'y':
            del expenses[index]
        else:
            continue

        finished_deleting = isFinished("deleting")