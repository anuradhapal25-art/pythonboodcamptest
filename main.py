
from storage import save_expenses, load_expenses
from reports import total_spent, biggest_expense
expenses = load_expenses()
for i in range(3):
    item = input("Enter item: ")
    try:
        amount = int(input("Enter amount: "))
        expenses.append((item, amount))
    except ValueError:
        print("Invalid amount!")
save_expenses(expenses)
print("Total spent:", total_spent(expenses))
print("Biggest expense:", biggest_expense(expenses))
