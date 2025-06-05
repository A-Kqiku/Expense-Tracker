from methods import *


app_status: bool= True
amount_of_expense: int = 0
expenses = {}

menu_text: str = "\n(1) Show Expenses \n(2) Add Expenses \n(3) Edit Expenses \n(4) Delete Expenses \n(5) Exit"


while app_status:
    user_input: int = int(input(menu_text))

    match user_input:
        case 1:
            show_expenses(expenses)
        case 2:
            amount_of_expense = add_expenses(expenses, amount_of_expense)
        case 3:
            show_expenses(expenses)
            edit_expenses(expenses)
        case 4:
            delete_expenses(expenses)
        case 5:
            print("Bye")
            app_status = False
        case _:
            print("Invalid input")
